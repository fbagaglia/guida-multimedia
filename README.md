# Creare video e contenuti multimediali senza strumenti a pagamento

Guida pratica, passo per passo: **dieci strumenti gratuiti**, **una tecnica** e l'**indice dei
progetti**, con i dati verificati sulle fonti ufficiali. Alla base di tutto c'è `ffmpeg`.

## I capitoli

| # | Argomento | Gratuito? |
|---|---|---|
| 1 | **ffmpeg** — montaggio, conversione, registrazione | sì, licenza libera (non esiste a pagamento) |
| 2 | **Recordly** (recordly.dev) — registrare lo schermo | sì, open source (AGPL-3.0) |
| 3 | **Playwright** + ffmpeg — il browser che si muove da solo | sì, open source (Apache-2.0) |
| 4 | **HyperFrames** — montare il video da una pagina | sì, open source (Apache-2.0) |
| 5 | **rrweb** — registrare il web, non lo schermo | sì, open source (MIT) |
| 6 | **GSAP** — animazione per il video | sì, anche per lavoro, ma licenza **proprietaria** |
| 7 | **Meshy** — oggetti 3D | 100 crediti/mese; gratis con **CC BY 4.0** (citare) |
| 8 | **ComfyUI / Comfy Cloud** — immagini e video generati | locale sì (serve GPU), cloud da ~20 $/mese |
| 9 | **AnyMP4 / AnyRec** — conversione e montaggio | desktop a pagamento; registratore **online** gratuito |
| 10 | **Pollinations** — contenuti via API | immagini senza chiave; testo solo sull'indirizzo semplice |
| 11 | **La tecnica: l'accesso delegato** — far entrare un agente nei propri profili **senza dargli la password** | tecnica, non prodotto |
| 12 | **Le skill** — procedure scritte una volta | — |
| 13 | **I connettori MCP** — dare le mani all'agente | 55 abilitati |
| 14 | **I progetti** — i repository e i cantieri, con la spiegazione di ciascuno | — |

## File

- `Guida-multimedia-gratuita.pdf` — il documento impaginato (copertina, testatina, numeri di pagina)
- `guida.md` — il testo sorgente, in Markdown
- `genera_pdf.py` — rigenera il PDF: `py -3.14 genera_pdf.py`
- `controlla_pdf.py` — verifica il PDF leggendone il testo (parole spezzate, sezioni, testatina, numeri)
- `rendi_pagine.py` — rende le pagine in immagini, per guardarle
- `verifica-fonti-8-strumenti.md` — le fonti ufficiali lette, con i link

## Nota sui dati

Dove un'informazione non era verificabile, **non è stata inventata**: è stata esclusa.
I prezzi e le licenze cambiano: prima di un lavoro commerciale, controlla la pagina ufficiale.
