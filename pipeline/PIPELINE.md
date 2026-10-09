# GripX per-lead demo pipeline

Build: `node build_modern.js leads/<slug>.json` -> out/<slug>/{index.html,style.css,chat.js,img.js}

Inputs per lead:
- leads/<slug>.json: real data only (name, address, phone, reviews, services with sources, rating if great, theme colors from the business's own logo/photos, mascotKind, qa[] grounded in real review quotes, images manifest).
- assets/<slug>/*.jpg: the business's own public photos (listing galleries, Facebook). Not committed (binary); sources are recorded in the lead JSON ("photoSources").

Rules: real info only, no invented services/prices/hours, DEMO banner always on top, chatbot never mentions the owner, rating only if great, noindex, mobile-first.

Deploy: public repo raj-28/gripx-previews (GitHub Pages from trunk root), folder = <slug>-<random 6 hex>. Photos are inlined as base64 in img.js because binary uploads fail in the cloud browser. deploy_gh.sh commits text files via the GitHub web editor.
Needs: node, python3 + Pillow, puppeteer-core for screenshots (shot3.cjs / vp2.cjs).

## Current flow (Oct 9 update)
1. Spec: add a dict per lead to a gen/genN.py (copy gen/gen5.py). It checks every review quote as a substring of the fetched listing text, sets rating (only if 4.5+), hours, heroPos and the enquiry fields (enqTitle/enqLabel/enqNote), and writes leads/<slug>.json. The Pexels hero is read from /tmp/px4/p<id>.jpg (download https://images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?auto=compress&cs=tinysrgb&w=1600 with a browser UA).
2. `node build_modern.js leads/<slug>.json` then `node enq.js leads/<slug>.json` (demo-only request form, sends nothing).
3. `node shot3.cjs out/<slug> <prefix>` for local shots; review the top 390x844.
4. Deploy: `./dep1.sh <slug> <folder> index.html style.css chat.js img.js` (folder `<slug>-<6 hex>`; MODE=edit for existing). Needs a cloud browser lease in /tmp/lease. About 16 s per file.
5. Verify live with `Q=x node vp2.cjs "<url>?v=$RANDOM"` (writes /tmp/lv-m-top.png at 390x844). GitHub Pages lags 1-3 min.
Template note: template-modern/style.css holds placeholder colors #ffd23f (accent), #14171c (ink), #262c36 (ink2), #2a3140 (glow), #b07d00 (accentDark); the builder swaps them per lead. Reproduced byte-identical against live Miller-Time, Dyer & Sons and Lines and Layers on Oct 9.
