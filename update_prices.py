"""Télécharge les 60 dernières séances VINCI (DG.PA) dans site/prices.json pour la version hébergée."""
import datetime
import json
import os

from server import fetch_prices

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site", "prices.json")
data = fetch_prices()
data["updated"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
with open(out, "w", encoding="utf-8") as f:
    json.dump(data, f)
print(f"{len(data['prices'])} séances écrites dans {out}")
