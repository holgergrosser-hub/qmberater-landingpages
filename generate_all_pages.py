#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QMBerater Landing Pages Generator  ·  Version 2  (18.08.2026)

Was sich gegenüber Version 1 geändert hat und WARUM:

1. INHALT STATT TEXTBAUSTEIN
   V1 hat produktion.html kopiert und nur den Branchennamen ersetzt. Ergebnis:
   acht Seiten mit 96 % identischem Text – aus Google-Sicht Doorway Pages.
   V2 baut jede Seite aus echten, branchenspezifischen Inhalten in
   branchen_content.py auf (Normtabelle, Nachweise, FAQ, Marktkontext).

2. RECHTSSEITEN
   Die Footer-Links zeigten auf qmberater.info/Sonstiges/impressum/ – dieser
   Pfad läuft in die Domain-Weiterleitung und landet auf qm-guru.de/ (Startseite).
   Es war also weder Impressum noch Datenschutz erreichbar. Jetzt: direkte Links
   auf die aktuellen Rechtsseiten der Hauptdomain, mit rel="nofollow".

3. GOOGLE FONTS ENTFERNT
   Inter wurde von fonts.googleapis.com nachgeladen – das ist in Deutschland
   bereits abgemahnt worden. Ersetzt durch einen System-Font-Stack (optisch
   nahezu identisch, keine externe Anfrage).

4. BEWERTUNGEN
   Die anonymen Zitate wurden je Branche ausgetauscht und wirkten damit generiert.
   Werbeaussagen müssen belegbar sein. V2 verlinkt stattdessen auf die echten
   Google-Bewertungen und die Referenzseite der Hauptdomain. Wenn echte,
   freigegebene Kundenzitate vorliegen: unten in ECHTE_STIMMEN eintragen.

5. SEO-GRUNDAUSSTATTUNG
   canonical, og:, twitter:, JSON-LD (Service + FAQPage + BreadcrumbList),
   robots-Meta. In V1 fehlte all das vollständig – Google hatte deshalb
   /it-dienstleistung UND /it-dienstleistung.html im Index.

6. UMZUGSFÄHIG
   SITE_BASE unten umstellen, neu generieren, fertig. Alle internen Links und
   Asset-Pfade sind relativ und funktionieren unter jedem Pfad-Präfix.

Aufruf:  python3 generate_all_pages.py
"""

import json
from pathlib import Path

from branchen_content import BRANCHEN
from faq_content import FAQ_SEITEN

# --------------------------------------------------------------------------- #
# KONFIGURATION
# --------------------------------------------------------------------------- #

# Aktuell:  https://landing.qmberater.info
# Nach dem Umzug auf:  https://qm-guru.de/iso-9001-branchen
SITE_BASE = 'https://landing.qmberater.info'

HAUPTDOMAIN   = 'https://qm-guru.de'
IMPRESSUM     = 'https://qm-guru.de/impressum/'
DATENSCHUTZ   = 'https://qm-guru.de/impressum/datenschutzerklarung/'
REFERENZEN    = 'https://qm-guru.de/5-stern-kundenbewertungen/'
KOSTENRECHNER = 'https://qm-guru.de/iso-9001-kosten-rechner/'
CALENDLY      = 'https://calendly.com/grosser-qmguru/termin-qm-system-iso-9001'
WHATSAPP      = 'https://wa.me/4915792316673'
GOOGLE_MAPS   = 'https://www.google.com/maps/place/Holger+Grosser+QM+Dienstleistungen'
TELEFON_LINK  = 'tel:091149522541'
TELEFON       = '0911-49522541'
JAHR          = 2026

# Echte, freigegebene Kundenstimmen hier eintragen – sonst bleibt der Block leer
# und es wird nur auf die Google-Bewertungen verlinkt.
# Format: (Zitat, Nennung, Branchen-Slug oder None für "auf allen Seiten")
ECHTE_STIMMEN = [
    # ('Zitat ...', 'Firma XY GmbH, Nürnberg', 'produktion'),
]

# Fragen, die in praktisch jeder Beratung kommen – die Antworten stammen aus der
# realen Beratungspraxis (Wissensdatenbank, FAQ-Tab), generalisiert und ohne
# Kundennamen. Wird NUR auf der Übersichtsseite ausgegeben, damit die
# Branchenseiten sich nicht wieder angleichen.
ALLGEMEINE_FAQ = [
    ('Müssen wir die ISO-9001-Norm kaufen und durchlesen?',
     'Nein, das bringt Ihnen nichts. Die Norm ist so verklausuliert, dass sie zu lesen wenig Sinn ergibt. '
     'Im Audit sagen Sie einfach: die Norm liegt beim Berater. Ich habe sie, ich kenne sie, und im Zweifel '
     'schieben Sie die Frage auf mich. Ihre Aufgabe ist es, das umzusetzen, was wir gemeinsam beschrieben haben.'),
    ('Wie erstellen wir die Risikoanalyse, ohne uns Risiken auszudenken?',
     'Sie müssen keine neuen Risiken erfinden. Wir nehmen Ihre Projekte und Investitionen der letzten rund '
     'vier Jahre – alles über etwa 2.000 Euro: neue Webseite, EDV-Ausstattung, Maschine, Umbau. Sie kaufen '
     'sich ja nichts ohne Grund. Hinter jeder dieser Entscheidungen steckt ein Nutzen und damit auch ein '
     'Risiko. Daraus wird die Risikobewertung.'),
    ('Wie messen wir Kundenzufriedenheit, wenn wir keine Fragebögen verschicken?',
     'Das simpelste Verfahren: Selbsteinschätzung mit Schulnoten. Nehmen Sie Ihre Hauptkunden – vier, fünf '
     'reichen – und bewerten Sie nach Kriterien wie Flexibilität, Zuverlässigkeit und Termintreue. '
     'Wir müssen keine Fragebögen an Großkonzerne schicken, damit das anerkannt wird.'),
    ('Müssen wir im Audit alle Normpunkte auswendig können?',
     'Auf keinen Fall auswendig lernen. Alles, was Sie auswendig aufsagen, klingt unnatürlich. Sie haben eine '
     'Liste als Spickzettel, damit Sie wissen, wo Sie nachschauen. Und ich bin beim Audit dabei und beantworte '
     'die Normfragen direkt, bevor Sie anfangen zu blättern.'),
    ('Können wir die Zertifizierung auf einen Teil der Firma begrenzen?',
     'In der Regel nicht – die ISO 9001 gilt für das ganze Unternehmen, so handhaben es die meisten '
     'Zertifizierungsstellen. Was Sie entscheiden können, ist die Formulierung des Geltungsbereichs: '
     'Was soll am Ende auf dem Zertifikat stehen, und was wollen Sie damit gegenüber Ihren Kunden zeigen?'),
    ('Was passiert, wenn im Audit etwas fehlt?',
     'Dann reichen wir es nach, das ist kein Drama. Wir stellen vor, was sich geändert hat, der Auditor stellt '
     'seine Fragen, wir haben die Nachweise. Wenn Hinweise oder Anregungen kommen, arbeiten wir die ein. '
     'Das ist der Normalfall, nicht die Ausnahme.'),
    ('Wie viel Aufwand ist das dauerhaft, nach der Zertifizierung?',
     'Einmal im Jahr durchgehen und aktualisieren – das sind drei, vier, fünf Stunden, dann ist das Thema '
     'wieder erledigt. Wer es drei, vier Jahre liegen lässt, fängt dagegen praktisch von vorne an.'),
]

FONT_STACK = ('-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, '
              '"Helvetica Neue", Arial, sans-serif')

STYLE = ('<style>\n'
         '  body{font-family:' + FONT_STACK + ';}\n'
         '  .prose-td{vertical-align:top;}\n'
         '</style>')


# --------------------------------------------------------------------------- #
# BAUSTEINE
# --------------------------------------------------------------------------- #

def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


def head(title, desc, url, extra_schema=None, up=''):
    schema_html = ''
    for s in (extra_schema or []):
        schema_html += ('    <script type="application/ld+json">'
                        + json.dumps(s, ensure_ascii=False) + '</script>\n')
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="canonical" href="{url}">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <meta name="author" content="Holger Grosser">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="de_DE">
    <meta property="og:site_name" content="QM-Guru · Holger Grosser">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{SITE_BASE}/images/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(desc)}">
    <meta name="twitter:image" content="{SITE_BASE}/images/og-image.jpg">
    <link rel="icon" href="{up}images/favicon.svg" type="image/svg+xml">
    <link rel="stylesheet" href="{up}assets/tailwind.css">
{STYLE}
{schema_html}</head>
<body class="bg-white text-gray-900">
'''


def header_html():
    return f'''
    <header class="bg-white border-b sticky top-0 z-50 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="{HAUPTDOMAIN}" class="text-2xl font-bold text-blue-600">QM-Guru</a>
            <div class="flex items-center gap-3">
                <a href="{TELEFON_LINK}" class="hidden sm:inline text-gray-600 hover:text-gray-900">{TELEFON}</a>
                <a href="{CALENDLY}" class="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700">Termin buchen</a>
            </div>
        </div>
    </header>
'''


def referenzen_html(slug):
    stimmen = [s for s in ECHTE_STIMMEN if s[2] in (None, slug)]
    if stimmen:
        cards = ''
        for zitat, nennung, _ in stimmen:
            cards += f'''
                <figure class="bg-white rounded-xl p-6 shadow">
                    <blockquote class="text-gray-700">„{esc(zitat)}"</blockquote>
                    <figcaption class="mt-4 text-sm text-gray-500">— {esc(nennung)}</figcaption>
                </figure>'''
        inner = f'<div class="grid md:grid-cols-2 gap-6 mb-8">{cards}</div>'
    else:
        # Bewusst keine erfundenen Zitate. Stattdessen Verweis auf nachprüfbare Quellen.
        inner = ('<p class="text-lg text-gray-700 mb-8 max-w-2xl mx-auto">'
                 'Seit 1994 begleite ich Unternehmen durch die ISO 9001 – vom Handwerksbetrieb '
                 'bis zum Mittelständler mit mehreren Standorten. Bewertungen und Referenzen '
                 'stehen öffentlich einsehbar auf der Hauptseite.</p>')
    return f'''
    <section class="py-16 bg-gray-50">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h2 class="text-3xl font-bold mb-6">Referenzen</h2>
            {inner}
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="{REFERENZEN}" class="border-2 border-blue-600 text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-blue-50">Kundenbewertungen ansehen</a>
                <a href="{GOOGLE_MAPS}" rel="nofollow" class="border-2 border-gray-300 text-gray-700 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100">Bewertungen bei Google</a>
            </div>
        </div>
    </section>
'''


def cta_html():
    return f'''
    <section class="py-16 bg-blue-600 text-white">
        <div class="max-w-3xl mx-auto px-4 text-center">
            <h2 class="text-3xl font-bold mb-4">Klären wir, was in Ihrem Fall nötig ist</h2>
            <p class="text-lg mb-8 text-blue-100">Kostenloses Erstgespräch, 30 Minuten, ohne Verpflichtung.
            Danach wissen Sie, was auf Sie zukommt – auch wenn Sie sich dagegen entscheiden.</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="{CALENDLY}" class="bg-white text-blue-600 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100">Termin buchen</a>
                <a href="{KOSTENRECHNER}" class="bg-blue-700 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-800">Kosten berechnen</a>
                <a href="{TELEFON_LINK}" class="bg-blue-700 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-800">{TELEFON}</a>
            </div>
        </div>
    </section>
'''


def footer_html(aktuelle_slug=None, up=''):
    branchen_links = ''
    for b in BRANCHEN:
        if b['slug'] == aktuelle_slug:
            branchen_links += f'                        <li class="text-white">{esc(b["name"])}</li>\n'
        else:
            branchen_links += (f'                        <li><a href="{up}{b["slug"]}.html" class="hover:text-white">'
                               f'{esc(b["name"])}</a></li>\n')
    return f'''
    <footer class="bg-gray-900 text-gray-400 py-12">
        <div class="max-w-6xl mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8 mb-8">
                <div>
                    <h3 class="text-white font-bold mb-4">QM-Guru</h3>
                    <p class="text-sm mb-4">Holger Grosser QM Dienstleistungen<br>Simonstr. 14<br>90763 Fürth</p>
                    <div class="space-y-2 text-sm">
                        <div><a href="{TELEFON_LINK}" class="hover:text-white">{TELEFON}</a></div>
                        <div><a href="{WHATSAPP}" rel="nofollow" class="hover:text-white">WhatsApp</a></div>
                    </div>
                </div>
                <div>
                    <h3 class="text-white font-bold mb-4">Branchen</h3>
                    <ul class="space-y-2 text-sm">
{branchen_links}                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-bold mb-4">Themen auf qm-guru.de</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="{HAUPTDOMAIN}/iso-9001-beratung/" class="hover:text-white">ISO 9001 Beratung</a></li>
                        <li><a href="{KOSTENRECHNER}" class="hover:text-white">Kosten berechnen</a></li>
                        <li><a href="{HAUPTDOMAIN}/iso-9001-express/" class="hover:text-white">Express-Zertifizierung</a></li>
                        <li><a href="{HAUPTDOMAIN}/fordergelder-fur-die-iso-9001-zertifizierung/" class="hover:text-white">BAFA-Förderung</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-bold mb-4">Rechtliches</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="{up}faq/" class="hover:text-white">Fragen &amp; Antworten</a></li>
                        <li><a href="{HAUPTDOMAIN}" class="hover:text-white">Hauptseite</a></li>
                        <li><a href="{IMPRESSUM}" rel="nofollow" class="hover:text-white">Impressum</a></li>
                        <li><a href="{DATENSCHUTZ}" rel="nofollow" class="hover:text-white">Datenschutz</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 pt-8 text-center text-sm">
                <p>&copy; {JAHR} Holger Grosser QM Dienstleistungen</p>
            </div>
        </div>
    </footer>

    <a href="{WHATSAPP}" rel="nofollow" aria-label="WhatsApp-Beratung"
       class="fixed bottom-6 right-6 bg-green-500 text-white px-5 py-4 rounded-full shadow-lg hover:bg-green-600 z-50 font-semibold">
        WhatsApp
    </a>

</body>
</html>
'''


# --------------------------------------------------------------------------- #
# BRANCHENSEITE
# --------------------------------------------------------------------------- #

def branchen_schema(b, url):
    service = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": f"ISO 9001 Beratung für {b['name_full']}",
        "serviceType": "ISO 9001 Beratung",
        "url": url,
        "areaServed": {"@type": "Country", "name": "Deutschland"},
        "provider": {
            "@type": "ProfessionalService",
            "name": "Holger Grosser QM Dienstleistungen",
            "url": HAUPTDOMAIN,
            "telephone": "+49 911 49522541",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Simonstr. 14",
                "postalCode": "90763",
                "addressLocality": "Fürth",
                "addressCountry": "DE",
            },
        },
        "audience": {"@type": "Audience", "audienceType": b['name_full']},
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for f, a in b['faq']
        ],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "QM-Guru", "item": HAUPTDOMAIN},
            {"@type": "ListItem", "position": 2, "name": "ISO 9001 nach Branche", "item": f"{SITE_BASE}/"},
            {"@type": "ListItem", "position": 3, "name": b['name'], "item": url},
        ],
    }
    return [service, faq, breadcrumb]


def generate_branchen_page(b):
    url = f"{SITE_BASE}/{b['slug']}.html"
    h = head(b['meta_title'], b['meta_desc'], url, branchen_schema(b, url))

    probleme = ''
    for titel, text in b['probleme']:
        probleme += f'''
                <div class="bg-white rounded-xl p-6 shadow border-l-4 border-red-400">
                    <h3 class="font-bold text-lg mb-2">{esc(titel)}</h3>
                    <p class="text-gray-700">{esc(text)}</p>
                </div>'''

    zeilen = ''
    for abschnitt, schwach, nachweis in b['normtabelle']:
        zeilen += f'''
                    <tr class="border-b">
                        <td class="prose-td py-4 pr-4 font-semibold text-blue-700 align-top">{esc(abschnitt)}</td>
                        <td class="prose-td py-4 pr-4 text-gray-700">{esc(schwach)}</td>
                        <td class="prose-td py-4 text-gray-700">{esc(nachweis)}</td>
                    </tr>'''

    dokumente = ''
    for d in b['dokumente']:
        dokumente += ('                <li class="flex gap-3"><span class="text-green-600 font-bold">&#10003;</span>'
                      f'<span>{esc(d)}</span></li>\n')

    phasen_titel = ['Bestandsaufnahme', 'Aufbau der Dokumentation', 'Auditvorbereitung']
    phasen = ''
    for i, (pt, ptext) in enumerate(zip(phasen_titel, b['phasen']), start=1):
        phasen += f'''
                <div class="bg-white rounded-xl p-6 shadow">
                    <div class="text-blue-600 font-bold text-3xl mb-2">{i}</div>
                    <h3 class="font-bold text-lg mb-2">{esc(pt)}</h3>
                    <p class="text-gray-700">{esc(ptext)}</p>
                </div>'''

    faq = ''
    for frage, antwort in b['faq']:
        faq += f'''
                <details class="bg-white rounded-xl p-6 shadow">
                    <summary class="font-bold text-lg cursor-pointer">{esc(frage)}</summary>
                    <p class="text-gray-700 mt-3">{esc(antwort)}</p>
                </details>'''

    verwandt = ''
    if b['verwandt']:
        vurl, vtext = b['verwandt']
        verwandt = f'''
            <div class="mt-8 bg-blue-50 border border-blue-200 rounded-xl p-6">
                <a href="{vurl}" class="text-blue-700 font-semibold hover:underline">{esc(vtext)} &rarr;</a>
            </div>'''

    andere = ''
    for other in BRANCHEN:
        if other['slug'] == b['slug']:
            continue
        andere += (f'                <a href="{other["slug"]}.html" class="bg-white border rounded-lg px-4 py-3 '
                   f'hover:border-blue-500 hover:text-blue-600">{other["icon"]} {esc(other["name"])}</a>\n')

    body = f'''
    <section class="bg-gradient-to-br from-blue-50 to-white py-16">
        <div class="max-w-4xl mx-auto px-4">
            <p class="text-sm font-bold tracking-widest text-blue-600 mb-4">SPEZIALISIERT AUF {esc(b['name_upper'])}</p>
            <h1 class="text-4xl md:text-5xl font-bold mb-6">{esc(b['h1'])}</h1>
            <p class="text-xl text-gray-700 mb-8 max-w-3xl">{esc(b['hero_sub'])}</p>
            <div class="flex flex-col sm:flex-row gap-4">
                <a href="{CALENDLY}" class="bg-blue-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-700">Kostenloses Erstgespräch</a>
                <a href="{KOSTENRECHNER}" class="bg-white border-2 border-blue-600 text-blue-600 px-8 py-4 rounded-lg font-semibold hover:bg-blue-50">Kosten berechnen</a>
            </div>
            <p class="text-sm text-gray-500 mt-6">Bis zu 1.750 &euro; BAFA-Förderung möglich &middot; 100 % Online-Beratung &middot; Zertifizierungsreif in 2&ndash;3 Monaten</p>
        </div>
    </section>

    <section class="py-16">
        <div class="max-w-5xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-3">Warum {esc(b['name_full'])} bei uns landen</h2>
            <p class="text-gray-600 mb-10 max-w-3xl">{esc(b['kontext'])}</p>
            <div class="grid md:grid-cols-3 gap-6">{probleme}
            </div>
        </div>
    </section>

    <section class="py-16 bg-gray-50">
        <div class="max-w-6xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-3">Woran es bei {esc(b['name_full'])} im Audit typischerweise hakt</h2>
            <p class="text-gray-600 mb-10 max-w-3xl">Diese Punkte kommen in dieser Branche immer wieder &ndash;
            und sie sind der Grund, warum ein Standard-QM-Handbuch aus dem Internet hier nicht trägt.</p>
            <div class="overflow-x-auto bg-white rounded-xl shadow p-6">
                <table class="w-full text-left text-sm">
                    <thead>
                        <tr class="border-b-2 border-gray-200">
                            <th class="py-3 pr-4">Normabschnitt</th>
                            <th class="py-3 pr-4">Typische Schwachstelle</th>
                            <th class="py-3">Was der Auditor sehen will</th>
                        </tr>
                    </thead>
                    <tbody>{zeilen}
                    </tbody>
                </table>
            </div>
        </div>
    </section>

    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-3">Was am Ende bei Ihnen liegt</h2>
            <p class="text-gray-600 mb-8">Keine Handbuchsammlung, sondern die Dokumente, die in Ihrer Branche
            tatsächlich gebraucht und im Audit auch gezeigt werden.</p>
            <ul class="space-y-3 text-gray-800">
{dokumente}            </ul>
            {verwandt}
        </div>
    </section>

    <section class="py-16 bg-gray-50">
        <div class="max-w-5xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-10">So läuft es ab</h2>
            <div class="grid md:grid-cols-3 gap-6">{phasen}
            </div>
        </div>
    </section>

    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-3">Was das kostet</h2>
            <p class="text-gray-700 mb-6">Der Aufwand hängt vor allem von der Mitarbeiterzahl und der Zahl der
            Standorte ab, nicht vom Umsatz. Über die BAFA-Förderung sind bis zu 1.750 &euro; erstattungsfähig,
            sofern die Voraussetzungen erfüllt sind.</p>
            <p class="text-gray-700 mb-8">Hinzu kommen die Gebühren der Zertifizierungsstelle, die separat
            abgerechnet werden. Was in Ihrem Fall zusammenkommt, rechnen Sie in zwanzig Sekunden selbst aus.</p>
            <a href="{KOSTENRECHNER}" class="inline-block bg-blue-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-700">Kosten für Ihren Betrieb berechnen</a>
        </div>
    </section>

    <section class="py-16 bg-gray-50">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-10">Häufige Fragen aus dieser Branche</h2>
            <div class="space-y-4">{faq}
            </div>
        </div>
    </section>

    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4">
            <div class="flex flex-col md:flex-row gap-8 items-center bg-gray-50 rounded-2xl p-8">
                <img src="images/holger-grosser.jpg" alt="Holger Grosser, QM-Berater"
                     class="w-40 h-40 rounded-full object-cover border-4 border-blue-500" loading="lazy" width="160" height="160">
                <div>
                    <h2 class="text-2xl font-bold mb-1">Holger Grosser</h2>
                    <p class="text-blue-600 mb-4">QM-Berater seit 1994 &middot; BAFA-zugelassen</p>
                    <p class="text-gray-700">Ich berate ausschließlich selbst &ndash; Sie haben von der ersten Stunde
                    bis zum Zertifizierungsaudit denselben Ansprechpartner. Mein Ansatz ist die schlankest
                    mögliche Dokumentation, die das Audit besteht und die Sie danach auch wirklich weiterführen.</p>
                </div>
            </div>
        </div>
    </section>
{referenzen_html(b['slug'])}
    <section class="py-12 bg-gray-50 border-t">
        <div class="max-w-5xl mx-auto px-4">
            <h2 class="text-xl font-bold mb-6">ISO 9001 in anderen Branchen</h2>
            <div class="flex flex-wrap gap-3">
{andere}            </div>
        </div>
    </section>
{cta_html()}'''

    return h + header_html() + body + footer_html(b['slug'])


# --------------------------------------------------------------------------- #
# ÜBERSICHTSSEITE
# --------------------------------------------------------------------------- #

def generate_index_page():
    url = f'{SITE_BASE}/'
    title = 'ISO 9001 Beratung nach Branche | QM-Guru Holger Grosser'
    desc = ('ISO 9001 Beratung zugeschnitten auf Ihre Branche: Produktion, Maschinenbau, Handel, '
            'IT, Sicherheit, Reinigung. 30+ Jahre Erfahrung, BAFA-Förderung bis 1.750 Euro.')

    schema = [{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": f,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for f, a in ALLGEMEINE_FAQ
        ],
    }, {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": title,
        "url": url,
        "isPartOf": {"@type": "WebSite", "name": "QM-Guru", "url": HAUPTDOMAIN},
        "hasPart": [
            {"@type": "WebPage", "name": f"ISO 9001 für {b['name_full']}",
             "url": f"{SITE_BASE}/{b['slug']}.html"} for b in BRANCHEN
        ],
    }]

    karten = ''
    for b in BRANCHEN:
        karten += f'''
                <a href="{b['slug']}.html" class="group bg-white rounded-2xl p-8 shadow hover:shadow-xl transition border-2 border-transparent hover:border-blue-500">
                    <div class="text-4xl mb-4">{b['icon']}</div>
                    <h3 class="text-xl font-bold mb-3 group-hover:text-blue-600">{esc(b['name_full'])}</h3>
                    <p class="text-gray-600 text-sm mb-4">{esc(b['probleme'][0][0])}</p>
                    <span class="text-blue-600 font-semibold text-sm">Zur Branchenseite &rarr;</span>
                </a>'''

    allgemeine_faq = ''
    for frage, antwort in ALLGEMEINE_FAQ:
        allgemeine_faq += f'''
                <details class="bg-white rounded-xl p-6 shadow">
                    <summary class="font-bold text-lg cursor-pointer">{esc(frage)}</summary>
                    <p class="text-gray-700 mt-3">{esc(antwort)}</p>
                </details>'''

    body = f'''
    <section class="bg-gradient-to-br from-blue-50 to-white py-20">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-6">ISO 9001 &ndash; zugeschnitten auf Ihre Branche</h1>
            <p class="text-xl text-gray-700 mb-8">Ein QM-System aus der Serienfertigung passt keinem
            Dienstleister, und ein Handelssystem hilft keinem Maschinenbauer. Wählen Sie Ihre Branche &ndash;
            dort steht, woran es dort im Audit konkret hakt.</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="{CALENDLY}" class="bg-blue-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-700">Kostenloses Erstgespräch</a>
                <a href="{KOSTENRECHNER}" class="bg-white border-2 border-blue-600 text-blue-600 px-8 py-4 rounded-lg font-semibold hover:bg-blue-50">Kosten berechnen</a>
            </div>
        </div>
    </section>

    <section class="py-16 bg-gray-50">
        <div class="max-w-6xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-10 text-center">Wählen Sie Ihre Branche</h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">{karten}
            </div>
        </div>
    </section>

    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-4">Warum branchenspezifisch?</h2>
            <p class="text-gray-700 mb-4">Die ISO 9001 ist bewusst allgemein formuliert &ndash; sie gilt für den
            Maschinenbauer genauso wie für den Pflegedienst. Genau das macht sie in der Praxis schwierig:
            Was in der Fertigung selbstverständlich ist, ergibt beim Softwarehaus keinen Sinn, und umgekehrt.</p>
            <p class="text-gray-700 mb-4">Die Abweichungen im Zertifizierungsaudit sind deshalb erstaunlich
            berechenbar. In der Produktion sind es fast immer Prüfmittel und Sperrware. Im Maschinenbau ist es
            Kapitel 8.3. Beim Dienstleister fehlt der Nachweis der erbrachten Leistung. Beim Sicherheitsdienst
            die Qualifikationsnachweise bei Fluktuation.</p>
            <p class="text-gray-700">Auf den Branchenseiten steht jeweils, welche Normabschnitte dort erfahrungsgemäß
            zum Problem werden und welchen Nachweis der Auditor konkret sehen will.</p>
        </div>
    </section>

    <section class="py-16 bg-gray-50">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-3">Fragen, die alle stellen</h2>
            <p class="text-gray-600 mb-8">Unabhängig von der Branche kommen diese Fragen in fast jeder Beratung –
            hier die Antworten, die ich auch am Telefon gebe.</p>
            <p class="mb-10"><a href="faq/" class="text-blue-700 font-semibold hover:underline">Zur vollständigen Fragensammlung mit über 70 Antworten &rarr;</a></p>
            <div class="space-y-4">{allgemeine_faq}
            </div>
        </div>
    </section>
{referenzen_html(None)}{cta_html()}'''

    return head(title, desc, url, schema) + header_html() + body + footer_html(None)



# --------------------------------------------------------------------------- #
# FAQ-BIBLIOTHEK  (liegt unter public/faq/)
# --------------------------------------------------------------------------- #

def faq_nav(aktiv=None, up=''):
    links = f'<a href="{up}faq/" class="px-3 py-2 rounded-lg hover:bg-blue-50 text-blue-700">Übersicht</a>\n'
    for f in FAQ_SEITEN:
        cls = ('px-3 py-2 rounded-lg bg-blue-600 text-white' if f['slug'] == aktiv
               else 'px-3 py-2 rounded-lg hover:bg-blue-50 text-blue-700')
        links += f'                <a href="{up}faq/{f["slug"]}.html" class="{cls}">{esc(f["titel"])}</a>\n'
    return f'''
    <nav class="bg-white border-b">
        <div class="max-w-6xl mx-auto px-4 py-4 flex flex-wrap gap-2 text-sm">
{links}            </div>
    </nav>
'''


def generate_faq_seite(seite):
    url = f"{SITE_BASE}/faq/{seite['slug']}.html"
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "name": seite['titel'],
            "url": url,
            "mainEntity": [
                {"@type": "Question", "name": f,
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for f, a in seite['fragen']
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "QM-Guru", "item": HAUPTDOMAIN},
                {"@type": "ListItem", "position": 2, "name": "Fragen & Antworten", "item": f"{SITE_BASE}/faq/"},
                {"@type": "ListItem", "position": 3, "name": seite['titel'], "item": url},
            ],
        },
    ]

    fragen = ''
    for i, (frage, antwort) in enumerate(seite['fragen'], start=1):
        fragen += f'''
                <article class="bg-white rounded-xl p-8 shadow" id="f{i}">
                    <h2 class="text-xl font-bold mb-4">{esc(frage)}</h2>
                    <p class="text-gray-700 leading-relaxed">{esc(antwort)}</p>
                </article>'''

    inhalt = ''
    for i, (frage, _) in enumerate(seite['fragen'], start=1):
        inhalt += f'                <li><a href="#f{i}" class="text-blue-700 hover:underline">{esc(frage)}</a></li>\n'

    weitere = ''
    for f in FAQ_SEITEN:
        if f['slug'] == seite['slug']:
            continue
        weitere += (f'                <a href="{f["slug"]}.html" class="bg-white border rounded-lg px-4 py-3 '
                    f'hover:border-blue-500 hover:text-blue-600">{esc(f["titel"])}</a>\n')

    body = f'''
    <section class="bg-gradient-to-br from-blue-50 to-white py-14">
        <div class="max-w-4xl mx-auto px-4">
            <p class="text-sm text-gray-500 mb-3"><a href="./" class="hover:underline">Fragen &amp; Antworten</a> &rsaquo; {esc(seite['titel'])}</p>
            <h1 class="text-4xl font-bold mb-4">{esc(seite['titel'])}</h1>
            <p class="text-lg text-gray-700 max-w-3xl">{esc(seite['intro'])}</p>
        </div>
    </section>

    <section class="py-10 bg-white border-b">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-sm font-bold uppercase tracking-wide text-gray-500 mb-4">Auf dieser Seite</h2>
            <ul class="space-y-2 text-sm">
{inhalt}            </ul>
        </div>
    </section>

    <section class="py-14 bg-gray-50">
        <div class="max-w-4xl mx-auto px-4 space-y-6">{fragen}
        </div>
    </section>

    <section class="py-12">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-xl font-bold mb-6">Weitere Themen</h2>
            <div class="flex flex-wrap gap-3">
{weitere}            </div>
        </div>
    </section>
{cta_html()}'''

    return (head(seite['meta_title'], seite['meta_desc'], url, schema, up='../')
            + header_html() + faq_nav(seite['slug'], up='../') + body
            + footer_html(None, up='../'))


def generate_faq_index():
    url = f'{SITE_BASE}/faq/'
    title = 'ISO 9001 – Fragen und Antworten aus der Beratungspraxis'
    desc = ('Über 70 echte Fragen aus ISO-9001-Beratungen, beantwortet ohne Normdeutsch: '
            'Dokumentation, Risiken, Lieferanten, Schulungen, Audit.')
    anzahl = sum(len(f['fragen']) for f in FAQ_SEITEN)

    schema = [{
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": title,
        "url": url,
        "isPartOf": {"@type": "WebSite", "name": "QM-Guru", "url": HAUPTDOMAIN},
        "hasPart": [
            {"@type": "WebPage", "name": f['titel'], "url": f"{SITE_BASE}/faq/{f['slug']}.html"}
            for f in FAQ_SEITEN
        ],
    }]

    karten = ''
    for f in FAQ_SEITEN:
        vorschau = ''
        for frage, _ in f['fragen'][:3]:
            vorschau += f'<li class="text-sm text-gray-600">{esc(frage)}</li>'
        karten += f'''
                <a href="{f['slug']}.html" class="group bg-white rounded-2xl p-7 shadow hover:shadow-xl transition border-2 border-transparent hover:border-blue-500">
                    <h2 class="text-lg font-bold mb-3 group-hover:text-blue-600">{esc(f['titel'])}</h2>
                    <ul class="space-y-1 mb-4 list-disc list-inside">{vorschau}</ul>
                    <span class="text-blue-600 font-semibold text-sm">{len(f['fragen'])} Fragen ansehen &rarr;</span>
                </a>'''

    body = f'''
    <section class="bg-gradient-to-br from-blue-50 to-white py-16">
        <div class="max-w-4xl mx-auto px-4">
            <h1 class="text-4xl md:text-5xl font-bold mb-6">ISO 9001 – Fragen und Antworten</h1>
            <p class="text-xl text-gray-700 mb-4">{anzahl} Fragen, die mir Kunden in über dreißig Jahren
            Beratung immer wieder gestellt haben – beantwortet so, wie ich sie am Telefon beantworte.
            Ohne Normdeutsch und ohne den Versuch, die Sache größer zu machen, als sie ist.</p>
            <p class="text-gray-600">Die meisten Antworten laufen auf dasselbe hinaus: weniger Dokumentation,
            als Sie befürchten – und dafür Nachweise, die im Alltag ohnehin entstehen.</p>
        </div>
    </section>

    <section class="py-16 bg-gray-50">
        <div class="max-w-6xl mx-auto px-4">
            <div class="grid md:grid-cols-2 gap-6">{karten}
            </div>
        </div>
    </section>

    <section class="py-14">
        <div class="max-w-4xl mx-auto px-4">
            <h2 class="text-2xl font-bold mb-4">Ihre Frage ist nicht dabei?</h2>
            <p class="text-gray-700 mb-6">Dann stellen Sie sie direkt. Ein Erstgespräch dauert dreißig Minuten
            und kostet nichts – danach wissen Sie, was in Ihrem Fall zu tun ist, auch wenn Sie sich am Ende
            gegen eine Zusammenarbeit entscheiden.</p>
            <a href="{CALENDLY}" class="inline-block bg-blue-600 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-700">Termin vereinbaren</a>
        </div>
    </section>

    <section class="py-12 bg-gray-50 border-t">
        <div class="max-w-6xl mx-auto px-4">
            <h2 class="text-xl font-bold mb-6">ISO 9001 nach Branche</h2>
            <div class="flex flex-wrap gap-3">
{"".join(f'                <a href="../{b["slug"]}.html" class="bg-white border rounded-lg px-4 py-3 hover:border-blue-500 hover:text-blue-600">{b["icon"]} {esc(b["name"])}</a>' + chr(10) for b in BRANCHEN)}            </div>
        </div>
    </section>
{cta_html()}'''

    return (head(title, desc, url, schema, up='../') + header_html()
            + faq_nav(None, up='../') + body + footer_html(None, up='../'))

# --------------------------------------------------------------------------- #
# SITEMAP / ROBOTS
# --------------------------------------------------------------------------- #

def generate_sitemap(datum='2026-08-18'):
    urls = ([f'{SITE_BASE}/']
            + [f"{SITE_BASE}/{b['slug']}.html" for b in BRANCHEN]
            + [f'{SITE_BASE}/faq/']
            + [f"{SITE_BASE}/faq/{f['slug']}.html" for f in FAQ_SEITEN])
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for i, u in enumerate(urls):
        out.append('  <url>')
        out.append(f'    <loc>{u}</loc>')
        out.append(f'    <lastmod>{datum}</lastmod>')
        out.append(f'    <priority>{"1.0" if i == 0 else "0.8"}</priority>')
        out.append('  </url>')
    out.append('</urlset>')
    return '\n'.join(out) + '\n'


def generate_robots():
    return f'User-agent: *\nAllow: /\n\nSitemap: {SITE_BASE}/sitemap.xml\n'


# --------------------------------------------------------------------------- #

def main():
    out = Path('public')
    out.mkdir(exist_ok=True)

    print('QMBerater Landing Pages Generator v2')
    print('=' * 52)
    print(f'SITE_BASE: {SITE_BASE}')
    print()

    for b in BRANCHEN:
        (out / f"{b['slug']}.html").write_text(generate_branchen_page(b), encoding='utf-8')
        print(f"  ok  {b['slug']}.html")

    (out / 'index.html').write_text(generate_index_page(), encoding='utf-8')
    print('  ok  index.html')

    faqdir = out / 'faq'
    faqdir.mkdir(exist_ok=True)
    for f in FAQ_SEITEN:
        (faqdir / f"{f['slug']}.html").write_text(generate_faq_seite(f), encoding='utf-8')
        print(f"  ok  faq/{f['slug']}.html")
    (faqdir / 'index.html').write_text(generate_faq_index(), encoding='utf-8')
    print('  ok  faq/index.html')

    (out / 'sitemap.xml').write_text(generate_sitemap(), encoding='utf-8')
    (out / 'robots.txt').write_text(generate_robots(), encoding='utf-8')
    print('  ok  sitemap.xml, robots.txt')

    print()
    print('Vor dem Deploy pruefen:')
    print('  - public/images/og-image.jpg vorhanden?')
    print('  - public/images/favicon.svg vorhanden?')
    print('  - ECHTE_STIMMEN gefuellt oder bewusst leer gelassen?')


if __name__ == '__main__':
    main()
