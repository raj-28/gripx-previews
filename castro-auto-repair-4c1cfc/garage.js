import * as THREE from 'three';
import { GLTFLoader } from 'https://gripx.tech/town/vendor/GLTFLoader.js';
import { clone } from 'https://gripx.tech/town/vendor/SkeletonUtils.js';
const cv=document.getElementById('gl');
const renderer=new THREE.WebGLRenderer({canvas:cv,antialias:true,powerPreference:'high-performance'});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setSize(innerWidth,innerHeight);
renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.05;
const scene=new THREE.Scene();scene.background=new THREE.Color(0x2a2631);scene.fog=new THREE.Fog(0x2a2631,14,34);
const camera=new THREE.PerspectiveCamera(48,innerWidth/innerHeight,.1,80);
const mat=(c,o={})=>new THREE.MeshStandardMaterial({color:c,roughness:.7,metalness:.05,...o});
const glow=(c,i=1)=>new THREE.MeshStandardMaterial({color:c,emissive:c,emissiveIntensity:i});
const tl=new THREE.TextureLoader();
function tex(n,rx,ry){const t=tl.load('https://gripx.tech/town/assets/'+n+'.jpg');t.colorSpace=THREE.SRGBColorSpace;t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(rx,ry);t.anisotropy=4;return t}
const box=(w,h,d,x,y,z,m,p=scene)=>{const o=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),m);o.position.set(x,y,z);p.add(o);return o};
function label(text,w,h,bg,fg,font){const c=document.createElement('canvas');c.width=512;c.height=Math.round(512*h/w);const g=c.getContext('2d');g.fillStyle=bg;g.fillRect(0,0,c.width,c.height);g.fillStyle=fg;g.font=font;g.textAlign='center';g.textBaseline='middle';g.fillText(text,c.width/2,c.height/2);const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;return t}
// room 12 wide, 7 deep, 4.4 high. Front (z>0) open toward camera.
const floor=new THREE.Mesh(new THREE.PlaneGeometry(14,12),new THREE.MeshStandardMaterial({map:tex('concrete',4,3),color:0xb8aca6,roughness:.6}));floor.rotation.x=-Math.PI/2;scene.add(floor);
// lane markings
box(.08,.01,6,-2.6,.006,0,mat(0xe6c35a));box(.08,.01,6,2.6,.006,0,mat(0xe6c35a));
const wallM=new THREE.MeshStandardMaterial({map:tex('brick',5,2),color:0xd9bfae,roughness:.9});
box(14,4.6,.3,0,2.3,-3.6,wallM);box(.3,4.6,8,-6.4,2.3,0,wallM);box(.3,4.6,8,6.4,2.3,0,wallM);
box(14,.25,8,0,4.55,0,mat(0x3a3340));
// big window + daylight sill (back-left)
box(3.2,2,.1,-3.2,2.4,-3.42,glow(0xbfe3ff,.9));
for(const x of [-4.8,-3.2,-1.6])box(.07,2.1,.14,x,2.4,-3.38,mat(0x2a2f36));box(3.3,.07,.14,-3.2,2.4,-3.38,mat(0x2a2f36));
// roll-up door (right wall) 
box(.1,3,3.4,6.2,1.6,-.4,mat(0x7d8790));for(let i=0;i<8;i++)box(.12,.05,3.4,6.15,.4+i*.36,-.4,mat(0x59626b));
// pegboard + tools on back wall right
box(3.4,1.9,.06,2.4,2.5,-3.4,mat(0x8a6b4b));
const toolC=[0xcfd4d8,0xe6a23c,0xc84b4b,0x5b8ab3];
for(let i=0;i<9;i++){const x=1.0+i*.36;box(.06,.7+(i%3)*.12,.05,x,2.5+(i%2)*.1,-3.34,mat(toolC[i%4],{metalness:.5,roughness:.35}));box(.16,.1,.05,x,2.95+(i%3)*.1,-3.34,mat(toolC[(i+1)%4],{metalness:.5}))}
// sign
const sign=new THREE.Mesh(new THREE.PlaneGeometry(3.4,.75),new THREE.MeshBasicMaterial({map:label("CASTRO AUTO REPAIR",3.4,.75,'#10242b','#f6d4aa','600 44px Georgia')}));sign.position.set(0,3.85,-3.42);scene.add(sign);
const neon=new THREE.Mesh(new THREE.PlaneGeometry(2.6,.42),new THREE.MeshBasicMaterial({map:label("FORT WAYNE, IN",2.6,.42,'#0b1517','#53f2d4','700 54px Arial')}));neon.position.set(-3.2,3.6,-3.4);scene.add(neon);
const enqMap=label('ENQUIRY RECEIVED',2.6,.42,'#0b1517','#ffb35a','700 54px Arial');
// workbench + chest back-right
box(2.6,.12,.9,2.6,1.0,-2.95,mat(0x6b4a30));for(const x of [1.4,3.8])box(.12,1,.8,x,.5,-2.95,mat(0x3a3f46));
const chest=box(1.1,1.5,.7,4.9,.75,-3.0,mat(0xb83a2e,{metalness:.3,roughness:.5}));for(let i=0;i<5;i++)box(.95,.02,.02,4.9,.25+i*.28,-2.64,mat(0x1b1b1b));
box(.5,.18,.35,2.1,1.15,-2.9,mat(0xd9a441,{metalness:.5,roughness:.4}));box(.28,.28,.28,3.1,1.2,-2.9,mat(0x4d7a8c));
// tires stack left wall
for(let i=0;i<4;i++){const t=new THREE.Mesh(new THREE.TorusGeometry(.42,.2,10,22),mat(0x1c1c20,{roughness:.9}));t.rotation.x=Math.PI/2;t.position.set(-5.5,.22+i*.4,-1.4);scene.add(t)}
// oil drum + sign poster
const drum=new THREE.Mesh(new THREE.CylinderGeometry(.34,.34,.9,16),mat(0x2f5f8f));drum.position.set(-5.6,.45,.4);scene.add(drum);
// two-post lift + car
const liftG=new THREE.Group();scene.add(liftG);
for(const x of [-2.5,2.5]){box(.3,3.4,.4,x,1.7,-.7,mat(0xe6b13c,{metalness:.3}))}
const arms=new THREE.Group();liftG.add(arms);
for(const x of [-1.2,1.2])box(.18,.14,1.8,x,.5,.1,mat(0x2c2f35),arms),box(.18,.14,1.8,x,.5,-1.4,mat(0x2c2f35),arms);
const car=new THREE.Group();arms.add(car);
const paint=mat(0x39c4b4,{metalness:.35,roughness:.35});
box(2.0,.62,4.3,0,.9,-.6,paint,car);
const cab=box(1.75,.6,2.1,0,1.5,-.7,mat(0x1f8f84,{metalness:.5,roughness:.3}),car);
box(1.6,.46,1.9,0,1.52,-.7,new THREE.MeshStandardMaterial({color:0xb8dbe8,roughness:.25,metalness:.3}),car);
for(const x of [-1.02,1.02])for(const z of [-1.8,.55]){const w=new THREE.Mesh(new THREE.CylinderGeometry(.42,.42,.26,18),mat(0x15161a,{roughness:.9}));w.rotation.z=Math.PI/2;w.position.set(x,.55,z);car.add(w);const h=new THREE.Mesh(new THREE.CylinderGeometry(.2,.2,.28,12),mat(0xb7bcc2,{metalness:.7,roughness:.3}));h.rotation.z=Math.PI/2;h.position.set(x*1.01,.55,z);car.add(h)}
for(const x of [-.6,.6]){box(.35,.16,.05,x,.95,1.57,glow(0xfff0d2,.9),car);box(.35,.14,.05,x,.95,-2.78,glow(0xff4b3e,.8),car)}
car.position.y=.55;car.rotation.y=.42;arms.position.y=0;
// hanging lamps
const lamps=[[-2.4,0],[2.4,0]].map(([x,z])=>{const g=new THREE.Group();box(.04,1,.04,x,4.0,z,mat(0x222),g);const sh=new THREE.Mesh(new THREE.ConeGeometry(.55,.4,16,1,true),new THREE.MeshStandardMaterial({color:0x2a2f36,side:THREE.DoubleSide}));sh.position.set(x,3.4,z);g.add(sh);const b=new THREE.Mesh(new THREE.SphereGeometry(.12,12,10),glow(0xffe1a8,2));b.position.set(x,3.3,z);g.add(b);scene.add(g);const l=new THREE.PointLight(0xffd9a3,24,10,1.6);l.position.set(x,3.2,z);scene.add(l);return l});
scene.add(new THREE.HemisphereLight(0xcfd8ff,0x4a3b44,.9));
const sun=new THREE.DirectionalLight(0xbfdcff,1.1);sun.position.set(-4,4,-1);scene.add(sun);
const fill=new THREE.DirectionalLight(0xfff0e0,1.5);fill.position.set(2,3,9);scene.add(fill);
const win=new THREE.PointLight(0xbfe3ff,10,9,1.5);win.position.set(-3.2,2.4,-2.4);scene.add(win);
// mechanic (Quaternius CC0), idle at the bench
let mixer=null;
new GLTFLoader().loadAsync('https://gripx.tech/town/assets/character.gltf').then(d=>{
 const m=clone(d.scene);const b=new THREE.Box3().setFromObject(m),s=b.getSize(new THREE.Vector3());const k=1.8/s.y;m.scale.setScalar(k);m.position.y=-b.min.y*k;
 m.traverse(o=>{if(o.isMesh){o.frustumCulled=false;o.material=o.material.clone();if(o.material.name==='Purple')o.material.color.setHex(0xd9803a)}});
 const g=new THREE.Group();g.add(m);g.position.set(.9,0,-1.6);g.rotation.y=.4;scene.add(g);
 mixer=new THREE.AnimationMixer(m);const a=mixer.clipAction(THREE.AnimationClip.findByName(d.animations,'Interact')||THREE.AnimationClip.findByName(d.animations,'Idle'));a.play();
}).catch(()=>{});
// dust motes
const N=70,pg=new THREE.BufferGeometry(),pp=new Float32Array(N*3);for(let i=0;i<N;i++){pp[i*3]=(Math.random()-.5)*9;pp[i*3+1]=Math.random()*3.8;pp[i*3+2]=(Math.random()-.5)*6}
pg.setAttribute('position',new THREE.BufferAttribute(pp,3));const motes=new THREE.Points(pg,new THREE.PointsMaterial({color:0xfff0d0,size:.03,transparent:true,opacity:.5}));scene.add(motes);
// camera + interaction
let px=0,py=0,t0=performance.now(),liftT=0,liftGoal=0,neonT=0;const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
addEventListener('pointermove',e=>{px=(e.clientX/innerWidth-.5);py=(e.clientY/innerHeight-.5)});
addEventListener('gx-enquiry',()=>{liftGoal=1;neon.material.map=enqMap;neon.material.needsUpdate=true;neonT=performance.now();setTimeout(()=>{liftGoal=0;neon.material.map=openMap;neon.material.needsUpdate=true},9000)});
const openMap=neon.material.map;
function fit(){const w=innerWidth,h=innerHeight;renderer.setSize(w,h);camera.aspect=w/h;
 if(w<700){camera.fov=64;camera.setViewOffset(w,h,0,h*.2,w,h)}else{camera.fov=48;camera.setViewOffset(w,h,w*.1,0,w,h)}camera.updateProjectionMatrix()}
addEventListener('resize',fit);fit();
let frames=0;const clock=new THREE.Clock();
function tick(){requestAnimationFrame(tick);if(document.hidden)return;const dt=Math.min(clock.getDelta(),.1),t=clock.elapsedTime;frames++;
 const sway=reduce?0:1;
 camera.position.set(Math.sin(t*.12)*.5*sway+px*1.4*sway,2.2-py*.5*sway,8.3);camera.lookAt(-.2+px*.4*sway,1.7,-1);
 liftT+=(liftGoal-liftT)*Math.min(1,dt*1.4);arms.position.y=liftT*1.55;
 if(neonT&&performance.now()-neonT<9000)neon.visible=Math.floor((performance.now()-neonT)/350)%4!==3;else neon.visible=true;
 lamps.forEach((l,i)=>{l.intensity=24+Math.sin(t*3+i*2)*(reduce?0:1.2)});
 if(mixer)mixer.update(dt);
 if(!reduce){const a=motes.geometry.attributes.position;for(let i=0;i<N;i++){a.array[i*3+1]+=dt*.04;if(a.array[i*3+1]>3.8)a.array[i*3+1]=0}a.needsUpdate=true}
 renderer.render(scene,camera);
 window.__garage={frames,lift:liftT};if(frames===5){window.__ready=true;document.getElementById('loading').hidden=true}}
tick();
