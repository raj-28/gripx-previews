import json,sys,re,os
from PIL import Image
sys.path.insert(0,'gen'); from specs2 import SPECS
src={x['name']:x for x in json.load(open('/downloads/builder-packet-d1097ab4.json'))}
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"').replace('‘',"'")).lower().strip()
for s in SPECS:
    r=src[s['pk']]; allrev=' || '.join(norm(x['text']) for x in r['reviews'])
    bad=[q for q in s['quotes'] if norm(q).rstrip('.!') not in allrev]
    for q,a in s['qa']:
        for m in re.findall(r'“([^”]+)”',a):
            m=m.strip('.,!');
            if norm(m).rstrip('.!') not in allrev: bad.append('QA:'+m)
    if bad: print('CHECK',s['slug'],bad)
    ph=re.sub(r'\D','',r['phone'] or '')
    if len(ph)==11: ph=ph[1:]
    if len(ph)!=10: ph=''
    tel='+1'+ph if ph else ''
    disp='(%s) %s-%s'%(ph[:3],ph[3:6],ph[6:]) if ph else 'the shop'
    noCall=bool(s.get('noCall')) or not ph
    addr=re.sub(r', United States$','',r['address']); addr=re.sub(r'-\d{4}(,|$)',r'\1',addr)
    L=dict(slug=s['slug'],kind=s['kind'],name=s['name'],short=s['short'],initial=s['name'][0],address=addr,
      phone='the shop' if noCall else disp,phoneTel='' if noCall else tel,lat=s['geo'][0],lon=s['geo'][1],rating=None,reviewStars=5,
      headline=s['headline'],leadText=s['lead'],reviews=s['quotes'],theme=s['theme'],mascot=s['short']+' Assistant',mascotKind=s['mk'],sampleCount=2,
      services=s['services'],qa=[{'q':q,'a':a} for q,a in s['qa']],
      photoSources=[x for x in [r['url'],r.get('corroboration_url'),'Hero image: Pexels stock photo (free to use), illustrative only, not the business\'s own'] if x],
      images={'hero':{'file':'hero.jpg'}},heroStock=True,heroPos=s['pos'])
    if s.get('hours'): L['hours']=s['hours']; L['hoursNote']=s['hoursNote']
    if noCall: L['noCall']=True
    json.dump(L,open(f"leads/{s['slug']}.json",'w'),indent=1,ensure_ascii=False)
    d=f"assets/{s['slug']}"; os.makedirs(d,exist_ok=True)
    im=Image.open(f"/tmp/px4/p{s['hero']}.jpg").convert('RGB'); im.thumbnail((1400,1400)); im.save(d+'/hero.jpg',quality=78)
print('done')
