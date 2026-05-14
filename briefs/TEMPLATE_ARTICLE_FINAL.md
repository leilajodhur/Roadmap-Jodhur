# 📐 TEMPLATE ARTICLE BLOG — Version finale validée

**Status** : ✅ Validé par Siham (13 mai 2026)
**Article référence** : [Comment faire pousser ses cheveux plus vite naturellement](https://jodhur.ma/blogs/news/comment-faire-pousser-cheveux-plus-vite-naturellement)
**Article ID Shopify** : `gid://shopify/Article/570289127481`

---

## 🎨 Spec Design (à appliquer à tous les 60 articles)

### Typography
- **Font-family** : `'Montserrat', -apple-system, sans-serif`
- **Chargement** : `<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">` en haut du body
- **Min font-size** : 1.6rem (jamais en dessous)

### Palette Jodhur (stricte)
| Couleur | Hex | Usage |
|---|---|---|
| Olive foncé | `#2d4a3a` | Titres H1, H2, H3 |
| Olive moyen | `#4a7c59` | Accents, CTAs, eyebrows |
| Terracotta | `#c89570` | Numéros, accents impact |
| Cream beige | `#f5f1ea` | Background hero & callouts |
| Cream très clair | `#f0f7f4` | Background CTA milieu |
| Or fin | `#d4a574` | Séparateurs lignes |
| Charcoal | `#2d2d2d` | Body text |
| Gris muted | `#555` / `#888` | Captions secondaires |
| Rouge soft | `#d97777` | Erreurs (section "à éviter") |
| Background erreur | `#fdf5f5` | Container erreur |

### Hiérarchie typographique
| Élément | Taille | Weight |
|---|---|---|
| H1 hero | **3rem** | 800 |
| Chiffres impact (1 cm / 2 cm) | **3.8rem** | 900 |
| Numéros section (1/2/3) | **3.4rem** | 900 |
| Timeline numbers | **2.6rem** | 900 |
| H2 sections | **2.4rem** | 800 |
| CTA "Prête à commencer ?" | **2.2rem** | 800 |
| H3 actifs | **2rem** | 700 |
| Besoin titres / Étape titres | **1.9rem** | 700 |
| Sous-titre hero | **1.7rem** | 400 |
| Featured snippet body | **1.7rem** | 400 |
| Pull quote italic | **1.7rem** | 400 italic |
| Lexique / refs titres | **1.7rem** | 700 |
| CTA bouton WhatsApp final | **1.7rem** | 700 |
| Sous-titre actif (terracotta) | **1.6rem** | 600 |
| CTA bouton WhatsApp middle | **1.6rem** | 700 |
| Body global | **1.6rem** | 400 |
| Eyebrows uppercase | **1.6rem** | 600-700 (letter-spacing 2.5px) |

---

## 🧩 Structure entonnoir (à respecter)

1. **HOOK** : Eyebrow + H1 hero + sous-titre (callout box cream)
2. **PROMISE** : Featured snippet "La réponse en 1 phrase" (border-left olive)
3. **CHIFFRE CHOC** : Comparaison gros chiffres (vitesse normale vs avec routine)
4. **WHY** : H2 + paragraphe + visuel infographie + cards "3 besoins" + pull quote italic
5. **SOLUTION** : H2 + 3 actifs numérotés (numéro géant + H3 + sous-titre + texte + CTA produit)
6. **HOW** : H2 + 3 cards routine (eyebrow date/heure + titre + bullets)
7. **CTA milieu** : Bouton WhatsApp Leila (background dégradé olive)
8. **OBJECTIONS** : H2 + 5 erreurs (cards rouge clair) avec ❌ Erreur + ✅ Solution
9. **PROOF** : H2 + timeline 4 milestones (chiffres impact + texte)
10. **CTA FINAL** : Block dégradé olive foncé blanc avec gros bouton WhatsApp
11. **Liens cluster** : Card avec 3 articles liés
12. **Lexique** : Box gris clair avec 6 termes scientifiques expliqués
13. **Références sci.** : PubMed liens + disclaimer médical italique

---

## 🧩 Widgets template Shopify à remplir (metafields)

Chaque article DOIT avoir ces 18 metafields :

### Fiche Express — 4 colonnes
| Key | Type | Exemple |
|---|---|---|
| `custom.q_colonne_1` | text | "Vitesse de pousse" |
| `custom.q_colonne_2` | text | "3 actifs clés" |
| `custom.q_colonne_3` | text | "Temps de résultats" |
| `custom.q_colonne_4` | text | "Origine" |
| `custom.mc1` | text | "2× plus vite — 2 cm/mois" |
| `custom.mc2` | text | "Romarin, ricin, fenugrec" |
| `custom.mc3` | text | "4 à 8 semaines" |
| `custom.mc4` | text | "Coopératives marocaines" |

### Questions Pratiques — 3 Q&A
| Key | Type | Exemple |
|---|---|---|
| `custom.fq1` + `custom.r1` | text + rich text | Q1 + R1 |
| `custom.fq2` + `custom.r2` | text + rich text | Q2 + R2 |
| `custom.q3` + `custom.r3` | text + rich text | Q3 + R3 |

### Recette Maison
- `custom.recette_titre` (text)
- `custom.recette_desq` (rich text)

### Produits liés
- `custom.blog_collection` (collection_reference)

### Leila Recommande
- `custom.leila_recommande` (rich text)

---

## 🎨 7 Visuels par article

| # | Type | Création |
|---|---|---|
| 1 | Photo héros | Smartphone par toi |
| 2 | Infographie concept clé | **Canva via prompt template** |
| 3 | Photo produit hero | Smartphone par toi |
| 4 | Photo produit complémentaire | Smartphone par toi |
| 5 | Calendrier routine | **Canva via prompt template** |
| 6 | Grille erreurs vs solutions | **Canva via prompt template** |
| 7 | Timeline résultats | **Canva via prompt template** |

### Canva — règles strictes
- Font : **Montserrat exclusif**
- Body text : **min 18pt** (= 1.6rem web)
- Numéros impact : **56pt+ weight 900**
- Couleurs : **palette Jodhur stricte** uniquement
- Style : **éditorial magazine premium**, breathing room, line illustrations monochrome
- **NO** emoji clipart, **NO** couleurs vives, **NO** gradients
- Format : Landscape 1200×630 (horizontal) ou 1200×800 (si plus de contenu)

---

## 🔬 Citations scientifiques

Pour chaque article santé/beauté, inclure :
- **Référence numérotée** [1] [2] avec PMID PubMed
- **Hyperlien** vers `https://pubmed.ncbi.nlm.nih.gov/{PMID}/`
- **Format** : `Auteur Y, et al. Titre italique. Journal. AAAA;Vol(Issue):pages.`
- **Disclaimer médical** italique en fin d'article

---

## 📊 SEO

- **Title (60c max)** : avec keyword principal + bénéfice + Jodhur ou variante
- **Meta-desc (155c max)** : promesse + actif principal + délai résultat
- **Schema HowTo** : si article "Comment ..." (metafield `aeo.howto_json`)
- **Schema FAQPage** : auto via `<details>` natif Shopify
- **Internal links** : 3-5 produits + 2-3 articles cluster

---

## 🌐 Hreflang FR ↔ AR

Pour chaque article FR, créer son équivalent AR dans `/ar/blogs/news/` avec slug Latin (ou translit AR).
Le theme gère automatiquement les hreflang via Shopify Markets.

---

## ✅ Checklist final article (avant publication)

- [ ] Title SEO 50-60 chars
- [ ] Meta-desc 140-155 chars
- [ ] Body avec Montserrat + min 1.6rem
- [ ] H1 hero avec chiffre impact
- [ ] Featured snippet "En 1 phrase"
- [ ] 3-5 sections H2 avec border-bottom
- [ ] 5 erreurs cards (si applicable)
- [ ] Timeline résultats avec chiffres
- [ ] CTA Leila milieu + fin
- [ ] 18 metafields widgets remplis
- [ ] Schema HowTo si "Comment X..."
- [ ] Lexique scientifique 6 termes
- [ ] 2 références PubMed + disclaimer médical
- [ ] 4-7 visuels Canva ou photos
- [ ] Tags : cluster + sous-thème + "guide-beaute"
- [ ] Auteur : "Leila — Conseillère Beauté Intelligente"

---

**🚀 PROCHAINE ÉTAPE** :

Avec ce template validé, générer les 29 autres articles FR + 30 articles AR.
Auto-scheduling Shopify : J+1 à J+30 (2 articles/jour FR+AR).
