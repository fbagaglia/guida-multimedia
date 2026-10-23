# -*- coding: utf-8 -*-
"""Guida «Creare multimedia senza strumenti a pagamento»: da Markdown a PDF con copertina.

    py -3.14 genera_pdf.py

Legge `guida.md` e produce `Guida-multimedia-gratuita.pdf`:
copertina disegnata, indice, intestazione e numero di pagina su ogni foglio.

Markdown riconosciuto: # ## ###, **grassetto**, `codice`, elenchi - e 1., tabelle | |,
blocchi ``` , righe di separazione ---, e i richiami > nota.
"""
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, NextPageTemplate, PageBreak,
                                PageTemplate, Paragraph, Preformatted, Spacer, Table, TableStyle)

QUI = os.path.dirname(os.path.abspath(__file__))
SORGENTE = os.path.join(QUI, "guida.md")
USCITA = os.path.join(QUI, "Guida-multimedia-gratuita.pdf")

# --- la tavolozza: sobria, da documento da leggere (non da depliant) -----------------
INCHIOSTRO = colors.HexColor("#1c2b3a")
TENUE = colors.HexColor("#5b6b7c")
ACCENTO = colors.HexColor("#b07a20")     # ocra, come le schede dei video
RIGA = colors.HexColor("#d8d3c8")
CARTA = colors.HexColor("#fdfcf8")

TITOLO = "Creare video e contenuti multimediali"
SOTTOTITOLO = "senza strumenti a pagamento"
DICITURA = "Guida pratica, passo per passo"


def stili():
    s = getSampleStyleSheet()
    fuori = {
        "h1": ParagraphStyle("h1", parent=s["Heading1"], fontName="Helvetica-Bold", fontSize=19,
                             leading=24, textColor=INCHIOSTRO, spaceBefore=16, spaceAfter=10),
        "h2": ParagraphStyle("h2", parent=s["Heading2"], fontName="Helvetica-Bold", fontSize=14.5,
                             leading=19, textColor=ACCENTO, spaceBefore=14, spaceAfter=7),
        "h3": ParagraphStyle("h3", parent=s["Heading3"], fontName="Helvetica-Bold", fontSize=12,
                             leading=16, textColor=INCHIOSTRO, spaceBefore=11, spaceAfter=5),
        "p": ParagraphStyle("p", parent=s["BodyText"], fontName="Helvetica", fontSize=10.5,
                            leading=15.5, textColor=INCHIOSTRO, alignment=TA_JUSTIFY, spaceAfter=7),
        "nota": ParagraphStyle("nota", parent=s["BodyText"], fontName="Helvetica-Oblique",
                               fontSize=10, leading=14.5, textColor=TENUE, leftIndent=9,
                               borderPadding=(0, 0, 0, 6), spaceAfter=8),
        "punto": ParagraphStyle("punto", parent=s["BodyText"], fontName="Helvetica", fontSize=10.5,
                                leading=15, textColor=INCHIOSTRO, leftIndent=13, bulletIndent=3,
                                spaceAfter=4),
        "codice": ParagraphStyle("codice", parent=s["Code"], fontName="Courier", fontSize=8.6,
                                 leading=12.2, textColor=colors.HexColor("#243b53"),
                                 backColor=colors.HexColor("#f2efe8"), borderPadding=6,
                                 leftIndent=6, spaceBefore=4, spaceAfter=8),
        "didascalia": ParagraphStyle("didascalia", parent=s["BodyText"], fontName="Helvetica-Oblique",
                                     fontSize=9, leading=12.5, textColor=TENUE, spaceAfter=9),
    }
    return fuori


def scappa(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def in_linea(t):
    """Grassetto, corsivo e codice: si scappa PRIMA, poi si mette il markup."""
    t = scappa(t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r'<font face="Courier" color="#243b53">\1</font>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#b07a20">\1</link>', t)
    return t


def copertina(canvas, doc):
    """Copertina: fondo carta, filetto ocra, titolo grande. Disegnata a mano, non un template."""
    L, A = A4
    canvas.saveState()
    canvas.setFillColor(CARTA)
    canvas.rect(0, 0, L, A, stroke=0, fill=1)
    # filetto ocra in alto e in basso
    canvas.setFillColor(ACCENTO)
    canvas.rect(0, A - 16 * mm, L, 3 * mm, stroke=0, fill=1)
    canvas.rect(0, 13 * mm, L, 1.2 * mm, stroke=0, fill=1)

    # il titolo va diviso PER PAROLE, non a un numero fisso di caratteri: tagliando a 26 caratteri
    # usciva «Creare video e contenuti m / ultimediali», cioe' una parola spezzata in due.
    import textwrap
    righe_titolo = textwrap.wrap(TITOLO, width=26)
    canvas.setFillColor(INCHIOSTRO)
    canvas.setFont("Helvetica-Bold", 27)
    y_titolo = A - 62 * mm
    for riga in righe_titolo:
        canvas.drawString(24 * mm, y_titolo, riga)
        y_titolo -= 12 * mm
    canvas.setFillColor(ACCENTO)
    canvas.setFont("Helvetica-Oblique", 18)
    canvas.drawString(24 * mm, A - 90 * mm, SOTTOTITOLO)

    canvas.setStrokeColor(RIGA)
    canvas.setLineWidth(0.7)
    canvas.line(24 * mm, A - 100 * mm, L - 24 * mm, A - 100 * mm)

    canvas.setFillColor(TENUE)
    canvas.setFont("Helvetica", 11.5)
    canvas.drawString(24 * mm, A - 112 * mm, DICITURA)
    canvas.setFont("Helvetica", 10)
    righe = [
        "Dieci strumenti gratuiti, una tecnica e i progetti: come far lavorare",
        "un agente sui propri profili, come montare tutto con ffmpeg,",
        "e l'indice dei cantieri.",
        "",
        "Con esempi, comandi e gli avvisi su ciò che è gratuito e ciò che non lo è.",
    ]
    y = A - 124 * mm
    for r in righe:
        canvas.drawString(24 * mm, y, r)
        y -= 6 * mm

    canvas.setFillColor(TENUE)
    canvas.setFont("Helvetica", 9)
    canvas.drawString(24 * mm, 22 * mm, "Documento di lavoro — verificato sulle fonti ufficiali")
    canvas.restoreState()


def testatina(canvas, doc):
    """Su ogni pagina: titolo a sinistra, numero a destra, filetto sottile."""
    L, A = A4
    canvas.saveState()
    canvas.setFillColor(TENUE)
    canvas.setFont("Helvetica", 8.5)
    canvas.drawString(22 * mm, A - 13 * mm, "Creare multimedia senza strumenti a pagamento")
    canvas.drawRightString(L - 22 * mm, A - 13 * mm, str(doc.page))
    canvas.setStrokeColor(RIGA)
    canvas.setLineWidth(0.5)
    canvas.line(22 * mm, A - 16 * mm, L - 22 * mm, A - 16 * mm)
    canvas.restoreState()


def markdown_a_story(testo, st):
    """Il Markdown diventa una sequenza di elementi, riga per riga."""
    fuori = []
    in_codice = False
    blocco = ""
    righe_tabella = []

    def chiudi_tabella():
        if not righe_tabella:
            return
        righe = [r for r in righe_tabella if not all(re.fullmatch(r"[-: ]+", c or " ") for c in r)]
        if righe:
            dati = [[Paragraph(in_linea(c.strip()), st["punto"]) for c in r] for r in righe]
            t = Table(dati, hAlign="LEFT", repeatRows=1)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f2efe8")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.4, RIGA),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]))
            fuori.append(t)
            fuori.append(Spacer(1, 8))
        righe_tabella.clear()

    for riga in testo.split("\n"):
        if riga.strip().startswith("```"):
            if in_codice:
                fuori.append(Preformatted(blocco.rstrip(), st["codice"]))
                blocco = ""
            in_codice = not in_codice
            continue
        if in_codice:
            blocco += riga + "\n"
            continue
        if riga.strip().startswith("|"):
            righe_tabella.append(riga.strip().strip("|").split("|"))
            continue
        chiudi_tabella()
        r = riga.rstrip()
        if not r.strip():
            continue
        if r.strip() == "---":
            fuori.append(Spacer(1, 6))
            continue
        if r.startswith("### "):
            fuori.append(Paragraph(in_linea(r[4:]), st["h3"]))
        elif r.startswith("## "):
            fuori.append(Paragraph(in_linea(r[3:]), st["h2"]))
        elif r.startswith("# "):
            fuori.append(Paragraph(in_linea(r[2:]), st["h1"]))
        elif r.startswith("> "):
            fuori.append(Paragraph(in_linea(r[2:]), st["nota"]))
        elif re.match(r"^\s*[-*] ", r):
            fuori.append(Paragraph(in_linea(re.sub(r"^\s*[-*] ", "", r)), st["punto"],
                                   bulletText="•"))
        elif re.match(r"^\s*\d+\. ", r):
            n = re.match(r"^\s*(\d+)\. ", r).group(1)
            fuori.append(Paragraph(in_linea(re.sub(r"^\s*\d+\. ", "", r)), st["punto"],
                                   bulletText=n + "."))
        else:
            fuori.append(Paragraph(in_linea(r), st["p"]))
    chiudi_tabella()
    if in_codice and blocco:
        fuori.append(Preformatted(blocco.rstrip(), st["codice"]))
    return fuori


def main():
    if not os.path.exists(SORGENTE):
        print("manca il file:", SORGENTE)
        raise SystemExit(1)
    testo = open(SORGENTE, encoding="utf-8").read()
    st = stili()

    doc = BaseDocTemplate(USCITA, pagesize=A4, leftMargin=22 * mm, rightMargin=22 * mm,
                          topMargin=22 * mm, bottomMargin=20 * mm,
                          title=TITOLO + " " + SOTTOTITOLO, author="Franco Bagaglia",
                          subject="Metodi gratuiti per creare multimedia")
    quadro = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="corpo")
    doc.addPageTemplates([
        PageTemplate(id="copertina", frames=[quadro], onPage=copertina),
        PageTemplate(id="pagine", frames=[quadro], onPage=testatina),
    ])

    # la copertina occupa la prima pagina; DALLA SECONDA si passa al template con la testatina.
    # Senza NextPageTemplate reportlab userebbe il primo template per TUTTO il documento, e ogni
    # pagina resterebbe senza intestazione e senza numero (verificato: la testatina non c'era).
    story = [Spacer(1, 1), NextPageTemplate("pagine"), PageBreak()]
    story += markdown_a_story(testo, st)
    doc.build(story)
    print("PDF scritto:", USCITA)
    print("pagine:", doc.page)
    print("byte:", os.path.getsize(USCITA))


if __name__ == "__main__":
    main()
