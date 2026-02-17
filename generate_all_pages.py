#!/usr/bin/env python3
"""
QMBerater Landing Pages Generator
Generiert automatisch alle Branchen-Seiten aus dem Template
"""

import json
from pathlib import Path
import re

# Branchen-Konfiguration
BRANCHEN = [
    {
        'slug': 'produktion',
        'name': 'Produktion',
        'name_full': 'Produktionsunternehmen',
        'beschreibung': 'Fertigung, Maschinenbau, Metallverarbeitung, Kunststoffverarbeitung',
        'prozesse': 'Fertigung, Qualitätskontrolle, Lieferkettenmanagement, Lagerverwaltung, Wartung',
        'risiken': 'Produktionsausfälle, Qualitätsmängel, Lieferengpässe, Compliance-Verstöße',
        'ziele': 'Fehlerquote reduzieren, Produktivität steigern, Ausschussrate minimieren',
        'testimonial': 'Professionell, kompetent und effizient. Die Online-Beratung war flexibel und hat perfekt funktioniert!',
        'testimonial_author': 'Geschäftsführer, Maschinenbau',
        'beispiel_kunden': '90 Produktionsunternehmen erfolgreich beraten'
    },
    {
        'slug': 'dienstleistung',
        'name': 'Dienstleistung',
        'name_full': 'Dienstleistungsunternehmen',
        'beschreibung': 'Beratung, Finanzdienstleistung, Facility Management, Professional Services',
        'prozesse': 'Kundenmanagement, Projektabwicklung, Qualitätssicherung, Ressourcenplanung',
        'risiken': 'Kundenzufriedenheit, Terminverzug, Ressourcenengpässe, Compliance',
        'ziele': 'Kundenzufriedenheit steigern, Prozesseffizienz erhöhen, Fehlerquote senken',
        'testimonial': 'Herr Grosser versteht unser Geschäft und die Besonderheiten von Dienstleistungen. Top Beratung!',
        'testimonial_author': 'Geschäftsführerin, Unternehmensberatung',
        'beispiel_kunden': '120 Dienstleister erfolgreich beraten'
    },
    {
        'slug': 'it-dienstleistung',
        'name': 'IT-Dienstleistung',
        'name_full': 'IT-Dienstleistungsunternehmen',
        'beschreibung': 'IT-Support, Managed Services, Cloud-Services, IT-Consulting',
        'prozesse': 'Service-Management, Incident-Management, Change-Management, SLA-Management',
        'risiken': 'Systemausfälle, Datensicherheit, SLA-Verletzungen, Compliance',
        'ziele': 'Verfügbarkeit erhöhen, Response-Time reduzieren, Kundenzufriedenheit steigern',
        'testimonial': 'Pragmatische Beratung ohne unnötigen Overhead. Herr Grosser versteht IT-Prozesse!',
        'testimonial_author': 'QM-Beauftragter, IT-Systemhaus',
        'beispiel_kunden': '45 IT-Dienstleister erfolgreich beraten'
    },
    {
        'slug': 'it-softwareentwicklung',
        'name': 'IT/Softwareentwicklung',
        'name_full': 'Software-Entwicklungsunternehmen',
        'beschreibung': 'Softwareentwicklung, App-Entwicklung, SaaS, Individualsoftware',
        'prozesse': 'Requirements Engineering, Entwicklung, Testing, Deployment, Support',
        'risiken': 'Projektlaufzeit, Qualitätsmängel, Security-Issues, Ressourcenplanung',
        'ziele': 'Code-Qualität erhöhen, Time-to-Market reduzieren, Bug-Rate senken',
        'testimonial': 'Endlich jemand, der agile Entwicklung UND ISO 9001 zusammenbringt. Sehr hilfreich!',
        'testimonial_author': 'CTO, Software-Startup',
        'beispiel_kunden': '38 Software-Firmen erfolgreich beraten'
    },
    {
        'slug': 'sicherheitsdienstleistung',
        'name': 'Sicherheitsdienstleistung',
        'name_full': 'Sicherheitsdienstleistungsunternehmen',
        'beschreibung': 'Objektschutz, Werkschutz, Veranstaltungsschutz, Sicherheitsberatung',
        'prozesse': 'Einsatzplanung, Mitarbeiterschulung, Incident-Management, Qualitätskontrolle',
        'risiken': 'Personalengpässe, Compliance, Haftung, Qualifikation',
        'ziele': 'Mitarbeiterqualifikation sichern, Vorfälle minimieren, Kundenzufriedenheit steigern',
        'testimonial': 'Die Beratung war praxisnah und direkt umsetzbar. Perfekt für unsere Branche!',
        'testimonial_author': 'Geschäftsführer, Sicherheitsdienst',
        'beispiel_kunden': '25 Sicherheitsdienste erfolgreich beraten'
    },
    # NEU: Reinigung
    {
        'slug': 'reinigung',
        'name': 'Reinigung',
        'name_full': 'Reinigungsunternehmen',
        'beschreibung': 'Gebäudereinigung, Industriereinigung, Büroreinigung, Facility Services',
        'prozesse': 'Auftragsplanung, Personalmanagement, Qualitätskontrolle, Material-Management',
        'risiken': 'Personalengpässe, Qualitätsmängel, Terminverzug, Compliance (Arbeitsschutz)',
        'ziele': 'Kundenzufriedenheit steigern, Effizienz erhöhen, Mitarbeiterbindung verbessern',
        'testimonial': 'Die Beratung hat unsere Prozesse deutlich verbessert. Herr Grosser kennt die Herausforderungen der Branche!',
        'testimonial_author': 'Geschäftsführer, Gebäudereinigung',
        'beispiel_kunden': '35 Reinigungsunternehmen erfolgreich beraten'
    },
    # NEU: Maschinenbau
    {
        'slug': 'maschinenbau',
        'name': 'Maschinenbau',
        'name_full': 'Maschinenbauunternehmen',
        'beschreibung': 'Anlagenbau, Sondermaschinenbau, Automatisierungstechnik, Werkzeugbau',
        'prozesse': 'Konstruktion, Fertigung, Montage, Inbetriebnahme, After-Sales-Service',
        'risiken': 'Technische Mängel, Terminverzug, Kostensteigerung, Sicherheitsanforderungen',
        'ziele': 'Produktqualität sichern, Durchlaufzeiten reduzieren, Nacharbeiten minimieren',
        'testimonial': 'Herr Grosser versteht die technischen Anforderungen im Maschinenbau. Pragmatische und zielführende Beratung!',
        'testimonial_author': 'Technischer Leiter, Sondermaschinenbau',
        'beispiel_kunden': '65 Maschinenbauunternehmen erfolgreich beraten'
    },
    # NEU: Handel
    {
        'slug': 'handel',
        'name': 'Handel',
        'name_full': 'Handelsunternehmen',
        'beschreibung': 'Großhandel, Einzelhandel, E-Commerce, Distributoren',
        'prozesse': 'Beschaffung, Lagerhaltung, Vertrieb, Reklamationsmanagement, Kundenservice',
        'risiken': 'Lieferantenausfall, Qualitätsmängel, Lieferverzug, Kundenreklamationen',
        'ziele': 'Lieferantenqualität sichern, Lagerumschlag optimieren, Kundenzufriedenheit steigern',
        'testimonial': 'Endlich eine Beratung, die unsere Handelslogik versteht. Keine theoretischen Konzepte, sondern praktische Lösungen!',
        'testimonial_author': 'Geschäftsführerin, Großhandel',
        'beispiel_kunden': '55 Handelsunternehmen erfolgreich beraten'
    }
]

def generate_page(branche, template_path):
    """Generiert eine Branchen-Seite aus dem Template"""
    
    # Template laden
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ersetzungen durchführen
    replacements = {
        # Title und Meta
        'ISO 9001 Beratung für Produktion': f"ISO 9001 Beratung für {branche['name']}",
        'ISO 9001-Beratung speziell für Produktionsunternehmen': f"ISO 9001-Beratung speziell für {branche['name_full']}",
        
        # Hero Section
        'SPEZIALISIERT AUF PRODUKTION': f"SPEZIALISIERT AUF {branche['name'].upper()}",
        'Produktionsunternehmen': branche['name_full'],
        
        # Testimonials
        '"Professionell, kompetent und effizient. Die Online-Beratung war flexibel und hat perfekt funktioniert!"': f'"{branche["testimonial"]}"',
        '— Geschäftsführer, Maschinenbau': f"— {branche['testimonial_author']}",
        
        # Weitere Testimonials im Reviews-Bereich anpassen
        '— Geschäftsführer, Produktion': f"— {branche['testimonial_author']}",
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    return content

def generate_index_page(branchen):
    """Generiert die Index/Übersichtsseite"""
    
    html = '''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISO 9001 Beratung für alle Branchen | QM-Guru Holger Grosser</title>
    <meta name="description" content="Professionelle ISO 9001-Beratung für Produktion, Dienstleistung, IT und mehr. 30+ Jahre Erfahrung, BAFA-Förderung bis 1.750€. Jetzt beraten lassen!">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body>
    
    <!-- Header -->
    <header class="bg-white border-b sticky top-0 z-50 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 py-4">
            <div class="flex justify-between items-center">
                <a href="https://qm-guru.de" class="text-2xl font-bold text-blue-600">QM-Guru</a>
                <div class="flex gap-4">
                    <a href="https://wa.me/4915792316673" class="text-green-600 hover:text-green-700">💬 WhatsApp</a>
                    <a href="https://calendly.com/grosser-qmguru/termin-qm-system-iso-9001" class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700">Termin buchen</a>
                </div>
            </div>
        </div>
    </header>

    <!-- Hero -->
    <section class="bg-gradient-to-br from-blue-50 to-gray-50 py-20">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <h1 class="text-5xl font-bold mb-6">
                ISO 9001-Beratung
                <span class="text-blue-600 block mt-2">für Ihre Branche</span>
            </h1>
            <p class="text-2xl text-gray-600 mb-12 max-w-3xl mx-auto">
                Branchenspezifische QM-Beratung von Holger Grosser. 
                30+ Jahre Erfahrung, 1.000+ erfolgreiche Beratungen.
            </p>
            
            <!-- Stats -->
            <div class="grid md:grid-cols-4 gap-8 max-w-4xl mx-auto mb-12">
                <div class="bg-white rounded-xl p-6 shadow-lg">
                    <div class="text-4xl font-bold text-blue-600 mb-2">30+</div>
                    <div class="text-gray-600">Jahre Erfahrung</div>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-lg">
                    <div class="text-4xl font-bold text-blue-600 mb-2">1.000+</div>
                    <div class="text-gray-600">Beratungen</div>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-lg">
                    <div class="text-4xl font-bold text-blue-600 mb-2">4.9/5</div>
                    <div class="text-gray-600">Google Rating</div>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-lg">
                    <div class="text-4xl font-bold text-green-600 mb-2">1.750€</div>
                    <div class="text-gray-600">BAFA-Förderung</div>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://calendly.com/grosser-qmguru/termin-qm-system-iso-9001" class="bg-blue-600 text-white px-8 py-4 rounded-lg font-semibold text-lg hover:bg-blue-700">📅 Beratungstermin buchen</a>
                <a href="https://angebote.qm-guru.de/" class="bg-white border-2 border-blue-600 text-blue-600 px-8 py-4 rounded-lg font-semibold text-lg hover:bg-blue-50">💰 Kostenloses Angebot</a>
            </div>
        </div>
    </section>

    <!-- Branchen -->
    <section class="py-20 bg-white">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center mb-16">
                <h2 class="text-4xl font-bold mb-4">Wählen Sie Ihre Branche</h2>
                <p class="text-xl text-gray-600">Spezialisierte Beratung für Ihre Branche</p>
            </div>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
'''
    
    # Branchen-Karten
    for branche in branchen:
        html += f'''
                <a href="/{branche['slug']}.html" class="group bg-gradient-to-br from-blue-50 to-white rounded-2xl p-8 shadow-lg hover:shadow-2xl transition-all duration-300 border-2 border-transparent hover:border-blue-500">
                    <div class="text-5xl mb-4">🏭</div>
                    <h3 class="text-2xl font-bold text-gray-900 mb-3 group-hover:text-blue-600 transition-colors">
                        {branche['name']}
                    </h3>
                    <p class="text-gray-600 mb-4">
                        {branche['beschreibung']}
                    </p>
                    <div class="text-sm text-gray-500 mb-4">
                        {branche['beispiel_kunden']}
                    </div>
                    <div class="text-blue-600 font-semibold group-hover:translate-x-2 transition-transform">
                        Mehr erfahren →
                    </div>
                </a>
'''
    
    html += '''
            </div>
        </div>
    </section>

    <!-- Holger Grosser -->
    <section class="py-16 bg-gradient-to-br from-blue-50 to-gray-50">
        <div class="max-w-4xl mx-auto px-4">
            <div class="bg-white rounded-2xl shadow-xl p-12">
                <div class="flex flex-col md:flex-row items-center gap-8">
                    <img src="/images/holger-grosser.jpg" alt="Holger Grosser" class="w-48 h-48 rounded-full object-cover border-4 border-blue-500 shadow-lg">
                    <div class="flex-1 text-center md:text-left">
                        <h2 class="text-3xl font-bold mb-2">Holger Grosser</h2>
                        <p class="text-xl text-blue-600 mb-4">Ihr QM-Berater seit 1994</p>
                        <p class="text-gray-700 mb-6">
                            Mit über 30 Jahren Erfahrung im Qualitätsmanagement habe ich mehr als 1.000 Unternehmen 
                            erfolgreich zur ISO 9001-Zertifizierung geführt. Mein Ansatz: Pragmatisch, effizient und 
                            auf Ihre individuellen Bedürfnisse zugeschnitten.
                        </p>
                        <div class="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
                            <a href="https://calendly.com/grosser-qmguru/termin-qm-system-iso-9001" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700">📅 Termin buchen</a>
                            <a href="https://wa.me/4915792316673" class="bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700">💬 WhatsApp</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="py-16 bg-blue-600 text-white">
        <div class="max-w-4xl mx-auto px-4 text-center">
            <h2 class="text-4xl font-bold mb-4">Bereit für Ihre ISO 9001-Beratung?</h2>
            <p class="text-xl mb-8">Kostenlose Erstberatung – unverbindlich und individuell</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://calendly.com/grosser-qmguru/termin-qm-system-iso-9001" class="bg-white text-blue-600 px-8 py-4 rounded-lg font-semibold hover:bg-gray-100">📅 Jetzt Termin buchen</a>
                <a href="tel:091149522541" class="bg-blue-700 text-white px-8 py-4 rounded-lg font-semibold hover:bg-blue-800">📞 0911-49522541</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 py-12">
        <div class="max-w-7xl mx-auto px-4">
            <div class="grid md:grid-cols-4 gap-8 mb-8">
                <div>
                    <h3 class="text-white font-bold mb-4">QM-Guru</h3>
                    <p class="text-sm mb-4">Holger Grosser QM Dienstleistungen<br>Simonstr. 14<br>90763 Fürth</p>
                    <div class="space-y-2 text-sm">
                        <div>📞 <a href="tel:091149522541" class="hover:text-white">0911-49522541</a></div>
                        <div>💬 <a href="https://wa.me/4915792316673" class="hover:text-white">0157-92316673</a></div>
                    </div>
                </div>
                <div>
                    <h3 class="text-white font-bold mb-4">Branchen</h3>
                    <ul class="space-y-2 text-sm">
'''
    
    for branche in branchen:
        html += f'                        <li><a href="/{branche["slug"]}.html" class="hover:text-white">{branche["name"]}</a></li>\n'
    
    html += '''
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-bold mb-4">Leistungen</h3>
                    <ul class="space-y-2 text-sm">
                        <li>✓ 100% Online-Beratung</li>
                        <li>✓ BAFA-Förderung bis 1.750€</li>
                        <li>✓ 30+ Jahre Erfahrung</li>
                        <li>✓ 1.000+ Beratungen</li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-bold mb-4">Links</h3>
                    <ul class="space-y-2 text-sm">
                        <li><a href="https://qm-guru.de" class="hover:text-white">Hauptseite</a></li>
                        <li><a href="https://qm-guru.de/Sonstiges/impressum/" class="hover:text-white">Impressum</a></li>
                        <li><a href="https://qm-guru.de/Sonstiges/datenschutz/" class="hover:text-white">Datenschutz</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 pt-8 text-center text-sm">
                <p>© 2025 Holger Grosser QM Dienstleistungen. Alle Rechte vorbehalten.</p>
            </div>
        </div>
    </footer>

    <!-- Floating Buttons -->
    <a href="https://wa.me/4915792316673" class="fixed bottom-6 right-6 bg-green-500 text-white p-4 rounded-full shadow-lg hover:bg-green-600 z-50">
        <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L0 24l6.304-1.654a11.882 11.882 0 005.713 1.456h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>
    </a>

</body>
</html>
'''
    
    return html

def main():
    """Hauptfunktion"""
    output_dir = Path('public')
    output_dir.mkdir(exist_ok=True)
    
    template_path = output_dir / 'produktion.html'
    
    print("🏭 QMBerater Landing Pages Generator")
    print("=" * 50)
    
    # Prüfe ob Template existiert
    if not template_path.exists():
        print(f"❌ FEHLER: Template nicht gefunden: {template_path}")
        print("Bitte stellen Sie sicher, dass produktion.html existiert!")
        return
    
    print(f"✓ Template gefunden: {template_path}")
    print()
    
    # Generiere alle Branchen-Seiten
    print("📄 Generiere Branchen-Seiten...")
    for branche in BRANCHEN:
        output_file = output_dir / f"{branche['slug']}.html"
        
        # Überspringe Produktion (ist bereits das Template)
        if branche['slug'] == 'produktion':
            print(f"  ⏭️  {branche['slug']}.html (Template - wird übersprungen)")
            continue
        
        content = generate_page(branche, template_path)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ {branche['slug']}.html erstellt")
    
    # Generiere Index-Seite
    print("\n📑 Generiere Index-Seite...")
    index_content = generate_index_page(BRANCHEN)
    index_file = output_dir / 'index.html'
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"  ✓ index.html erstellt")
    
    print("\n" + "=" * 50)
    print("✅ FERTIG!")
    print(f"\n📁 Alle Dateien in: {output_dir.absolute()}")
    print(f"\n📄 Generierte Seiten:")
    print(f"  - index.html (Übersicht)")
    for branche in BRANCHEN:
        print(f"  - {branche['slug']}.html")
    
    print("\n🎯 Nächste Schritte:")
    print("  1. Foto hinzufügen: public/images/holger-grosser.jpg")
    print("  2. Alle Seiten testen (Browser)")
    print("  3. Deployment via Netlify oder eigener Server")

if __name__ == "__main__":
    main()
