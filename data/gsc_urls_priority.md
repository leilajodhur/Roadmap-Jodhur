# 🔍 URLs prioritaires Request Indexing GSC

**Date** : 13 mai 2026
**Statut sitemap** : 810 URLs soumises, 0 indexées (re-soumise aujourd'hui)
**Objectif** : forcer Google à crawler ces 15 URLs critiques en priorité → indexation 3-7 jours au lieu de 4-6 semaines

## 📋 Comment procéder (5 min)

1. Va sur [Google Search Console](https://search.google.com/search-console)
2. Sélectionne la propriété **sc-domain:jodhur.ma**
3. Pour chaque URL ci-dessous :
   - Colle l'URL dans la **barre de recherche** en haut
   - Attendre l'analyse (10-20 sec)
   - Cliquer **"Demander l'indexation"** ou **"Request indexing"**
   - Attendre confirmation (10 sec)
   - Passer à l'URL suivante

⚠️ **Quota GSC** : ~10-20 URLs/jour. Si tu hits la limite, reprendre demain.

---

## 🎯 15 URLs PRIORITAIRES (ordre d'importance)

### Tier 1 — Homepages multilingues (3)
- [ ] https://jodhur.ma/
- [ ] https://jodhur.ma/ar
- [ ] https://jodhur.ma/en

### Tier 2 — Page Leila (1, nouvelle URL après changement handle)
- [ ] https://jodhur.ma/pages/leila-conseillere-cosmetique-gratuitement

### Tier 3 — Collections symptômes (5) — futures landing pages ads
- [ ] https://jodhur.ma/collections/chute-de-cheveux
- [ ] https://jodhur.ma/collections/acne-boutons
- [ ] https://jodhur.ma/collections/pousse-des-cheveux
- [ ] https://jodhur.ma/collections/rides-anti-age
- [ ] https://jodhur.ma/collections/peau-seche

### Tier 4 — Articles Guide Beauté (5) — content authority
- [ ] https://jodhur.ma/blogs/guide-beaute/chute-de-cheveux
- [ ] https://jodhur.ma/blogs/guide-beaute/pousse-des-cheveux
- [ ] https://jodhur.ma/blogs/guide-beaute/les-boutons-acne
- [ ] https://jodhur.ma/blogs/guide-beaute/rides-signes-de-lage
- [ ] https://jodhur.ma/blogs/guide-beaute/huile-d-argan

### Tier 5 — Top produit signature (1)
- [ ] https://jodhur.ma/products/huile-argan-pure-bio-anti-age-maroc

---

## 📊 Suivi après indexation (~7 jours plus tard)

Vérifier dans GSC > Pages > Pages indexées : ces 15 doivent passer en "Indexée".

Si une URL reste "Découverte mais pas indexée" après 14 jours, vérifier :
- Schema valide (test Rich Results)
- Pas de noindex meta
- Performance mobile ≥ 50
