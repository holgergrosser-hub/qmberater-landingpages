/**
 * Cloudflare Worker: blendet die Netlify-Site unter qm-guru.de/iso-9001-wissen/ ein.
 *
 * Worker-Name:  wissen-proxy
 * Routen (Zone qm-guru.de):
 *     qm-guru.de/iso-9001-wissen*
 *     www.qm-guru.de/iso-9001-wissen*
 *
 * Einrichtung:
 * 1. Cloudflare -> Workers & Pages -> Create -> Worker
 *    -> Vorlage "Starten Sie mit Hello World!" -> Name "wissen-proxy" -> Deploy
 * 2. Edit Code -> diesen Code komplett einfuegen -> Deploy
 * 3. Beide Routen oben anlegen, Fehlermodus auf Standard lassen
 * 4. Test: https://qm-guru.de/iso-9001-wissen/
 */

const PREFIX = "/iso-9001-wissen";
const ORIGIN = "https://landingpage-qmberater.netlify.app";

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // /iso-9001-wissen  ->  /iso-9001-wissen/   (dauerhaft)
    if (url.pathname === PREFIX) {
      return Response.redirect("https://qm-guru.de" + PREFIX + "/" + url.search, 301);
    }

    // /iso-9001-wissen/xyz  ->  Netlify /xyz
    const upstream = ORIGIN + url.pathname.slice(PREFIX.length) + url.search;
    return fetch(upstream, request);
  },
};
