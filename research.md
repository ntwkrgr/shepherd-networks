# Shepherd Networks — Research & Design Notes

## Project Goal
Convert the multi-page Jekyll site to a polished, single-page website for Shepherd Networks — a network consulting business based in San Angelo, TX.

---

## Logo Image Analysis

| File | Size | Format | Notes |
|---|---|---|---|
| `shepherd-final.png` | 500×500 | RGBA (PNG color type 6) | Full-color logo with alpha channel. Likely has white background baked in. Used in header. |
| `shepherd-outline.png` | 612×612 | Grayscale (PNG color type 0) | Outline/minimal version. No alpha channel. Used in footer. |

### Transparency Fix (CSS)
Since the images may have white background pixels embedded:
- **Header (white bg):** Apply `mix-blend-mode: multiply` to `.logo-img`. White pixels × white bg = white (invisible). Colored logo pixels remain visible.
- **Footer (dark bg):** Apply `mix-blend-mode: screen` to `.footer-logo-img`. White areas of grayscale image remain bright/white. Dark areas disappear into the dark footer.

Both modes avoid needing to re-export the images with proper alpha channels.

---

## One-Page Template Research

### GitHub Templates Reviewed
- **HTML5 UP "Stellar"** — [html5up.net/stellar](https://html5up.net/stellar) (MIT/CCA 3.0 license) — Very popular free one-page template with icon-grid feature sections, spotlight alternating sections, clean tables, and contact form. Chosen as design inspiration.
- **HTML5 UP "Prologue"** — [html5up.net/prologue](https://html5up.net/prologue) — Good for portfolios, sidebar nav. Less suited for B2B services.
- **learning-zone/website-templates** — [github.com/learning-zone/website-templates](https://github.com/learning-zone/website-templates) — 150+ templates, more variety than quality.
- **designmodo/html-website-templates** — [github.com/designmodo/html-website-templates](https://github.com/designmodo/html-website-templates) — Clean Slides-based templates.

### Template Chosen: Stellar-Inspired (HTML5 UP)
Custom implementation inspired by HTML5 UP Stellar. Clean, professional, icon-forward layout suited for a B2B consulting firm. Licensed under Creative Commons Attribution 3.0.

#### Key Stellar Features Adopted:
- Sticky dark header with logo + anchor navigation
- Full-height hero with gradient background and centered CTA
- Icon feature cards grid for services
- Alternating section backgrounds (white / light gray)
- Rates tables with accent-color headers
- Two-column contact section
- Clean footer with minimal links

---

## One-Page Architecture

### URL Structure
All content served from `index.html`. Internal anchor navigation:
- `#home` → Hero section
- `#services` → All 8 services as cards
- `#why-us` → "Why Shepherd Networks?" features
- `#rates` → Pricing tables
- `#contact` → Contact form + info

### Navigation
Header nav uses anchor links. JS (IntersectionObserver) highlights the active nav item as user scrolls.

### Pages Kept (Backward Compatibility)
`services.html`, `rates.html`, `contact.html` remain in the repo but are no longer linked from nav. GitHub Pages will still serve them at their old URLs.

---

## Color Palette
| Variable | Hex | Usage |
|---|---|---|
| `--primary` | `#1d2e47` | Header, hero, footer, headings |
| `--primary-dark` | `#131d2e` | Hero gradient end, footer bottom |
| `--accent` | `#b8834a` | Buttons, icons, highlights |
| `--accent-dark` | `#9a6838` | Button hover |
| `--text` | `#2c3e50` | Body text |
| `--text-light` | `#6c7a89` | Subtext, table notes |
| `--bg` | `#ffffff` | White sections |
| `--bg-light` | `#f4f6f9` | Alternate sections |

---

## File Changes Summary

| File | Change |
|---|---|
| `index.html` | Full rewrite — all page content consolidated into one page with 5 sections |
| `_includes/header.html` | Dark header, anchor navigation, logo with `mix-blend-mode: screen` |
| `_includes/footer.html` | Simplified — no separate page links needed |
| `assets/css/style.css` | Full redesign — Stellar-inspired, larger logos, transparency fixes |
| `assets/js/main.js` | Added IntersectionObserver for active nav, smooth scroll, header scroll effects |
| `research.md` | This file — documents decisions and context |
