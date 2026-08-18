#!/bin/sh
# Kompletter Build: HTML generieren, danach Tailwind-CSS aus dem erzeugten HTML bauen.
# Einmalig vorher:  npm install
# Reihenfolge ist wichtig - Tailwind scannt die HTML-Dateien nach benutzten Klassen.
set -e
python3 generate_all_pages.py
npx --no-install tailwindcss -c tailwind.config.js -i build/input.css -o public/assets/tailwind.css --minify
echo "Build fertig."
