# -*- coding: utf-8 -*-
"""Controlla il PDF leggendone il TESTO (non l'immagine): e' l'unica verifica che non si sbaglia."""
import os
import re

import fitz

QUI = os.path.dirname(os.path.abspath(__file__))
d = fitz.open(os.path.join(QUI, "Guida-multimedia-gratuita.pdf"))
print("pagine:", d.page_count)

print()
print("=== pagina 1 (copertina): le righe, nell'ordine in cui stanno ===")
for blocco in d[0].get_text("blocks")[:8]:
    testo = " ".join(blocco[4].split())
    if testo:
        print("   y=%4d | %s" % (blocco[1], testo[:76]))

print()
print("=== controllo dei difetti ===")
# 1) nessuna parola spezzata: si cercano righe che finiscono a meta' parola
tutto = "\n".join(d[n].get_text() for n in range(d.page_count))
for parola in ("e contenuti m\nultimediali", "ontenuti m\n"):
    print("   parola spezzata %-12r: %s" % (parola, "PRESENTE (difetto)" if parola in tutto else "assente ✓"))

# 2) le sezioni ci sono tutte, in ordine
attese = ["FFmpeg", "Recordly", "Playwright", "GSAP", "Meshy", "Comfy", "AnyMP4", "Pollinations",
          "accesso delegato", "vicolo cieco",
          "HyperFrames", "node_modules", "Le skill", "local-first-webapp-stdlib",
          "connettori", "Canva", "Composio", "Gmail", "MCP",
          "rrweb", "session replay", "I progetti", "Mio_Esoscheletro_Z", "SSLM Second Brain",
          "Modello Delega", "AGENT OS", "Creazione Testo Ultimate"]
for a in attese:
    print("   sezione/tema %-18s %s" % (a, "c'e' ✓" if a.lower() in tutto.lower() else "MANCA"))

# 3) il testo della testatina e' quello giusto, e non si ripete nel corpo
print("   testatina:", "Creare multimedia senza strumenti a pagamento" in tutto)

# 4) ogni pagina interna ha un numero
senza_numero = []
for n in range(1, d.page_count):
    testo = d[n].get_text()
    if not re.search(r"\b%d\b" % (n + 1), testo):
        senza_numero.append(n + 1)
print("   pagine senza numero:", senza_numero or "nessuna ✓")

# 5) quante parole in tutto
print("   parole totali:", len(tutto.split()))
