const ICONS={
 home:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.8 3 10.2V20a1.2 1.2 0 0 0 1.2 1.2h5.1v-6.4h5.4v6.4h5.1A1.2 1.2 0 0 0 21 20v-9.8L12 2.8Z"/></svg>',
 search:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="7.2"/><path d="m20.5 20.5-4.4-4.4"/></svg>',
 user:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9.2"/><circle cx="12" cy="9.6" r="3.2"/><path d="M5.8 18.6c1.6-2.6 3.7-3.6 6.2-3.6s4.6 1 6.2 3.6"/></svg>',
 arrow:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 back:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
 bolt:'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13 2 4 14h6l-1 8 9-12h-6l1-8Z"/></svg>'};
const L={ // logo glyphs, drawn inline (no external assets)
 cursor:'<svg viewBox="0 0 32 32"><path d="M16 3 27 9.5v13L16 29 5 22.5v-13L16 3Z" fill="#E8EAF0"/><path d="M16 16 27 9.5M16 16 5 9.5M16 16v13" stroke="#05070D" stroke-width="1.6"/></svg>',
 modal:'<svg viewBox="0 0 32 32" fill="none" stroke="#B6F23A" stroke-width="3.4" stroke-linecap="round"><path d="M16 16c-2.4-3.6-4.2-5.2-6.4-5.2a5.2 5.2 0 0 0 0 10.4c2.2 0 4-1.6 6.4-5.2s4.2-5.2 6.4-5.2a5.2 5.2 0 0 1 0 10.4c-2.200 0-4-1.600-6.400-5.200Z" stroke="#fff"/></svg>',
 lang:'<svg viewBox="0 0 32 32"><path d="M6 21c3-1 3-5 6-6s4 1 6-1 2-5 6-5c-1 4-1 6-3 8s-1 4-4 6-6 0-8-1-3 0-3-1Z" fill="#F5C443"/><circle cx="22" cy="10" r="1.2" fill="#05070D"/></svg>',
 vercel:'<svg viewBox="0 0 32 32"><path d="M16 6 28 26H4L16 6Z" fill="#fff"/></svg>',
 supa:'<svg viewBox="0 0 32 32"><path d="M18 3v11h9L14 29V18H5L18 3Z" fill="#3ECF8E"/></svg>',
 pine:'<svg viewBox="0 0 32 32"><path d="M16 4 24 20H8L16 4Z" fill="#6D7BFF"/><rect x="14.500" y="20" width="3" height="8" fill="#6D7BFF"/></svg>',
 dd:'<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="11" fill="none" stroke="#9B6BFF" stroke-width="3.200"/><circle cx="16" cy="16" r="3.800" fill="#9B6BFF"/></svg>',
 wb:'<svg viewBox="0 0 32 32" fill="#FFC21A"><circle cx="9" cy="9" r="3"/><circle cx="9" cy="23" r="3"/><circle cx="23" cy="9" r="3"/><circle cx="23" cy="23" r="3"/><circle cx="16" cy="16" r="3"/></svg>',
 rail:'<svg viewBox="0 0 32 32" fill="none" stroke="#fff" stroke-width="2.600" stroke-linecap="round"><path d="M5 12h22M5 20h22M9 6v20M16 6v20M23 6v20" stroke-width="2"/></svg>',
 lin:'<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="11" fill="#5E6AD2"/><path d="m10 17 5 5M12 12l8 8" stroke="#fff" stroke-width="2.200" stroke-linecap="round"/></svg>'};
const DEALS=[
 {id:'cursor',name:'Cursor Pro',cat:'Dev Tools',tag:'AI Code Editor',line:'GPT-4 & Claude Access',old:48,unit:'/yr',logo:'cursor',claimed:4812,save:'$48',desc:'An AI-first code editor with frontier model access built in.'},
 {id:'modal',name:'Modal',cat:'Compute',tag:'Serverless GPUs',line:'Serverless GPUs',old:600,unit:'/yr',logo:'modal',claimed:3120,desc:'Run GPU workloads without managing infrastructure.'},
 {id:'langsmith',name:'LangSmith',cat:'Observability',tag:'LLM Observability',line:'LLM Observability',old:468,unit:'/yr',logo:'lang',claimed:2740,desc:'Trace, evaluate and monitor LLM applications.'},
 {id:'vercel',name:'Vercel Pro',cat:'Compute',tag:'Edge Hosting',line:'Frontend cloud & edge',old:240,unit:'/yr',logo:'vercel',claimed:2388,desc:'Deploy frontends on a global edge network.'},
 {id:'supabase',name:'Supabase',cat:'Databases',tag:'Postgres + Auth',line:'Postgres, auth & storage',old:300,unit:'/yr',logo:'supa',claimed:2210,desc:'Open-source Postgres backend with auth and storage.'},
 {id:'pinecone',name:'Pinecone',cat:'Databases',tag:'Vector Database',line:'Managed vector search',old:840,unit:'/yr',logo:'pine',claimed:1904,desc:'Managed vector database for retrieval workloads.'},
 {id:'datadog',name:'Datadog',cat:'Observability',tag:'Monitoring',line:'Infra & APM monitoring',old:1380,unit:'/yr',logo:'dd',claimed:1522,desc:'Full-stack monitoring and APM.'},
 {id:'wandb',name:'Weights & Biases',cat:'APIs',tag:'ML Experiment Tracking',line:'Experiment tracking',old:600,unit:'/yr',logo:'wb',claimed:1311,desc:'Track experiments, datasets and models.'},
 {id:'railway',name:'Railway',cat:'Compute',tag:'App Hosting',line:'Ship backends in minutes',old:120,unit:'/yr',logo:'rail',claimed:988,desc:'Deploy backends and databases with zero config.'},
 {id:'linear',name:'Linear',cat:'Dev Tools',tag:'Issue Tracking',line:'Issue tracking for teams',old:96,unit:'/yr',logo:'lin',claimed:874,desc:'Plan and ship product with fast issue tracking.'}];
const CATS=['All Tools','Compute','APIs','Observability','Databases','Dev Tools'];
const $=(s,r=document)=>r.querySelector(s);
const money=n=>'$'+n.toLocaleString('en-US');
const metaOf=d=>d.tag===d.line?d.tag:d.tag+' | '+d.line;
const price=d=>`${money(d.old)}${d.unit}`;
const chip=d=>`<div class="chip">${L[d.logo]}</div>`;
const TOTAL=142850;
function nav(page,cls){const a=(h,i,k,t)=>`<a href="${h}" class="${page===k?'active':''}" aria-label="${t}">${ICONS[i]}${cls?`<span>${t}</span>`:''}</a>`;
 return a('index.html','home','home','Home')+a('index.html','search','search','Search')+a('profile.html','user','profile','Profile');}
const FEED=[['Maya','Cursor Pro','12s'],['Dev','Modal','34s'],['Ana','Supabase','1m'],['Kofi','LangSmith','2m'],['Lee','Vercel Pro','3m'],['Sam','Pinecone','4m'],['Ivy','Datadog','6m']];
const COLORS=['#5EEAD4','#8CB4FF','#B79CFF','#F5C443','#7CF5CF','#6DD5EE'];
function feedHTML(){return FEED.map((f,i)=>`<li><span class="av" style="background:${COLORS[i%6]}">${f[0][0]}</span><span><b>${f[0]}</b> unlocked ${f[1]}</span><span class="t">${f[2]}</span></li>`).join('');}
function barsHTML(){const c={};DEALS.forEach(d=>c[d.cat]=(c[d.cat]||0)+d.old);const m=Math.max(...Object.values(c));
 return Object.entries(c).sort((a,b)=>b[1]-a[1]).map(([k,v])=>`<div class="bar"><div><span>${k}</span><span class="mono">${money(v)}</span></div><div class="track"><i style="width:${v/m*100}%"></i></div></div>`).join('');}
function topHTML(){return DEALS.slice(0,4).map(d=>`<a class="mini" href="deal.html?id=${d.id}">${chip(d)}<div><b>${d.name}</b><span>${d.claimed.toLocaleString()} claimed</span></div><span class="tag">FREE</span></a>`).join('');}
function widgets(){return `
 <section class="glass widget"><h4>Value unlocked <span class="live"><i></i>LIVE</span></h4><div class="bigstat" id="bigstat">${money(TOTAL)}</div><p class="mono" style="color:var(--muted);font-size:12px;margin-top:8px">across ${DEALS.length*37} deals · +$1,240 today</p></section>
 <section class="glass widget"><h4>Live claims <span class="live"><i></i>NOW</span></h4><ul class="feed">${feedHTML()}</ul></section>
 <section class="glass widget"><h4>Value by category</h4><div class="bars">${barsHTML()}</div></section>
 <section class="glass widget"><h4>Most claimed</h4>${topHTML()}</section>`;}
function shell(page,inner){
 document.body.insertAdjacentHTML('afterbegin',`<div class="bg-aurora"></div><div class="shell">
 <aside class="rail"><a class="brand" href="index.html"><i>${ICONS.bolt}</i>DealDrop</a>
  <nav class="railnav">${nav(page,1)}</nav>
  <div class="group"><h5>Categories</h5><nav class="railnav" id="railcats">${CATS.map(c=>`<a href="index.html?c=${encodeURIComponent(c)}" data-c="${c}">${c}</a>`).join("")}</nav></div>
  <div class="group glass widget" style="margin-top:34px"><h4>Sample theme</h4><p style="font-size:13px;color:var(--muted)">Placeholder data. Theme: Midnight Glass v1.</p></div></aside>
 <main class="main">${inner}<p class="foot">DealDrop · sample theme · placeholder data only</p></main>
 <aside class="side">${widgets()}</aside></div>
 <nav class="bottomnav">${nav(page,0)}</nav>`);}
function animateTotal(){const el=$('#bigstat');if(!el)return;let n=TOTAL-1500;const t=setInterval(()=>{n+=Math.ceil((TOTAL-n)/6);el.textContent=money(n);if(n>=TOTAL)clearInterval(t)},40)}
