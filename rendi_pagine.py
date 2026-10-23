# -*- coding: utf-8 -*-
"""Rende alcune pagine del PDF in immagini, per guardarle e controllarle."""
import os
import sys

import fitz

QUI = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(QUI, "Guida-multimedia-gratuita.pdf")
USCITA = os.environ.get("TEMP", QUI)

d = fitz.open(PDF)
print("pagine:", d.page_count)
for n in [int(x) for x in (sys.argv[1:] or ["1", "4"])]:
    if 1 <= n <= d.page_count:
        pix = d[n - 1].get_pixmap(dpi=105)
        f = os.path.join(USCITA, "guida_pag%d.png" % n)
        pix.save(f)
        print("pagina %d -> %s" % (n, f))
