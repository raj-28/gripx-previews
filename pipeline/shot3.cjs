const http=require('http'),fs=require('fs'),path=require('path'),p=require('puppeteer-core');const wait=ms=>new Promise(r=>setTimeout(r,ms));
const root=process.argv[2],pre=process.argv[3],remote=process.argv[4];const T={'.html':'text/html','.js':'text/javascript','.css':'text/css'};
(async()=>{let s,U=remote;if(!U){s=http.createServer((q,r)=>{let f=path.join(root,q.url==='/'?'index.html':q.url.split('?')[0]);fs.readFile(f,(e,d)=>{if(e){r.statusCode=404;return r.end()}r.setHeader('content-type',T[path.extname(f)]||'text/plain');r.end(d)})}).listen(8152);U='http://127.0.0.1:8152/'}
const b=await p.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});
for(const m of [false,true]){const k=m?'m':'d';const pg=await b.newPage();const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('requestfailed',r=>errs.push('REQFAIL '+r.url()));
await pg.setViewport(m?{width:390,height:844,isMobile:true,hasTouch:true}:{width:1280,height:800});await pg.goto(U,{waitUntil:'networkidle2'});await wait(800);
await pg.screenshot({path:`${pre}-${k}-full.png`,fullPage:true});
await pg.click('#chips button');await wait(1500);await pg.screenshot({path:`${pre}-${k}-chat.png`});console.log(k,JSON.stringify(errs));await pg.close()}
await b.close();if(s)s.close()})();
