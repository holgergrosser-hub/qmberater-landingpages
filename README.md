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

## Umzug auf die Hauptdomain

1. In `generate_all_pages.py` `SITE_BASE` auf
   `https://qm-guru.de/iso-9001-branchen` umstellen
2. `./build.sh`
3. Cloudflare-Worker `branchen-proxy` anlegen, Routen
   `qm-guru.de/iso-9001-branchen*` und `www.qm-guru.de/iso-9001-branchen*`
4. Erst danach den 301-Block in `netlify.toml` einkommentieren und committen

Alle internen Links und Asset-Pfade sind relativ und funktionieren unter jedem
Pfad-Präfix – am HTML muss für den Umzug nichts angefasst werden.

---

## Externe Abhängigkeiten

Keine. Fonts sind ein System-Stack, Tailwind wird lokal kompiliert. Es werden
beim Seitenaufruf **keine** Dateien von Google, Cloudflare-CDNs oder jsDelivr
nachgeladen.
