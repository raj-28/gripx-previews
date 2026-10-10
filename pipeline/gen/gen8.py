import json, re

rows = json.load(open('/tmp/rows19_33.json'))
briefs = {}
for r in rows:
    briefs[r[0]] = ' '.join(str(c) for c in r if c)
def sq(s): return re.sub(r'\s+', '', s).lower()

T = {
 'rose':   {"accent":"#e08bb0","ink":"#121113","ink2":"#1c1a1d","glow":"#3a2d33","accentDark":"#b0658a","note":"rose on the grooming photo"},
 'teal':   {"accent":"#5ec8b7","ink":"#101312","ink2":"#181d1c","glow":"#27393a","accentDark":"#3fa191","note":"teal on the grooming photo"},
 'amber':  {"accent":"#e0a35b","ink":"#131110","ink2":"#1d1917","glow":"#3a2f24","accentDark":"#b07e42","note":"amber on the grooming photo"},
 'mint':   {"accent":"#7bd6a8","ink":"#101311","ink2":"#181d1a","glow":"#273a2f","accentDark":"#57b084","note":"mint on the grooming photo"},
 'sky':    {"accent":"#7fb8e6","ink":"#101213","ink2":"#181c1f","glow":"#27333f","accentDark":"#5d93c2","note":"sky on the grooming photo"},
 'violet': {"accent":"#a78bfa","ink":"#121114","ink2":"#1a181f","glow":"#2f2a3f","accentDark":"#8263d6","note":"violet on the studio photo"},
 'red':    {"accent":"#e05b5b","ink":"#131111","ink2":"#1d1818","glow":"#3a2424","accentDark":"#b04242","note":"ink red on the studio photo"},
 'plum':   {"accent":"#c77fdb","ink":"#131114","ink2":"#1d1820","glow":"#362a3f","accentDark":"#a257b8","note":"plum on the studio photo"},
 'blue':   {"accent":"#5ba8e0","ink":"#101313","ink2":"#181d24","glow":"#24303f","accentDark":"#4282b0","note":"blue on the work photo"},
 'green':  {"accent":"#7bbf5e","ink":"#111310","ink2":"#1a1d17","glow":"#2a3524","accentDark":"#5d9942","note":"green on the lawn photo"},
 'polish': {"accent":"#e0678a","ink":"#131112","ink2":"#1d181b","glow":"#3a2430","accentDark":"#b04267","note":"polish red on the manicure photo"},
 'orange': {"accent":"#e08a4f","ink":"#131110","ink2":"#1d1815","glow":"#3a2b20","accentDark":"#b06836","note":"burnt orange on the tire photo"},
 'steel':  {"accent":"#9fb3c8","ink":"#111314","ink2":"#191d20","glow":"#2a3238","accentDark":"#7b90a6","note":"steel on the painter photo"},
}

def base(code, slug, kind, name, short, initial, address, phone, email, headline, leadText, services, qa, hoursNote, theme, mascotKind, noMap=False, hours=None):
    b = briefs[code]
    checks = [re.sub(r'\D','',phone), sq(address.split(',')[0])]
    if email: checks.append(sq(email))
    for fact in checks:
        assert fact in sq(b), slug + ': fact not in brief: ' + fact
    L = {
        "slug": slug, "kind": kind, "name": name, "short": short, "initial": initial,
        "address": address, "phone": phone, "phoneTel": '+1' + re.sub(r'\D', '', phone),
        "lat": 0, "lon": 0,
        "headline": headline, "leadText": leadText,
        "reviews": [], "theme": T[theme], "mascot": short + " Assistant", "mascotKind": mascotKind,
        "sampleCount": 2, "services": services, "qa": qa,
        "enquiryTitle": "Ask " + short + " anything.",
        "enquiryLabel": "What do you need?",
        "enquiryNote": "Or reach the shop directly: call " + phone + ((" or email " + email) if email else "") + ".",
        "heroStock": True, "heroPos": "center 35%", "images": [], "photoSources": [],
        "hoursNote": hoursNote,
    }
    if hours: L["hours"] = hours
    if noMap: L["noMap"] = True
    return L

def svc(t, d, src): return {"t": t, "d": d, "src": src}
def q(q_, a): return {"q": q_, "a": a}

OWN = "From the shop's own page"
DIR = "From directory listings"

specs = [
base("GR-001","pawsitively-purrfect","pet","Pawsitively Purrfect Pet Grooming LLC","Pawsitively Purrfect","P",
 "1229 12th Avenue, Grafton, WI","(262) 685-8031",None,
 "Dog grooming in<br><em>Grafton,</em> eco-friendly.",
 "Pawsitively Purrfect Pet Grooming at 1229 12th Avenue, Grafton. A full-service groomer focused on eco-friendly grooming and animal comfort, per its own page and directory listings.",
 [svc("Full-service grooming","Full-service grooming for dogs, per the shop's own page.",OWN),
  svc("Eco-friendly products","The shop describes its grooming as eco-friendly, per its own page.",OWN),
  svc("Animal comfort first","A grooming approach built around animal comfort, per the shop's own page.",OWN)],
 [q("Where is the salon?","1229 12th Avenue, Grafton, WI."),
  q("Do they use eco-friendly products?","The shop describes its grooming as eco-friendly on its own page."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (262) 685-8031 to confirm.")],
 "Call to confirm today's hours.","rose","paw"),

base("WO-001","pampered-paws-woodruff","pet","Pampered Paws","Pampered Paws","P",
 "9198 Thrall Rd, Woodruff, WI","(715) 358-5588",None,
 "Grooming and pet<br><em>supplies</em> in Woodruff.",
 "Pampered Paws at 9198 Thrall Rd, Woodruff. Caring grooming plus cat and dog supplies, per its own page and a retailer profile.",
 [svc("Caring grooming","Grooming with a caring approach, per the shop's own page.",OWN),
  svc("Cat and dog supplies","Pet supplies for cats and dogs, per the shop's retailer profile.",DIR),
  svc("Cats and dogs","The shop works with both cats and dogs, per its own page.",OWN)],
 [q("Where is the shop?","9198 Thrall Rd, Woodruff, WI."),
  q("Do they sell pet supplies?","Yes - cat and dog supplies, per the shop's retailer profile."),
  q("What are your hours?","Directory listings say Mon-Fri 9-5:30, but call (715) 358-5588 to confirm before visiting.")],
 "Directory listings say Mon-Fri 9-5:30 - call to confirm.","amber","paw",False,"Mon-Fri 9-5:30"),

base("EC-001","midwest-tattoo","tattoo","Midwest Tattoo","Midwest Tattoo","M",
 "Eau Claire, WI","(715) 864-4377","midwestattoo@gmail.com",
 "Tattoos in<br><em>Eau Claire,</em> by appointment.",
 "Midwest Tattoo in Eau Claire. An appointment-only tattoo and piercing studio - call or text for availability, per its own page.",
 [svc("Tattoos","Custom tattoo work, by appointment only.",OWN),
  svc("Piercings","Piercing services, by appointment only.",OWN),
  svc("Private appointments","The studio works by appointment - call or text to set a time.",OWN)],
 [q("Where is the studio?","Eau Claire, WI. The studio is appointment-only - call or text (715) 864-4377 and they'll share details when you book."),
  q("Do you take walk-ins?","No - the studio is appointment only, per its own page. Call or text (715) 864-4377 for availability."),
  q("What are your hours?","Hours vary by artist. Call or text (715) 864-4377 for availability, or email midwestattoo@gmail.com.")],
 "Appointment only. Hours vary - call or text for availability.","violet","sparkle",True),

base("OP-001","pawsitively-perfect","pet","Pawsitively Perfect","Pawsitively Perfect","P",
 "7711 W 151st St, Overland Park, KS","(913) 345-8245",None,
 "Grooming and boarding<br>in <em>Overland Park.</em>",
 "Pawsitively Perfect at 7711 W 151st St, Overland Park. Dog and cat grooming and boarding with personalized service, per its own page.",
 [svc("Dog and cat grooming","Grooming for both dogs and cats, per the shop's own page.",OWN),
  svc("Boarding","Pet boarding, per the shop's own page.",OWN),
  svc("Personalized service","The shop emphasizes personalized service for each pet.",OWN)],
 [q("Where is the salon?","7711 W 151st St, Overland Park, KS."),
  q("Do they board pets?","Yes - boarding is one of the services on the shop's own page."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (913) 345-8245 to confirm.")],
 "Call to confirm today's hours.","teal","paw"),

base("MA-001","black-mammoth-tattoo","tattoo","Black Mammoth Tattoo","Black Mammoth","B",
 "2047 Fort Riley Ln, Manhattan, KS","(785) 320-7707",None,
 "Tattoos and piercings<br>in <em>Manhattan, KS.</em>",
 "Black Mammoth Tattoo at 2047 Fort Riley Ln, Manhattan. Tattoo and piercing shop; walk-in tattoos on Saturdays, per its own page.",
 [svc("Tattoos","Tattoo work, per the shop's own page.",OWN),
  svc("Piercings","Piercing services, per the shop's own page.",OWN),
  svc("Saturday walk-in tattoos","Walk-in tattoos on Saturdays only, per the shop's own page.",OWN)],
 [q("Where is the shop?","2047 Fort Riley Ln, Manhattan, KS."),
  q("Do you take walk-ins?","Walk-in tattoos on Saturdays only, per the shop's own page. Other times, call (785) 320-7707 to ask."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (785) 320-7707 to confirm.")],
 "Call to confirm today's hours.","red","sparkle"),

base("LE-001","artistic-soul-tattoos","tattoo","Artistic Soul Tattoos","Artistic Soul","A",
 "145 Thain Road Unit E, Lewiston, ID","(208) 743-9131",None,
 "Tattoos and piercings<br>in <em>Lewiston, ID.</em>",
 "Artistic Soul Tattoos at 145 Thain Road Unit E, Lewiston. A tattoo and piercing studio with a four-artist roster, per its own intro.",
 [svc("Tattoos","Tattoo work from a four-artist roster.",OWN),
  svc("Piercings","Piercing services, per the shop's own page.",OWN),
  svc("Resident artists","Bobby Heflin, Josh Corder, Justine Walters and Corry Swanson, per the shop's own intro.",OWN)],
 [q("Where is the studio?","145 Thain Road Unit E, Lewiston, ID."),
  q("Who are the artists?","The shop's own intro names Bobby Heflin, Josh Corder, Justine Walters and Corry Swanson."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (208) 743-9131 to confirm.")],
 "Call to confirm today's hours.","plum","sparkle"),

base("SM-001","barks-and-bubbles","pet","Barks & Bubbles Groom Shop","Barks & Bubbles","B",
 "402 N 10th St, Saint Maries, ID","(208) 245-5755",None,
 "Grooming and boarding<br>in <em>Saint Maries.</em>",
 "Barks & Bubbles Groom Shop at 402 N 10th St, Saint Maries. Pet grooming and boarding, per its own page.",
 [svc("Pet grooming","Grooming services, per the shop's own page.",OWN),
  svc("Pet boarding","Boarding services, per the shop's own page.",OWN)],
 [q("Where is the shop?","402 N 10th St, Saint Maries, ID."),
  q("Do they board pets?","Yes - boarding is one of the services on the shop's own page."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (208) 245-5755 to confirm.")],
 "Call to confirm today's hours.","mint","paw"),

base("AB-001","albuquerque-ink","tattoo","Albuquerque Ink Tattoo","Albuquerque Ink","A",
 "Albuquerque, NM","(505) 306-8623","albuquerqueink@gmail.com",
 "Tattoos and piercings<br>in <em>Albuquerque.</em>",
 "Albuquerque Ink Tattoo in Albuquerque, NM. A tattoo and piercing shop - walk-ins welcome and open every day, per its own intro.",
 [svc("Tattoos","Tattoo work, per the shop's own page.",OWN),
  svc("Piercings","Piercing services, per the shop's own page.",OWN),
  svc("Walk-ins welcome","The shop's own intro says walk-ins are welcome and it is open every day.",OWN)],
 [q("Where is the shop?","Albuquerque, NM. Call (505) 306-8623 or email albuquerqueink@gmail.com and they'll share the details."),
  q("Do you take walk-ins?","The shop's own intro says walk-ins are welcome and it is open every day. Call (505) 306-8623 to confirm before visiting."),
  q("What are your hours?","The shop says it is open every day, but exact hours aren't published - call (505) 306-8623 to confirm.")],
 "Walk-ins welcome, open every day, per the shop's own intro. Call to confirm.","violet","sparkle",True),

base("RU-001","four-paws-pet-spa","pet","Four Paws Pet Spa","Four Paws","F",
 "11591 Wards Rd, Rustburg, VA","(434) 616-2156","fourpawspetx3@aol.com",
 "Dog grooming in<br><em>Rustburg,</em> since 2017.",
 "Four Paws Pet Spa at 11591 Wards Rd, Rustburg. Professional dog grooming, established 2017, per its own page.",
 [svc("Professional dog grooming","Dog grooming from a dedicated spa, per the shop's own page.",OWN),
  svc("Established 2017","Serving the area since 2017, per the shop's own page.",OWN)],
 [q("Where is the spa?","11591 Wards Rd, Rustburg, VA."),
  q("Do they groom cats?","The shop describes itself as a professional dog grooming spa - call (434) 616-2156 to ask about other pets."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (434) 616-2156 to confirm.")],
 "Call to confirm today's hours.","sky","paw"),

base("KR-001","krug-and-sons-hvac","trade","Krug & Sons Mechanical & HVAC Services Inc","Krug & Sons","K",
 "4619 Valley View Dr, Knoxville, TN","(865) 850-1183","krugheatingandair@gmail.com",
 "Heating and air in<br><em>Knoxville,</em> family owned.",
 "Krug & Sons Mechanical & HVAC Services at 4619 Valley View Dr, Knoxville. A locally and family owned heating and air company, per its own page.",
 [svc("Heating","Heating service for local homes, per the shop's own page.",OWN),
  svc("Air conditioning","Air conditioning service, per the shop's own page.",OWN),
  svc("Locally and family owned","A locally and family owned company, per its own page.",OWN)],
 [q("Where are they based?","4619 Valley View Dr, Knoxville, TN."),
  q("Are they family owned?","Yes - the company describes itself as locally and family owned."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (865) 850-1183 to confirm.")],
 "Call to confirm today's hours.","blue","sparkle"),

base("GE-001","gr-electrical","trade","GR Electrical","GR Electrical","G",
 "McMinnville, TN","(931) 314-5031","GRElectricalTN@gmail.com",
 "Electrical work in<br><em>McMinnville, TN.</em>",
 "GR Electrical in McMinnville, TN. General electrical service - call or email to talk through your job, per its own page.",
 [svc("Electrical service","General electrical work, per the shop's own page.",OWN),
  svc("Local electrician","Based in McMinnville, TN, per the shop's own page.",OWN)],
 [q("Where are they based?","McMinnville, TN. Call (931) 314-5031 or email GRElectricalTN@gmail.com to arrange a visit."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (931) 314-5031 to confirm.")],
 "Call to confirm today's hours.","blue","sparkle",True),

base("GM-001","green-meadows-landscaping","trade","Green Meadows Lawn & Landscaping","Green Meadows","G",
 "Pittsburg, KS","(417) 214-4831","meadowslawncare@hotmail.com",
 "Landscaping across<br><em>Southeast Kansas</em> and beyond.",
 "Green Meadows Lawn & Landscaping, based in Pittsburg, KS. A full-service landscaping company serving Southeast Kansas, Southwest Missouri and Northwest Arkansas, per its own page.",
 [svc("Full-service landscaping","A full-service landscaping company, per its own page.",OWN),
  svc("Regional service area","Serves Southeast Kansas, Southwest Missouri and Northwest Arkansas, per its own page.",OWN)],
 [q("Where do they work?","Based in Pittsburg, KS, serving Southeast Kansas, Southwest Missouri and Northwest Arkansas, per the shop's own page."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (417) 214-4831 to confirm.")],
 "Call to confirm today's hours.","green","sparkle",True),

base("RI-001","tire-and-wheel-pro","auto","Tire & Wheel Pro Services LLC","Tire & Wheel Pro","T",
 "12380 San Pablo Ave, Richmond, CA","(510) 234-7007",None,
 "Tires, wheels and<br><em>alignment</em> in Richmond.",
 "Tire & Wheel Pro Services at 12380 San Pablo Ave, Richmond. All brands of tires, custom wheels and wheel alignment, open 7 days a week, per its own page.",
 [svc("All brands of tires","Tires from all brands, per the shop's own page.",OWN),
  svc("Custom wheels","Custom wheels, per the shop's own page.",OWN),
  svc("Wheel alignment","Wheel alignment, per the shop's own page.",OWN)],
 [q("Where is the shop?","12380 San Pablo Ave, Richmond, CA."),
  q("Are they open weekends?","The shop's own page says it is open 7 days a week - call (510) 234-7007 for exact hours."),
  q("What are your hours?","Open 7 days a week per the shop's own page; exact hours aren't published - call (510) 234-7007.")],
 "Open 7 days a week, per the shop's own page. Call for exact hours.","orange","tire"),

base("CV-001","modern-nails-corvallis","salon","Modern Nails","Modern Nails","M",
 "1330 NW 9th St, Corvallis, OR","(541) 757-1098","abbyngo2001@yahoo.com",
 "Nails in<br><em>Corvallis,</em> manicure and pedicure.",
 "Modern Nails at 1330 NW 9th St, Corvallis. A nail salon for manicures and pedicures, per its own page.",
 [svc("Manicures","Manicure services, per the shop's own page.",OWN),
  svc("Pedicures","Pedicure services, per the shop's own page.",OWN)],
 [q("Where is the salon?","1330 NW 9th St, Corvallis, OR."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (541) 757-1098 to confirm.")],
 "Call to confirm today's hours.","polish","scissors"),

base("AP-001","alabama-paint-company","trade","Alabama Paint Company","Alabama Paint","A",
 "Mobile, AL","(251) 366-2999","Alabamapaintco@yahoo.com",
 "House painting in<br><em>Mobile, AL.</em>",
 "Alabama Paint Company in Mobile, AL. A house painting company - call or email for a quote, per its own page.",
 [svc("House painting","House painting services, per the shop's own page.",OWN),
  svc("Local painters","Based in Mobile, AL, per the shop's own page.",OWN)],
 [q("Where are they based?","Mobile, AL. Call (251) 366-2999 or email Alabamapaintco@yahoo.com to arrange a quote."),
  q("What are your hours?","Hours aren't published in the listings we checked - please call (251) 366-2999 to confirm.")],
 "Call to confirm today's hours.","steel","sparkle",True),
]

for L in specs:
    json.dump(L, open('leads/' + L['slug'] + '.json', 'w'), indent=1, ensure_ascii=False)
    print('wrote', L['slug'])
print('ALL SPECS VERIFIED')
