import json,re,os
from PIL import Image
G="From customer reviews"; L_="From public listings"
S=lambda t,d,s=G:{"t":t,"d":d,"src":s}
T=lambda a,i,i2,g,d,n:{"accent":a,"ink":i,"ink2":i2,"glow":g,"accentDark":d,"note":n}
W="A customer wrote in a review: "
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).lower().strip()
SP=[
dict(slug="moores-body-shop",name="Moore's Body Shop",short="Moore's Body Shop",kind="auto",mk="car",hero="6870310",pos="50% 22%",geo=(38.0115785,-87.59938919999999),
 address="3539 N St Joseph Ave, Evansville, IN 47720",phone="(812) 425-8659",tel="+18124258659",rating={"value":"4.8","count":"40"},
 theme=T("#ff6b35","#0f1115","#171b22","#2a3d57","#c94a1a","orange on the dark blue-grey body shop photo"),
 headline="Auto body repair in<br><em>Evansville,</em> Indiana.",
 lead="Moore's Body Shop at 3539 N St Joseph Ave, Evansville. Customers say careful repairs, clear updates and help with insurance.",
 quotes=["Super nice and knowledgeable. They did an amazing job on my car and left it clean!","The work was easily scheduled and completed on time, and the price I paid was outstanding!","The staff was extremely friendly and helpful they kept me updated on repairs","He gave me updates along the way with progress photos."],
 services=[S("Body and collision repair","Customers describe door, tail light and storm and deer damage repairs.",G),S("Free estimates","Listed by Carwise.","From Carwise listing"),S("Insurance assistance","Listed by Carwise; a customer says they helped navigate insurance.","From Carwise listing and reviews"),S("Paintless dent repair","Listed by Carwise.","From Carwise listing")],
 hours="Mon-Fri 8-5",hoursNote="Closed Saturday and Sunday. Hours from the shop's Facebook and Carwise, call to confirm.",
 qa=[("Do you help with insurance?",W+"“helped us navigate insurance, repairs, post-insurance nonsense and more.”"),("Will I get updates?",W+"“He gave me updates along the way with progress photos.”"),("Do you take cards?",W+"“they don't accept debit or credit cards.” That review is from 2018, so please call to check."),("What are your hours?","Monday to Friday 8 AM to 5 PM, closed weekends, per the shop's Facebook and Carwise. Please call to confirm.")],
 src=["https://exa.ai/library/place/kcvh2zxw4k4","https://www.carwise.com (free estimates, insurance assistance, paintless dent repair)"],rev="/tmp/f_mo.txt",
 enq=("Tell the shop about your vehicle and damage.","Vehicle (year, make, model) and what happened","This is a request form only. It does not give an estimate or book a repair.")),
dict(slug="arts-alignment-auto-repair",name="Arts Alignment & Auto Repair",short="Arts Alignment",kind="auto",mk="car",hero="8986101",pos="68% 55%",geo=(38.0079779,-87.5922465),
 address="2001 Allens Ln, Evansville, IN 47720",phone="(812) 424-6955",tel="+18124246955",rating={"value":"4.9","count":"29"},
 theme=T("#4fc3f7","#0b1118","#121b26","#1f3a5c","#2a8fc0","blue from the mechanic's coveralls in the hero photo"),
 headline="Alignment and auto repair in<br><em>Evansville,</em> Indiana.",
 lead="Arts Alignment & Auto Repair at 2001 Allens Ln, Evansville. Customers say honest pricing, clear explanations and alignments that fix the drive.",
 quotes=["Great job installing a ball joint and doing an alignment on my 83 mustang. It drives great!","He broke down each cost so you understood what you were paying for.","Jeff, was so honest, totally reasonable on prices. Plus he does great work.".replace("Jeff, was","He was").replace("Jeff, ","")[:0] or "I feel so much safer in my car now with new brakes!!","We just had an alignment done on our 1992 Chevy GMT-400 and it drives like a dream now."],
 services=[S("Wheel alignment","Customers describe alignments on classic and daily cars.",G),S("Suspension and ball joints","A customer had a ball joint installed.",G),S("Complete auto repair","From the shop's own introduction.","From the shop's own page"),S("Brakes, tires and maintenance","From the shop's own introduction; a customer mentions new brakes.","From the shop's own page and reviews"),S("A/C charge and check-engine diagnosis","From the shop's own introduction.","From the shop's own page")],
 hours="Mon-Fri 8-4",hoursNote="Closed Saturday and Sunday. Hours from the shop's own page and listings, call to confirm.",
 qa=[("Do you do alignments?",W+"“doing an alignment on my 83 mustang. It drives great!”"),("Is pricing clear?",W+"“He broke down each cost so you understood what you were paying for.”"),("Do you do brakes?",W+"“I feel so much safer in my car now with new brakes!!”"),("What are your hours?","Monday to Friday 8 AM to 4 PM, closed weekends. Please call to confirm.")],
 src=["https://exa.ai/library/place/xk11xf3z9dt"],rev="/tmp/f_ar.txt",
 enq=("Tell the shop what your vehicle needs.","Vehicle (year, make, model) and the service you need","This is a request form only. It does not give a diagnosis or book an appointment.")),
]
for s in SP:
    allrev=norm(open(s['rev']).read())
    bad=[q for q in s['quotes'] if norm(q).rstrip('.!') not in allrev]
    for q,a in s['qa']:
        for m in re.findall(r'“([^”]+)”',a):
            m=m.strip('.,!')
            if norm(m).rstrip('.!') not in allrev: bad.append('QA:'+m)
    if bad: print('CHECK',s['slug'],bad)
    L=dict(slug=s['slug'],kind=s['kind'],name=s['name'],short=s['short'],initial=s['name'][0],address=s['address'],phone=s['phone'],phoneTel=s['tel'],lat=s['geo'][0],lon=s['geo'][1],rating=s['rating'],reviewStars=5,
      headline=s['headline'],leadText=s['lead'],reviews=s['quotes'],theme=s['theme'],mascot=s['short']+' Assistant',mascotKind=s['mk'],sampleCount=2,hours=s['hours'],hoursNote=s['hoursNote'],
      services=s['services'],qa=[{'q':q,'a':a} for q,a in s['qa']],
      photoSources=s['src']+["Hero image: Pexels stock photo (free to use), illustrative only, not the business's own"],
      images={'hero':{'file':'hero.jpg'}},heroStock=True,heroPos=s['pos'],enquiryTitle=s['enq'][0],enquiryLabel=s['enq'][1],enquiryNote=s['enq'][2])
    json.dump(L,open(f"leads/{s['slug']}.json",'w'),indent=1,ensure_ascii=False)
    d=f"assets/{s['slug']}"; os.makedirs(d,exist_ok=True)
    im=Image.open(f"/tmp/px4/p{s['hero']}.jpg").convert('RGB'); im.thumbnail((1400,1400)); im.save(d+'/hero.jpg',quality=78)
print('done')
