const fs=require('fs'),path=require('path');const L=JSON.parse(fs.readFileSync(process.argv[2]));const out='out/'+L.slug;
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const sec=`<section id="enquiry" class="sec alt"><div class="wrap"><p class="eyebrow dark">REQUEST</p><h2>${esc(L.enquiryTitle)}</h2>
<form class="enq" onsubmit="event.preventDefault();var b=this.querySelector('.enqmsg');b.hidden=false;b.textContent='Demo only: this form sends nothing. On the live site it would send your request to the shop, and they would follow up. No quote or appointment is confirmed.';">
<label>Name<input required name="n" autocomplete="name"></label>
<label>Phone<input required name="p" inputmode="tel" autocomplete="tel"></label>
<label>${esc(L.enquiryLabel)}<textarea required name="d" rows="4"></textarea></label>
<button class="btn" type="submit">Send request</button>
<p class="enqmsg" hidden></p><p class="enqnote">${esc(L.enquiryNote)}</p></form></div></section>
`;
let h=fs.readFileSync(path.join(out,'index.html'),'utf8');h=h.replace('<section id="visit"',sec+'<section id="visit"');fs.writeFileSync(path.join(out,'index.html'),h);
fs.appendFileSync(path.join(out,'style.css'),`
.enq{display:grid;gap:14px;max-width:560px}.enq label{display:grid;gap:6px;font-weight:700;font-size:15px}.enq input,.enq textarea{font:inherit;padding:12px 14px;border-radius:10px;border:1px solid #c9ced6;background:#fff;color:#14171c}.enq .btn{border:0;cursor:pointer;font-size:16px;justify-self:start}.enqmsg{background:#14171c;color:#fff;padding:12px 14px;border-radius:10px;margin:0}.enqnote{font-size:13px;opacity:.7;margin:0}
`);
