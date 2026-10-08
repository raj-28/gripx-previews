# GripX per-lead demo pipeline

Build: `node build_modern.js leads/<slug>.json` -> out/<slug>/{index.html,style.css,chat.js,img.js}

Inputs per lead:
- leads/<slug>.json: real data only (name, address, phone, reviews, services with sources, rating if great, theme colors from the business's own logo/photos, mascotKind, qa[] grounded in real review quotes, images manifest).
- assets/<slug>/*.jpg: the business's own public photos (listing galleries, Facebook). Not committed (binary); sources are recorded in the lead JSON ("photoSources").

Rules: real info only, no invented services/prices/hours, DEMO banner always on top, chatbot never mentions the owner, rating only if great, noindex, mobile-first.

Deploy: public repo raj-28/gripx-previews (GitHub Pages from trunk root), folder = <slug>-<random 6 hex>. Photos are inlined as base64 in img.js because binary uploads fail in the cloud browser. deploy_gh.sh commits text files via the GitHub web editor.
Needs: node, python3 + Pillow, puppeteer-core for screenshots (shot3.cjs / vp2.cjs).
