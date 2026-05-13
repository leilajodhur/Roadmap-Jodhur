# 🛠️ Scripts d'exécution

## 📌 push_remaining_cls.py

**Mission** : pousser le fix CLS sur les 27 collections restantes (sur 50 total).

**Prérequis** :
1. Avoir un Shopify Admin API access token
2. L'ajouter dans `.env` à la racine du repo :
   ```
   SHOPIFY_STORE_DOMAIN=jodhur.myshopify.com
   SHOPIFY_ACCESS_TOKEN=shpat_xxxxx
   ```

**Comment obtenir le token** (5 min) :
1. Shopify Admin → Settings → Apps and sales channels → Develop apps
2. Create an app → "Claude Auto SEO"
3. Configuration → Admin API integration → Configure
4. Cocher : `write_products` + `read_products` + `write_product_listings`
5. Save → Install app → Reveal API access token once → copier `shpat_...`
6. Coller dans `.env`

**Exécution** :
```bash
pip install requests python-dotenv
python scripts/push_remaining_cls.py
```

**Résultat attendu** : 27 OK / 0 failed en ~30 secondes.

**Impact SEO** : CLS = 0 sur toutes les collections (vs 0.5-0.7 actuellement sur les non-fixées).

---

## 📊 État actuel CLS

| Statut | Nombre | Détail |
|---|---|---|
| ✅ Fixées | 23 | Symptômes + Catégories principales (priorité ads) |
| ⬜ À fixer via script | 27 | Ingrédients + sous-catégories |
| **Total** | **50** | 100% des collections |

---

## 🎯 Autres scripts à venir

- `audit_remaining_products.py` — audit SEO complet des 90 produits non-audités
- `enrich_short_metas.py` — enrichir les ~15 metas <130 chars détectées
- `generate_articles_FR_AR.py` — générer les 60 articles à partir des briefs
- `auto_schedule_articles.py` — programmer publication J+1...J+30 via API
