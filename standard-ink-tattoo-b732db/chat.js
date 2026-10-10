(function(){
var S=window.SHOP;
var log=document.getElementById('log'),form=document.getElementById('form'),msg=document.getElementById('msg'),chips=document.getElementById('chips');
function add(cls,text){var d=document.createElement('div');d.className='m '+cls;d.textContent=text;log.appendChild(d);log.scrollTop=log.scrollHeight;return d}
function typing(){var d=document.createElement('div');d.className='m bot typing';d.innerHTML='<i></i><i></i><i></i>';log.appendChild(d);log.scrollTop=log.scrollHeight;return d}
var fallback="I don't have that one. For anything else, call the shop at "+S.phone+".";
var rules=[
 [/where|address|locat|direction|find you|street/i,"We're at "+S.address+"."],
 [/phone|call|number|contact|reach/i,"You can call the shop at "+S.phone+"."],
 [/hour|open|close|when|today|sunday|saturday/i,"I don't have confirmed hours. Please call "+S.phone+" to check."],
 [/price|cost|how much|quote|estimate|cheap|afford/i,"I don't have prices and can't give a quote here. For a quote, call "+S.phone+"."],
 [/review|customer|good|say|trust|service|friendly/i,"Customers say: \u201C"+S.reviews[0]+"\u201D and \u201C"+S.reviews[1]+"\u201D (online reviews)."],
 [/subaru|honda|toyota|ford|chevy|make|model/i,S.kind==="auto"?"I can't confirm every make from here. Call "+S.phone+" with your car's make and model.":null],
 [S.kind==="auto"?/ac|a\/c|coolant|leak|spark|brake|engine|noise|repair|fix|diagnos|wrong/i:/service|offer|do you do|menu|what do/i,S.kind==="auto"?"The shop does auto repair. Call "+S.phone+" and describe what your car is doing.":(S.servicesLine||"Call "+S.phone+" to ask about services.")]
];
function reply(q){for(var i=0;i<rules.length;i++){if(rules[i][1]&&rules[i][0].test(q))return rules[i][1]}return fallback}
add('bot',"Hi, I'm the "+S.short+" assistant. This is a demo chatbot made by GripX. Here are two questions customers might ask:");
for(var i=0;i<(S.sampleCount||0);i++){add('me',S.qa[i].q);add('bot',S.qa[i].a)}
log.scrollTop=0;
S.qa.slice(S.sampleCount||0).forEach(function(x){var b=document.createElement('button');b.type='button';b.textContent=x.q;b.onclick=function(){b.remove();send(x.q,x.a)};chips.appendChild(b)});
form.addEventListener('submit',function(e){e.preventDefault();var v=msg.value.trim();if(v)send(v)});
function send(text,ans){msg.value='';add('me',text);var t=typing();var rep=ans||reply(text);
 setTimeout(function(){t.remove();add('bot',rep)},650)}
})();
