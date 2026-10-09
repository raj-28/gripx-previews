import json,re,os,sys
from PIL import Image
G="From customer reviews"; L_="From public listings"
S=lambda t,d,s=G:{"t":t,"d":d,"src":s}
T=lambda a,i,i2,g,d,n:{"accent":a,"ink":i,"ink2":i2,"glow":g,"accentDark":d,"note":n}
W="A customer wrote in a review: "
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).lower().strip()
CARD_GEO=tuple(float(x) for x in open('/tmp/cardgeo.txt').read().strip().split(','))
SP=[
dict(slug="dtails-pet-salon",name="D'tails Pet Salon",short="D'tails Pet Salon",kind="pet",mk="paw",hero="19145879",pos="67% 45%",geo=(41.079587,-85.130143),
 address="626 E Wayne St, Fort Wayne, IN 46802",phone="(260) 715-3647",tel="+12607153647",rating={"value":"5.0","count":"31"},
 theme=T("#e0a05a","#16110d","#221a14","#4a3322","#b0703a","warm copper-brown from the spaniel hero photo"),
 headline="Dog grooming in<br><em>Fort Wayne,</em> friendly and careful.",
 lead="D'tails Pet Salon at 626 E Wayne St, Fort Wayne. Customers say friendly groomers and dogs that come home looking and smelling great, some for over ten years.",
 quotes=["Every-time I get them they look and smell amazing.","They do an excellent job with my anxious senior dog! Highly recommend!","They did a fantastic job on my little man! Very friendly, great communication.","From puppy to senior she has always been well taken care of and comes out smelling and looking wonderful."],
 services=[S("Dog grooming","Listed as a pet grooming service.",L_),S("Full grooming","A customer mentions bringing her poodle for a full grooming."),S("Care for anxious and senior dogs","A customer says her anxious senior dog is well looked after."),S("Photos of first baths","A customer says photos of her puppies' first baths were sent on request.")],
 qa=[("Do you groom anxious dogs?",W+"“They do an excellent job with my anxious senior dog!”"),("Is communication good?",W+"“Very friendly, great communication.”"),("What are your hours?","Hours are not confirmed, so please call the salon before you go.")],
 src=["https://exa.ai/library/place/gzcpgyv5hpn"],pk="rev",
 revs=None),
dict(slug="cardinal-tattoo-piercing",name="Cardinal Tattoo & Piercing",short="Cardinal Tattoo",kind="beauty",mk="sparkle",hero="18097867",pos="50% 30%",geo=CARD_GEO,
 address="1509 Spy Run Ave, Fort Wayne, IN 46805",phone="(260) 426-1509",tel="+12604261509",rating=None,
 theme=T("#e24a4a","#100c0c","#1a1414","#3a1f1f","#b02f2f","cardinal red chosen from the shop name against the dark studio photo"),
 headline="Tattoo and piercing in<br><em>Fort Wayne,</em> since 2006.".replace(" since 2006",""),
 lead="Cardinal Tattoo & Piercing at 1509 Spy Run Ave, Fort Wayne. Customers say a professional, kind staff and a very clean shop.",
 quotes=["Have gone back multiple times, always fantastic work!","The staff was professional and kind and my tattoo turned out just as I asked.","I felt very comfortable and the shop is immaculate and decorated really cool."],
 services=[S("Tattoos","Listed under tattoos in public directories.",L_),S("Body piercing","Listed under body piercing in public directories.",L_)],
 qa=[("Do you do piercings?","Public directories list both tattoos and body piercing. Please call to confirm what is offered."),("Is the shop clean?",W+"“the shop is immaculate and decorated really cool.”"),("Will I feel comfortable?",W+"“I felt very comfortable”")],
 src=["https://www.yellowpages.com/fort-wayne-in/mip/cardinal-tattoo-piercing-25499986","https://nextdoor.com/pages/cardinal-tattoo-piercing-fort-wayne-in/"]),
dict(slug="avocado-shag-shop",name="Avocado Shag Shop",short="Avocado Shag Shop",kind="beauty",mk="sparkle",hero="31858722",pos="50% 40%",geo=(41.04087,-85.16883),noCall=True,
 address="4540 Bluffton Rd, Fort Wayne, IN 46809",phone="",tel="",rating={"value":"5.0","count":"20"},
 theme=T("#8bc34a","#0f1410","#17201a","#2e4a30","#5f8f2a","avocado green to match the shop name, with the colorful racks in the hero photo"),
 headline="Vintage clothing in<br><em>Fort Wayne,</em> curated finds.",
 lead="Avocado Shag Shop at 4540 Bluffton Rd, Fort Wayne. Customers say hand-picked vintage in great condition and a shop with its own style.",
 quotes=["Highly recommend checking out avocado shag shop for your vintage needs.","Wonderful business with exceptional style and a class all of their own.","everything has always been quality, and as expected for vintage clothes.","Her collections are ALWAYS authentically vintage and in MAGNIFICENT condition!"],
 services=[S("Vintage clothing","Listed as a clothing store; customers call it a vintage second hand retailer."),S("Vintage bags and shoes","Customers mention vintage bags, clothing and shoes."),S("Pop-ups and events","A customer says the shop is always doing pop ups and events.")],
 qa=[("What do you sell?",W+"“this is a vintage second hand retailer”"),("Is the quality good?",W+"“everything has always been quality, and as expected for vintage clothes.”"),("What are your hours?","Hours are not confirmed yet, so please check before you go.")],
 src=["https://exa.ai/library/place/d90jlz4tn6j","https://www.instagram.com/avocadoshagshop"]),
]
revtext={"dtails-pet-salon":"/tmp/f_dt.txt","cardinal-tattoo-piercing":"/tmp/f_cd.txt","avocado-shag-shop":"/tmp/f_av.txt"}
for s in SP:
    allrev=norm(open(revtext[s['slug']]).read())
    bad=[q for q in s['quotes'] if norm(q).rstrip('.!') not in allrev]
    for q,a in s['qa']:
        for m in re.findall(r'“([^”]+)”',a):
            m=m.strip('.,!')
            if norm(m).rstrip('.!') not in allrev: bad.append('QA:'+m)
    if bad: print('CHECK',s['slug'],bad)
    L=dict(slug=s['slug'],kind=s['kind'],name=s['name'],short=s['short'],initial=s['name'][0],address=s['address'],
      phone=s['phone'] or 'the shop',phoneTel=s['tel'],lat=s['geo'][0],lon=s['geo'][1],rating=s['rating'],reviewStars=5,
      headline=s['headline'],leadText=s['lead'],reviews=s['quotes'],theme=s['theme'],mascot=s['short']+' Assistant',mascotKind=s['mk'],sampleCount=2,
      services=s['services'],qa=[{'q':q,'a':a} for q,a in s['qa']],
      photoSources=s['src']+["Hero image: Pexels stock photo (free to use), illustrative only, not the business's own"],
      images={'hero':{'file':'hero.jpg'}},heroStock=True,heroPos=s['pos'])
    if s.get('noCall'): L['noCall']=True
    json.dump(L,open(f"leads/{s['slug']}.json",'w'),indent=1,ensure_ascii=False)
    d=f"assets/{s['slug']}"; os.makedirs(d,exist_ok=True)
    im=Image.open(f"/tmp/px4/p{s['hero']}.jpg").convert('RGB'); im.thumbnail((1400,1400)); im.save(d+'/hero.jpg',quality=78)
print('done')
