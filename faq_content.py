# -*- coding: utf-8 -*-
"""
FAQ-Bibliothek – Fragen aus der Beratungspraxis von Holger Grosser.

HERKUNFT: Die Antworten stammen aus der Wissensdatenbank (Transkripte echter
Beratungsgespräche). Sie wurden für die Veröffentlichung generalisiert:
KEINE Kundennamen, KEINE Firmennamen von Auftraggebern, KEINE Personennamen,
KEINE Dienstleisternamen, keine kundenspezifischen Zahlen.

REGEL für neue Einträge: Wenn eine Antwort nur mit dem Kontext eines bestimmten
Kunden verständlich ist, gehört sie hier NICHT hinein. Umschreiben, bis sie für
jeden Leser stimmt – oder weglassen.

PFLEGE: halbjährlich (siehe README). Dabei prüfen:
  - Sind Aussagen zu Normen, Fristen und Förderbeträgen noch aktuell?
  - Sind neue wiederkehrende Fragen dazugekommen?
  - Steht irgendwo doch ein Name?
"""

FAQ_SEITEN = [

    # ------------------------------------------------------------------ #
    {
        'slug': 'grundlagen',
        'titel': 'Grundlagen der ISO 9001',
        'meta_title': 'ISO 9001 Grundlagen – häufige Fragen | QM-Guru',
        'meta_desc': 'Muss man die Norm kaufen? Kann man den Geltungsbereich begrenzen? Wie umfangreich '
                     'muss das Handbuch sein? Antworten aus 30 Jahren Beratungspraxis.',
        'intro': 'Die Fragen, die fast immer im ersten Gespräch kommen – meist noch bevor irgendjemand '
                 'ein Dokument gesehen hat.',
        'fragen': [
            ('Müssen wir die ISO-9001-Norm kaufen und durchlesen?',
             'Nein, das bringt Ihnen nichts. Die Norm ist so verklausuliert, dass sie zu lesen unsinnig ist – '
             'und wenn Sie sie im Haus haben, müssen Sie im Audit auch Antworten dazu geben. Sagen Sie im Audit '
             'einfach: die Norm liegt beim Berater. Ihre Aufgabe ist es, dass das umgesetzt wird, was wir '
             'gemeinsam beschrieben haben – nicht, Normtexte zu interpretieren.'),
            ('Können wir die Zertifizierung auf einen Teil der Firma begrenzen?',
             'In der Regel nicht. Die ISO 9001 gilt für das ganze Unternehmen, das handhaben die meisten '
             'Zertifizierungsstellen so. Sie müssen also alle relevanten Prozesse einbeziehen. Was Sie sehr wohl '
             'gestalten können, ist die Formulierung des Geltungsbereichs – also was am Ende auf dem Zertifikat '
             'steht und was Sie damit gegenüber Ihren Kunden zeigen wollen.'),
            ('Wie begründen wir, dass einzelne Normforderungen bei uns nicht anwendbar sind?',
             'Bei den allermeisten Firmen geht eine einfache Erklärung durch. Wenn offensichtlich ist, dass Sie '
             'keine Entwicklung betreiben, reicht eine kurze Begründung im Anwendungsbereich. Manche Auditoren '
             'wollen mehr Details, aber das ist oft an den Haaren herbeigezogen. Verkomplizieren Sie es nicht.'),
            ('Wie detailliert muss das QM-Handbuch sein?',
             'Deutlich weniger detailliert, als die meisten denken. Was wir in der Beratung beschreiben, reicht '
             'auch für eine akkreditierte Zertifizierung – völlig unabhängig davon, welche Stelle prüft. Der Kunde '
             'beschreibt das, was er hat. Nicht umfangreich, nicht bis ins letzte Detail, aber es reicht. '
             'Bei uns sind das etwa zehn Seiten, und die sind nicht vollgeschrieben.'),
            ('Sollen wir uns ein QM-Handbuch aus dem Internet als Vorlage nehmen?',
             'Davon rate ich ab. Sie bekommen ein Dokument, das ein anderes Unternehmen beschreibt, und müssen es '
             'dann rückwärts an Ihre Realität anpassen. Das dauert länger, als es gleich richtig zu machen – und '
             'im Audit merkt man sofort, wenn ein Handbuch nicht zur Firma passt.'),
            ('Unser Handbuch ist riesig und liest niemand. Muss das so bleiben?',
             'Nein. Wenn ein Handbuch so groß ist, dass es seit Jahren keiner gelesen hat, erfüllt es seinen Zweck '
             'nicht mehr. Solche Dokumente stammen oft von jemandem, der längst nicht mehr im Betrieb ist. Man kann '
             'die Dokumentation Schritt für Schritt zurückschneiden. Kümmern Sie sich lieber um die Dinge, die '
             'wirklich wichtig sind – zum Beispiel darum, dass Aufträge reinkommen.'),
            ('Wie kompliziert wird das mit der ISO 9001 wirklich?',
             'Man kann es kompliziert machen. Man kann es auch einfach aufbauen – dann tragen die Firmen das im '
             'Audit selbst vor und gut ist. Mehr Schau geht immer, und manche verkaufen das auch so. Notwendig ist '
             'es nicht.'),
            ('Müssen wir auf die neue Normfassung warten?',
             'Nein. Was heute sauber aufgebaut wird, enthält die neuen Anforderungen bereits. Eine Normrevision ist '
             'im Kern ein formaler Akt, und es gibt regelmäßig eine mehrjährige Übergangsfrist. Die Trennung von '
             'Risiken und Chancen zum Beispiel machen wir ohnehin seit jeher so. Damit müssen Sie sich nicht '
             'beschäftigen.'),
            ('Lohnt sich zusätzlich die ISO 14001?',
             'Das hängt von Ihrer Umweltrelevanz ab. Wer keine eigene Produktion, keine eigenen Anlagen und keine '
             'Gefahrstoffe hat, hat wenig harte Fakten für ein Umweltmanagement – Lieferantenauswahl nach '
             'Umweltkriterien ist weich. Wenn es sinnvoll ist, ergänzt man das bestehende Handbuch um einige Seiten '
             'und baut die Umweltthemen in vorhandene Dokumente ein: Kontextanalyse, Risiken, Managementbewertung. '
             'Man macht kein zweites System daneben.'),
            ('Ist eine nicht akkreditierte Zertifizierung genauso anerkannt wie eine vom TÜV?',
             'Nicht genauso anerkannt – aber sie funktioniert. Für viele Kunden gilt: ohne Zertifikat kommen Sie gar '
             'nicht erst rein, und dafür reicht sie. Wenn später ein Großkunde ausdrücklich ein akkreditiertes '
             'Zertifikat verlangt, haben Sie alle Dokumente bereits und können schnell wechseln. Prüfen Sie im '
             'Zweifel die Vergabe- oder Vertragsunterlagen – dort steht manchmal ausdrücklich „akkreditiert".'),
        ],
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'dokumentation',
        'titel': 'Dokumentation und Prozessbeschreibungen',
        'meta_title': 'QM-Dokumentation: wie viel ist nötig? | ISO 9001 FAQ',
        'meta_desc': 'Wie detailliert müssen Prozessbeschreibungen sein? Reicht Cloud-Backup? Müssen '
                     'Mitarbeiter Prozesse auswendig können? Praxisantworten zur ISO-9001-Dokumentation.',
        'intro': 'Der häufigste Fehler beim QM-Aufbau ist zu viel Dokumentation, nicht zu wenig. '
                 'Was zu detailliert beschrieben ist und nicht gelebt wird, fällt im Audit auf.',
        'fragen': [
            ('Wie detailliert müssen Prozessbeschreibungen sein?',
             'Im ersten Schritt bitte nicht zu detailliert – fünfzig bis sechzig Prozent Genauigkeit reichen. Wenn '
             'Sie zu genau beschreiben und sich dann keiner daran hält, haben wir schon verloren und müssen jedes '
             'Jahr nachziehen. Lieber „Wir erstellen ein Angebot mit einer Software" als drei Absätze darüber, wie '
             'genau. Detaillierte Anweisungen ergeben nur Sinn, wenn Sie auch sicherstellen, dass sie aktuell '
             'bleiben.'),
            ('Ab welchem Punkt müssen wir Prozesse überhaupt beschreiben?',
             'Die Akquise darf wild sein – wie Sie an Kontakte kommen, ist Ihre Sache. Ab der Angebotserstellung '
             'sollte aber etwas da sein. Von dort an läuft die Kette, die im Audit nachvollzogen wird.'),
            ('Müssen die Mitarbeiter die Prozessbeschreibungen auswendig können?',
             'Auf keinen Fall. Mitarbeiter sollen NICHT anhand des Ablaufdiagramms erklären „Das ist Schritt eins, '
             'Schritt zwei, Schritt drei" – das geht meistens schief. Sie sollen ihre normale Tagestätigkeit an '
             'einem echten Vorgang zeigen, so wie sie es täglich machen. Wenn der Auditor dann sagt „zeigen Sie mir '
             'das mal im Prozess", ist das einfach. Andersherum konzentrieren sich die Leute auf ein unnatürliches '
             'Dokument statt auf ihre echte Arbeit.'),
            ('Wie strukturieren wir die QM-Dokumentation am besten?',
             'Ein zentraler Ordner, nach Auditjahren geordnet, mit Unterordnern für Auditberichte, '
             'Managementbewertung und so weiter. Schulungsnachweise dürfen separat liegen, Hauptsache es ist '
             'verknüpft. Wenn Sie ein Intranet oder Wiki haben, ist das ideal – dort finden die Mitarbeiter alles, '
             'und genau das zeigen Sie im Audit.'),
            ('Wir haben zwei parallele Ablagesysteme. Ist das ein Problem?',
             'Ja. Wenn ich als Prüfer zwei Systeme sehe, sehe ich sofort ein Problem – ein bisschen findet man hier, '
             'ein bisschen dort. Sie können nicht in ein Audit gehen und schon selbst wissen, dass es dort hakt. '
             'Machen Sie vorher eine saubere Regelung. Diese Aufräumaktion steht ohnehin einmal im Jahr an.'),
            ('Reicht ein Cloud-Backup, oder brauchen wir eine eigene Sicherung?',
             'Für den Anfang ist Cloud in Ordnung. Schreiben Sie nur auf, welches System Sie wofür nutzen – das '
             'reicht als Nachweis. Wenn Sie später ein zusätzliches Backup-Werkzeug einführen, umso besser, aber es '
             'ist kein Hinderungsgrund für die Zertifizierung.'),
            ('Müssen wir alle Dokumente fürs Audit ausdrucken?',
             'Ich würde es tun. Die Unterlagen, die Sie aktualisiert haben – Lieferantenbewertung, Ersthelfer, '
             'Notfallnummern, Umweltaspekte – legen Sie dem Auditor vor, dann ist das Thema durch. Das geht '
             'schneller, als am Bildschirm zu suchen.'),
            ('Wie dokumentieren wir interne und externe Kommunikation?',
             'Mit einem Satz. Zum Beispiel: „Interne und externe Kommunikation erfolgt durch persönliche Gespräche, '
             'schriftlich oder anlassbezogene Besprechungen." Das ist alles. Im Audit reden Sie darüber oder zeigen '
             'es – ein eigenes Kommunikationskonzept braucht niemand.'),
            ('Wie viel Dokumentation braucht es insgesamt für die Zertifizierung?',
             'Eine Beschreibung des QM-Systems, Ziele, Organigramm, Prozessbeschreibungen, Lieferantenbewertung und '
             'etwas zur Kundenzufriedenheit. Beschreiben Sie, was Sie tun. Das meiste davon existiert in Ihrem '
             'Betrieb bereits in irgendeiner Form – es heißt nur anders.'),
        ],
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'organisation-und-verantwortung',
        'titel': 'Organigramm, Verantwortung und die Rolle des QMB',
        'meta_title': 'Organigramm & QMB-Rolle nach ISO 9001 | FAQ',
        'meta_desc': 'Wie detailliert muss das Organigramm sein? Wer ist Prozesseigner in kleinen Firmen? '
                     'Muss sich der QMB um alles kümmern? Antworten aus der Praxis.',
        'intro': 'Rund um Organigramm und Zuständigkeiten entsteht viel unnötige Arbeit – meist, weil '
                 'jemand glaubt, es müsse aussehen wie im Konzern.',
        'fragen': [
            ('Wie detailliert muss das Organigramm sein? Brauchen wir Namen?',
             'Funktionen reichen, Namen sind nicht zwingend. Und es muss auch kein grafisch gebautes Organigramm '
             'sein – eine stichwortartige Beschreibung genügt: wie viele Mitarbeiter, wer macht was, welche externen '
             'Stellen sind eingebunden (Steuerberatung, IT, Rechtsberatung). Basteln Sie nicht stundenlang an einem '
             'Schaubild.'),
            ('Kommen Minijobber und Werkstudenten ins Organigramm?',
             'Erstmal nicht. Legen Sie dem Prüfer nicht mehr vor als nötig. Die Hauptbesetzung reicht fürs Erste.'),
            ('Was gehört in die Verantwortungen und Befugnisse?',
             'Für jeden Bereich aus dem Organigramm drei, vier Hauptaufgaben in Stichworten. Personal macht '
             'Einstellungen und Schulungen, Lager macht Wareneingang und Bereitstellung – mehr nicht. Wenn man das '
             'nicht so schlank hält, landet man bei Stellenbeschreibungen, und das ufert aus.'),
            ('Wer ist Prozesseigner in einem kleinen Unternehmen?',
             'In kleinen Firmen ganz pragmatisch die Geschäftsführung. Es gibt schlicht nicht genug Leute, um jeden '
             'Prozess einzeln zu verteilen. Das ist völlig in Ordnung und realistisch – und im Audit auch '
             'nachvollziehbar.'),
            ('Muss sich der Qualitätsbeauftragte um alle Verbesserungen im Betrieb kümmern?',
             'Nein, und lassen Sie sich nicht in diese Ecke drängen. Jeder schaut in seinem Bereich ohnehin, was '
             'besser laufen könnte – das ist ein kontinuierlicher Prozess, der in den Abteilungen stattfindet. Ihre '
             'Aufgabe als QMB ist es, die Fäden zusammenzuhalten und das Audit zu organisieren. Mehr nicht.'),
            ('Welche Gesetze und Normen müssen wir auflisten?',
             'Die, die für Sie tatsächlich gelten. Verantwortlich für Ermittlung und Einhaltung ist die '
             'Geschäftsführung – das ist nicht nur Arbeitssicherheit, sondern ganz allgemein behördliche und '
             'gesetzliche Anforderungen. Die Liste soll übersichtlich bleiben, nicht vollständig im juristischen '
             'Sinn.'),
            ('Wird Datenschutz im ISO-Audit geprüft?',
             'Gefragt wird, ob Sie sich damit beschäftigt haben und wie Sie damit umgehen. Manche Auditoren gehen '
             'tiefer hinein, andere lassen das Thema komplett aus. Wenn Sie zeigen können, dass Sie sich gekümmert '
             'haben und eine Antwort haben, reicht das. Daraus kann Ihnen niemand einen Strick drehen.'),
            ('Müssen wir das QM-System anpassen, wenn sich Lieferanten ändern oder Maschinen dazukommen?',
             'Nein, dann machen wir nur Updates. So wenig wie möglich, so viel wie nötig. Alles andere frustriert und '
             'bringt keinen Mehrwert.'),
        ],
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'risiken-und-ziele',
        'titel': 'Risiken, Chancen und Qualitätsziele',
        'meta_title': 'Risikoanalyse & Qualitätsziele ISO 9001 | FAQ',
        'meta_desc': 'Risikoanalyse ohne erfundene Risiken: aus Projekten und Investitionen ableiten. '
                     'Dazu: welche Qualitätsziele nötig sind und wer sie festlegt.',
        'intro': 'Kapitel 6 macht vielen Sorgen, weil sie glauben, sie müssten sich Risiken ausdenken. '
                 'Müssen sie nicht – die Entscheidungen der letzten Jahre enthalten sie bereits.',
        'fragen': [
            ('Wie erstellen wir eine Risikobewertung, ohne uns Risiken auszudenken?',
             'Ganz pragmatisch über Ihre Projekte und Investitionen. Listen Sie die letzten rund vier Jahre auf – '
             'alles über etwa 2.000 Euro: neue Webseite, EDV-Ausstattung, Server, Umbau, Maschine. Dazu die geplanten '
             'Vorhaben. Sie kaufen sich ja keinen Server, weil Sie Spaß daran haben, sondern weil Sie ein Risiko oder '
             'eine Chance gesehen haben. Daraus wird die Risikobewertung. Sie müssen nichts Neues finden – Sie haben '
             'das heute schon im Griff.'),
            ('Sind mit „Projekten und Investitionen" unsere Kundenprojekte gemeint?',
             'Nein, ausdrücklich nicht. Es geht um Investitionen in die eigene Firma: Webseite, Eingangsbereich, '
             'Rechner, Server, Zulassungen, eine neue Stelle. Also das, was Sie getan haben, damit der Betrieb '
             'funktioniert und wächst. Ungefähr zwanzig vergangene und dazu die geplanten. Die 2.000 Euro sind kein '
             'Gesetz, sie sollen nur verhindern, dass Kleinkram in der Liste landet.'),
            ('Müssen wir wegen Nachhaltigkeit und Klimaneutralität viel ergänzen?',
             'Nein. Man muss das Thema einmal betrachten, mehr nicht. Bei den interessierten Parteien ergänzt man es '
             'an zwei, drei Stellen, dazu in der Risikobewertung und in der Managementbewertung. Und dann ein '
             'sauberer Satz, etwa: „Unser Risiko zum Thema Klimaneutralität ist gering ausgeprägt." Damit ist das '
             'Thema erledigt.'),
            ('Können wir die Risikoanalyse aus der ISO 27001 mit der ISO 9001 zusammenführen?',
             'Ja, das ergibt absolut Sinn. Der erste Teil beider Normen ist sehr ähnlich – Ziele, '
             'Managementbewertung, interne Audits. Ziehen Sie das gleich, damit Sie nicht zwei Systeme parallel '
             'pflegen. In der 27001 stecken mehr technische Risiken, die kaufmännischen haben Sie ohnehin schon.'),
            ('Welche Qualitätsziele brauchen wir?',
             'Messbare Ziele rund um Wertschöpfung und Kunden. Wenn Sie eine Geschäftsplanung haben, ergeben sich die '
             'Ziele daraus fast von selbst – inklusive Zahlen, Maßnahmen und Verantwortlichkeiten. Die '
             'Verantwortlichkeiten kommen wiederum aus dem Organigramm.'),
            ('Kann der Qualitätsbeauftragte die Ziele selbst festlegen?',
             'Nein, dafür müssen Sie mit der Geschäftsführung sprechen. Im Audit muss die Geschäftsführung die Ziele '
             'vertreten und erklären können. Welche messbaren Ziele werden verfolgt – Umsatz, Kundenzahl, etwas ganz '
             'anderes? Wahrscheinlich steht das bereits in einer Planung.'),
            ('Können wir Ziele nachträglich anpassen, wenn sie zu ambitioniert waren?',
             'Natürlich, jederzeit. Wenn zehn Prozent Umsatzsteigerung unrealistisch sind, gehen Sie auf vier oder '
             'fünf. Wichtig ist, dass die Ziele erreichbar sind – ein dauerhaft verfehltes Ziel hilft niemandem.'),
            ('Sollen wir bei Beschwerden das Ziel „null" eintragen?',
             'Ja, bei ernsthaften Beschwerden schon. Damit sind nicht die Kleinigkeiten gemeint, die immer mal '
             'passieren – ein Termin geht unter. Gemeint ist der Fall, in dem ein Kunde die Zusammenarbeit beendet, '
             'weil etwas grundlegend schiefgelaufen ist. Solche Fälle dokumentieren Sie hier.'),
        ],
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'lieferanten-und-pruefungen',
        'titel': 'Lieferanten, Einkauf und Prüfmittel',
        'meta_title': 'Lieferantenbewertung & Prüfmittel ISO 9001 | FAQ',
        'meta_desc': 'Wie viele Lieferanten müssen bewertet werden? Reicht Excel? Muss jede '
                     'Wareneingangsprüfung dokumentiert werden? Wie oft Prüfmittel kalibrieren?',
        'intro': 'Kapitel 8.4 wird regelmäßig zu kompliziert angelegt. Für die meisten Betriebe reicht '
                 'eine Liste und ein Schulnotensystem.',
        'fragen': [
            ('Wie viele Lieferanten müssen in die Bewertung?',
             'Fünf bis sieben Hauptlieferanten wären ideal, aber fünfzehn bis zwanzig sind auch kein Thema – dann '
             'erweitern Sie die Liste einfach. Tragen Sie den Firmennamen ein und was der Lieferant abdeckt, keine '
             'Adressen. Bewerten Sie nach Schulnoten von eins bis sechs, etwa nach Zuverlässigkeit, Qualität und '
             'Preis-Leistung. Die Kriterien dürfen Sie anpassen. Maßnahmen müssen Sie nur eintragen, wenn ein '
             'Lieferant schlecht bewertet ist – bei durchweg guten Noten braucht es keine.'),
            ('Brauchen wir dafür ein EDV-System?',
             'Nein. Wenn Sie eine Handvoll fester Lieferanten haben, reicht Excel völlig. Hauptsache, die Daten sind '
             'irgendwo erfasst und nachvollziehbar. Nicht überkomplizieren.'),
            ('Wir haben kaum Materiallieferanten, sondern Dienstleister. Was dann?',
             'Ersetzen Sie das Wort „Lieferant" durch „Dienstleister" und tragen Sie die ein, die für Sie wichtig '
             'sind. Bewertung nach demselben Schulnotensystem. Maßnahmen erst, wenn die Bewertung schlecht ausfällt.'),
            ('Müssen wir alle neuen Lieferanten sofort aufnehmen?',
             'Ganz pragmatisch: Hat sich nichts getan, bleibt die Liste wie sie ist. Kommt einer dazu, kommt er rein. '
             'Fällt einer weg, fliegt er raus. Mehr Aufwand muss das nicht sein.'),
            ('Brauchen wir einen formalen Lieferantenfreigabeprozess?',
             'Nein. Freigegebene und gesperrte Lieferanten sind ein Thema für größere Organisationen, wo ein Einkauf '
             'für nachgelagerte Besteller vorgibt, wer bestellt werden darf. Wenn bei Ihnen die Geschäftsführung oder '
             'eine Person im selben Raum bestellt, wird faktisch nichts freigegeben oder gesperrt – dann muss man es '
             'auch nicht dokumentieren.'),
            ('Reicht eine formlose E-Mail als Bestellung?',
             'Ja, das reicht völlig. Wichtig ist nur, dass nachvollziehbar ist, was wann von wem bestellt wurde. Das '
             'ist Ihre Bestellung.'),
            ('Müssen wir jede Wareneingangsprüfung dokumentieren?',
             'Wenn Sie ohnehin zu hundert Prozent prüfen, ist es schlau und pragmatisch, nur die Abweichungen zu '
             'dokumentieren. Das spart Papier. Wichtig ist nur: Es muss genau so in der Prüfanweisung stehen – dann '
             'ist das in Ordnung.'),
            ('Ein wichtiger Lieferant ist insolvent. Was heißt das fürs QM-System?',
             'Dokumentieren und anpassen, mehr nicht. Entscheidend ist, ob die Belieferung für Sie weiterhin '
             'funktioniert. Im QM-System aktualisieren Sie die Liste und gut ist.'),
            ('Müssen Messschieber und ähnliche Prüfmittel kalibriert werden?',
             'Ja, aber nicht zwingend jedes Jahr. Erfassen Sie zunächst, wie viele Prüfmittel überhaupt im Betrieb '
             'sind. Einmal jährlich ist üblich, zwei Jahre sind je nach Einsatzintensität ebenfalls vertretbar. '
             'Entscheidend ist, dass die Regelung praktikabel bleibt – und dass sie eingehalten wird.'),
            ('Müssen wir für jede Maschine monatlich Wartungsnachweise führen?',
             'Es darf keine Unterschriftenorgie werden, bei der jemand unterschreibt, ohne dass gewartet wurde. Die '
             'Wartung muss tatsächlich stattfinden. Legen Sie fest, wer zuständig ist, und dokumentieren Sie in '
             'sinnvollen Abständen – das reicht.'),
        ],
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'personal-und-arbeitssicherheit',
        'titel': 'Personal, Schulung und Arbeitssicherheit',
        'meta_title': 'Schulungen & Arbeitssicherheit nach ISO 9001 | FAQ',
        'meta_desc': 'Brauchen wir eine Qualifikationsmatrix? Was gehört in den Schulungsplan? Brauchen '
                     'kleine Betriebe eine Fachkraft für Arbeitssicherheit? Antworten aus der Praxis.',
        'intro': 'Kapitel 7.2 und die Arbeitssicherheit hängen eng zusammen. Beides lässt sich schlank '
                 'lösen – bis auf einen Punkt, bei dem ich ausdrücklich nicht zur Sparsamkeit rate.',
        'fragen': [
            ('Brauchen wir eine Qualifikationsmatrix?',
             'Kann man machen, muss man nicht. Interessant wird sie, wenn Sie daran arbeiten wollen, dass Aufgaben '
             'doppelt besetzt sind – wenn also nicht nur eine Person eine bestimmte Maschine bedienen kann. Wenn Sie '
             'solche Schwachstellen sehen und angehen wollen, ist die Matrix ein gutes Werkzeug. Wenn nicht, lassen '
             'wir sie weg.'),
            ('Was gehört in den Schulungsplan?',
             'Es geht nicht darum, Schulungen zu erfinden, sondern zu erfassen, was gelaufen ist. Sammeln Sie, was im '
             'letzten Jahr stattgefunden hat, und was für das kommende geplant ist – Fachqualifikationen, Lehrgänge, '
             'Unterweisungen. Geben Sie die Datei der Person, über die die Anmeldungen ohnehin laufen. Bilden Sie '
             'Gruppen statt jeden Namen einzeln aufzulisten. Wenn externe Nachweislisten existieren, verweisen Sie '
             'einfach darauf.'),
            ('Was heißt „Wirksamkeit" bei Schulungen?',
             'Bei Fachschulungen ein Zertifikat oder eine kurze Wissensabfrage. Bei Sicherheitsunterweisungen ist die '
             'Wirksamkeit, dass die gesetzlichen Anforderungen erfüllt sind und keine Unfälle passiert sind. Mehr '
             'braucht es nicht.'),
            ('Wir haben jetzt erstmals Mitarbeiter – brauchen wir Unterweisungen?',
             'Ja. Sobald Sie Mitarbeiter haben, kommt das Thema dazu. Eine kurze Online-Unterweisung, Nachweis '
             'zurück, abgelegt – damit ist es dokumentiert. Das gilt für Festangestellte genauso wie für Praktikanten '
             'und alle, die für Sie arbeiten.'),
            ('Was ist bei reinen Büroarbeitsplätzen nötig?',
             'Eine Grundunterweisung Arbeitsschutz, für Homeoffice zusätzlich das Thema Telearbeitsplatz. Das dauert '
             'zehn Minuten pro Person. Das tatsächliche Risiko ist im Büro gering, aber gesetzlich muss etwas '
             'geschehen – und wenn etwas passiert, haften Sie.'),
            ('Brauchen wir eine Fachkraft für Arbeitssicherheit?',
             'Neben der betriebsärztlichen Betreuung brauchen Sie in der Regel auch eine Fachkraft für '
             'Arbeitssicherheit, meist extern. Alternativ kann die Geschäftsführung selbst den Lehrgang machen – das '
             'ist allerdings nicht delegierbar. Wichtig fürs Audit ist zunächst, dass dokumentiert ist, dass Sie sich '
             'darum kümmern. Der Nachweis, dass die Leistung erbracht wird, reicht – ein förmlicher Vertrag ist nicht '
             'zwingend, eine Auftragsbestätigung genügt.'),
            ('Reicht es, Unterweisungen unterschreiben zu lassen?',
             'Nein, und hier rate ich ausdrücklich nicht zur Sparsamkeit. Fragen Sie nach, ob es angekommen ist. Wenn '
             'etwas passiert, befragt die Berufsgenossenschaft die Mitarbeiter – und wenn die sagen „ich habe nur '
             'unterschrieben", hilft das niemandem. Gerade erfahrene Leute werden übermütig: „Mache ich seit dreißig '
             'Jahren so", und dann ist der Finger ab. Bei Kran, Gurten und Maschinenschaltern immer wieder nachfassen.'),
            ('Muss der Qualitätsbeauftragte eine ISO-9001-Schulung machen?',
             'Die Norm müssen Sie sich nicht kaufen, die ist zu verklausuliert. Ihre Aufgabe ist festzustellen, ob '
             'das, was beschrieben wurde, noch gelebt wird – und wenn nicht, die Beschreibung an die Wirklichkeit '
             'anzupassen. Wenn Sie sich fachlich vertiefen wollen, gibt es Wochenkurse. Nötig für die Zertifizierung '
             'sind sie nicht.'),
        ],
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'kundenzufriedenheit',
        'titel': 'Kundenzufriedenheit messen',
        'meta_title': 'Kundenzufriedenheit nach ISO 9001 messen | FAQ',
        'meta_desc': 'Kundenzufriedenheit ohne Fragebögen: Selbsteinschätzung mit Schulnoten. Wie viele '
                     'Kunden, wer bewertet wen, und was tun bei Vertraulichkeit?',
        'intro': 'Kapitel 9.1.2 wird oft als Aufforderung zur großen Kundenbefragung missverstanden. '
                 'Das ist es nicht – und Befragungen, die niemand beantwortet, helfen ohnehin nicht.',
        'fragen': [
            ('Wie messen wir Kundenzufriedenheit, wenn wir keine schriftlichen Rückmeldungen bekommen?',
             'Dann machen Sie eine Selbsteinschätzung: Wie sieht der Kunde Sie? Sie bewerten nicht den Kunden, '
             'sondern wie der Kunde Sie in Punkten wie Flexibilität, Zuverlässigkeit und Liefertreue wahrnimmt. '
             'Beschränken Sie sich auf die Hauptkunden – vier, fünf reichen, zehn sind auch noch in Ordnung, aber '
             'bitte nicht hundert. Das ist ehrlicher und aussagekräftiger als eine Befragung, die niemand '
             'zurückschickt.'),
            ('Bewerten wir den Kunden oder bewertet der Kunde uns?',
             'Sie bewerten, wie der KUNDE SIE sieht – nicht umgekehrt. Wenn Sie keine Vorstellung davon haben, wie '
             'ein Kunde Sie wahrnimmt, wird es irgendwann schwierig mit den Aufträgen. Bemerkungen wie „schlechte '
             'interne Kommunikation beim Kunden" gehören dort nicht hinein, denn das ist nicht, wie er Sie sieht.'),
            ('Was, wenn Kunden aus Vertraulichkeitsgründen nichts Öffentliches abgeben?',
             'Machen Sie eine Eigenbewertung über vier bis fünf wichtige Projekte oder Kunden, nach Schulnoten von '
             'eins bis sechs. Wenn Sie einzelne positive Rückmeldungen haben – ein Referenzschreiben, eine E-Mail – '
             'verweisen Sie im Bemerkungsfeld darauf. Das untermauert Ihre Einschätzung.'),
            ('Müssen die Kundennamen in der Bewertung stehen?',
             'Nein. Wenn Ihre Kunden das nicht möchten, arbeiten wir mit Nummern: eine Spalte mit laufender Nummer, '
             'und in der Bewertung wird nur die Nummer referenziert. Die Region oder Branche sollte erkennbar sein, '
             'der Name nicht.'),
            ('Müssen wir alle Kunden dokumentieren?',
             'Nein, nur die Hauptkunden. Bei zehn Kunden reichen vier bis fünf. Es geht darum, ein belastbares Bild '
             'zu bekommen, nicht um Vollständigkeit.'),
            ('Müssen wir nach jedem Auftrag eine Umfrage verschicken?',
             'Nein. Der Prozess soll der Realität entsprechen und nichts Zusätzliches sein. Wenn Sie das gebündelt '
             'machen, etwa einmal im Monat, dokumentieren wir es so. Wichtiger als das Verschicken ist übrigens, dass '
             'Sie auf schlechte Rückmeldungen auch reagieren.'),
            ('Vorsicht bei zu guten Selbstbewertungen?',
             'Ja, unbedingt. Wenn Sie durchweg Bestnoten eintragen und eine halbe Stunde später im Audit erzählen, '
             'dass es mit einem Kunden Probleme gibt, passt das nicht zusammen. Tragen Sie ein, wie der Kunde Sie '
             'wirklich sieht.'),
        ],
    },

    # ------------------------------------------------------------------ #
    {
        'slug': 'audit-und-zertifizierung',
        'titel': 'Audit und Zertifizierung',
        'meta_title': 'ISO 9001 Audit: Ablauf und Vorbereitung | FAQ',
        'meta_desc': 'Wie läuft das Zertifizierungsaudit ab? Muss man Normpunkte auswendig können? Wie '
                     'oft internes Audit? Was passiert bei Abweichungen? Antworten aus der Praxis.',
        'intro': 'Die meiste Unsicherheit entsteht vor dem Audit, nicht darin. Hier steht, was tatsächlich '
                 'passiert.',
        'fragen': [
            ('Wie läuft ein Zertifizierungsaudit ab?',
             'In zwei Stufen. Stufe 1 ist die Dokumentenprüfung: Sie schicken die QM-Dokumente vorab, der Auditor '
             'sieht sie sich an. Am ersten Tag gehen Sie die Dokumente gemeinsam durch – gibt es ein QM-System, gibt '
             'es Ziele, gibt es eine Managementbewertung. Stufe 2 ist die Praxis: Der Auditor schaut sich an, wie es '
             'tatsächlich läuft.'),
            ('Müssen wir alle Normpunkte auswendig können?',
             'Auf keinen Fall. Alles, was Sie auswendig aufsagen, klingt unnatürlich. Sie haben eine Liste als '
             'Spickzettel, damit Sie wissen, wo Sie nachschauen. Wichtig ist nur ein Punkt bei der '
             'Managementbewertung: Sie haben den Entwurf erstellt und alles gesammelt, und die Geschäftsführung hat '
             'die Maßnahmen festgelegt und die Entscheidungen getroffen. Was im Einzelnen drinsteht, steht im Bericht '
             '– den kann man zeigen.'),
            ('Was will der Auditor bei der Prozessüberwachung konkret sehen?',
             'Er will nachvollziehen können, dass die Arbeit gemacht wurde. Fertige E-Mails, fertige Dokumente, '
             'Einträge im System. Nicht die Vorlagen, nicht die Automatisierung – das Ergebnis. Zeigen Sie einen '
             'abgeschlossenen Fall, an dem man von Anfang bis Ende alle Schritte sieht.'),
            ('Wir arbeiten ohne spezielle Software, nur per E-Mail. Geht das?',
             'Völlig in Ordnung. E-Mails sind Nachweise. Wichtig ist: Wenn Sie über eine Liste sprechen, müssen Sie '
             'die Liste zeigen können. Wenn Sie über eine E-Mail sprechen, die E-Mail. Es geht nicht darum, was Sie '
             'erzählen, sondern was Sie zeigen können.'),
            ('Brauchen wir für jede Anfrage ein förmliches Angebot?',
             'Sie brauchen eine Spur. Der Kunde fragt an, Sie kalkulieren, Sie machen ein Angebot – das ist Ihr '
             'Nachweis. Wird nachverhandelt, auch gut, aber die finale Auftragsbestätigung muss erkennbar sein. '
             'Telefonisch bestätigt? Dann eine kurze E-Mail hinterher: „Wie besprochen, Auftrag über X zum Preis Y." '
             'Fertig.'),
            ('Müssen alle Prozesse fertig sein, bevor zertifiziert wird?',
             'Nein. Wo etwas noch läuft, schreiben wir „in Umsetzung" und setzen ein Datum. Wichtig ist, dass die '
             'Punkte, die noch nicht vollständig erfüllt sind, dokumentiert und im Maßnahmenplan sind. Das ist der '
             'Normalfall, nicht die Ausnahme.'),
            ('Wie oft und wie aufwendig ist das interne Audit?',
             'Große Firmen legen einen Jahresplan an – im Januar Vertrieb, im Februar Einkauf. Für einen kleinen '
             'Betrieb ist das Unsinn: Sie machen einmal im Jahr ein internes Audit für die gesamte Firma. Die Planung '
             'steht in der Managementbewertung, mit Quartal und ausführender Stelle. Wenn ein externer Auditor das '
             'übernimmt, erledigt sich damit auch gleich die Diskussion über die Qualifikation.'),
            ('Müssen interner Auditbericht und Managementbewertung unterschiedlich aussehen?',
             'Ja, ein wenig. Sie sollten sich nicht Wort für Wort gleichen. Es genügt, die Formulierungen an einigen '
             'Stellen zu variieren – nicht alles umschreiben.'),
            ('Was passiert, wenn im Audit ein Hinweis oder eine Abweichung kommt?',
             'Dann arbeiten wir das ein. Wir stellen vor, was sich geändert hat, der Auditor stellt seine Fragen, wir '
             'haben die Nachweise. Kommen Hinweise oder Anregungen, gut, dann machen wir das. Eine Nebenabweichung '
             'ist kein Drama.'),
            ('Was muss die Geschäftsführung tun?',
             'Bei der Managementbewertung muss sie eingebunden sein, und im externen Audit muss sie die Ziele '
             'vertreten können. Vorbereiten lässt sich alles – aber die Geschäftsführung muss dazu etwas sagen '
             'können.'),
            ('Wie läuft das Überwachungsaudit im Folgejahr?',
             'Deutlich kleiner. Der Auditor schaut sich die Unterlagen an, Sie zeigen einen Auftrag wie gehabt, das '
             'war es. Im dritten Jahr wird es wieder etwas ausführlicher. Ein Berater muss dabei nicht anwesend sein '
             '– das spart Kosten, geht schneller, und der Auditor kann lockerer mit Ihnen sprechen.'),
            ('Wie bereiten wir uns vor, wenn lange nichts passiert ist?',
             'Eine Woche vor dem Audit gehen Sie noch einmal in Ruhe über alle Unterlagen. Mehr ist nicht nötig. '
             'Wichtig ist, dass Sie wissen, was in Ihren Dokumenten steht – wenn Sie im Audit über einen eigenen '
             'Satz stolpern, sieht das nicht gut aus.'),
            ('Was, wenn in den Dokumenten kleine Fehler sind?',
             'Ein einzelner Punkt ist unerheblich, darüber fällt kein Auditor. Problematisch wird es erst, wenn sich '
             'viele Kleinigkeiten häufen. Deshalb: Lesen Sie Ihre Dokumente einmal durch und prüfen Sie, ob Sie damit '
             'leben können und ob alles Sinn ergibt.'),
        ],
    },
]
