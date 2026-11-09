"""Shared pieces for the Goel Dental Care + Delhi Dental Smiles single-file sites."""
import base64, html, json
from pathlib import Path

IMG = Path(__file__).parent / "img"
_cache = {}

def img(name):
    if name not in _cache:
        _cache[name] = "data:image/webp;base64," + base64.b64encode((IMG / f"{name}.webp").read_bytes()).decode()
    return _cache[name]

def pic(name, alt, cls="", eager=True):
    return f'<img src="{img(name)}" alt="{html.escape(alt)}"{" class=" + chr(34) + cls + chr(34) if cls else ""}{"" if eager else " loading=" + chr(34) + "lazy" + chr(34)}>'

PHONE_DISPLAY = "+91 93102 07552"
TEL = "+919310207552"
WA = "919310207552"
MAPS = "https://www.google.com/maps/search/?api=1&query=Goel+Dental+14%2F185+Main+Shivalik+Road+Malviya+Nagar+New+Delhi"

ICON = {
 "phone": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 3h3l2 5-2.5 1.5a11 11 0 0 0 7 7L16 14l5 2v3a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.8-1.4a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>',
}

def flag(t="To confirm"):
    return f'<span class="pending">{html.escape(t)}</span>'

CSS = r"""
[hidden]{display:none!important}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:84px}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.65 var(--sans);-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}
a{color:inherit}
h1,h2,h3{font-family:var(--display);font-weight:500;line-height:1.08;letter-spacing:-.01em;margin:0 0 .5em;text-wrap:balance}
h1{font-size:clamp(38px,5.4vw,72px)}
h2{font-size:clamp(30px,3.6vw,50px)}
h3{font-size:clamp(20px,1.7vw,24px);line-height:1.2}
p{margin:0 0 1em;max-width:var(--read)}
:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.wrap{max-width:var(--maxw);margin:0 auto;padding-left:max(var(--gut),env(safe-area-inset-left,0px));padding-right:max(var(--gut),env(safe-area-inset-right,0px))}
.skip{position:absolute;left:12px;top:-60px;z-index:100;background:var(--ink);color:var(--paper);padding:12px 18px}
.skip:focus{top:12px}
.eyebrow{font:600 12px/1.3 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--accent-text);margin:0 0 18px}
.lead{font-size:clamp(18px,1.5vw,21px);color:var(--mute);line-height:1.6}
.small{font-size:14.5px}.muted{color:var(--mute)}
.pending{display:inline-flex;align-items:center;gap:6px;font:600 10.5px/1 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--accent-text);border:1px solid var(--accent);padding:5px 8px;border-radius:2px;vertical-align:middle;max-width:100%;line-height:1.3;background:var(--accent-soft)}
.pending::before{content:"◆";font-size:8px;color:var(--accent)}
.preview{background:var(--night);color:var(--on-night-mute);font:500 12.5px/1.4 var(--sans);text-align:center;padding:8px var(--gut)}
.preview b{color:var(--on-night)}
/* header */
.hd{position:sticky;top:0;z-index:60;background:color-mix(in srgb,var(--paper) 94%,transparent);backdrop-filter:saturate(1.2) blur(14px);border-bottom:1px solid var(--line)}
.hd .wrap{display:flex;align-items:center;gap:24px;height:72px}
.logo{font:500 24px/1 var(--display);text-decoration:none;letter-spacing:.01em;display:flex;align-items:baseline;gap:10px;color:var(--ink)}
.logo small{font:600 10.5px/1.2 var(--sans);letter-spacing:.22em;text-transform:uppercase;color:var(--mute)}
.nav{display:none;margin-left:auto;gap:26px;align-items:center}
.nav a{white-space:nowrap;font:500 14px var(--sans);text-decoration:none;color:var(--ink-2)}
.nav a:hover{color:var(--accent-text)}
.hd-cta{display:none}
.burger{margin-left:auto;display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border:1px solid var(--line-2);background:transparent;cursor:pointer;color:var(--ink)}
.drawer{display:none;border-top:1px solid var(--line);background:var(--paper)}
.drawer.open{display:block}
.drawer a{display:block;padding:15px var(--gut);border-bottom:1px solid var(--line);text-decoration:none;font-weight:500}
@media(min-width:1080px){.logo{white-space:nowrap}.nav{display:flex}.hd-cta{display:inline-flex}.burger,.drawer{display:none!important}}
/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:50px;padding:0 26px;background:var(--ink);color:var(--paper);border:1px solid var(--ink);font:600 12.5px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;text-decoration:none;cursor:pointer;border-radius:var(--r);transition:background .2s,color .2s,border-color .2s}
.btn svg{width:18px;height:18px}
.btn:hover{background:var(--accent-dark);border-color:var(--accent-dark)}
.btn.ghost{background:transparent;color:var(--ink);border-color:var(--line-2)}
.btn.ghost:hover{border-color:var(--ink)}
.btn.accent{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.btn.wa{background:#157A43;border-color:#157A43;color:#fff}
.btn.urgent{background:#A8361F;border-color:#A8361F;color:#fff}
.btn.sm{min-height:42px;padding:0 18px;font-size:11.5px}
.btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px}
/* hero */
.hero{position:relative;background:var(--night);color:var(--on-night);overflow:hidden}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:var(--hero-op,.5)}
.hero::after{content:"";position:absolute;inset:0;background:var(--hero-grad);z-index:1}
.hero .wrap{position:relative;z-index:2;padding-top:clamp(72px,11vw,150px);padding-bottom:clamp(56px,8vw,110px)}
.hero h1{color:var(--on-night);max-width:17ch}
.hero .lead{color:var(--on-night-mute)}
.hero .eyebrow{color:var(--accent)}
.hero .btn.ghost{color:var(--on-night);border-color:rgba(255,255,255,.45)}
.hero .pending{color:var(--on-night);background:rgba(255,255,255,.08)}
.stats{display:flex;flex-wrap:wrap;gap:12px 44px;margin-top:44px;padding-top:26px;border-top:1px solid rgba(255,255,255,.2)}
.stats div{display:grid;gap:4px}
.stats b{font:500 clamp(30px,3vw,42px)/1 var(--display);color:var(--on-night)}
.stats span{font:600 11px/1.3 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--on-night-mute)}
/* sections */
.section{padding:clamp(60px,8vw,108px) 0}
.section.alt{background:var(--ivory)}
.section.dark{background:var(--night);color:var(--on-night)}
.section.dark h2,.section.dark h3{color:var(--on-night)}
.section.dark p,.section.dark .lead{color:var(--on-night-mute)}
.head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:20px 40px;margin-bottom:44px}
.head>div{max-width:760px}
.head h2{margin:0}
.grid{display:grid;gap:28px}
.g2{grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(min(100%,290px),1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr))}
.split{display:grid;gap:clamp(32px,5vw,72px);align-items:center}
@media(min-width:900px){.split{grid-template-columns:1fr 1fr}.split.r>:first-child{order:2}}
.photo{position:relative;overflow:hidden;background:var(--sand)}
.photo img{width:100%;height:100%;object-fit:cover}
.cap{font:500 13px/1.4 var(--sans);color:var(--mute);margin-top:10px}
/* mosaic */
.mosaic{display:grid;gap:12px;grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:190px;grid-auto-flow:dense}
@media(min-width:900px){.mosaic{grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:230px}.mosaic .w2{grid-column:span 2}}
.mosaic .t2{grid-row:span 2}
.mosaic a{position:relative;overflow:hidden;display:block;text-decoration:none;background:var(--sand)}
.mosaic img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .5s}
.mosaic a:hover img{transform:scale(1.04)}
.mosaic span{position:absolute;left:0;right:0;bottom:0;padding:34px 16px 14px;color:#fff;background:linear-gradient(transparent,rgba(0,0,0,.72));display:grid;gap:2px}
.mosaic span b{font:500 20px/1.15 var(--display)}
.mosaic span i{font:500 12.5px/1.3 var(--sans);font-style:normal;opacity:.85}
/* concern chips */
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chip{min-height:46px;padding:0 18px;border:1px solid var(--line-2);background:var(--white);color:var(--ink);font:500 15px var(--sans);cursor:pointer;border-radius:999px}
.chip[aria-pressed=true]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.router-out{margin-top:28px;padding:26px;background:var(--white);border:1px solid var(--line);display:grid;gap:10px}
.router-out .lvl{font:600 11.5px var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--accent-text)}
.router-out .lvl.u{color:#A8361F}
/* cards */
.card>.tag,.card>.pending{justify-self:start}.card{background:var(--white);border:1px solid var(--line);padding:28px;display:grid;gap:10px;align-content:start}
.doc{display:grid;gap:14px;align-content:start}
.doc .photo{aspect-ratio:4/5}
.doc .role{font:600 11.5px/1.4 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--accent-text)}
.doc .cred{font-size:14.5px;color:var(--mute);margin:0}
.mono-av{aspect-ratio:4/5;background:var(--ivory);display:grid;place-items:center;font:500 54px var(--display);color:var(--accent-text);border:1px solid var(--line)}
/* tables */
.tbl{width:100%;border-collapse:collapse;font-size:15.5px;background:var(--white)}
.tbl th,.tbl td{text-align:left;padding:13px 16px;border-bottom:1px solid var(--line);vertical-align:top}
.tbl th{font:600 11px/1.3 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--mute);background:var(--ivory)}
.tbl td.n{font-variant-numeric:tabular-nums;white-space:nowrap;font-weight:600}
.tw{overflow-x:auto;border:1px solid var(--line)}
/* before after */
.ba{position:relative;aspect-ratio:740/507;overflow:hidden;background:var(--sand);user-select:none;touch-action:pan-y}
.ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ba .after{clip-path:inset(0 0 0 var(--pos,50%))}
.ba input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0}
.ba .hdl{position:absolute;top:0;bottom:0;left:var(--pos,50%);width:2px;background:#fff;pointer-events:none}
.ba .hdl::after{content:"‹ ›";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;background:#fff;color:#111;display:grid;place-items:center;font:600 16px var(--sans);box-shadow:0 4px 18px rgba(0,0,0,.25)}
.ba .l{position:absolute;top:12px;font:600 10.5px var(--sans);letter-spacing:.16em;text-transform:uppercase;background:rgba(0,0,0,.6);color:#fff;padding:6px 9px}
.ba .l.a{left:12px}.ba .l.b{right:12px}
/* quotes */
.quote{background:var(--white);border:1px solid var(--line);padding:30px;display:grid;gap:16px;align-content:start}
.quote blockquote{margin:0;font:400 19px/1.55 var(--display);color:var(--ink)}
.quote figcaption{font:600 12px/1.4 var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--mute)}
/* steps */
.steps{list-style:none;padding:0;margin:0;display:grid;gap:0;counter-reset:s}
@media(min-width:900px){.steps{grid-template-columns:repeat(5,1fr)}}
.steps li{counter-increment:s;border-top:1px solid var(--line-2);padding:22px 22px 22px 0}
.steps li::before{content:"0" counter(s);display:block;font:500 34px/1 var(--display);color:var(--accent-text);margin-bottom:14px}
.steps h3{font-size:20px}
.steps p{font-size:15px;color:var(--mute);margin:0}
/* faq */
.faq details{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;padding:20px 40px 20px 0;font:500 21px/1.3 var(--display);position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:4px;top:18px;font:300 26px/1 var(--sans);color:var(--accent-text)}
.faq details[open] summary::after{content:"–"}
.faq .a{padding:0 0 22px;color:var(--mute)}
/* urgent */
.urgent{background:#FBEDE8;border-left:4px solid #A8361F;padding:clamp(24px,4vw,44px)}
.urgent .eyebrow{color:#A8361F}
.ticks{list-style:none;padding:0;margin:0 0 1em;display:grid;gap:8px}
.ticks li{padding-left:26px;position:relative}
.ticks li::before{content:"";position:absolute;left:2px;top:.6em;width:12px;height:7px;border-left:2px solid var(--accent-text);border-bottom:2px solid var(--accent-text);transform:rotate(-45deg)}
/* form */
.form{display:grid;gap:16px}
.field{display:grid;gap:6px}
.field label,.legend{font:600 14px var(--sans)}
.input{width:100%;min-height:52px;padding:12px 14px;border:1px solid var(--line-2);background:var(--white);color:var(--ink);font:400 16px var(--sans);border-radius:var(--r)}
.input:focus{outline:2px solid var(--accent);border-color:var(--accent)}
.phone-in{display:grid;grid-template-columns:62px 1fr}
.phone-in span{display:grid;place-items:center;border:1px solid var(--line-2);border-right:0;background:var(--ivory);font-weight:600}
.opts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.opt{position:relative}.opt input{position:absolute;opacity:0;inset:0}
.opt span{display:flex;align-items:center;min-height:50px;padding:10px 14px;border:1px solid var(--line-2);background:var(--white);font:500 14.5px var(--sans);cursor:pointer}
.opt input:checked+span{border-color:var(--ink);background:var(--accent-soft)}
.opt input:focus-visible+span{outline:2px solid var(--accent)}
.consent{display:grid;grid-template-columns:22px 1fr;gap:10px;font-size:13.5px;color:var(--mute)}
.consent input{width:20px;height:20px;margin:2px 0 0;accent-color:var(--ink)}
.err{color:#A8361F;font-size:13px;font-weight:600;margin:0}
.formcard{background:var(--white);border:1px solid var(--line);padding:clamp(22px,3vw,40px);box-shadow:var(--shadow)}
.confirm{display:grid;gap:12px}
.confirm .ref{font:600 24px var(--sans);letter-spacing:.06em}
/* footer */
.ft{background:var(--night);color:var(--on-night-mute);padding:72px 0 120px;font-size:15px}
.ft a{color:var(--on-night);text-decoration:none}.ft a:hover{text-decoration:underline}
.ft-grid{display:grid;gap:40px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.ft h2{font:600 11px/1.3 var(--sans);letter-spacing:.2em;text-transform:uppercase;color:var(--accent);margin-bottom:14px}
.ft ul{list-style:none;padding:0;margin:0}.ft li{margin:0 0 8px}
.ft .logo{color:var(--on-night)}
.ft-base{border-top:1px solid rgba(255,255,255,.14);margin-top:48px;padding-top:24px;display:flex;flex-wrap:wrap;gap:12px 28px;font-size:13px}
.ft-base button{background:none;border:1px solid rgba(255,255,255,.3);color:var(--on-night-mute);padding:6px 12px;font:500 12px var(--sans);cursor:pointer}
.ft .pending{color:var(--on-night-mute);background:transparent}
/* mobile bar */
.mbar{position:fixed;left:0;right:0;bottom:0;z-index:55;display:grid;grid-template-columns:1fr 1fr 1.2fr;gap:1px;background:var(--line);border-top:1px solid var(--line);padding-bottom:env(safe-area-inset-bottom,0)}
.mbar a{display:flex;align-items:center;justify-content:center;gap:8px;min-height:56px;font:600 12px var(--sans);letter-spacing:.12em;text-transform:uppercase;text-decoration:none;background:var(--paper);color:var(--ink)}
.mbar a svg{width:18px;height:18px}
.mbar a.wa{color:#157A43}.mbar a.bk{background:var(--ink);color:var(--paper)}
@media(min-width:1080px){.mbar{display:none}.ft{padding-bottom:72px}}
/* tracking inspector */
.tlog{position:fixed;right:12px;bottom:72px;z-index:80;width:min(360px,calc(100vw - 24px));max-height:46vh;overflow:auto;background:#111;color:#E8E2D6;font:400 11.5px/1.5 ui-monospace,Menlo,monospace;padding:12px;box-shadow:0 12px 40px rgba(0,0,0,.35)}
.tlog h2{font:600 11px var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--accent);display:flex;justify-content:space-between;margin:0 0 8px}
.tlog h2 button{background:none;border:0;color:#fff;cursor:pointer}
.tlog .ev{border-top:1px solid rgba(255,255,255,.12);padding:6px 0}.tlog .ev b{color:#FFD36B}
@media(min-width:1080px){.tlog{bottom:16px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
@media print{.hd,.mbar,.preview,.tlog,.burger,.drawer{display:none!important}.hero>img{opacity:.35}.section{padding:36px 0;break-inside:auto}.mosaic a,.card,.quote,.doc,.ba,.tbl tr{break-inside:avoid}body{font-size:13px}.ft{padding:32px 0}.ba input,.ba .hdl{display:none}.ba .after{clip-path:inset(0 0 0 50%)}}
"""

def tracking_js(brand):
    return r"""
(function(){var W=window,D=document;W.dataLayer=W.dataLayer||[];
var CFG={brand:"%BRAND%",tel:"%TEL%",wa:"%WA%"};
function g(k){try{return JSON.parse(localStorage.getItem(k))}catch(e){return null}}function s(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
var K=["utm_source","utm_medium","utm_campaign","utm_term","utm_content","gclid","gbraid","wbraid","fbclid"],p={},q;try{q=new URLSearchParams(location.search);K.forEach(function(k){var v=q.get(k);if(v)p[k]=v.slice(0,150)})}catch(e){}
var ref=D.referrer&&D.referrer.indexOf(location.host)<0?D.referrer:"";
function ch(){if(p.gclid||p.gbraid||p.wbraid)return"google_ads";if(p.fbclid&&/paid|cpc/i.test(p.utm_medium||""))return"meta_ads";if(p.utm_source==="gbp")return"google_business_profile";if(p.utm_medium)return(p.utm_source||"?")+" / "+p.utm_medium;if(/google\./.test(ref))return"organic_google";if(/facebook|instagram/.test(ref))return"organic_social";return ref?"referral":"direct"}
var t={ts:Date.now(),landing:location.pathname.split("/").pop()||"/",channel:ch()};K.forEach(function(k){if(p[k])t[k]=p[k]});
var ft=g("gd_ft");if(!ft){ft=t;s("gd_ft",t)}var lt=g("gd_lt");if(Object.keys(p).length||ref||!lt){lt=t;s("gd_lt",t)}
var R;try{R=sessionStorage.getItem("gd_ref")}catch(e){}if(!R){var a="ABCDEFGHJKLMNPQRSTUVWXYZ23456789";R="GD-";for(var i=0;i<5;i++)R+=a[Math.floor(Math.random()*a.length)];try{sessionStorage.setItem("gd_ref",R)}catch(e){}}
var L=[];function tr(ev,x){var o={event:ev,brand:CFG.brand,ref_code:R};for(var k in x||{})o[k]=x[k];W.dataLayer.push(o);L.forEach(function(f){f(o)});return o}
W.GD={track:tr,ref:R,on:function(f){L.push(f)},attr:function(){return{ref_code:R,ft_channel:ft.channel,ft_campaign:ft.utm_campaign||"",ft_landing:ft.landing,lt_channel:lt.channel,lt_source:lt.utm_source||"",lt_medium:lt.utm_medium||"",lt_campaign:lt.utm_campaign||"",lt_term:lt.utm_term||"",gclid:lt.gclid||ft.gclid||"",fbclid:lt.fbclid||ft.fbclid||""}}};
W.dataLayer.push({event:"gd_context",brand:CFG.brand,attribution:W.GD.attr()});
function wa(t){return"https://wa.me/"+CFG.wa+"?text="+encodeURIComponent("Hi Goel Dental, I'd like to book"+(t?" for "+t:"")+". (Ref "+R+")")}W.GD.wa=wa;
D.addEventListener("click",function(e){var el=e.target.closest&&e.target.closest("a,button");if(!el)return;var c=el.getAttribute("data-cta")||"inline",t=el.getAttribute("data-t")||"",h=el.getAttribute("href")||"";
if(h.indexOf("tel:")===0)tr("click_call",{cta_location:c,treatment:t});else if(el.hasAttribute("data-wa")){el.setAttribute("href",wa(t));tr("click_whatsapp",{cta_location:c,treatment:t})}else if(el.hasAttribute("data-book"))tr("click_book",{cta_location:c,treatment:t});else if(/google\.com\/maps/.test(h))tr("click_directions",{cta_location:c})},true);
var io="IntersectionObserver"in W?new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){tr("treatment_view",{treatment:en.target.getAttribute("data-treatment")});io.unobserve(en.target)}})},{threshold:.4}):null;
D.querySelectorAll("[data-treatment]").forEach(function(n){io&&io.observe(n)});
D.addEventListener("toggle",function(e){if(e.target.tagName==="DETAILS"&&e.target.open){var sm=e.target.querySelector("summary");tr("faq_open",{q:sm?sm.textContent.trim().slice(0,70):""})}},true);
// menu
var b=D.querySelector(".burger"),dr=D.querySelector(".drawer");if(b)b.addEventListener("click",function(){var o=dr.classList.toggle("open");b.setAttribute("aria-expanded",o)});if(dr)dr.addEventListener("click",function(e){if(e.target.tagName==="A"){dr.classList.remove("open");b.setAttribute("aria-expanded","false")}});
// before/after
D.querySelectorAll(".ba input").forEach(function(i){var f=function(){i.parentNode.style.setProperty("--pos",i.value+"%")};i.addEventListener("input",f);f()});
// router
var RT=W.GD_ROUTES||{},ro=D.querySelector("[data-router]");if(ro){var out=ro.querySelector(".router-out");ro.querySelectorAll(".chip").forEach(function(c){c.addEventListener("click",function(){var r=RT[c.getAttribute("data-r")];ro.querySelectorAll(".chip").forEach(function(x){x.setAttribute("aria-pressed",x===c)});
out.innerHTML='<span class="lvl'+(r.u?" u":"")+'">'+r.lvl+'</span><h3>'+r.t+'</h3><p class="muted" style="margin:0">'+r.d+'</p><div class="btns" style="margin-top:12px">'+(r.u?'<a class="btn urgent" href="tel:'+CFG.tel+'" data-cta="router" data-t="'+r.t+'">Call now</a>':'<a class="btn" href="#book" data-book data-cta="router" data-t="'+r.t+'" data-pick="'+(r.pick||"")+'">Book</a>')+'<a class="btn wa" href="#" data-wa data-cta="router" data-t="'+r.t+'">WhatsApp</a>'+(r.go?'<a class="btn ghost" href="'+r.go+'">Read more</a>':'')+'</div>';out.hidden=false;tr("router_select",{symptom:r.t,urgency:r.u?"urgent":"planned"})})})}
D.addEventListener("click",function(e){var el=e.target.closest&&e.target.closest("[data-pick]");if(!el)return;var v=el.getAttribute("data-pick");var r=v&&D.querySelector('#book input[name=treatment][value="'+v+'"]');if(r){r.checked=true}});
// booking form
var f=D.getElementById("bookform");if(f){var st=false;f.addEventListener("focusin",function(){if(!st){st=true;tr("appointment_start",{form_id:"bookform"})}});
f.addEventListener("submit",function(e){e.preventDefault();var fd=new FormData(f),n=(fd.get("name")||"").trim(),ph=(fd.get("phone")||"").replace(/\D/g,"").replace(/^(91|0)(?=\d{10}$)/,""),ok=true;
var en=f.querySelector("[data-e=name]"),ep=f.querySelector("[data-e=phone]"),ec=f.querySelector("[data-e=consent]");en.hidden=!!n;if(!n)ok=false;var pv=/^[6-9]\d{9}$/.test(ph);ep.hidden=pv;if(!pv)ok=false;var cc=f.querySelector("[name=consent]").checked;ec.hidden=cc;if(!cc)ok=false;if(!ok)return;
var A=W.GD.attr();Object.keys(A).forEach(function(k){var h=f.querySelector('[name="'+k+'"]');if(!h){h=D.createElement("input");h.type="hidden";h.name=k;f.appendChild(h)}h.value=A[k]});
var tx=fd.get("treatment")||"General check-up",lid=R+"-"+Date.now().toString(36).toUpperCase().slice(-4),c={form_id:"bookform",treatment:tx,preferred_time:fd.get("time")||"",lead_id:lid};
tr("appointment_submit",c);tr("form_submit",c);tr("lead_generated",{lead_id:lid,treatment:tx,value:0,currency:"INR"});
var d=D.getElementById("bookdone");d.querySelector("[data-f=ref]").textContent=lid;d.querySelector("[data-f=t]").textContent=tx;d.querySelector("[data-wa]").setAttribute("href",wa(tx));f.hidden=true;d.hidden=false;d.querySelector("h3").focus();tr("booking_confirmation",{lead_id:lid,treatment:tx})})}
// tracking inspector
var lg=null;function openLog(){if(lg)return;lg=D.createElement("aside");lg.className="tlog";lg.setAttribute("aria-live","polite");lg.innerHTML='<h2>dataLayer events <button type="button" aria-label="Close">×</button></h2><div></div>';D.body.appendChild(lg);lg.querySelector("button").onclick=function(){lg.remove();lg=null};var box=lg.querySelector("div");function add(o){if(!lg||!o.event)return;var d=D.createElement("div");d.className="ev";d.innerHTML="<b>"+o.event+"</b> "+Object.keys(o).filter(function(k){return k!=="event"&&k!=="attribution"&&o[k]!==""}).slice(0,6).map(function(k){return k+"="+String(o[k]).slice(0,36)}).join(" · ");box.prepend(d)}W.dataLayer.forEach(add);W.GD.on(add)}
if(/[?&]debug=1/.test(location.search))openLog();var tb=D.querySelector("[data-tlog]");if(tb)tb.addEventListener("click",openLog);
})();
""".replace("%BRAND%", brand).replace("%TEL%", TEL).replace("%WA%", WA)

def head(title, desc, canonical, tokens, fonts, schema):
    return f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:locale" content="en_IN">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<!-- Google Tag Manager container goes here (GTM-XXXXXXX). Vendor tags live in GTM, not in this file. -->
<style>:root{{{tokens}}}{CSS}</style>
{''.join('<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>' for s in schema)}
</head>"""

def book_form(options, title="Book an appointment", sub="Two details. The front desk confirms the time by phone or WhatsApp.", free_note=""):
    opts = "".join(f'<label class="opt"><input type="radio" name="treatment" value="{html.escape(o)}"><span>{html.escape(o)}</span></label>' for o in options)
    return f"""<div class="formcard">
<form class="form" id="bookform" novalidate>
<div><h3 style="margin-bottom:6px">{title}</h3><p class="small muted" style="margin:0">{sub} {free_note}</p></div>
<fieldset style="border:0;padding:0;margin:0" class="field"><legend class="legend" style="margin-bottom:8px">What is it for? <span class="muted" style="font-weight:400">(optional)</span></legend><div class="opts">{opts}</div></fieldset>
<div class="field"><label for="bf-time">Preferred time <span class="muted" style="font-weight:400">(optional)</span></label><select class="input" id="bf-time" name="time"><option value="">Any time</option><option>Today</option><option>Tomorrow morning</option><option>Tomorrow evening</option><option>This week</option><option>Weekend</option></select></div>
<div class="field"><label for="bf-name">Your name</label><input class="input" id="bf-name" name="name" autocomplete="name"><p class="err" data-e="name" hidden>Add your name so we know who to ask for.</p></div>
<div class="field"><label for="bf-phone">Mobile number</label><div class="phone-in"><span>+91</span><input class="input" id="bf-phone" name="phone" inputmode="tel" autocomplete="tel-national" placeholder="98xxxxxxxx"></div><p class="err" data-e="phone" hidden>Enter a 10-digit Indian mobile number.</p></div>
<label class="consent"><input type="checkbox" name="consent"><span>I agree to be contacted about this appointment. Details are used only to arrange care.</span></label><p class="err" data-e="consent" hidden>Please tick to let us contact you.</p>
<button class="btn" type="submit">Request appointment</button>
</form>
<div class="confirm" id="bookdone" hidden>
<p class="eyebrow" style="margin:0">Request received</p><h3 tabindex="-1">Thank you. We'll call you to confirm.</h3>
<p class="muted" style="margin:0">Reference <b class="ref" data-f="ref"></b><br>For: <b data-f="t"></b></p>
<p class="small muted" style="margin:0">During clinic hours the front desk calls back within 30 minutes {flag('Confirm SLA')}. Prototype: nothing is sent. Use "Show tracking events" in the footer to see what GTM receives.</p>
<a class="btn wa" href="#" data-wa data-cta="confirmation">{ICON['wa']} Continue on WhatsApp</a>
</div></div>"""

def ba(pre, post, alt_pre, alt_post):
    return f"""<div class="ba">{pic(pre, alt_pre)}<img class="after" src="{img(post)}" alt="{html.escape(alt_post)}"><span class="l a">Before</span><span class="l b">After</span><input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"><span class="hdl" aria-hidden="true"></span></div>"""

def mbar(cta_label="Book"):
    return f"""<nav class="mbar" aria-label="Quick contact"><a href="tel:{TEL}" data-cta="sticky_mobile">{ICON['phone']} Call</a><a class="wa" href="#" data-wa data-cta="sticky_mobile">{ICON['wa']} WhatsApp</a><a class="bk" href="#book" data-book data-cta="sticky_mobile">{cta_label}</a></nav>"""
