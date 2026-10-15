"""Petit serveur local : sert la page et relaie les cours VINCI (DG.PA) depuis Yahoo Finance."""
import http.server
import json
import os
import urllib.request

PORT = 8000
YAHOO_URL = "https://query1.finance.yahoo.com/v8/finance/chart/DG.PA?range=3mo&interval=1d"
ROOT = os.path.dirname(os.path.abspath(__file__))


def fetch_prices():
    req = urllib.request.Request(YAHOO_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.load(resp)
    result = data["chart"]["result"][0]
    quote = result["indicators"]["quote"][0]
    rows = []
    for ts, o, c in zip(result["timestamp"], quote["open"], quote["close"]):
        if o is not None and c is not None:
            rows.append({"t": ts, "open": round(o, 2), "close": round(c, 2)})
    # 60 séances : couvre toute la période de calcul, même après la date de fixation
    return {"currency": result["meta"].get("currency", "EUR"), "prices": rows[-60:]}


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        if self.path.startswith("/api/prices"):
            try:
                body = json.dumps(fetch_prices()).encode()
                self.send_response(200)
            except Exception as exc:  # erreur réseau ou format inattendu
                body = json.dumps({"error": str(exc)}).encode()
                self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            super().do_GET()


if __name__ == "__main__":
    print(f"Site disponible sur http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(("", PORT), Handler).serve_forever()
