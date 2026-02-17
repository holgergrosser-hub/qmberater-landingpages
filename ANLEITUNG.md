# 📚 SCHRITT-FÜR-SCHRITT ANLEITUNG
## QMBerater Landing Pages - Von 0 bis Live

---

## ✅ STATUS: ALLE SEITEN FERTIG!

Das Automatische Script hat ALLE Seiten erstellt:

- ✅ **index.html** - Übersichtsseite mit allen Branchen
- ✅ **produktion.html** - Produktion
- ✅ **dienstleistung.html** - Dienstleistung  
- ✅ **it-dienstleistung.html** - IT-Dienstleistung
- ✅ **it-softwareentwicklung.html** - IT/Softwareentwicklung
- ✅ **sicherheitsdienstleistung.html** - Sicherheitsdienstleistung

**Sie müssen NICHTS mehr manuell kopieren oder ersetzen!**

---

## 🎯 WAS SIE JETZT TUN MÜSSEN

### SCHRITT 1: Foto hinzufügen (WICHTIG!) 🖼️

**Ohne diesen Schritt funktionieren die Seiten nicht richtig!**

1. **Ihr Foto vorbereiten:**
   - Format: JPG oder WebP
   - Größe: Mindestens 500x500 Pixel (quadratisch!)
   - Professionelles Foto: Kopf & Schultern, Blickkontakt
   - Dateigröße: Unter 200 KB (für schnelle Ladezeit)

2. **Ordner erstellen:**
   ```bash
   # Im Terminal/CMD
   cd qmberater-landingpages/public
   mkdir images
   ```

3. **Foto kopieren:**
   ```bash
   # Windows (Explorer):
   # Kopieren Sie Ihr Foto nach:
   # qmberater-landingpages/public/images/holger-grosser.jpg
   
   # Mac (Finder):
   # Kopieren Sie Ihr Foto nach:
   # qmberater-landingpages/public/images/holger-grosser.jpg
   
   # Linux/Terminal:
   cp /pfad/zu/ihrem/foto.jpg qmberater-landingpages/public/images/holger-grosser.jpg
   ```

**Dateiname MUSS exakt sein:** `holger-grosser.jpg` (Kleinbuchstaben!)

---

### SCHRITT 2: Seiten lokal testen 🧪

**Option A: Mit Python (Einfachste Methode)**

```bash
# 1. Terminal öffnen
# 2. Zum Ordner navigieren
cd qmberater-landingpages/public

# 3. Webserver starten
python3 -m http.server 8000

# 4. Browser öffnen
# → http://localhost:8000
```

**Option B: Direkt im Browser öffnen**

```bash
# Windows:
# Doppelklick auf: qmberater-landingpages/public/index.html

# Mac:
open qmberater-landingpages/public/index.html

# Linux:
xdg-open qmberater-landingpages/public/index.html
```

**Was testen:**
- ✅ Foto wird angezeigt
- ✅ Alle Links funktionieren
- ✅ Mobile-Ansicht (Browser Developer Tools: F12 → Device Toolbar)
- ✅ WhatsApp-Button funktioniert
- ✅ Telefon-Button funktioniert
- ✅ Calendly-Link öffnet

---

### SCHRITT 3: Git Repository erstellen 📦

```bash
# 1. Terminal öffnen, zum Ordner navigieren
cd qmberater-landingpages

# 2. Git initialisieren
git init

# 3. Alle Dateien hinzufügen
git add .

# 4. Ersten Commit erstellen
git commit -m "Initial: QMBerater Landing Pages mit allen Branchen"

# 5. GitHub Repository erstellen (auf github.com):
# → "New Repository" klicken
# → Name: qmberater-landing
# → Public oder Private
# → Create Repository

# 6. Lokales Repo mit GitHub verbinden
git remote add origin https://github.com/IHR-USERNAME/qmberater-landing.git

# 7. Hochladen
git branch -M main
git push -u origin main
```

**Fertig!** Ihr Code ist jetzt auf GitHub.

---

### SCHRITT 4: Netlify Deployment 🚀

#### 4.1 Netlify Account

1. Gehen Sie zu: https://app.netlify.com
2. "Sign up" klicken
3. Mit GitHub einloggen

#### 4.2 Site erstellen

1. **"Add new site"** klicken
2. **"Import an existing project"** wählen
3. **GitHub** auswählen
4. **Repository autorisieren** (einmalig)
5. **Ihr Repository** wählen: `qmberater-landing`

#### 4.3 Build Settings

```
Build command:    (leer lassen)
Publish directory: public
```

6. **"Deploy site"** klicken

#### 4.4 Warten

- Deployment dauert: 30-60 Sekunden
- Status: "Site deploy in progress" → "Published"
- Sie erhalten automatisch eine URL: `https://random-name-123.netlify.app`

---

### SCHRITT 5: Custom Domain einrichten 🌐

#### 5.1 In Netlify

1. **Site settings** → **Domain management**
2. **"Add custom domain"** klicken
3. Eingeben: `qmberater.info`
4. Netlify zeigt DNS-Einstellungen

#### 5.2 Bei Ihrem Domain-Provider

**Variante A: Nameservers (Empfohlen)**

```
Netlify Nameservers:
dns1.p05.nsone.net
dns2.p05.nsone.net
dns3.p05.nsone.net
dns4.p05.nsone.net
```

1. Gehen Sie zu Ihrem Domain-Provider (z.B. Strato, IONOS, GoDaddy)
2. Domain-Einstellungen → Nameserver
3. Ersetzen Sie die bestehenden Nameserver mit den Netlify-Nameservern
4. Speichern

**Variante B: DNS Records (Falls Sie WordPress behalten)**

```
Type: A
Name: @ oder qmberater.info
Value: 75.2.60.5

Type: CNAME
Name: www
Value: IHR-SITE-NAME.netlify.app
```

#### 5.3 SSL-Zertifikat (Automatisch)

- Netlify erstellt automatisch ein kostenloses SSL-Zertifikat (Let's Encrypt)
- Dauert: 0-24 Stunden
- Danach: `https://qmberater.info` funktioniert

---

### SCHRITT 6: Testen Sie die Live-Seite ✅

Nach 5-60 Minuten (DNS-Propagation):

1. Öffnen: `https://qmberater.info`
2. Testen Sie:
   - ✅ Alle 6 Seiten laden
   - ✅ Ihr Foto wird angezeigt
   - ✅ WhatsApp-Button öffnet WhatsApp
   - ✅ Telefon-Button startet Anruf
   - ✅ Calendly öffnet sich
   - ✅ Angebote.qm-guru.de öffnet sich
   - ✅ Mobile-Ansicht funktioniert (Smartphone testen!)

---

## 🔄 UPDATES MACHEN

### Änderungen an den Seiten:

```bash
# 1. Datei bearbeiten (z.B. produktion.html)
# 2. Änderungen speichern
# 3. Git Commit

git add .
git commit -m "Update: Preis geändert"
git push

# 4. Netlify deployed AUTOMATISCH!
# → Nach 30 Sekunden ist die Änderung live
```

### Neue Seite hinzufügen:

```bash
# 1. Neue Branchen-Konfiguration in generate_all_pages.py hinzufügen
# 2. Script ausführen
python3 generate_all_pages.py

# 3. Hochladen
git add .
git commit -m "Neue Branche: Logistik"
git push
```

---

## 🛠️ TROUBLESHOOTING

### Problem: "Foto wird nicht angezeigt"

**Lösung:**
```bash
# Prüfen Sie den Dateipfad:
ls -la public/images/holger-grosser.jpg

# Sollte anzeigen:
# -rw-r--r-- 1 user user 123456 Feb 16 12:00 holger-grosser.jpg

# Wenn "No such file or directory":
# → Foto ist nicht am richtigen Ort!
```

### Problem: "WhatsApp-Link funktioniert nicht"

**Lösung:**
- Desktop: WhatsApp Web öffnet sich (normal)
- Mobile: WhatsApp App öffnet sich (normal)
- Nummer prüfen: `0157-92316673` korrekt?

### Problem: "Netlify Deploy failed"

**Lösung:**
```bash
# Prüfen Sie die Netlify Deploy Logs
# → Site → Deploys → Failed deploy → Show logs

# Häufigster Fehler: Publish directory falsch
# → Muss sein: public (nicht Public oder PUBLIC)
```

### Problem: "Domain funktioniert nicht"

**Lösung:**
```bash
# DNS-Propagation prüfen:
# → https://dnschecker.org
# → Domain eingeben: qmberater.info
# → Warten bis grün (bis zu 24h)

# Cache leeren:
# → Browser: Strg+Shift+R (Windows) / Cmd+Shift+R (Mac)
```

---

## 📊 ANALYTICS HINZUFÜGEN (Optional)

### Google Analytics

1. **Google Analytics Account** erstellen
2. **Measurement ID** kopieren (G-XXXXXXXXXX)
3. **In jede HTML-Datei** vor `</head>` einfügen:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

4. **Hochladen:**
```bash
git add .
git commit -m "Add: Google Analytics"
git push
```

---

## 🎨 ANPASSUNGEN

### Telefonnummer ändern:

**Suchen & Ersetzen in ALLEN HTML-Dateien:**

```
Alt: 0911-49522541
Neu: IHRE-NUMMER

Alt: 091149522541  (ohne Bindestriche!)
Neu: IHRE-NUMMER-OHNE-BINDESTRICHE

Alt: 0157-92316673
Neu: IHRE-WHATSAPP-NUMMER
```

**Tool-Tipp:**
- VS Code: Strg+Shift+H → "Replace in Files"
- Sublime: Strg+Shift+F → "Find in Files"

### Preise ändern:

**In allen Branchen-Seiten** (produktion.html, dienstleistung.html, etc.):

```html
<!-- Suchen: -->
<div class="text-5xl font-bold text-blue-600 mb-4">ab 3.800€</div>

<!-- Ersetzen mit: -->
<div class="text-5xl font-bold text-blue-600 mb-4">ab NEUER-PREIS€</div>
```

**BAFA-Förderung anpassen:**

```html
<!-- Suchen: -->
<p class="text-2xl font-bold text-green-700">💰 Sie sparen bis zu 1.750€ durch BAFA-Förderung!</p>

<!-- Ersetzen mit: -->
<p class="text-2xl font-bold text-green-700">💰 Sie sparen bis zu NEUER-BETRAG€ durch BAFA-Förderung!</p>
```

---

## 📋 CHECKLISTE - BEREIT FÜR LIVE?

- [ ] ✅ Foto holger-grosser.jpg hinzugefügt
- [ ] ✅ Alle Seiten lokal getestet
- [ ] ✅ Telefonnummern korrekt
- [ ] ✅ WhatsApp-Nummer korrekt
- [ ] ✅ Calendly-Link funktioniert
- [ ] ✅ Angebote-Link funktioniert
- [ ] ✅ Git Repository erstellt
- [ ] ✅ Auf GitHub gepusht
- [ ] ✅ Netlify verbunden
- [ ] ✅ Domain konfiguriert
- [ ] ✅ SSL aktiv (HTTPS)
- [ ] ✅ Mobile-Test durchgeführt
- [ ] ✅ Alle 6 Seiten funktionieren
- [ ] ✅ Google Analytics (optional)

---

## 🎯 SCHNELLSTART (TL;DR)

Für erfahrene Benutzer:

```bash
# 1. Foto hinzufügen
mkdir -p public/images
cp IHR-FOTO.jpg public/images/holger-grosser.jpg

# 2. Lokal testen
cd public && python3 -m http.server 8000

# 3. Git
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/IHR-USERNAME/qmberater-landing.git
git push -u origin main

# 4. Netlify
# → app.netlify.com
# → Import from GitHub
# → Publish dir: public
# → Deploy

# 5. Domain
# → Domain settings
# → Add custom domain: qmberater.info
# → Update DNS

# 6. Fertig! 🎉
```

---

## 📞 SUPPORT

**Bei Problemen:**

1. **README.md** nochmal lesen
2. **Netlify Docs:** https://docs.netlify.com
3. **Git Tutorial:** https://git-scm.com/docs
4. **Stack Overflow** für spezifische Fehler

**Typische Fragen:**

**F: Wie lange dauert DNS-Propagation?**  
A: 5 Minuten bis 24 Stunden. Meist 1-2 Stunden.

**F: Kann ich die Seiten auch ohne Netlify hosten?**  
A: Ja! Einfach alle Dateien aus `public/` auf Ihren Webserver hochladen.

**F: Kostet Netlify Geld?**  
A: Nein! Für Ihre Nutzung ist Netlify 100% kostenlos.

**F: Kann ich weitere Branchen hinzufügen?**  
A: Ja! `generate_all_pages.py` bearbeiten, ausführen, pushen.

**F: Wie mache ich SEO-Optimierung?**  
A: Die Seiten sind bereits SEO-optimiert (Meta-Tags, Schema.org). Für mehr: Google Search Console einrichten.

---

## ✅ NÄCHSTE SCHRITTE NACH GO-LIVE

1. **Google Search Console** einrichten
2. **Google My Business** updaten (Link zu neuen Seiten)
3. **Social Media** Posts (LinkedIn, Facebook)
4. **E-Mail-Signatur** mit Link zu Landing Pages
5. **Google Ads** Kampagnen starten
6. **Analytics** täglich prüfen
7. **A/B-Tests** durchführen (Headlines, CTAs)

---

**Version:** 1.0  
**Letzte Aktualisierung:** 2026-02-16  
**Erstellt für:** Holger Grosser / QM-Guru

**🎉 VIEL ERFOLG MIT IHREN LANDING PAGES! 🎉**
