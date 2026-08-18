# QM-Berater Landing Pages – ISO 9001 nach Branche

Acht branchenspezifische Landingpages plus Übersichtsseite für die
ISO-9001-Beratung von Holger Grosser (QM-Dienstleistungen).

Live: https://landing.qmberater.info
Netlify-Site: `landingpage-qmberater.netlify.app`

---

## Wie man etwas ändert

**Inhalte** stehen in `branchen_content.py` – pro Branche ein Eintrag mit
Meta-Daten, Problemen, Normtabelle, Nachweisliste, Ablauf, FAQ und Marktkontext.

**Layout** steht in `generate_all_pages.py`.

Nach jeder Änderung:

```sh
./build.sh
```

Das erzeugt die HTML-Dateien neu **und** baut die Tailwind-CSS aus den
tatsächlich verwendeten Klassen. Beides wird committet, Netlify deployt
automatisch. `public/` wird vollständig generiert – dort nichts von Hand ändern.

---

## Wichtige Regel: keine Textbausteine

Version 1 hat alle acht Seiten aus einer Vorlage erzeugt und nur den
Branchennamen ersetzt. Ergebnis: 96 % identischer Text auf allen Seiten – aus
Google-Sicht Doorway Pages, dazu 2 Klicks in drei Monaten.

Jede neue Branche braucht deshalb **echten eigenen Inhalt**:

- Normtabelle mit den Abschnitten, die in *dieser* Branche wirklich Probleme machen
- Nachweise, die dort tatsächlich verlangt werden
- FAQ aus echten Kundenfragen
- Marktkontext (wer fordert das Zertifikat und warum)

Richtwert: die Seiten dürfen sich zu höchstens ~50 % ähneln. Prüfen mit:

```sh
python3 tools/similarity_check.py
```

---

## Kundenstimmen

In `generate_all_pages.py` gibt es die Liste `ECHTE_STIMMEN`. Sie ist bewusst
leer. Nur **echte, vom Kunden freigegebene** Zitate eintragen – Werbeaussagen
müssen belegbar sein. Solange die Liste leer ist, wird auf die öffentlichen
Google-Bewertungen und die Referenzseite der Hauptdomain verlinkt.

---

## FAQ-Bibliothek

Unter `public/faq/` liegen acht Themenseiten mit insgesamt 73 Fragen aus echten
Beratungsgesprächen. Inhalte stehen in `faq_content.py`.

**Herkunft und Regel:** Die Antworten stammen aus der Wissensdatenbank
(Transkripte). Für die Veröffentlichung wurden sie generalisiert – keine
Kundennamen, keine Auftraggeber, keine Personennamen, keine Dienstleisternamen.
Wenn eine Antwort nur mit dem Kontext eines bestimmten Kunden verständlich ist,
gehört sie nicht auf die Seite.

**Verhältnis zum KI-Bot auf qm-guru.de:** Kein Widerspruch, sondern zwei Rollen.
Der Bot beantwortet Fragen von Leuten, die schon auf der Seite sind – er ist die
Conversion-Schicht. Die Bibliothek ist crawlbar, hat eigene URLs, FAQPage-Schema
und kann von Suchmaschinen und KI-Assistenten zitiert werden – sie ist die
Akquise-Schicht. Damit nichts auseinanderläuft, gilt: **die Bibliothek ist die
Quelle**, der Bot zieht daraus. Nicht umgekehrt.

### Halbjährliche Pflege (Februar und August)

Eine wiederkehrende Aufgabe erinnert daran. Durchzugehen sind:

1. **Aktualität** – Aussagen zu Normfassungen, Fristen, Förderbeträgen und
   Preisen prüfen. Was sich geändert hat, in `faq_content.py` korrigieren.
2. **Neue Fragen** – aus den Beratungen des letzten Halbjahres die
   wiederkehrenden Fragen ergänzen (Wissensdatenbank, FAQ-Tab).
3. **Vertraulichkeit** – erneut gegen Namen prüfen:
   `grep -oiE "gmbh|ag\b|herr |frau " public/faq/*.html`
4. **Search Console** – welche FAQ-Seiten ziehen Impressionen? Themen mit
   Nachfrage ausbauen, tote Themen zusammenlegen.
5. **Bot-Abgleich** – gibt der KI-Bot auf qm-guru.de zu diesen Fragen noch
   dieselbe Antwort? Wenn nicht: Bibliothek gewinnt, Bot nachziehen.
6. Danach `./build.sh` und committen.

---

## Umzug auf die Hauptdomain – vorbereitet

Ziel: `https://qm-guru.de/iso-9001-wissen/`

`SITE_BASE` steht bereits auf dem neuen Pfad, `public/` ist entsprechend gebaut,
`netlify.toml` enthält den aktiven 301-Block, `worker.js` liegt einsatzfertig bei.

**Reihenfolge:** erst den Cloudflare-Worker `wissen-proxy` deployen und die Routen
`qm-guru.de/iso-9001-wissen*` sowie `www.qm-guru.de/iso-9001-wissen*` anlegen –
DANN committen. Umgekehrt leitet die Subdomain auf eine 404.

Vorher lokal prüfen:

```sh
python3 tools/simulate.py
```

Das baut Worker und Netlify nach und testet 17 URLs (Seiten, Assets, Sitemap,
Query-Parameter, fremde Pfade). Alle müssen bestehen.

Alle internen Links und Asset-Pfade sind relativ – am HTML muss für den Umzug
nichts angefasst werden.

---

## Externe Abhängigkeiten

Keine. Fonts sind ein System-Stack, Tailwind wird lokal kompiliert. Es werden
beim Seitenaufruf **keine** Dateien von Google, Cloudflare-CDNs oder jsDelivr
nachgeladen.
