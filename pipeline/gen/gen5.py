import json,re,os
from PIL import Image
G="From customer reviews"; L_="From public listings"
S=lambda t,d,s=G:{"t":t,"d":d,"src":s}
T=lambda a,i,i2,g,d,n:{"accent":a,"ink":i,"ink2":i2,"glow":g,"accentDark":d,"note":n}
W="A customer wrote in a review: "
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"')).lower().strip()
SP=[
dict(slug="miller-time-mechanics",name="Miller-Time Mechanics",short="Miller-Time Mechanics",kind="auto",mk="car",hero="32208774",pos="50% 28%",geo=(38.674265,-87.516483),
 address="806 N 14th St, Vincennes, IN 47591",phone="(812) 890-7676",tel="+18128907676",rating=None,
 theme=T("#f2b134","#0f1114","#171b20","#24415c","#b9810f","amber against the blue shop photo"),
 headline="Automotive repairs in<br><em>Vincennes,</em> Indiana.",
 lead="Miller-Time Mechanics at 806 N 14th St, Vincennes. A local shop doing automotive repairs, with recent work posted on its Facebook page.",
 quotes=["good"],
 services=[S("Automotive repairs","Listed as an automotive repair shop and described that way on the shop's Facebook page.","From the shop's Facebook page and listing")],
 hours="Mon-Fri 9-5",hoursNote="Closed Saturday and Sunday. Hours from the shop's Facebook and listings, call to confirm.",
 qa=[("What do you work on?","The shop's page describes automotive repairs. Call to ask about your vehicle and problem."),("What are your hours?","Monday to Friday 9 AM to 5 PM, closed weekends, per the shop's Facebook and listings. Please call to confirm."),("What does it cost?","No prices are published, so please call or send a request and the shop can tell you.")],
 src=["https://www.facebook.com/MillerTimeMechanicsLLC/","https://exa.ai/library/place/b0vy3tvhhkx"],rev="/tmp/f_mt.txt",
 enq=("Tell the shop about your vehicle and the problem.","Vehicle (year, make, model) and what is wrong","This is a request form only. It does not give a quote or book an appointment.")),
dict(slug="dyer-and-sons-automotive",name="Dyer & Sons Automotive",short="Dyer & Sons",kind="auto",mk="car",hero="8985601",pos="72% 62%",geo=(41.12328,-85.142458),
 address="4914 Speedway Dr, Fort Wayne, IN 46825",phone="(260) 471-3937",tel="+12604713937",rating={"value":"5.0","count":"142"},
 theme=T("#e8504a","#0f1012","#181a1d","#3a2a28","#b5342f","red on the dark underbody photo"),
 headline="Auto repair in<br><em>Fort Wayne,</em> from maintenance to engine work.",
 lead="Dyer & Sons Automotive at 4914 Speedway Dr, Fort Wayne. Customers call it an honest, family-owned shop with fair prices.",
 quotes=["Hands down the best mechanic I've ever had work on any of my vehicles.","The prices are fair and honest. The work is exceptional.","This is a super honest, family-owned shop.","did a complete inspection on my truck and listed everything in order of importance."],
 services=[S("Basic maintenance to major engine repair","From the shop's own Facebook post.","From the shop's Facebook page"),S("Vehicle inspections","A customer describes a complete inspection listed in order of importance."),S("Diagnosis","A customer says their car was diagnosed and explained quickly."),S("Brake checks","A customer says the shop checked their brake pads and told them what was needed.")],
 hours="Mon-Fri 8-5",hoursNote="Closed Saturday and Sunday. Hours from the shop's Facebook and listings, call to confirm.",
 qa=[("Are the prices fair?",W+"“The prices are fair and honest.”"),("Do you do inspections?",W+"“did a complete inspection on my truck and listed everything in order of importance.”"),("Is it family owned?",W+"“This is a super honest, family-owned shop.”"),("What are your hours?","Monday to Friday 8 AM to 5 PM, closed weekends. Please call to confirm.")],
 src=["https://www.facebook.com/people/Dyer-Sons-Automotive-Inc/100063686330734/","https://exa.ai/library/place/38lc2shzf8y"],rev="/tmp/f_dy.txt",
 enq=("Tell the shop about your vehicle and the problem.","Vehicle (year, make, model) and what you need","This is a request form only. It does not give a quote or book an appointment.")),
dict(slug="lines-and-layers-barber",name="Lines and Layers Barber and Beauty Salon",short="Lines and Layers",kind="barber",mk="scissors",hero="4625627",pos="50% 38%",geo=(41.06692,-85.13326),
 address="2033 Lafayette St, Fort Wayne, IN 46803",phone="(260) 399-0427",tel="+12603990427",rating={"value":"4.9","count":"8"},
 theme=T("#e0b04a","#101010","#1a1918","#3a3022","#a8801f","warm gold on the dark barber photo"),
 headline="Barber shop in<br><em>Fort Wayne,</em> haircuts and beard trims.",
 lead="Lines and Layers Barber and Beauty Salon at 2033 Lafayette St, Fort Wayne. Customers say great haircuts and beard trims. The entrance is on the Buchanan side.",
 quotes=["When I do get my haircut this is the only barber I'm going to!! Best of the best hands down!!","One of the best barbers in the city!!","a touch up or a full haircut and beard trim"],
 services=[S("Haircuts","Customers praise the haircuts.",G),S("Beard trims","A customer mentions a full haircut and beard trim.",G),S("Touch-ups","A customer mentions getting a touch up.",G)],
 hours="Posted: Tue-Fri 10-5, Sat 9-5",hoursNote="Posted hours, about 5 years old and Monday listings differ. Call to confirm.",
 qa=[("Where is the entrance?","The shop's Facebook page says the entrance is on the Buchanan side."),("Do you do beard trims?",W+"“a touch up or a full haircut and beard trim”"),("What are your hours?","The shop's posted hours were Tuesday to Friday 10 AM to 5 PM and Saturday 9 AM to 5 PM, closed Sunday, but they are about 5 years old. Please call to confirm.")],
 src=["https://www.facebook.com/LinesandLayersBarberandBeautySalon/","https://exa.ai/library/place/lwm89zrptqq"],rev="/tmp/f_ll.txt",
 enq=("Ask the shop about a haircut or beard trim.","What you would like (haircut, beard trim) and when","This is a request form only. It does not book an appointment.")),
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
