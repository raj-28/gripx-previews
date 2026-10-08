(function(){
var S=window.SHOP;
var log=document.getElementById('log'),form=document.getElementById('form'),msg=document.getElementById('msg'),chips=document.getElementById('chips'),chat=document.getElementById('chat');
function add(cls,text){var d=document.createElement('div');d.className='m '+cls;d.textContent=text;log.appendChild(d);log.scrollTop=log.scrollHeight;return d}
function typing(){var d=document.createElement('div');d.className='m bot typing';d.innerHTML='<i></i><i></i><i></i>';log.appendChild(d);log.scrollTop=log.scrollHeight;return d}
var fallback="I don't have that one. For anything else, call the shop at "+S.phone+".";
var rules=[
 [/where|address|locat|direction|find you|street/i,"We're at "+S.address+"."],
 [/phone|call|number|contact|reach/i,"You can call the shop at "+S.phone+"."],
 [/service|do you|fix|repair|work on|offer/i,"The shop does auto repair. For what a specific job involves, call "+S.phone+"."],
 [/review|customer|good|say|trust|rating/i,"Customers say: \u201C"+S.reviews[0]+"\u201D and \u201C"+S.reviews[1]+"\u201D (Google reviews)."],
 [/hour|open|close|when|today|sunday|saturday/i,"I don't have confirmed hours. Please call "+S.phone+" to check."],
 [/price|cost|how much|quote|estimate|cheap/i,"I can't give prices here. Call "+S.phone+" for a quote."]
];
add('bot',"Hi, I'm the "+S.short+" chat assistant. This is a demo made by GripX, so I only know the shop's public details. Ask me where we are, what we do, or what customers say.");
var Q=['Where are you?','What do you do?','What do customers say?','Can I call you?'];
Q.forEach(function(q){var b=document.createElement('button');b.type='button';b.textContent=q;b.onclick=function(){send(q)};chips.appendChild(b)});
document.getElementById('min').onclick=function(){chat.classList.add('min');document.body.classList.add('chat-min')};
document.getElementById('open').onclick=function(){chat.classList.remove('min');document.body.classList.remove('chat-min');msg.focus()};
form.addEventListener('submit',function(e){e.preventDefault();var v=msg.value.trim();if(v)send(v)});
function send(text){msg.value='';chips.style.display='none';add('me',text);var t=typing();
 var rep=fallback;for(var i=0;i<rules.length;i++){if(rules[i][0].test(text)){rep=rules[i][1];break}}
 setTimeout(function(){t.remove();add('bot',rep)},650)}
})();
