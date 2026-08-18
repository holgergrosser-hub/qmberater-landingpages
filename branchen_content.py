# -*- coding: utf-8 -*-
"""
Branchen-Inhalte für die ISO-9001-Landingpages.

WICHTIG: Hier steht der INHALT, nicht das Layout. Jede Branche muss sich
inhaltlich echt unterscheiden – sonst entstehen wieder Beinahe-Dubletten,
die Google als Doorway Pages einstuft.

Pflichtfelder je Branche:
  slug, name, name_full, name_upper, icon
  meta_title (max. ~60 Zeichen), meta_desc (max. ~155 Zeichen)
  h1, hero_sub
  probleme     – 3 x (titel, text)   -> branchenspezifisch!
  normtabelle  – 4-6 x (abschnitt, schwachstelle, nachweis)
  dokumente    – 5-7 Stichpunkte
  phasen       – 3 x branchenspezifischer Satz zum jeweiligen Projektschritt
  faq          – 4-5 x (frage, antwort)  -> wird als FAQPage-Schema ausgegeben
  kontext      – 1 Absatz Markt-/Ausschreibungssituation
  verwandt     – optional: (url, text) für einen weiterführenden internen Link
"""

BRANCHEN = [

    # ------------------------------------------------------------------ #
    {
        'slug': 'produktion',
        'name': 'Produktion',
        'name_full': 'Produktionsbetriebe',
        'name_upper': 'PRODUKTION',
        'icon': '🏭',
        'meta_title': 'ISO 9001 für Produktionsbetriebe | QM-Beratung',
        'meta_desc': 'ISO 9001 für Fertigung und Produktion: Prüfmittelüberwachung, '
                     'Rückverfolgbarkeit, Sperrware, Lieferantenbewertung. Beratung mit BAFA-Förderung.',
        'h1': 'ISO 9001 für Produktionsbetriebe',
        'hero_sub': 'Zertifizierungsreif in 2–3 Monaten – ohne dass Ihre Fertigung stillsteht. '
                    'Wir bauen das QM-System entlang Ihrer Fertigungsprozesse auf, nicht daneben.',

        'probleme': [
            ('Ein Großkunde macht das Zertifikat zur Vertragsbedingung',
             'In Rahmenverträgen und Lieferantenselbstauskünften taucht die ISO 9001 inzwischen '
             'standardmäßig auf. Fehlt sie, fliegen Sie aus der Lieferantenliste – unabhängig davon, '
             'wie gut Sie fertigen.'),
            ('Ausschuss und Nacharbeit sind da, aber nicht auswertbar',
             'Jeder in der Fertigung weiß ungefähr, wo es klemmt. Nur steht es nirgends so, dass man '
             'daraus eine Entscheidung ableiten könnte. Genau das fragt der Auditor unter Kapitel 9.1 ab.'),
            ('Die Prüfmittel sind ein Thema, das keiner anfassen will',
             'Messschieber in der Schublade, Kalibrierscheine irgendwo im Ordner, kein Überblick, '
             'welches Prüfmittel wann fällig ist. Das ist erfahrungsgemäß die häufigste Abweichung '
             'im Zertifizierungsaudit von Produktionsbetrieben.'),
        ],

        'normtabelle': [
            ('7.1.5 Ressourcen zur Überwachung und Messung',
             'Prüfmittel ohne Kalibrierhistorie, keine Rückführbarkeit auf Normale',
             'Prüfmittelliste mit Kalibrierintervall, Kalibrierscheine, Regelung für Prüfmittel außer Betrieb'),
            ('8.5.2 Kennzeichnung und Rückverfolgbarkeit',
             'Chargen lassen sich im Reklamationsfall nicht zurückverfolgen',
             'Chargen- oder Auftragskennzeichnung, Laufkarte/Fertigungsauftrag, Zuordnung Wareneingang → Los'),
            ('8.7 Steuerung nichtkonformer Ergebnisse',
             'Sperrware steht unmarkiert neben Gutteilen, Entscheidungen sind nicht nachvollziehbar',
             'Gekennzeichneter Sperrbereich, Sperrvermerk, dokumentierte Entscheidung (Nacharbeit / Sonderfreigabe / Verschrottung)'),
            ('8.4 Steuerung extern bereitgestellter Prozesse',
             'Lieferanten wurden nie systematisch bewertet, Wareneingang ist reine Mengenprüfung',
             'Lieferantenliste mit Bewertungskriterien, risikobasierte Wareneingangsprüfung, Reklamationsverfahren gegenüber Lieferanten'),
            ('9.1.1 Überwachung, Messung, Analyse',
             'Es gibt keine Kennzahlen, an denen sich Qualität ablesen lässt',
             'Ausschuss- und Nacharbeitsquote, Liefertreue, Reklamationsquote – mit Zielwert und Auswertung'),
            ('7.1.3 Infrastruktur',
             'Maschinenwartung passiert nach Gefühl und wird nicht dokumentiert',
             'Wartungsplan je Maschine, Wartungsnachweise, Regelung für Störungen'),
        ],

        'dokumente': [
            'Prozesslandkarte entlang Ihrer realen Fertigungskette',
            'Fertigungsauftrag / Laufkarte als zentraler Qualitätsnachweis',
            'Prüfplan Wareneingang, Zwischen- und Endprüfung',
            'Prüfmittelüberwachung mit Fälligkeitsübersicht',
            'Reklamations- und Korrekturmaßnahmenverfahren (8D-fähig)',
            'Lieferantenbewertung mit nachvollziehbaren Kriterien',
            'Wartungs- und Instandhaltungsnachweise',
        ],

        'phasen': [
            'Wir gehen einmal durch die Fertigung – vom Wareneingang bis zum Versand – und halten fest, '
            'was Sie bereits tun. Erfahrungsgemäß sind 60–70 % der Normforderungen längst erfüllt, nur nicht aufgeschrieben.',
            'Wir bauen die Dokumentation auf Ihren vorhandenen Papieren auf: Fertigungsauftrag, Prüfplan, '
            'Wartungsplan. Es entsteht kein Parallelsystem, das später keiner pflegt.',
            'Wir gehen die typischen Auditfragen für Produktionsbetriebe durch – Prüfmittel, Sperrware, '
            'Rückverfolgbarkeit – und schließen die Lücken, bevor der Zertifizierer kommt.',
        ],

        'faq': [
            ('Brauchen wir für die ISO 9001 eine FMEA?',
             'Nein. Die ISO 9001 fordert keine FMEA. Sie fordert in Kapitel 6.1, dass Sie Risiken und Chancen '
             'bestimmen und behandeln – das geht auch mit einer einfachen Tabelle. Eine FMEA brauchen Sie erst, '
             'wenn Ihr Kunde sie fordert oder Sie in Richtung IATF 16949 gehen.'),
            ('Muss jede Maschine kalibriert werden?',
             'Nein. Kapitel 7.1.5 betrifft nur Mittel, mit denen Sie die Konformität des Produkts nachweisen – '
             'also Messschieber, Messuhren, Waagen, Prüflehren. Eine Drehmaschine ist ein Betriebsmittel, kein Prüfmittel.'),
            ('Was ist der Unterschied zur IATF 16949?',
             'Die IATF 16949 baut auf der ISO 9001 auf und ergänzt sie um automobilspezifische Forderungen '
             '(APQP, PPAP, MSA, FMEA). Für Zulieferer außerhalb der direkten Automobilkette reicht in aller Regel die ISO 9001.'),
            ('Wie viel Zeit kostet uns das im laufenden Betrieb?',
             'Realistisch 15–25 Stunden verteilt über zwei bis drei Monate, überwiegend beim Geschäftsführer '
             'und beim künftigen QM-Beauftragten. Die Fertigung selbst wird kaum gebunden.'),
            ('Wie viele Lieferanten müssen in die Lieferantenbewertung?',
             'Fünf bis sieben Hauptlieferanten wären ideal, aber fünfzehn bis zwanzig sind auch kein Thema – dann erweitern Sie einfach die Liste. Und nein, dafür braucht es kein EDV-System. Wenn Sie eine Handvoll fester Lieferanten haben, reicht Excel völlig. Hauptsache, es ist erfasst und nachvollziehbar.'),
        ],

        'kontext': 'In der Zulieferindustrie ist die ISO 9001 faktisch Marktzugang. Lieferantenselbstauskünfte, '
                   'Rahmenverträge und Kundenaudits fragen sie standardmäßig ab. Wer sie nicht hat, wird bei '
                   'Neuvergaben oft schon in der Vorauswahl aussortiert – ohne dass jemand die Fertigungsqualität '
                   'überhaupt angesehen hätte.',
        'verwandt': None,
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'maschinenbau',
        'name': 'Maschinenbau',
        'name_full': 'Maschinen- und Anlagenbauer',
        'name_upper': 'MASCHINENBAU',
        'icon': '⚙️',
        'meta_title': 'ISO 9001 im Maschinenbau | Beratung Sondermaschinen',
        'meta_desc': 'ISO 9001 für Maschinen- und Anlagenbau: Entwicklung nach 8.3, Konstruktionsfreigabe, '
                     'Abnahmeprotokolle, CE-Abgrenzung. Beratung mit BAFA-Förderung.',
        'h1': 'ISO 9001 für Maschinen- und Anlagenbauer',
        'hero_sub': 'Projektfertigung, Konstruktion, Inbetriebnahme beim Kunden – ein QM-System, das zur '
                    'Einzel- und Kleinserienfertigung passt und nicht aus der Serienproduktion abgeschrieben ist.',

        'probleme': [
            ('Sie können die Entwicklung nicht ausschließen – und wissen nicht, was das bedeutet',
             'Sobald Sie Sondermaschinen oder kundenspezifische Anlagen bauen, ist Kapitel 8.3 (Entwicklung) '
             'anwendbar. Viele Betriebe stolpern genau darüber, weil sie ihre Konstruktion nie als '
             '„Entwicklungsprozess" gedacht haben.'),
            ('Jedes Projekt läuft anders, das System soll trotzdem passen',
             'Bei Einzelfertigung gibt es keine Serie, an der man Prozesse festmachen kann. Ein aus der '
             'Massenfertigung kopiertes QM-System erzeugt hier nur Papier, das niemand ausfüllt.'),
            ('Die Abnahme beim Kunden ist der kritischste Moment – und der am schlechtesten dokumentierte',
             'Inbetriebnahme, Restpunkteliste, Übergabe: technisch beherrschen Sie das. Im Audit fehlt '
             'regelmäßig der Nachweis, wer wann was abgenommen hat.'),
        ],

        'normtabelle': [
            ('8.3 Entwicklung von Produkten und Dienstleistungen',
             'Konstruktion läuft ohne dokumentierte Planung, Freigabe und Änderungsverfolgung',
             'Lastenheft/Pflichtenheft, Konstruktionsfreigabe, Design-Review (auch formlos), Änderungsdokumentation mit Indexstand'),
            ('8.3.4 Steuerung der Entwicklung',
             'Verifizierung und Validierung werden nicht unterschieden',
             'Verifizierung = Berechnung/Prüfung gegen Spezifikation, Validierung = Abnahme unter Einsatzbedingungen; beides mit Nachweis'),
            ('8.5.1 Steuerung der Produktion und Dienstleistungserbringung',
             'Montage und Inbetriebnahme beim Kunden ohne Protokoll',
             'Abnahme-/Inbetriebnahmeprotokoll, Restpunkteliste, Einweisungsnachweis des Kunden'),
            ('8.2.3 Überprüfung der Anforderungen',
             'Angebote gehen ohne dokumentierte technische Machbarkeitsprüfung raus',
             'Technische Klärung vor Angebotsabgabe, Auftragsklärung, Nachweis der Machbarkeitsprüfung'),
            ('8.5.3 Eigentum der Kunden oder externen Anbieter',
             'Beistellteile des Kunden werden nicht gesondert behandelt',
             'Kennzeichnung und Nachweis für Beistellungen, Meldeverfahren bei Beschädigung'),
            ('8.4 Externe Anbieter',
             'Zukaufteile und Fremdfertigung ohne Qualitätsvereinbarung',
             'Bewertung der Fremdfertiger, Anforderungen in der Bestellung, Eingangsprüfung sicherheitsrelevanter Teile'),
        ],

        'dokumente': [
            'Projektakte als roter Faden vom Angebot bis zur Abnahme',
            'Konstruktions- und Freigabeprozess inkl. Änderungsindex',
            'Technische Klärung / Machbarkeitsprüfung vor Angebotsabgabe',
            'Abnahme- und Inbetriebnahmeprotokoll mit Restpunkteliste',
            'Qualitätssicherungsvereinbarung für Fremdfertiger',
            'Reklamations- und Serviceprozess nach Auslieferung',
            'Schnittstelle zur CE-Dokumentation (ohne Doppelarbeit)',
        ],

        'phasen': [
            'Wir nehmen ein typisches Projekt als Referenz und zeichnen daran den realen Ablauf nach: '
            'Anfrage, Klärung, Konstruktion, Fertigung, Montage, Abnahme, Service.',
            'Die Dokumentation entsteht projektbezogen statt seriell – eine Projektakte, in der die '
            'Nachweise ohnehin anfallen, statt zusätzlicher Formulare.',
            'Wir prüfen besonders Kapitel 8.3, weil dort im Maschinenbau die meisten Abweichungen entstehen, '
            'und klären sauber ab, was CE-Dokumentation und was QM-System ist.',
        ],

        'faq': [
            ('Können wir die Entwicklung (Kapitel 8.3) ausschließen?',
             'Im Sondermaschinen- und Anlagenbau in aller Regel nicht. Sobald Sie auf Basis von Kundenanforderungen '
             'konstruieren, ist das Entwicklung im Sinne der Norm. Ausschließen können Sie 8.3 nur, wenn Sie '
             'ausschließlich nach fremden, vollständigen Vorgaben fertigen.'),
            ('Ersetzt die ISO 9001 die CE-Konformität nach Maschinenrichtlinie?',
             'Nein, das sind zwei verschiedene Ebenen. Die CE-Kennzeichnung ist gesetzlich vorgeschrieben und '
             'produktbezogen, die ISO 9001 ist freiwillig und systembezogen. Sinnvoll ist, die Nachweise so zu '
             'verzahnen, dass Risikobeurteilung und Betriebsanleitung nicht doppelt geführt werden.'),
            ('Wie dokumentiert man Einzelfertigung sinnvoll?',
             'Projektbezogen statt prozessbezogen. Eine Projektakte je Auftrag, in der Klärung, Freigaben, '
             'Änderungen und Abnahme abgelegt sind, erfüllt die Norm und ist gleichzeitig das, was Ihre '
             'Projektleiter ohnehin brauchen.'),
            ('Was ist mit Montage und Service beim Kunden?',
             'Das fällt unter 8.5.1 und – für die Zeit nach der Lieferung – unter 8.5.5. Gefordert sind '
             'nachvollziehbare Nachweise: wer war vor Ort, was wurde abgenommen, welche Punkte blieben offen.'),
            ('Wie detailliert müssen wir den Entwicklungsprozess beschreiben?',
             'Entwicklung ist einer der einfachsten Prozesse überhaupt: Der Kunde möchte etwas, gibt einen Auftrag, Sie entwerfen, stellen vor, der Kunde gibt frei – oder es gibt eine nächste Runde. So simpel ist das. Man muss nicht versuchen, jede Variante im Detail zu beschreiben, sonst passen Sie das Dokument dauernd an.'),
        ],

        'kontext': 'Im Maschinen- und Anlagenbau kommt der Druck meist von zwei Seiten: Endkunden aus der '
                   'Industrie fordern das Zertifikat in der Lieferantenqualifizierung, und bei öffentlichen '
                   'oder halböffentlichen Auftraggebern ist es in der Eignungsprüfung häufig gesetzt.',
        'verwandt': None,
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'handel',
        'name': 'Handel',
        'name_full': 'Handelsunternehmen',
        'name_upper': 'HANDEL',
        'icon': '📦',
        'meta_title': 'ISO 9001 für Handel & Großhandel | QM-Beratung',
        'meta_desc': 'ISO 9001 für Groß- und Einzelhandel: Lieferantenbewertung, Wareneingang, Lagerung, '
                     'Retouren. Entwicklung meist ausschließbar. Beratung mit BAFA-Förderung.',
        'h1': 'ISO 9001 für Handelsunternehmen',
        'hero_sub': 'Sie stellen nichts her – Ihr Qualitätsmanagement dreht sich um Lieferanten, Ware und '
                    'Kundenversprechen. Genau darauf schneiden wir das System zu, statt Ihnen ein Fertigungs-QM überzustülpen.',

        'probleme': [
            ('Ihnen wird ein QM-System angeboten, das für Fabriken gemacht ist',
             'Prüfpläne, Fertigungslenkung, Prozessvalidierung – vieles davon betrifft Sie schlicht nicht. '
             'Wer das trotzdem einführt, produziert Papier ohne jeden Nutzen.'),
            ('Die Lieferantenqualität entscheidet über Ihre Qualität – ohne dass Sie sie steuern',
             'Im Handel ist Kapitel 8.4 das Herzstück. Wenn Lieferanten nie bewertet werden und '
             'Reklamationen nicht zurückgespielt werden, fehlt der wichtigste Regelkreis.'),
            ('Reklamationen und Retouren laufen über Zuruf',
             'Jeder löst sie, keiner zählt sie. Damit fehlt Ihnen die Grundlage für Kapitel 9.1 – und die '
             'Argumente gegenüber Ihren Lieferanten.'),
        ],

        'normtabelle': [
            ('8.4 Steuerung extern bereitgestellter Prozesse, Produkte und Dienstleistungen',
             'Lieferanten sind gesetzt, werden aber nicht bewertet',
             'Lieferantenliste, Bewertungskriterien (Liefertreue, Mängelquote, Reaktionszeit), regelmäßige Bewertung mit Konsequenz'),
            ('8.5.4 Erhaltung',
             'Lagerbedingungen, Haltbarkeit und Rotation sind nicht geregelt',
             'Lagerordnung, FIFO/MHD-Regelung, ggf. Temperaturnachweis, Umgang mit beschädigter Ware'),
            ('8.7 Steuerung nichtkonformer Ergebnisse',
             'Retouren und Sperrware liegen unmarkiert im Lager',
             'Gekennzeichneter Sperrbereich, dokumentierte Entscheidung, Rückmeldung an den Lieferanten'),
            ('8.2 Anforderungen an Produkte und Dienstleistungen',
             'Zusagen aus dem Vertrieb sind nicht dokumentiert',
             'Angebot und Auftragsbestätigung als Nachweis, Regelung für Sonderzusagen und Änderungen'),
            ('7.5 Dokumentierte Information',
             'Produktdatenblätter und Konformitätsunterlagen sind verstreut',
             'Geordnete Ablage für Datenblätter, Konformitätserklärungen und Sicherheitsdatenblätter'),
            ('9.1.2 Kundenzufriedenheit',
             'Es gibt keine Rückmeldung außer Beschwerden',
             'Auswertung von Reklamationen, Liefertreue und – wo sinnvoll – eine schlanke Kundenabfrage'),
        ],

        'dokumente': [
            'Lieferantenbewertung mit Kriterien, die Sie ohnehin kennen',
            'Wareneingangsregelung – risikobasiert, nicht pauschal',
            'Lager- und Erhaltungsregelung (FIFO, MHD, Beschädigung)',
            'Reklamations- und Retourenprozess mit Auswertung',
            'Angebots- und Auftragsprozess als Nachweiskette',
            'Ablage für Datenblätter und Konformitätsunterlagen',
            'Kennzahlen: Liefertreue, Mängelquote, Reklamationsquote',
        ],

        'phasen': [
            'Wir klären zuerst den Anwendungsbereich – im Handel lässt sich Kapitel 8.3 (Entwicklung) '
            'meist begründet ausschließen. Das spart von vornherein einen ganzen Themenblock.',
            'Wir bauen das System um Ihre Warenwirtschaft herum. Was das ERP ohnehin auswertet, wird Nachweis; '
            'zusätzliche Listen entstehen nur, wo wirklich nichts vorhanden ist.',
            'Wir prüfen die Punkte, an denen Handelsbetriebe im Audit typischerweise hängen: '
            'Lieferantenbewertung, Sperrware, Rückverfolgbarkeit der Charge.',
        ],

        'faq': [
            ('Können wir die Entwicklung (Kapitel 8.3) ausschließen?',
             'In der Regel ja. Wenn Sie ausschließlich handeln und keine Produkte konstruieren oder '
             'spezifizieren lassen, ist 8.3 nicht anwendbar. Der Ausschluss muss im Anwendungsbereich '
             'begründet werden – das machen wir gemeinsam.'),
            ('Müssen wir jede Wareneingangslieferung prüfen?',
             'Nein. Die Norm verlangt eine risikobasierte Festlegung. Bei einem langjährig zuverlässigen '
             'Markenlieferanten kann die Prüfung auf Menge und Transportschaden beschränkt sein, bei '
             'kritischen Artikeln oder neuen Lieferanten wird genauer geprüft.'),
            ('Wie gehen wir mit Streckengeschäften um, wo wir die Ware nie sehen?',
             'Das ist ein klassischer 8.4-Fall: Sie steuern über die Auswahl und Bewertung des Lieferanten '
             'sowie über die Rückmeldung Ihrer Kunden. Der Nachweis liegt in der Lieferantenbewertung, '
             'nicht in einer physischen Prüfung.'),
            ('Gilt das auch für reinen E-Commerce?',
             'Ja, und die Norm passt dort oft überraschend gut: Shop-System, Retourenquote und '
             'Bewertungsmanagement liefern die Kennzahlen für Kapitel 9.1 praktisch frei Haus.'),
            ('Müssen wir jede Wareneingangsprüfung dokumentieren?',
             'Wenn Sie ohnehin zu 100 Prozent prüfen, dokumentieren Sie nur die Abweichungen – das ist pragmatisch und spart Papier. Wichtig ist nur, dass es genau so in der Prüfanweisung steht. Dann ist das in Ordnung.'),
        ],

        'kontext': 'Im Handel kommt die Forderung nach der ISO 9001 meist über Ausschreibungen und über '
                   'Industriekunden, die ihre gesamte Lieferkette qualifizieren müssen. Häufig genügt schon '
                   'ein einziger Großkunde, der seine Lieferantenanforderungen verschärft.',
        'verwandt': None,
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'dienstleistung',
        'name': 'Dienstleistung',
        'name_full': 'Dienstleistungsunternehmen',
        'name_upper': 'DIENSTLEISTUNG',
        'icon': '🤝',
        'meta_title': 'ISO 9001 für Dienstleister | QM-Beratung',
        'meta_desc': 'ISO 9001 für Dienstleistungsunternehmen: Leistungsnachweise, Kompetenzmatrix, '
                     'Kundenzufriedenheit. Schlankes QM ohne Fertigungsballast. Mit BAFA-Förderung.',
        'h1': 'ISO 9001 für Dienstleistungsunternehmen',
        'hero_sub': 'Ihre Leistung ist nicht anfassbar – Ihre Nachweise müssen es sein. Wir zeigen, wie '
                    'Qualität bei Dienstleistungen belegbar wird, ohne dass Sie zu Formularschiebern werden.',

        'probleme': [
            ('„Wie sollen wir etwas dokumentieren, das man nicht anfassen kann?"',
             'Die häufigste Frage in der ersten Beratungsstunde. Die Antwort ist unspektakulär: über die '
             'Spur, die Ihre Leistung ohnehin hinterlässt – Angebot, Auftragsklärung, Protokoll, Abnahme, Rechnung.'),
            ('Die Qualität hängt an einzelnen Köpfen',
             'Bei Dienstleistungen ist die Kompetenz der Mitarbeiter der Produktionsprozess. Kapitel 7.2 '
             'fragt genau das ab – und die meisten Betriebe haben dazu nichts Schriftliches.'),
            ('Sie wissen nicht wirklich, wie zufrieden Ihre Kunden sind',
             'Kein Beschwerdeeingang heißt nicht Zufriedenheit. Kapitel 9.1.2 verlangt, dass Sie die '
             'Wahrnehmung Ihrer Kunden aktiv erfassen – nicht, dass Sie eine große Umfrage fahren.'),
        ],

        'normtabelle': [
            ('7.2 Kompetenz',
             'Qualifikationen und Einarbeitung sind nicht nachgewiesen',
             'Kompetenzmatrix je Rolle, Einarbeitungsplan, Nachweis von Schulungen und deren Wirksamkeit'),
            ('8.5.1 Steuerung der Dienstleistungserbringung',
             'Es gibt keinen Nachweis, was beim Kunden tatsächlich geleistet wurde',
             'Leistungsnachweis, Projekt- oder Einsatzdokumentation, Protokolle, Freigabe durch den Kunden'),
            ('8.2.2 / 8.2.3 Anforderungen bestimmen und überprüfen',
             'Mündliche Zusagen im Vertrieb, Streit über den Leistungsumfang',
             'Dokumentierte Auftragsklärung, Angebot mit Leistungsabgrenzung, Regelung für Änderungswünsche'),
            ('9.1.2 Kundenzufriedenheit',
             'Zufriedenheit wird nur über ausbleibende Beschwerden vermutet',
             'Ein einfaches, regelmäßiges Feedbackverfahren – Kurzabfrage nach Projektende genügt oft'),
            ('8.5.5 Tätigkeiten nach der Lieferung',
             'Nachbetreuung und Gewährleistung sind nicht geregelt',
             'Regelung für Nacharbeit, Support und Gewährleistungsfälle mit Nachweis'),
            ('6.1 Risiken und Chancen',
             'Abhängigkeit von Schlüsselpersonen ist bekannt, aber nicht behandelt',
             'Risikoübersicht mit Maßnahmen – Vertretungsregelung, Wissenssicherung, Kundenkonzentration'),
        ],

        'dokumente': [
            'Prozesslandkarte vom Erstkontakt bis zur Nachbetreuung',
            'Auftragsklärung mit klarer Leistungsabgrenzung',
            'Leistungs- bzw. Projektnachweis als zentrales Dokument',
            'Kompetenzmatrix und Einarbeitungsplan',
            'Schlankes Feedback- und Beschwerdeverfahren',
            'Kennzahlen: Termintreue, Nacharbeit, Kundenrückmeldungen',
            'Vertretungs- und Wissenssicherungsregelung',
        ],

        'phasen': [
            'Wir sehen uns an, welche Spuren Ihre Leistung heute schon hinterlässt. In fast allen Fällen '
            'sind die Nachweise vorhanden – sie heißen nur anders und liegen verstreut.',
            'Wir machen daraus ein System mit möglichst wenigen Dokumenten. Für Dienstleister sind '
            'zehn bis fünfzehn schlanke Dokumente völlig ausreichend.',
            'Wir üben die Auditsituation: Der Zertifizierer wird fragen, wie Sie Qualität bei einer '
            'unsichtbaren Leistung sicherstellen. Auf diese Frage bereiten wir Sie gezielt vor.',
        ],

        'faq': [
            ('Wie dokumentiert man eine Leistung, die man nicht anfassen kann?',
             'Über die Nachweise, die ohnehin entstehen: Auftragsklärung, Termin- oder Einsatzprotokoll, '
             'Zwischenstände, Abnahme, Rechnung. Die Norm verlangt keine neue Dokumentenwelt, sondern dass '
             'die vorhandene nachvollziehbar ist.'),
            ('Müssen wir eine Kundenbefragung durchführen?',
             'Nicht zwingend. Kapitel 9.1.2 verlangt, dass Sie die Kundenwahrnehmung erfassen – das kann eine '
             'strukturierte Nachfrage bei Projektabschluss sein, die Auswertung von Bewertungen oder ein '
             'dokumentiertes Jahresgespräch mit den wichtigsten Kunden.'),
            ('Wie viele Prozesse brauchen wir?',
             'Weniger, als die meisten denken. Für ein Dienstleistungsunternehmen mit bis zu 50 Mitarbeitern '
             'reichen typischerweise vier bis sechs Prozesse plus die Führungs- und Unterstützungsthemen.'),
            ('Lohnt sich das bei fünf Mitarbeitern überhaupt?',
             'Wenn ein Kunde oder eine Ausschreibung das Zertifikat fordert: ja, und der Aufwand ist bei '
             'kleinen Betrieben deutlich geringer. Ohne diesen äußeren Anlass sollten Sie ehrlich prüfen, '
             'was Sie sich davon versprechen – das besprechen wir im Erstgespräch offen.'),
            ('Wie messen wir Kundenzufriedenheit, wenn wir keine Fragebögen verschicken wollen?',
             'Das simpelste Verfahren: Selbsteinschätzung mit Schulnoten. Nehmen Sie Ihre Hauptkunden – vier, fünf reichen – und bewerten Sie nach Kriterien wie Flexibilität, Zuverlässigkeit und Termintreue. Wir müssen nicht anfangen, Fragebögen an Großkonzerne zu schicken.'),
        ],

        'kontext': 'Dienstleister geraten meist über zwei Wege an die ISO 9001: über Ausschreibungen der '
                   'öffentlichen Hand, in denen ein QM-Nachweis als Eignungskriterium steht, und über '
                   'Industriekunden, die ihre Dienstleister genauso qualifizieren wie ihre Materiallieferanten.',
        'verwandt': None,
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'it-dienstleistung',
        'name': 'IT-Dienstleistung',
        'name_full': 'IT-Dienstleister und Systemhäuser',
        'name_upper': 'IT-DIENSTLEISTUNG',
        'icon': '🖥️',
        'meta_title': 'ISO 9001 für IT-Dienstleister & Systemhäuser',
        'meta_desc': 'ISO 9001 für IT-Dienstleister: Ticketsystem als Nachweis, SLA, Change-Management, '
                     'Abgrenzung zur ISO 27001. Beratung mit BAFA-Förderung.',
        'h1': 'ISO 9001 für IT-Dienstleister und Systemhäuser',
        'hero_sub': 'Ihr Ticketsystem ist bereits das halbe QM-System. Wir machen daraus einen Nachweis, '
                    'der im Audit trägt – statt eine zweite Dokumentenwelt daneben aufzubauen.',

        'probleme': [
            ('Kunden fordern plötzlich Zertifikate – und meinen mal 9001, mal 27001',
             'In Ausschreibungen und Rahmenverträgen tauchen beide auf, oft ohne saubere Unterscheidung. '
             'Wer das falsche Projekt startet, verbrennt Zeit und Geld.'),
            ('Alles steckt im Ticketsystem, aber niemand kann es als QM-Nachweis erklären',
             'Reaktionszeiten, Eskalationen, Lösungswege – die Daten sind da. Im Audit fehlt nur die '
             'Zuordnung zur Norm und die Auswertung.'),
            ('SLAs sind vertraglich zugesagt, aber nicht überwacht',
             'Kapitel 9.1 fragt genau danach: Woher wissen Sie, dass Sie Ihre eigenen Zusagen einhalten?'),
        ],

        'normtabelle': [
            ('8.5.1 Steuerung der Dienstleistungserbringung',
             'Leistungen werden erbracht, aber nicht nachvollziehbar dokumentiert',
             'Ticketsystem als führendes Nachweissystem: Kategorien, Bearbeitungsstände, Lösungsdokumentation'),
            ('8.2.1 Kommunikation mit Kunden',
             'Eskalationswege und Erreichbarkeiten sind nicht verbindlich geregelt',
             'SLA-Dokument, definierte Reaktions- und Wiederherstellungszeiten, Eskalationsmatrix'),
            ('8.5.6 Steuerung von Änderungen',
             'Änderungen an Kundensystemen laufen ohne dokumentierte Freigabe',
             'Change-Verfahren mit Bewertung, Freigabe, Rückfallplan und Nachweis'),
            ('7.1.3 Infrastruktur',
             'Eigene Systeme, Backups und Monitoring sind nicht geregelt',
             'Backup- und Wiederanlaufkonzept, Monitoring-Nachweis, Wartungszyklen'),
            ('6.1 Risiken und Chancen',
             'Ausfall-, Personal- und Datenverlustrisiken sind bekannt, aber nicht behandelt',
             'Risikoübersicht mit Maßnahmen, Notfallregelung, Vertretungsregelung'),
            ('8.4 Externe Anbieter',
             'Cloud- und Vorlieferanten werden nicht als Lieferanten gesehen',
             'Bewertung von Cloud-, Rechenzentrums- und Subunternehmerleistungen, Verfügbarkeitsnachweise'),
        ],

        'dokumente': [
            'Service-Katalog mit klarer Leistungsabgrenzung',
            'SLA-Regelung inkl. Reaktions- und Eskalationsstufen',
            'Ticketprozess als dokumentierter Kernprozess',
            'Change-Verfahren mit Freigabe und Rückfallplan',
            'Backup-, Monitoring- und Wiederanlaufregelung',
            'Bewertung von Cloud- und Subdienstleistern',
            'Kennzahlen: SLA-Einhaltung, Erstlösungsquote, Wiederöffnungsrate',
        ],

        'phasen': [
            'Wir sehen uns Ticketsystem, SLA-Vorlagen und Monitoring an und ordnen zu, welche '
            'Normforderung damit bereits erfüllt ist. Meist ist das der größere Teil.',
            'Wir ergänzen genau die Lücken – üblicherweise Change-Verfahren, Kompetenznachweise und '
            'die Auswertung der ohnehin vorhandenen Kennzahlen.',
            'Wir klären die Abgrenzung zur ISO 27001, damit Sie im Kundengespräch sauber argumentieren '
            'können, was Ihr Zertifikat abdeckt und was nicht.',
        ],

        'faq': [
            ('Brauchen wir ISO 27001 statt oder zusätzlich zur ISO 9001?',
             'Das sind unterschiedliche Ziele: Die ISO 9001 sichert die Qualität Ihrer Leistung, die ISO 27001 '
             'die Informationssicherheit. Viele IT-Dienstleister starten mit der 9001, weil sie schneller und '
             'günstiger ist, und ergänzen die 27001, wenn Kunden es konkret fordern. Prüfen Sie zuerst, was in '
             'der Ausschreibung tatsächlich steht.'),
            ('Reicht unser Ticketsystem als QM-Nachweis?',
             'In der Regel ja, und zwar erstaunlich weitgehend. Was fehlt, ist meist die Zuordnung zur Norm, '
             'eine dokumentierte Kategorisierung und die regelmäßige Auswertung. Ein separates QM-Formularwesen '
             'daneben ist fast immer überflüssig.'),
            ('Wie gehen wir mit Auftragsverarbeitung und DSGVO um?',
             'Die DSGVO ist eine rechtliche Anforderung und fällt unter Kapitel 4.2 als Anforderung '
             'interessierter Parteien. Das QM-System muss sicherstellen, dass diese Pflichten erkannt und '
             'erfüllt werden – die inhaltliche Datenschutzberatung ersetzt es nicht.'),
            ('Zählen Cloud-Anbieter als externe Anbieter nach 8.4?',
             'Ja. Wenn Sie Leistungen weiterreichen, die Sie selbst einkaufen, müssen Sie diese Anbieter '
             'auswählen, bewerten und überwachen – meist über Verfügbarkeitsberichte und Störungshistorie.'),
            ('Wir haben auch die ISO 27001 im Blick – können wir die Risikoanalyse zusammenführen?',
             'Ja, das macht absolut Sinn. Der erste Teil beider Normen ist sehr ähnlich: Ziele, Managementbewertung, interne Audits. Ziehen Sie das gleich, damit Sie nicht zwei Systeme parallel pflegen müssen. Was schon da ist, wird ergänzt – nicht neu gemacht.'),
        ],

        'kontext': 'Bei IT-Dienstleistern kommt die Anforderung fast immer aus Rahmenverträgen mit '
                   'Industriekunden und aus öffentlichen Ausschreibungen. Häufig ist die ISO 9001 dort die '
                   'Mindestanforderung, während die ISO 27001 nur für bestimmte Lose verlangt wird.',
        'verwandt': None,
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'it-softwareentwicklung',
        'name': 'Softwareentwicklung',
        'name_full': 'Softwareentwicklungs-Unternehmen',
        'name_upper': 'SOFTWAREENTWICKLUNG',
        'icon': '💻',
        'meta_title': 'ISO 9001 für Softwareentwicklung | Agil & Norm',
        'meta_desc': 'ISO 9001 für Softwarehäuser: Kapitel 8.3 mit Scrum erfüllen, Git und Jira als Nachweis, '
                     'Release-Freigabe, Code-Review. Beratung mit BAFA-Förderung.',
        'h1': 'ISO 9001 für Softwareentwicklung',
        'hero_sub': 'Scrum und ISO 9001 sind kein Widerspruch. Ihre Sprints, Reviews und Merge Requests '
                    'sind bereits normkonforme Entwicklungsnachweise – man muss sie nur richtig zuordnen.',

        'probleme': [
            ('Die Sorge, dass die Norm agiles Arbeiten kaputt macht',
             'Die verbreitetste Befürchtung – und die unbegründetste. Die ISO 9001 schreibt kein '
             'Vorgehensmodell vor. Sie fragt, ob Entwicklung geplant, geprüft und freigegeben wird. '
             'Genau das tut Scrum.'),
            ('Kapitel 8.3 ist bei Ihnen der Kernprozess – und wird meist unterschätzt',
             'Anders als bei Handel oder klassischer Dienstleistung ist Entwicklung bei Ihnen nicht '
             'ausschließbar. Der gesamte Abschnitt 8.3 mit Planung, Eingaben, Steuerung, Ergebnissen und '
             'Änderungen ist anzuwenden.'),
            ('Alles steckt in Git, Jira und der CI – nur nicht in einem Handbuch',
             'Das ist kein Problem, sondern ein Vorteil. Es fehlt nur die Brücke zwischen Werkzeugkette '
             'und Normforderung.'),
        ],

        'normtabelle': [
            ('8.3.2 Entwicklungsplanung',
             'Es gibt keine erkennbare Planung – dabei ist sie längst da',
             'Product Backlog, Sprint-Planung, Roadmap und Definition of Done als dokumentierte Planung'),
            ('8.3.3 Entwicklungseingaben',
             'Anforderungen sind mündlich oder nur im Chat',
             'User Stories mit Akzeptanzkriterien, Anforderungsdokument, Nachweis der Kundenabstimmung'),
            ('8.3.4 Entwicklungssteuerung',
             'Verifizierung und Validierung sind nicht unterschieden',
             'Code Review / Merge Request und automatisierte Tests = Verifizierung; Abnahme durch den Kunden = Validierung'),
            ('8.3.6 Entwicklungsänderungen',
             'Änderungen an Anforderungen sind nicht nachvollziehbar',
             'Change-Tickets mit Bewertung und Freigabe, Verknüpfung von Ticket, Commit und Release'),
            ('8.5.6 / 7.5.3 Steuerung von Änderungen und Dokumenten',
             'Releases gehen ohne dokumentierte Freigabe live',
             'Release-Freigabe mit benanntem Verantwortlichen, Versionsverwaltung, Release Notes'),
            ('8.4 Externe Anbieter',
             'Open-Source- und Fremdkomponenten werden nicht bewertet',
             'Übersicht eingesetzter Fremdkomponenten inkl. Lizenz- und Sicherheitsbewertung'),
        ],

        'dokumente': [
            'Entwicklungsprozess in Ihrer eigenen Sprache (Sprint statt Phase)',
            'Definition of Done als normkonforme Freigaberegel',
            'Anforderungs- und Akzeptanzkriterien-Vorlage',
            'Review- und Testnachweis aus der bestehenden Toolkette',
            'Release- und Deployment-Freigabe',
            'Übersicht der Fremd- und Open-Source-Komponenten',
            'Kennzahlen: Bug-Rate nach Release, Durchlaufzeit, Wiederöffnungsquote',
        ],

        'phasen': [
            'Wir schauen uns Ihre Toolkette an – Repository, Ticketsystem, CI-Pipeline – und ordnen die '
            'vorhandenen Artefakte den Abschnitten von Kapitel 8.3 zu.',
            'Wir schreiben den Prozess so auf, wie Sie tatsächlich arbeiten. Kein Wasserfallmodell, '
            'sondern Ihr Sprint-Ablauf mit den Nachweisen, die dabei ohnehin entstehen.',
            'Wir bereiten Sie auf die typische Auditfrage vor: „Zeigen Sie mir, wie aus einer '
            'Kundenanforderung ein freigegebenes Release wird." Das ist in agilen Teams gut zeigbar.',
        ],

        'faq': [
            ('Ist Scrum mit der ISO 9001 vereinbar?',
             'Ja, ausdrücklich. Die Norm schreibt kein Vorgehensmodell vor. Sprint Planning ist '
             'Entwicklungsplanung, das Review ist eine Entwicklungsprüfung, die Definition of Done ist ein '
             'Freigabekriterium. Wir übersetzen das, statt es zu ersetzen.'),
            ('Müssen wir für die Zertifizierung auf Wasserfall umstellen?',
             'Nein. Diese Empfehlung stammt aus einer Zeit, in der Auditoren agile Verfahren nicht kannten. '
             'Ein Zertifizierer, der das heute noch verlangt, sollte gewechselt werden.'),
            ('Reichen Git und Jira als Dokumentation?',
             'Weitgehend ja. Commit-Historie, Merge Requests, Tickets und Pipeline-Ergebnisse sind '
             'dokumentierte Information im Sinne der Norm. Ergänzt werden muss meist nur eine kurze '
             'Beschreibung des Prozesses und die Regelung der Release-Freigabe.'),
            ('Was ist mit ISO 27001 oder TISAX?',
             'Die betreffen Informationssicherheit, nicht Entwicklungsqualität. Wenn Ihre Kunden aus der '
             'Automobilbranche kommen, kann TISAX zusätzlich gefordert sein – das ist ein eigenes Projekt '
             'und sollte nicht mit der ISO 9001 vermischt werden.'),
            ('Wie detailliert müssen wir unsere Entwicklungsprozesse beschreiben?',
             'Vorsichtig – das muss einfach bleiben. Beschreiben Sie den übergeordneten Prozess: Anforderungen bekommen, Projekt aufsetzen, entwickeln, freigeben. Nicht die Details der einzelnen Verfahren, denn die müssten Sie sonst dauernd anpassen. Der erste Entwurf muss auch nicht perfekt sein.'),
        ],

        'kontext': 'Softwarehäuser brauchen das Zertifikat meist dann, wenn sie in den Mittelstand oder in '
                   'die Industrie verkaufen. Dort ist die Lieferantenqualifizierung standardisiert, und ein '
                   'fehlendes QM-Zertifikat führt schon in der Vorauswahl zum Ausschluss.',
        'verwandt': None,
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'sicherheitsdienstleistung',
        'name': 'Sicherheitsdienst',
        'name_full': 'Sicherheitsdienstleister',
        'name_upper': 'SICHERHEITSDIENST',
        'icon': '🛡️',
        'meta_title': 'ISO 9001 für Sicherheitsdienste | Ausschreibungen',
        'meta_desc': 'ISO 9001 für Sicherheitsdienstleister: Dienstanweisungen, Sachkunde nach §34a, '
                     'Wachbuch, Objektkontrollen. Pflicht in vielen Ausschreibungen. Mit BAFA-Förderung.',
        'h1': 'ISO 9001 für Sicherheitsdienstleister',
        'hero_sub': 'In Ausschreibungen der öffentlichen Hand ist der QM-Nachweis fast immer Eignungskriterium. '
                    'Wir bauen ein System, das Ihre Einsatzrealität abbildet – Schichtdienst, Fluktuation und alles.',

        'probleme': [
            ('Ohne Zertifikat kommen Sie in vielen Ausschreibungen gar nicht erst in die Wertung',
             'Kommunen, Kliniken, Verkehrsbetriebe und Industriekunden setzen einen QM-Nachweis regelmäßig '
             'als Eignungskriterium an. Der beste Preis nützt nichts, wenn die Eignung nicht belegt ist.'),
            ('Hohe Fluktuation macht Qualifikationsnachweise zum Dauerthema',
             'Kapitel 7.2 verlangt, dass jeder Mitarbeiter für seine Aufgabe kompetent ist – nachgewiesen. '
             'Bei ständigem Personalwechsel wird das ohne System schnell unübersichtlich.'),
            ('Was nachts im Objekt passiert, steht nirgends nachvollziehbar',
             'Streifengänge, Vorkommnisse, Übergaben: Der Auditor fragt nach dem Nachweis, nicht nach der Erinnerung.'),
        ],

        'normtabelle': [
            ('7.2 Kompetenz',
             'Sachkunde- und Unterrichtungsnachweise sind nicht systematisch geführt',
             'Personalakte mit Nachweis nach § 34a GewO, Eintrag im Bewacherregister, Schulungs- und Unterweisungsnachweise'),
            ('8.5.1 Steuerung der Dienstleistungserbringung',
             'Es gibt keine objektbezogene Vorgabe, jeder macht es etwas anders',
             'Dienstanweisung je Objekt, Objektmappe, Wachbuch bzw. elektronischer Streifennachweis'),
            ('8.2.2 Bestimmung der Anforderungen',
             'Der Leistungsumfang aus der Ausschreibung ist nicht in die Praxis übersetzt',
             'Objektaufnahme, Leistungsverzeichnis, Übersetzung in konkrete Dienstanweisungen'),
            ('8.7 Steuerung nichtkonformer Ergebnisse',
             'Vorfälle werden gemeldet, aber nicht ausgewertet',
             'Vorfallmeldung mit Eskalationsstufen, Auswertung und abgeleitete Maßnahmen'),
            ('9.1 Überwachung und Messung',
             'Objektkontrollen finden statt, sind aber nicht belegt',
             'Kontrollplan je Objekt, dokumentierte Objektkontrolle durch die Einsatzleitung, Kundenrückmeldung'),
            ('7.1.2 Personen / 6.1 Risiken',
             'Ausfälle im Schichtdienst werden improvisiert',
             'Einsatz- und Vertretungsplanung, Regelung für kurzfristigen Ausfall, Springerkonzept'),
        ],

        'dokumente': [
            'Objektmappe mit Dienstanweisung je Einsatzort',
            'Personal- und Qualifikationsübersicht inkl. § 34a-Nachweisen',
            'Einweisungsnachweis für neue Kräfte am Objekt',
            'Wachbuch bzw. elektronischer Streifennachweis',
            'Vorfall- und Eskalationsverfahren',
            'Kontrollplan und Protokoll der Objektkontrollen',
            'Kennzahlen: Ausfallquote, Vorfälle je Objekt, Kundenbeschwerden',
        ],

        'phasen': [
            'Wir nehmen ein bestehendes Objekt als Muster und bauen daran die Dienstanweisung und die '
            'Nachweiskette auf. Die übrigen Objekte folgen demselben Schema.',
            'Wir richten die Personal- und Qualifikationsübersicht so ein, dass Sie bei Fluktuation nicht '
            'jedes Mal neu suchen müssen – das ist der größte Dauernutzen in Ihrer Branche.',
            'Wir bereiten die Nachweise so auf, dass sie zugleich für Ausschreibungsunterlagen taugen. '
            'Vieles, was der Auditor sehen will, will auch der Auftraggeber sehen.',
        ],

        'faq': [
            ('Reicht die Sachkundeprüfung nach § 34a GewO nicht aus?',
             'Nein, das sind zwei verschiedene Ebenen. § 34a ist eine gewerberechtliche Voraussetzung für '
             'Personen. Die ISO 9001 betrifft Ihr Unternehmen und seine Prozesse. In Ausschreibungen werden '
             'regelmäßig beide verlangt.'),
            ('Brauchen wir zusätzlich die DIN 77200?',
             'Das hängt von Ihren Auftraggebern ab. Die DIN 77200 beschreibt Anforderungen an '
             'Sicherungsdienstleistungen konkret und wird in manchen Ausschreibungen ausdrücklich gefordert. '
             'Prüfen Sie die Vergabeunterlagen – die ISO 9001 ist der breitere, häufiger geforderte Nachweis.'),
            ('Wie dokumentiert man Nachtdienste ohne zusätzlichen Aufwand?',
             'Über das, was ohnehin geführt wird: Wachbuch, Streifenkontrollpunkte, Übergabeprotokoll. '
             'Wenn Sie ein elektronisches System einsetzen, liefert es die Nachweise bereits auswertbar.'),
            ('Wie gehen wir mit hoher Personalfluktuation um?',
             'Über einen standardisierten Einweisungsprozess: fester Einweisungsbogen je Objekt, '
             'Unterschrift, Ablage in der Personalakte. Das ist im Audit sofort zeigbar und reduziert '
             'gleichzeitig Ihre Haftungsrisiken.'),
            ('Brauchen wir eine Qualifikationsmatrix für unsere Mitarbeiter?',
             'Kann man machen, muss man nicht. Interessant wird die Matrix, wenn Sie daran arbeiten wollen, dass Stellen doppelt besetzt sind – wenn also nicht nur einer eine bestimmte Aufgabe übernehmen kann. Bei hoher Fluktuation ist genau das oft der Punkt, an dem sie sich lohnt.'),
        ],

        'kontext': 'Im Sicherheitsgewerbe ist die ISO 9001 überwiegend ein Vertriebsthema: Vergabestellen '
                   'verlangen einen QM-Nachweis als Eignungskriterium, und Industriekunden ziehen bei '
                   'Rahmenverträgen nach. Ohne Zertifikat bleibt ein wachsender Teil des Marktes verschlossen.',
        'verwandt': None,
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'reinigung',
        'name': 'Reinigung',
        'name_full': 'Reinigungsunternehmen',
        'name_upper': 'REINIGUNG',
        'icon': '🧽',
        'meta_title': 'ISO 9001 für Reinigungsunternehmen | Ausschreibung',
        'meta_desc': 'ISO 9001 für Reinigungsbetriebe: Objektmappe, Leistungsverzeichnis, Objektkontrollen, '
                     'Gefahrstoffe, Einweisung. Voraussetzung für viele Ausschreibungen.',
        'h1': 'ISO 9001 für Reinigungsunternehmen',
        'hero_sub': 'Viele Objekte, wechselndes Personal, Kontrollen, die belegbar sein müssen. Wir bauen ein '
                    'QM-System, das mit der Zahl Ihrer Objekte mitwächst statt zu ersticken.',

        'probleme': [
            ('Ausschreibungen fordern den QM-Nachweis – und Sie können ihn nicht liefern',
             'Kommunen, Kliniken, Wohnungsgesellschaften und Industriekunden setzen ein zertifiziertes '
             'QM-System regelmäßig als Eignungskriterium an. Ohne Nachweis kommen Sie nicht in die Wertung.'),
            ('Bei vierzig Objekten weiß niemand mehr, was wo vereinbart ist',
             'Leistungsverzeichnisse liegen im Angebotsordner, die Realität steckt im Kopf des Objektleiters. '
             'Der Auditor fragt nach der Verbindung zwischen beidem.'),
            ('Qualitätskontrollen finden statt – nur nicht nachweisbar',
             'Der Objektleiter schaut vorbei und sagt Bescheid. Für Kapitel 9.1 braucht es ein Protokoll, '
             'aus dem hervorgeht, was geprüft wurde und was daraus folgte.'),
        ],

        'normtabelle': [
            ('8.5.1 Steuerung der Dienstleistungserbringung',
             'Was im Objekt konkret zu tun ist, steht nirgends verbindlich',
             'Objektmappe mit Leistungsverzeichnis, Reinigungs- und Turnusplan, Raumbuch'),
            ('7.2 Kompetenz',
             'Neue Kräfte werden „mitgenommen", ohne Nachweis der Einweisung',
             'Standardisierter Einweisungsbogen je Objekt mit Unterschrift, Nachweis von Unterweisungen'),
            ('9.1.1 Überwachung und Messung',
             'Objektkontrollen sind nicht dokumentiert',
             'Kontrollplan je Objekt, Kontrollprotokoll mit Bewertung, Maßnahmen bei Abweichung'),
            ('7.1.4 / 8.5.1 Prozessumgebung und Betriebsmittel',
             'Gefahrstoffe und Maschinen sind nicht geregelt',
             'Gefahrstoffverzeichnis, Sicherheitsdatenblätter, Betriebsanweisungen, Wartung der Maschinen'),
            ('8.4 Externe Anbieter',
             'Subunternehmer erbringen Leistung ohne Qualitätsvorgabe',
             'Auswahl- und Bewertungsverfahren für Subunternehmer, Weitergabe der Objektvorgaben, Kontrolle'),
            ('8.7 / 10.2 Abweichungen und Korrekturmaßnahmen',
             'Kundenbeschwerden werden gelöst, aber nicht ausgewertet',
             'Beschwerdeerfassung je Objekt, Ursachenanalyse, dokumentierte Maßnahme mit Wirksamkeitsprüfung'),
        ],

        'dokumente': [
            'Objektmappe als zentrales Dokument je Einsatzort',
            'Leistungsverzeichnis und Turnusplan aus dem Angebot abgeleitet',
            'Einweisungsnachweis für neue Reinigungskräfte',
            'Kontrollplan und Objektkontrollprotokoll',
            'Gefahrstoffverzeichnis mit Sicherheitsdatenblättern und Betriebsanweisungen',
            'Subunternehmerbewertung, falls Sie fremd vergeben',
            'Kennzahlen: Beschwerden je Objekt, Kontrollergebnisse, Fluktuation',
        ],

        'phasen': [
            'Wir nehmen ein typisches Objekt und bauen daran die Objektmappe auf. Diese Struktur lässt sich '
            'anschließend auf alle weiteren Objekte übertragen, ohne jedes Mal neu zu denken.',
            'Wir verbinden Angebot, Leistungsverzeichnis und Reinigungsplan zu einer Kette – das ist genau '
            'der Nachweis, den Auditor und Auftraggeber sehen wollen.',
            'Wir richten die Objektkontrolle so ein, dass sie in wenigen Minuten dokumentiert ist. '
            'Alles andere wird im Alltag nicht durchgehalten.',
        ],

        'faq': [
            ('Was fordern Kliniken und Pflegeeinrichtungen zusätzlich?',
             'Dort kommen Hygieneanforderungen hinzu – Hygieneplan, Desinfektionspläne, abgestimmte Zuständigkeit '
             'mit der Hygienefachkraft des Auftraggebers. Die ISO 9001 deckt den organisatorischen Rahmen ab; '
             'die konkreten Hygienevorgaben kommen vom Auftraggeber und aus dem Infektionsschutzrecht.'),
            ('Brauchen wir eine Qualitätsmessung nach INSTA 800 oder DIN 13549?',
             'Nur wenn Ihr Auftraggeber sie fordert. Diese Normen beschreiben, wie Reinigungsqualität objektiv '
             'gemessen wird, und tauchen vor allem in größeren Ausschreibungen auf. Für die ISO 9001 genügt '
             'ein nachvollziehbares eigenes Kontrollverfahren.'),
            ('Wie dokumentiert man Kontrollen bei vierzig Objekten?',
             'Mit einem einheitlichen Kurzprotokoll, das in zwei bis drei Minuten ausgefüllt ist – gern digital '
             'per Smartphone. Entscheidend ist nicht der Umfang, sondern dass Abweichungen zu einer '
             'nachvollziehbaren Maßnahme führen.'),
            ('Was gilt für Subunternehmer?',
             'Sie bleiben gegenüber Ihrem Kunden verantwortlich. Kapitel 8.4 verlangt, dass Sie Subunternehmer '
             'auswählen, ihnen die Objektvorgaben weitergeben und ihre Leistung kontrollieren – mit Nachweis.'),
            ('Können wir die Zertifizierung auf einen Teil der Firma begrenzen?',
             'In der Regel nicht. Die ISO 9001 gilt für das ganze Unternehmen, das handhaben die meisten Zertifizierungsstellen so. Was Sie sehr wohl entscheiden können, ist die Formulierung des Geltungsbereichs – also was am Ende auf dem Zertifikat steht und was Sie damit gegenüber Ihren Auftraggebern zeigen wollen.'),
        ],

        'kontext': 'In der Gebäudereinigung entscheidet die ISO 9001 häufig über den Zugang zu größeren '
                   'Aufträgen. Kommunale Vergabestellen, Kliniken und Wohnungsgesellschaften setzen den '
                   'QM-Nachweis als Eignungskriterium an – und Ausschreibungen sind in dieser Branche der '
                   'entscheidende Vertriebskanal.',
        'verwandt': ('https://qm-guru.de/iso-9001-gebaeudereinigung/',
                     'Ausführlich für die Gebäudereinigung: Ablauf, Kosten und Ausschreibungspraxis'),
    },
]
