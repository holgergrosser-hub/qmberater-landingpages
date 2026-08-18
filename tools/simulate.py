#!/usr/bin/env python3
"""Simuliert Cloudflare-Worker + Netlify lokal, bevor irgendetwas live geht.

Port 8081 spielt Netlify  -> liefert public/
Port 8080 spielt qm-guru.de mit Worker-Route:
    /iso-9001-wissen*  -> Prefix abschneiden, an 8081 weiterreichen
    alles andere       -> 404 ("WordPress")
"""
import http.server
import socketserver
import threading
import urllib.request
import urllib.error
import functools
import sys

PUBLIC = str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'public')
PREFIX = '/iso-9001-wissen'

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=PUBLIC)
netlify = socketserver.TCPServer(('', 8081), Handler)
netlify.allow_reuse_address = True
threading.Thread(target=netlify.serve_forever, daemon=True).start()


class WorkerHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if not self.path.startswith(PREFIX):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'WordPress 404')
            return
        if self.path == PREFIX:
            self.send_response(301)
            self.send_header('Location', PREFIX + '/')
            self.end_headers()
            return
        rest = self.path[len(PREFIX):] or '/'
        try:
            with urllib.request.urlopen('http://127.0.0.1:8081' + rest) as r:
                body = r.read()
                self.send_response(r.status)
                for k, v in r.headers.items():
                    if k.lower() not in ('transfer-encoding', 'connection'):
                        self.send_header(k, v)
                self.end_headers()
                self.wfile.write(body)
        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(e.read())


worker = socketserver.TCPServer(('', 8080), WorkerHandler)
worker.allow_reuse_address = True
threading.Thread(target=worker.serve_forever, daemon=True).start()

TESTS = [
    ('/iso-9001-wissen/', 200, 'Hub-Startseite'),
    ('/iso-9001-wissen/produktion.html', 200, 'Branchenseite'),
    ('/iso-9001-wissen/bau-montage.html', 200, 'neue Branchenseite'),
    ('/iso-9001-wissen/logistik-spedition.html', 200, 'neue Branchenseite'),
    ('/iso-9001-wissen/personaldienstleistung.html', 200, 'neue Branchenseite'),
    ('/iso-9001-wissen/faq/', 200, 'FAQ-Uebersicht'),
    ('/iso-9001-wissen/faq/grundlagen.html', 200, 'FAQ-Themenseite'),
    ('/iso-9001-wissen/faq/audit-und-zertifizierung.html', 200, 'FAQ-Themenseite'),
    ('/iso-9001-wissen/assets/tailwind.css', 200, 'CSS'),
    ('/iso-9001-wissen/images/holger-grosser.jpg', 200, 'Foto'),
    ('/iso-9001-wissen/images/og-image.jpg', 200, 'OG-Bild'),
    ('/iso-9001-wissen/images/favicon.svg', 200, 'Favicon'),
    ('/iso-9001-wissen/sitemap.xml', 200, 'Sitemap'),
    ('/iso-9001-wissen/robots.txt', 200, 'robots.txt'),
    ('/iso-9001-wissen/handel.html?utm_source=test', 200, 'mit Query-Parameter'),
    ('/iso-9001-beratung/', 404, 'fremder Pfad -> WordPress'),
    ('/', 404, 'Startseite -> WordPress'),
]

fehler = 0
for pfad, erwartet, was in TESTS:
    try:
        req = urllib.request.Request('http://127.0.0.1:8080' + pfad)
        with urllib.request.urlopen(req) as r:
            code = r.status
    except urllib.error.HTTPError as e:
        code = e.code
    ok = code == erwartet
    fehler += 0 if ok else 1
    print(f"  {'OK ' if ok else 'FEHLER'}  {code:3d} (erwartet {erwartet})  {pfad:52s} {was}")

print()
print('Alle Tests bestanden.' if fehler == 0 else f'{fehler} Test(s) fehlgeschlagen!')
sys.exit(1 if fehler else 0)
