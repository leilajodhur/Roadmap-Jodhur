"""
Push CLS fix sur les 27 collections restantes.

PRÉREQUIS :
1. Avoir un Shopify Admin API access token (custom app)
2. Le mettre dans .env :
    SHOPIFY_STORE_DOMAIN=jodhur.myshopify.com
    SHOPIFY_ACCESS_TOKEN=shpat_xxxxxxxx

USAGE :
    pip install requests python-dotenv
    python scripts/push_remaining_cls.py

CE QUE FAIT LE SCRIPT :
- Lit les fichiers data/cls_remaining/b*.json (49 collections au total)
- Skip les collections déjà fixées (23 listées dans DONE_HANDLES)
- Pour les 27 restantes : push collectionUpdate avec descriptionHtml corrigé
  (script JS reorder retiré + handle Leila mis à jour)
- Affiche le résultat OK/FAIL par collection

DURÉE : ~30 secondes pour les 27 collections
RISQUE : 0 — méthode validée sur 23 collections précédemment

Author: Claude AI assistant for Jodhur
Date: 13 mai 2026
"""
import json
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

DOMAIN = os.getenv("SHOPIFY_STORE_DOMAIN", "jodhur.myshopify.com")
TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")
API_VERSION = "2025-01"

if not TOKEN:
    print("❌ ERROR: missing SHOPIFY_ACCESS_TOKEN in .env")
    print("Crée un custom app Shopify, génère un Admin API token, et ajoute-le dans .env :")
    print("  SHOPIFY_ACCESS_TOKEN=shpat_xxxxx")
    sys.exit(1)

URL = f"https://{DOMAIN}/admin/api/{API_VERSION}/graphql.json"
HEADERS = {"X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"}

MUTATION = """
mutation collectionUpdate($input: CollectionInput!) {
  collectionUpdate(input: $input) {
    collection { id handle }
    userErrors { field message }
  }
}
"""

# 23 collections déjà fixées dans les sessions précédentes
DONE_HANDLES = {
    "acne-boutons",  # initial
    # Batch 0
    "visage", "cheveux", "voyage", "corps", "nettoyants-gommages",
    "hydratants-serums", "soins-specifiques",
    # Batch 1
    "eaux-florales-1", "shampoings-apres-shampoings", "soins-capillaires",
    "huiles-hydrolats", "savons-gommages", "huiles-beurres", "chute-de-cheveux",
    # Batch 2
    "pousse-des-cheveux", "taches-eclat", "peau-seche", "rides-anti-age",
    "sensibilite-rougeurs", "vergetures", "cicatrices",
    # + 1 supplémentaire
    "pellicules-1",
}

fixes_dir = ROOT / "data" / "cls_remaining"
all_collections = []
for batch_file in sorted(fixes_dir.glob("b*.json")):
    batch = json.loads(batch_file.read_text(encoding="utf-8"))
    all_collections.extend(batch)

print(f"📊 Total collections dans data/cls_remaining/ : {len(all_collections)}")
print(f"✅ Déjà fixées (skip) : {len(DONE_HANDLES)}")

to_push = [c for c in all_collections if c["handle"] not in DONE_HANDLES]
print(f"🚀 À pusher maintenant : {len(to_push)}")
print()

ok, fail = 0, 0
for i, c in enumerate(to_push, 1):
    handle = c["handle"]
    payload = {
        "query": MUTATION,
        "variables": {"input": {
            "id": c["id"],
            "descriptionHtml": c["descriptionHtml"]
        }},
    }
    print(f"  [{i:2d}/{len(to_push)}] {handle}...", end=" ", flush=True)
    try:
        r = requests.post(URL, headers=HEADERS, json=payload, timeout=30)
        data = r.json()
        errs = data.get("data", {}).get("collectionUpdate", {}).get("userErrors", [])
        if errs or "errors" in data:
            print(f"❌ {errs or data.get('errors')}")
            fail += 1
        else:
            print("✅ OK")
            ok += 1
    except Exception as e:
        print(f"❌ {e}")
        fail += 1

print()
print(f"📊 Résultat : {ok} OK / {fail} failed sur {len(to_push)} total")
if ok == len(to_push):
    print("🎉 Toutes les collections sont maintenant CLS-fixées !")
