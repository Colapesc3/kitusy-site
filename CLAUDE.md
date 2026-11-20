# Sito Kitusy — kitusy.com

Memoria di lavoro del sito. Leggila prima di ogni modifica e aggiornala (sezione «Storia») dopo ogni modifica pubblicata.

## Cos'è

Sito vetrina della software house Kitusy: presenta le app, ospita le pagine di privacy e supporto richieste dagli store, raccoglie candidature di collaboratori. Sito statico, senza framework, senza cookie, senza tracciamento, senza richieste a server esterni.

## Pubblicazione

- Repository: `Colapesc3/kitusy-site`, ramo `main`.
- Cloudflare Pages pubblica la radice del repository a ogni push su `main` (1–2 minuti). Non c'è un passo di build su Cloudflare.
- Tutto ciò che sta nel repository è raggiungibile dal web, salvo quanto escluso in `_redirects`. Non scrivere qui né altrove dati riservati (credenziali, account, dati personali).
- Indirizzi senza estensione: `privacy.html` risponde su `/privacy`. Nei link interni non usare mai `.html`.
- `_headers`: i file in `/picciuli/demo/` vengono scaricati come allegato.
- `_redirects`: nasconde questo file e la cartella `src/`.

## Struttura

| Percorso | Contenuto |
|---|---|
| `src/index.template.html` | Sorgente della home. **Si modifica questo, non `index.html`.** |
| `src/build.py` | Rigenera `index.html` inserendo i loghi SVG (`{{KITE}}`, `{{LOGO}}`). |
| `index.html` | Home generata. Va sempre committata insieme al template. |
| `privacy.html` | Informativa privacy del sito (sezione `#candidature`). |
| `collabora.html` | Pagina «Collabora con Kitusy». |
| `404.html` | «Questa pagina è volata via» (noindex). |
| `picciuli/` | Pagina dell'app, `supporto`, `privacy`, cartella `img/`, `demo/Picciuli-Demo.picciuli`. |
| `picciuli/en/` | Versione inglese: `index`, `support`, `privacy`. |
| `cartanza/` | Pagina dell'app (sezione `#prova` per il test), `privacy`, `elimina-account`, `img/`. |
| `assets/` | Loghi Kitusy, icone delle app, `og.png`, caratteri, icone social. |
| `sitemap.xml`, `robots.txt` | Indicizzazione. |

Solo la home passa da `build.py`. Tutte le altre pagine sono HTML scritto a mano, ognuna con il proprio `<style>`.

## Come modificare

1. `git pull` prima di toccare qualsiasi file.
2. Home: modificare `src/index.template.html`, poi `python3 src/build.py`.
3. Home bilingue: ogni testo ha `data-i18n="chiave"` (o `data-i18n-html`). L'italiano è nell'HTML, l'inglese nell'oggetto `T.en` in fondo al template. **Ogni testo nuovo o cambiato va aggiornato in entrambe le lingue.**
4. Pagine di Pìcciuli: esistono in italiano e in inglese (`picciuli/en/`). Una modifica di contenuto va fatta in tutte e due.
5. Pagina nuova: aggiungerla a `sitemap.xml`. Pagina modificata: aggiornare il suo `lastmod`.
6. Nelle sottocartelle usare collegamenti assoluti (`/assets/...`, `/picciuli/privacy`): quelli relativi si rompono secondo che l'indirizzo finisca o no con `/`.
7. Verifica visiva prima del push: schermata a 390 px (telefono) e a 1280 px (computer).
8. Commit in italiano, una riga che dice cosa cambia per chi visita il sito (vedi `git log`). Poi `git fetch origin main && git rebase origin/main && git push origin HEAD:main`.
9. Dopo il push controllare la pagina online.

## Aggiungere un'app alla home

Nel template, dentro `.apps`, copiare una scheda `.app` esistente:

- icona in `assets/` (PNG quadrato o SVG);
- nome, significato (`*_meaning`), descrizione (`*_desc`), piattaforme (`.platforms`);
- stato: `pill live` «Disponibile», `pill test` «In fase di test», `pill dev` «In sviluppo»;
- collegamenti `link-sm` (Scopri, Supporto, Privacy) e pulsante `btn` solo se esistono davvero;
- chiavi inglesi in `T.en`.

Stato attuale: Pìcciuli (disponibile, App Store), Cartanza (in fase di test, TestFlight), Aunnè, Cuntàri e KitMetry (in sviluppo).

## Grafica

- Sfondo blu del logo `#0B2A4A`; riquadri `#0F3560`; linee `#24507d`; testo bianco; testo secondario `#A9C1DA`.
- Cinque colori dell'aquilone: blu `#1F5FAF`, ciano `#26A9C9`, verde `#4CAF7A`, ambra `#F2A541`, rosso `#E4572E`.
- Proporzioni auree: colonne 1 : 1,618; spaziature `--s0…--s3` = 1 / 1,618 / 2,618 / 4,236 rem.
- Caratteri: Lexend (titoli) e Source Sans 3 (testo), ospitati in `assets/fonts/`. Non collegare Google Fonts né altre risorse esterne.
- Logo: `kitusy-kite.svg` (solo aquilone), `kitusy-logo.svg` (con sfondo), `kitusy-logo-trasparente.svg`. Il logo non si ridisegna.
- Motto: «Kit easy, life easy.» Titolo: «App che alleggeriscono il lavoro e il tempo libero.»

## Regole di contenuto

- Nessuna località nei testi né nel piè di pagina.
- Nel piè di pagina e nelle pagine compare solo «Kitusy». Il nome del titolare compare soltanto nelle informative privacy, dove è obbligatorio.
- Tono: frasi brevi, concrete, nessuna promessa non verificabile.
- Le pagine di privacy descrivono ciò che l'app fa davvero: si aggiornano quando cambia l'app, non prima.

## Indirizzi

- Email: `supporto@` (assistenza), `segnalazioni@` (bug), `info@` (informazioni), `collabora@` (candidature), `privacy@` (privacy), tutte su `kitusy.com`.
- Social: Instagram `@kitusyapp_`, Facebook `facebook.com/Kitusyapp`, TikTok `@kitusy`, X `@kitusyapp_`.
- Pìcciuli su App Store: `https://apps.apple.com/it/app/p%C3%ACcciuli/id6793956859`.
- Cartanza su TestFlight: `https://testflight.apple.com/join/YKyRn8wZ`.
- Tester Android di Pìcciuli: `https://groups.google.com/g/picciuli-tester`.

## Vincoli esterni

- Gli indirizzi di privacy, supporto e marketing dichiarati su App Store Connect si cambiano solo con una nuova versione dell'app. Non spostare né rinominare le pagine `picciuli/*` e `cartanza/*` senza lasciare un rinvio.
- Le vecchie pagine su `colapesc3.github.io/picciuli-privacy/` (repository `Colapesc3/picciuli-privacy`) rinviano a `kitusy.com/picciuli/privacy` e `/supporto`. Vanno lasciate finché l'app in vendita le cita.
- `cartanza/elimina-account` è richiesta da Google Play: l'indirizzo non deve cambiare.

## Storia

- 19 ott 2026 — Prima versione: home con Pìcciuli, Aunnè, Cartanza, Cuntàri.
- 20 ott 2026 — Privacy e supporto di Pìcciuli portati sul sito; informativa privacy del sito; caratteri in locale; link e icone social; anteprima dei link (`og.png`), icona Home, sitemap, pagina 404.
- 23 ott 2026 — Pagina Collabora e privacy delle candidature; tolta la località da piè di pagina e descrizioni; contatti separati.
- 24–26 ott 2026 — Privacy di Pìcciuli: sincronizzazione, AI, Android, cifratura; file dimostrativo scaricabile.
- 1–2 nov 2026 — Pagina di Pìcciuli 1.2 con foto; versione inglese di pagina, supporto e privacy; collegamenti assoluti.
- 15–17 nov 2026 — Pagina di Cartanza con iscrizione al test; privacy ed eliminazione account; KitMetry in home; testi Filosofia corretti; pulsante TestFlight.
- 19 nov 2026 — Privacy di Cartanza: pubblicità tolta per 6 mesi o un anno.
- 20 nov 2026 — Aggiunto questo file; `_redirects` per non esporlo sul web.

## Da sistemare

- `sitemap.xml`: il `lastmod` della home è fermo al 20 ott 2026, ma la home è cambiata il 16 nov 2026.
