import json,sys,re,os
from PIL import Image
sys.path.insert(0,'gen'); from specs import SPECS
src={x['id']:x for x in json.load(open('/downloads/next15-a91ca2f5.json'))}
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"').replace('‘',"'")).lower().strip()
for s in SPECS:
    r=src[s['id']]; allrev=' || '.join(norm(x['text']) for x in r['reviews'])
    bad=[q for q in s['quotes'] if norm(q) not in allrev]
    # qa inline quotes
    for q,a in s['qa']:
        for m in re.findall(r'“([^”]+)”',a):
            m=m.strip('.,!');
            if norm(m).rstrip('.!') not in allrev: bad.append('QA:'+m)
    if bad: print('CHECK',s['slug'],bad)
    ph=re.sub(r'\D','',r['phone'] or '')
    if len(ph)==11: ph=ph[1:]
    tel='+1'+ph if ph else ''
    disp='(%s) %s-%s'%(ph[:3],ph[3:6],ph[6:]) if ph else 'the shop'
    noCall=bool(s.get('noCall')) or not ph
    L=dict(slug=s['slug'],kind=s['kind'],name=s['name'],short=s['short'],initial=s['name'][0],address=r['address'].replace('IN47711','IN 47711'),
      phone='the shop' if noCall else disp,phoneTel='' if noCall else tel,lat=s['geo'][0],lon=s['geo'][1],rating=None,reviewStars=5,
      headline=s['headline'],leadText=s['lead'],reviews=s['quotes'],theme=s['theme'],mascot=s['short']+' Assistant',mascotKind=s['mk'],sampleCount=2,
      services=s['services'],qa=[{'q':q,'a':a} for q,a in s['qa']],
      photoSources=[r['url'],'Hero image: Pexels stock photo (free to use), illustrative only, not the business\'s own'],
      images={'hero':{'file':'hero.jpg'}},heroStock=True,heroPos=s['pos'])
    if noCall: L['noCall']=True
    if r['address'].startswith('600 N Weinbach'): L['address']='600 N Weinbach Ave Suite 520, Evansville, IN 47711'
    json.dump(L,open(f"leads/{s['slug']}.json",'w'),indent=1,ensure_ascii=False)
    d=f"assets/{s['slug']}"; os.makedirs(d,exist_ok=True)
    im=Image.open(f"/tmp/px2/p{s['hero']}.jpg").convert('RGB'); im.thumbnail((1400,1400)); im.save(d+'/hero.jpg',quality=78)
print('done')
