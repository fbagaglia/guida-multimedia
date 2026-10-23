# Verifica su fonti ufficiali — 8 strumenti per video e contenuti multimediali
Data verifica: 23 ottobre 2026. Solo fonti primarie (sito ufficiale / pagina prezzi / licenza / repo ufficiale).

## 1. GSAP (greensock.com → gsap.com)
- (a) Libreria JavaScript per animazioni web (motion su DOM/SVG, scroll, timeline). Non fa video: fa animazioni dentro pagine web/HTML.
- (b) **Gratuito, anche per uso commerciale.**
- (c) Licenza proprietaria "GSAP Standard License" (licenza "no-charge"): NON è open source (non è MIT/Apache/GPL). Dal 2025, dopo l'acquisizione da parte di Webflow, l'intero toolset — inclusi i plugin ex-Club (SplitText, MorphSVG, ScrollSmoother…) — è gratuito e la licenza standard è stata estesa all'uso commerciale. Vincoli residui: non rimuovere le note di copyright/proprietà del software.
- (d) Nessuna GPU. Nessun account. Nessuna installazione obbligatoria (CDN, npm `gsap`, o download da gsap.com). Gira nel browser (locale, lato client).
- (e) https://gsap.com/pricing/ · https://webflow.com/blog/gsap-becomes-free · https://gsap.com/blog/3-13/ · https://github.com/greensock/GSAP (sezione License)
  - Nota: la pagina con il testo integrale (https://gsap.com/standard-license, alias /community/standard-license) al momento della verifica rimandava alla pagina "Forums offline"; licenza confermata dalle fonti sopra.

## 2. Recordly (recordly.dev)
- (a) Registratore di schermo + editor integrato per desktop: auto-zoom, cursore "morbido", bolla webcam, timeline di editing, export MP4/GIF.
- (b) **Gratuito e open source** (nessun paywall dichiarato).
- (c) Licenza **AGPL-3.0** (AGPL-3.0 = open source; richiede di rendere disponibile il sorgente delle versioni modificate distribuite/erogate in rete). "Free" e "open source": le due cose coincidono qui.
- (d) Nessuna GPU dedicata necessaria (usa l'accelerazione di sistema). Nessun account. Piattaforme: macOS 14+, Windows 10 (build 19041+), Linux (distro moderne). Gira **in locale**.
- (e) https://recordly.dev/ · https://github.com/webadderallorg/recordly (badge: macOS/Windows/Linux, AGPL 3.0; README "for free").
  - ⚠️ Attenzione omonimia: esiste un sito **recordly.vip** che vende un "Recordly" per **$19,99 una tantum** (prodotto commerciale diverso, non open source). Chi cerca "Recordly screen recorder" può atterrare lì.

## 3. Playwright (playwright.dev)
- (a) Framework di automazione/test browser di Microsoft (Chromium, Firefox, WebKit con un'unica API). Usabile per script, test E2E, e agenti AI (MCP/CLI). Utile per generare screenshot/registrazioni di pagine in modo programmatico.
- (b) **Gratuito e open source.**
- (c) Licenza **Apache-2.0** (permissiva, uso commerciale consentito). Il framework è gratis; si paga solo l'infrastruttura che eventualmente usi per eseguirlo.
- (d) Nessuna GPU. Nessun account. Windows/macOS/Linux, headless e headed. Binding: TypeScript/JS, Python, .NET, Java. Gira **in locale** (scarica i browser).
- (e) https://playwright.dev/ · https://github.com/microsoft/playwright · https://github.com/microsoft/playwright/blob/main/LICENSE

## 4. Meshy (meshy.ai)
- (a) Generazione di modelli 3D con AI da testo o immagini (e texturing/rigging), fruibile da web app/cloud.
- (b) **Gratis con limiti** (piano Free), a pagamento sopra.
- (c) Piano **Free: $0, senza carta di credito**, 100 crediti/mese (azzerati il 1° del mese), fino a ~10 asset/mese, 1 task simultaneo, coda a bassa priorità; **download limitato a 10 modelli "Meshy 6 Lite"/mese**. Licenza degli output del piano Free: **CC BY 4.0** → uso commerciale **consentito ma con attribuzione**; i modelli restano di tua proprietà. Piani a pagamento: **Pro $20/mese**, Premium $40, Ultra $100 (spesso 50% sul primo mese); con i piani a pagamento la licenza diventa "Private", commerciale piena senza attribuzione.
- (d) Nessuna GPU locale: gira nel **cloud** (serve solo browser + account). Windows/Mac/Linux indifferenti.
- (e) https://www.meshy.ai/pricing · https://docs.meshy.ai/en/webapp/pricing · https://help.meshy.ai/en/articles/9992001-can-i-use-meshy-assets-commercially-license-copyright-explained

## 5. ComfyUI locale vs Comfy Cloud (comfy.org)
- (a) ComfyUI = motore/interfaccia a nodi per modelli di diffusione (immagini, video, audio…). Due modalità: **self-hosted locale** e **Comfy Cloud** (gestito, su GPU in cloud).
- (b) Locale: **gratuito e open source**. Cloud: **freemium** (tier gratuito minimo + abbonamenti).
- (c) ComfyUI locale: **GPL-3.0** (open source), software gratis; paghi solo l'hardware. Comfy Cloud: prova gratuita con **5 run gratis** su GPU reali + crediti Comfy Agent per i nuovi utenti; poi **Standard $20/mese** (annuale $16/mese), **Creator $35/mese** ($28 annuale), **Pro $100/mese** ($80 annuale), **Team $700/mese**; modello a crediti (≈11 crediti per un video 5 s di riferimento). API: GPU da $3,49/h (RTX PRO 6000) fino a $11,23/h (B200).
- (d) **GPU — punto critico per una macchina senza GPU (i5-1235U):**
  - Locale: gira ufficialmente anche **solo CPU** (flag `--cpu`, "più lento"); per prestazioni reali serve GPU NVIDIA/AMD/Intel Arc o Apple Silicon. Su un i5 senza GPU dedicata è tecnicamente possibile ma di fatto **molto lento** (in pratica poco utilizzabile per video).
  - Cloud: **nessuna GPU locale**, tutto su Blackwell RTX 6000 Pro (96 GB). Windows/macOS/Linux indifferenti. Richiede account e connessione.
  - OS supportati in locale: Windows, Linux, macOS (Apple Silicon). Comfy Desktop: Windows/macOS/Linux.
- (e) https://comfy.org/pricing/ · https://docs.comfy.org/get_started/cloud · https://docs.comfy.org/installation/system_requirements · https://github.com/Comfy-Org/ComfyUI (GPL-3.0)
  - Nota: sul piano Cloud le pagine ufficiali parlano sia di "free trial/5 run gratis" sia di "free tier"; l'entità esatta del tier gratuito nel tempo → **non verificato**.

## 6. AnyMP4 / AnyRec (anymp4.com, anyrec.io)
- (a) Suite di programmi desktop per registrare schermo/webcam/audio e per convertire/editare video. Prodotti commerciali (non open source).
- (b) **A pagamento**, con due eccezioni gratuite: (1) un **registratore web "online"** gratuito; (2) il "**Free Download**" del desktop, che è un **trial**.
- (c) **AnyMP4**: versione desktop a pagamento (licenza Business/5 PC $99,96; prezzo individuale indicato dallo stesso sito ~**$12,45/mese**, lifetime disponibile — dato dal sito AnyMP4, da confermare al checkout). Il **Free Screen Recorder Online** di AnyMP4 è dichiarato "senza watermark", ma limitato rispetto alla versione Pro (nella tabella ufficiale Free vs Pro: fps max 24 invece di 60, formati di export ridotti WMV/MP4, strumenti di editing ridotti, niente registrazione programmata/preview). **AnyRec**: **$14,50/mese** o **$54,95 lifetime**; il suo **Free Screen Recorder Online** è "100% free, senza limiti di durata, senza account", ma **aggiunge un watermark by default** (dichiarato esplicitamente sul sito). La versione **desktop free** di entrambi è un trial: i limiti precisi (watermark/durata) **non sono dichiarati in modo esplicito nelle pagine ufficiali lette → non verificato** (per AnyMP4 uno statement ufficiale parla di "watermark al centro del video" nel trial, ma riferito ad articolo generico, non alla scheda prodotto).
- (d) Nessuna GPU necessaria. Nessun account per le versioni online; per il desktop serve licenza (e per AnyRec l'attivazione è legata a un solo computer, errore 4104 se riattivata altrove). Piattaforme: **Windows e macOS** (non Linux). Gira **in locale** (il desktop), l'online nel browser.
- (e) https://www.anymp4.com/screen-recorder/ · https://www.anymp4.com/purchase/screen-recorder.html · https://www.anymp4.com/free-online-screen-recorder/ · https://www.anyrec.io/screen-recorder/ · https://www.anyrec.io/purchase/screen-recorder/ · https://www.anyrec.io/free-online-screen-recorder/
  - ⚠️ Nel contesto dato, **AnyRec NON è installato** sulla macchina Windows dell'utente.

## 7. Pollinations (pollinations.ai)
- (a) Infrastruttura/API unica (compatibile OpenAI SDK) per generare **testo, immagini, audio (TTS), video, 3D ed embeddings**; incluso storage media e MCP tool.
- (b) **Freemium**: modello "pay as you go" a crediti ("pollen", 1 pollen = $1) + crediti gratuiti ("Quest pollen").
- (c) **Cosa funziona senza chiave (verificato ora con richieste reali da questa macchina):** generazione **immagini** SENZA chiave — `GET https://gen.pollinations.ai/image/{prompt}` (testata: HTTP 200, JPEG reale di 15 KB) e anche l'endpoint legacy `https://image.pollinations.ai/prompt/{prompt}` (200). **Testo senza chiave:** una richiesta `POST /v1/chat/completions` sul modello gratuito di default ha risposto 200 con contenuto valido; anche `https://text.pollinations.ai/{prompt}` ha risposto 200. Quindi, di fatto, oggi funzionano senza chiave sia immagini sia testo sui modelli gratuiti.
  - **Ma la documentazione ufficiale** dichiara che la chiave è necessaria per le richieste di generazione ("Use a secret key for generation requests"); solo gli endpoint di elenco modelli sono dichiaratamente senza autenticazione. La chiave (`sk_`) serve comunque per: modelli a pagamento, budget/limiti maggiori, BYOP/quote, chiavi app. Esistono anche chiavi pubbliche raw (`pk_`) "legacy" con limite 1 pollen/IP/ora.
  - Distinzione da tenere: **codice open source (MIT, repo GitHub)** ≠ servizio gratuito per tutti (il servizio è a crediti). L'uso anonimo è una tolleranza di fatto, non un diritto documentato: per un uso didattico stabile conviene una chiave.
- (d) Nessuna GPU: tutto in **cloud**. Nessun account per l'uso anonimo (immagini/testo base), account consigliato per chiave/crediti. Indipendente dall'OS (chiamate HTTP/CLI `npx @pollinations/cli`).
- (e) https://gen.pollinations.ai/docs · https://pollinations.ai/ · https://github.com/pollinations/pollinations (MIT)

## 8. FFmpeg (ffmpeg.org)
- (a) Libreria + CLI di riferimento per registrare, convertire, filtrare e fare streaming di audio/video (muxing, codec, filtri, concat, GIF, ritagli, estrazione audio…). È il "motore" video a riga di comando.
- (b) **Gratuito e open source.**
- (c) Licenza **LGPL v2.1 o superiore**; alcune parti opzionali (es. `libx264`, altri componenti) sono sotto **GPL v2**: se incluse, l'intero FFmpeg passa a GPL. Uso personale senza problemi; per redistribuirlo dentro prodotti commerciali valgono gli obblighi LGPL/GPL (checklist ufficiale sul sito). **Non è disponibile una licenza proprietaria/commerciale a pagamento**, nemmeno pagando.
- (d) **Nessuna GPU necessaria** (decodifica/encoding prevalentemente su CPU; esistono accelerazioni hardware opzionali come CUDA/Vulkan/D3D, non richieste). Nessun account. Cross-platform Windows/macOS/Linux. Gira **in locale**.
- (e) https://ffmpeg.org/ · https://ffmpeg.org/legal.html
  - Già verificato in contesto: **ffmpeg è installato e funzionante** sulla macchina Windows dell'utente.

---
### Sintesi "serve una GPU?"
- **No GPU:** GSAP, Recordly, Playwright, Meshy (cloud), AnyMP4/AnyRec, Pollinations (cloud), FFmpeg.
- **GPU sì (in locale):** ComfyUI self-hosted — ufficialmente funziona anche CPU-only (`--cpu`) ma lentamente; su un i5-1235U senza GPU è sconsigliato. In alternativa **Comfy Cloud** (nessuna GPU locale, da ~$20/mese, con pochi run gratis iniziali).