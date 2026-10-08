const p=require('puppeteer-core');const wait=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{const b=await p.launch({executablePath:'/usr/bin/google-chrome',headless:true,args:['--no-sandbox']});const e=[];
for(const [k,vp] of [['d',{width:1280,height:800}],['m',{width:390,height:844,isMobile:true,hasTouch:true}]]){const pg=await b.newPage();pg.on('pageerror',x=>e.push(x.message));pg.on('requestfailed',r=>e.push('FAIL '+r.url()));
await pg.setViewport(vp);await pg.goto(process.argv[2],{waitUntil:'networkidle2'});await wait(500);await pg.screenshot({path:`/tmp/lv-${k}-top.png`});
if(k==='m'){await pg.evaluate(()=>document.getElementById('chat').scrollIntoView());await wait(300);await pg.screenshot({path:`/tmp/lv-m-chat.png`})}
else{await pg.type('#msg','how much is a brake job');await pg.keyboard.press('Enter');await wait(1200);await pg.screenshot({path:`/tmp/lv-d-typed.png`})}
await pg.screenshot({path:`/tmp/lv-${k}-full.png`,fullPage:true})}
console.log(e);await b.close()})();
