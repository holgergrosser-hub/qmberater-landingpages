# 🚀 GITHUB DEPLOYMENT ANLEITUNG

**Von 0 bis Live in 10 Minuten!**

---

## 📋 VORAUSSETZUNGEN

- [ ] GitHub Account (kostenlos erstellen auf https://github.com)
- [ ] Git installiert (https://git-scm.com/downloads)
- [ ] Netlify Account (kostenlos, mit GitHub einloggen)
- [ ] Foto: `public/images/holger-grosser.jpg` hinzugefügt

---

## SCHRITT 1: FOTO HINZUFÜGEN (2 Min) 🖼️

```bash
# 1. Ordner erstellen
mkdir -p public/images

# 2. Ihr Foto kopieren
# Windows (Explorer):
#   → Datei kopieren nach: public/images/holger-grosser.jpg
# Mac (Finder):
#   → Datei kopieren nach: public/images/holger-grosser.jpg
# Linux (Terminal):
cp /pfad/zu/ihrem/foto.jpg public/images/holger-grosser.jpg
```

**Wichtig:** Dateiname MUSS `holger-grosser.jpg` sein (Kleinbuchstaben!)

---

## SCHRITT 2: GITHUB REPOSITORY ERSTELLEN (3 Min) 📦

### A) Auf GitHub.com

1. Gehen Sie zu: https://github.com
2. Oben rechts: **"+"** → **"New repository"**
3. Eingeben:
   - **Repository name:** `qmberater-landing`
   - **Description:** `Landing Pages für QM-Guru ISO 9001 Beratung`
   - **Public** (oder Private)
   - ✅ **NICHT** "Initialize with README" anklicken!
4. Click **"Create repository"**

GitHub zeigt Ihnen jetzt Befehle → **KOPIEREN SIE DIE URL!**

Beispiel: `https://github.com/IHR-USERNAME/qmberater-landing.git`

### B) Lokal Git initialisieren

Öffnen Sie Terminal/CMD im Projekt-Ordner:

```bash
# 1. Zum Projekt navigieren
cd pfad/zu/qmberater-landingpages

# 2. Git initialisieren
git init

# 3. Alle Dateien hinzufügen
git add .

# 4. Ersten Commit erstellen
git commit -m "Initial: QMBerater Landing Pages - 8 Branchen"

# 5. Branch umbenennen (falls nötig)
git branch -M main

# 6. Mit GitHub verbinden (IHRE URL einfügen!)
git remote add origin https://github.com/IHR-USERNAME/qmberater-landing.git

# 7. Hochladen
git push -u origin main
```

**Fertig!** Code ist jetzt auf GitHub! 🎉

---

## SCHRITT 3: NETLIFY DEPLOYMENT (3 Min) 🚀

### A) Bei Netlify anmelden

1. Gehen Sie zu: https://app.netlify.com
2. Click **"Sign up"**
3. Wählen Sie: **"Sign up with GitHub"**
4. Autorisieren Sie Netlify

### B) Site erstellen

1. Click **"Add new site"**
2. Click **"Import an existing project"**
3. Wählen Sie: **"GitHub"**
4. Autorisieren Sie Netlify (falls nötig)
5. Wählen Sie Ihr Repository: **`qmberater-landing`**

### C) Build Settings

```
Build command:     (leer lassen)
Publish directory: public
```

6. Click **"Deploy site"**

### D) Warten

- ⏱️ Deployment: 30-60 Sekunden
- Status: "Site deploy in progress" → "Published"
- URL: `https://random-name-123.netlify.app`

**Testen Sie die URL!** 🎉

---

## SCHRITT 4: CUSTOM DOMAIN (2 Min) 🌐

### A) In Netlify

1. Click **"Site settings"**
2. Click **"Domain management"**
3. Click **"Add custom domain"**
4. Eingeben: `qmberater.info`
5. Click **"Verify"**

Netlify zeigt DNS-Einstellungen:

```
Nameservers:
dns1.p05.nsone.net
dns2.p05.nsone.net
dns3.p05.nsone.net
dns4.p05.nsone.net
```

### B) Bei Ihrem Domain-Provider

Gehen Sie zu Ihrem Domain-Provider (Strato, IONOS, GoDaddy, etc.)

**Option 1: Nameservers (Empfohlen)**

1. Domain-Einstellungen → **Nameserver**
2. Ersetzen Sie bestehende Nameserver mit Netlify-Nameservern
3. Speichern

**Option 2: DNS Records (Falls Sie WordPress behalten)**

```
Type: A
Name: @ oder qmberater.info
Value: 75.2.60.5

Type: CNAME
Name: www
Value: IHR-SITE-NAME.netlify.app
```

### C) SSL-Zertifikat (Automatisch!)

- Netlify erstellt automatisch SSL (HTTPS)
- Dauert: 0-24 Stunden
- Danach: `https://qmberater.info` funktioniert ✅

---

## ✅ GESCHAFFT! IHRE SITE IST LIVE!

Nach 5-60 Minuten (DNS-Propagation):

```
https://qmberater.info
```

### Prüfen Sie:

- [ ] Index-Seite lädt (8 Branchen-Karten)
- [ ] Alle Branchen-Seiten funktionieren
- [ ] Ihr Foto wird angezeigt
- [ ] WhatsApp-Button funktioniert (öffnet WhatsApp)
- [ ] Telefon-Button funktioniert (startet Anruf)
- [ ] Calendly-Link öffnet sich
- [ ] Angebote-Formular öffnet sich
- [ ] Mobile-Ansicht funktioniert (Smartphone testen!)

---

## 🔄 UPDATES MACHEN

### Änderungen hochladen

```bash
# 1. Dateien bearbeiten
# (z.B. Preise ändern in produktion.html)

# 2. Status prüfen
git status

# 3. Änderungen hinzufügen
git add .

# 4. Commit erstellen
git commit -m "Update: Preise angepasst"

# 5. Hochladen
git push

# 6. Netlify deployed AUTOMATISCH!
# Nach 30 Sekunden ist die Änderung live
```

### Neue Branche hinzufügen

```bash
# 1. generate_all_pages.py bearbeiten
# (Neue Branche zur BRANCHEN-Liste hinzufügen)

# 2. Script ausführen
python3 generate_all_pages.py

# 3. Hochladen
git add .
git commit -m "Add: Neue Branche Logistik"
git push

# 4. Automatisch deployed!
```

---

## 📊 MONITORING

### Netlify Dashboard

**Deployment Status:**
- https://app.netlify.com/sites/IHR-SITE-NAME/deploys

**Metriken:**
- Besucher
- Bandbreite
- Build-Zeit

### Google Analytics (Optional)

Nach Setup:
- https://analytics.google.com

---

## 🛠️ TROUBLESHOOTING

### Problem: "Git not found"

**Lösung:**
```bash
# Git installieren:
# Windows: https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt install git

# Version prüfen:
git --version
```

### Problem: "Permission denied (publickey)"

**Lösung:**
```bash
# SSH Key generieren:
ssh-keygen -t ed25519 -C "ihre@email.de"

# Key zu GitHub hinzufügen:
# → GitHub Settings → SSH Keys → New SSH Key
# → Key einfügen (aus ~/.ssh/id_ed25519.pub)
```

### Problem: "Failed to deploy"

**Lösung:**
1. Netlify → Site → Deploys → Failed deploy → **Show logs**
2. Häufig: Publish directory falsch → Muss `public` sein
3. Re-deploy: Deploys → Trigger deploy → Deploy site

### Problem: "Domain nicht erreichbar"

**Lösung:**
```bash
# DNS Propagation prüfen:
# → https://dnschecker.org
# → Domain eingeben: qmberater.info
# → Warten (bis zu 24h, meist 1-2h)

# Cache leeren:
# Browser: Strg+Shift+R (Windows)
# Browser: Cmd+Shift+R (Mac)
```

---

## 📚 ZUSÄTZLICHE RESSOURCEN

### Git Cheat Sheet

```bash
# Status prüfen
git status

# Änderungen sehen
git diff

# Commit rückgängig machen
git reset HEAD~1

# Branch erstellen
git checkout -b neue-feature

# Branches mergen
git merge neue-feature

# Remote URL ändern
git remote set-url origin NEUE-URL
```

### Netlify CLI (Optional)

```bash
# Installieren
npm install -g netlify-cli

# Login
netlify login

# Lokal testen
netlify dev

# Deploy
netlify deploy --prod
```

---

## ✅ CHECKLISTE - DEPLOYMENT KOMPLETT

- [ ] GitHub Account erstellt
- [ ] Repository angelegt
- [ ] Code hochgeladen
- [ ] Netlify verbunden
- [ ] Site deployed
- [ ] Custom Domain konfiguriert
- [ ] SSL aktiv (HTTPS)
- [ ] Alle Seiten getestet
- [ ] Mobile getestet
- [ ] Foto vorhanden
- [ ] Google Search Console (optional)
- [ ] Google Analytics (optional)

---

## 🎯 NÄCHSTE SCHRITTE

1. **Marketing starten**
   - LinkedIn-Posts zu den Branchen
   - Google Ads Kampagnen
   - E-Mail-Signatur updaten

2. **SEO optimieren**
   - Google Search Console einrichten
   - Sitemap submitten
   - Backlinks aufbauen

3. **A/B-Tests**
   - Headlines testen
   - CTA-Buttons testen
   - Preise testen

4. **Analytics**
   - Conversion-Rate tracken
   - Heatmaps (Hotjar)
   - User-Feedback sammeln

---

## 🎉 GESCHAFFT!

**Ihr Repository ist live:**
- 🌐 **GitHub:** https://github.com/IHR-USERNAME/qmberater-landing
- 🚀 **Netlify:** https://qmberater.info
- 📊 **Status:** ✅ Produktionsbereit

**Automatische Deployments:**
- Jeder `git push` → Netlify deployed automatisch
- Nach 30 Sekunden live
- Keine manuellen Schritte nötig

**Weitere Branchen hinzufügen:**
- Script bearbeiten
- Ausführen
- Pushen
- Fertig!

---

**Happy Deploying! 🚀**

---

**Erstellt:** 2026-02-16  
**Version:** 1.0  
**Für:** qmberater.info
