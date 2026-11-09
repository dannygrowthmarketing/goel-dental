# Goel Dental — website prototypes & strategy review

Prepared by Daniel Deepak for Dr Saurabh Goel and Dr Shikha Goel, 9 Nov 2026.

| File | What it is |
|---|---|
| `index.html` | Project hub |
| `goel-dental-care.html` | goeldentalcare.com prototype: general dentistry, 5–8 km catchment |
| `delhi-dental-smiles.html` | delhidentalsmiles.com prototype: cosmetic dentistry, South Delhi |
| `strategy-and-google-ads.html` | Google Ads history (₹24.88L all time), keyword evidence, competitors, page plan, tracking |
| `*.pdf` | PDF versions of the three pages |

Each HTML file is self-contained: photos from the clinic's own websites are embedded, no build step.
Open any page with `?debug=1` (or the footer button) to watch the tracking events.
Orange/gold badges mark details the clinic must confirm. Pages carry `noindex` so the preview never competes with the live sites.

Source: `/src` (Python generators + optimised WebP images). Rebuild: `cd src && python3 build_all.py`.
