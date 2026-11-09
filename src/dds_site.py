from shared import *

TOK = ("--ink:#141210;--ink-2:#2A2622;--mute:#5E574D;--line:rgba(20,18,16,.14);--line-2:rgba(20,18,16,.26);"
       "--paper:#FBF8F2;--ivory:#F3EDE1;--sand:#E7DDCB;--white:#fff;--accent:#B38F47;--accent-dark:#6B4A2E;--accent-text:#6F5115;"
       "--accent-soft:rgba(179,143,71,.14);--on-accent:#120D03;--night:#0E0D0C;--on-night:#F3EDE1;--on-night-mute:#B9AE9C;"
       "--display:'Bodoni Moda',Didot,'Bodoni 72',Georgia,serif;--sans:'Inter','Helvetica Neue',Arial,sans-serif;--gut:clamp(16px,4vw,48px);"
       "--maxw:1280px;--read:68ch;--r:2px;--shadow:0 1px 2px rgba(0,0,0,.04),0 8px 30px rgba(20,18,16,.06);color-scheme:light;"
       "--hero-op:.8;--hero-grad:linear-gradient(90deg,rgba(14,13,12,.93) 0%,rgba(14,13,12,.68) 45%,rgba(14,13,12,.05) 100%)")
FONTS = "family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500&family=Inter:wght@400;500;600"

SCHEMA = [{"@context": "https://schema.org", "@type": "Dentist", "name": "Goel Dental · Delhi Dental Smiles", "url": "https://delhidentalsmiles.com/",
  "telephone": TEL, "email": "info@delhidentalsmiles.com",
  "address": {"@type": "PostalAddress", "streetAddress": "14/185, Main Shivalik Road", "addressLocality": "Malviya Nagar, New Delhi", "postalCode": "110017", "addressCountry": "IN"},
  "medicalSpecialty": "Dentistry", "knowsAbout": ["Porcelain veneers", "Invisalign", "Teeth whitening", "Smile makeover", "Dental implants", "Same-day crowns"]}]

ROUTES = {
 "gap": {"t": "Gaps between front teeth", "lvl": "Bonding, veneers or Invisalign", "d": "Small gaps close with bonding in one visit (₹2,500 per tooth). Larger gaps: veneers or Invisalign, depending on bite.", "pick": "Smile makeover"},
 "chip": {"t": "Chipped or uneven teeth", "lvl": "Often one visit", "d": "Edge bonding from ₹1,500, or CAD/CAM and E.max veneers when more shape change is needed.", "pick": "Veneers"},
 "yellow": {"t": "Yellow or stained teeth", "lvl": "Cleaning, then whitening", "d": "EMS Airflow cleaning removes surface stains. Philips Zoom whitening lifts the shade further. Fluorosis and tetracycline stains may need veneers.", "pick": "Teeth whitening"},
 "crooked": {"t": "Crooked or protruding teeth", "lvl": "Invisalign or braces", "d": "Free consultation with an intraoral scan and a simulation of the result before you decide.", "pick": "Invisalign"},
 "missing": {"t": "Missing tooth", "lvl": "Implant consultation (free)", "d": "Implants from ₹17,000 (Adin/Alpha Bio) to ₹55,000 (Straumann) per implant, plus the crown.", "pick": "Dental implants"},
 "old": {"t": "Old crowns or veneers", "lvl": "Replace with metal-free", "d": "Dark lines at the gum and dull old crowns are replaced with zirconia, E.max or same-day CAD/CAM crowns.", "pick": "Veneers"},
 "gummy": {"t": "Gummy smile", "lvl": "Laser contouring", "d": "Laser gum contouring evens the gum line, sometimes combined with veneers.", "pick": "Smile makeover"},
 "wedding": {"t": "Wedding or event coming up", "lvl": "Plan by the date", "d": "Tell us the date. The plan is built backwards from it: whitening, bonding and veneers can often be finished within days.", "pick": "Smile makeover"},
}

def page():
    certs = [("cert-reg", "Delhi Dental Council registration"), ("cert-vita", "VITA Academy shade course"), ("cert-osstem", "Osstem implant master course"), ("cert-ivoclar", "Ivoclar ceramics training"), ("cert-navident", "Navident digital implant navigation, 2025"), ("cert-aomsi", "AOMSI digital implantology, 2025")]
    return head("Delhi Dental Smiles | Smile Makeovers, Veneers & Invisalign in South Delhi",
        "Cosmetic dentistry by Goel Dental, Malviya Nagar: E.max veneers, Invisalign, Philips Zoom whitening, same-day CAD/CAM crowns and implants. Real cases, published prices, free cosmetic consultation.",
        "https://delhidentalsmiles.com/", TOK, FONTS, SCHEMA) + f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="preview"><b>Preview build.</b> Gold badges mark details still to be confirmed. Photos and cases are from delhidentalsmiles.com.</div>
<header class="hd"><div class="wrap">
<a class="logo" href="#top">Delhi Dental Smiles <small>by Goel Dental</small></a>
<nav class="nav" aria-label="Main"><a href="#concerns">Your concern</a><a href="#journeys">Smile journeys</a><a href="#treatments">Treatments</a><a href="#same-day">Same-day</a><a href="#dr-goel">Dr Goel</a><a href="#prices">Prices</a></nav>
<a class="btn sm hd-cta" href="#book" data-book data-cta="header">Free consultation</a>
<button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
</div><nav class="drawer" id="drawer" aria-label="Mobile"><a href="#concerns">Your concern</a><a href="#journeys">Smile journeys</a><a href="#treatments">Treatments</a><a href="#same-day">Same-day dentistry</a><a href="#dr-goel">Dr Shikha Goel</a><a href="#prices">Prices</a><a href="#book">Book free consultation</a></nav></header>
<main id="main">
<section class="hero" id="top" aria-labelledby="h1" style="--hero-op:1">{pic('hero-smile','Smiling woman after cosmetic dental treatment', eager=True)}
<div class="wrap">
<p class="eyebrow">Cosmetic dentistry · Malviya Nagar, South Delhi</p>
<h1 id="h1">Smile makeovers in South Delhi, designed with you.</h1>
<p class="lead">E.max veneers, Invisalign, Philips Zoom whitening and same-day CAD/CAM crowns, planned by Dr Shikha Goel. You see the design before a tooth is touched.</p>
<div class="btns"><a class="btn accent" href="#book" data-book data-cta="hero">Book free consultation</a><a class="btn ghost" href="#journeys">See real smiles</a><a class="btn wa" href="#" data-wa data-cta="hero" data-t="Cosmetic consultation">{ICON['wa']} WhatsApp</a></div>
<div class="stats"><div><b>₹0</b><span>Cosmetic consultation</span></div><div><b>1 day</b><span>Many veneers &amp; crowns</span></div><div><b>4.8★</b><span>708 Google reviews</span></div></div>
</div></section>

<section class="section alt" id="concerns" aria-labelledby="c-h" data-router><div class="wrap">
<div class="head"><div><p class="eyebrow">Start with what you want to change</p><h2 id="c-h">What would you change about your smile?</h2></div></div>
<div class="chips" role="group" aria-label="Choose a concern">{''.join(f'<button class="chip" type="button" aria-pressed="false" data-r="{k}">{v["t"]}</button>' for k,v in ROUTES.items())}</div>
<div class="router-out" aria-live="polite" hidden></div>
</div></section>

<section class="section" id="journeys" aria-labelledby="j-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Smile journeys</p><h2 id="j-h">Real patients. Real results.</h2><p class="lead" style="margin:12px 0 0">Cases treated at Goel Dental, as published on the clinic's site. Results vary between patients.</p></div><span>{flag('Confirm consent for each case')}</span></div>
<div class="grid g2">
<figure style="margin:0" data-treatment="Veneers"><div class="photo" style="aspect-ratio:5/4">{pic('case2','Before and after: midline gap corrected with six E.max veneers')}</div><figcaption class="cap"><b>Midline gap.</b> Six E.max veneers, finished in two days.</figcaption></figure>
<figure style="margin:0"><div class="photo" style="aspect-ratio:5/4">{pic('case1','Before and after: chipped front teeth restored with four E.max veneers')}</div><figcaption class="cap"><b>Chipped front teeth.</b> Four E.max ceramic veneers in one day.</figcaption></figure>
<figure style="margin:0"><div class="photo" style="aspect-ratio:5/4">{pic('case3','Before and after: uneven teeth corrected with two CAD/CAM composite veneers')}</div><figcaption class="cap"><b>Uneven teeth.</b> Two CAD/CAM composite veneers, single visit.</figcaption></figure>
<figure style="margin:0"><div class="photo" style="aspect-ratio:5/4">{pic('case4','Before and after: fractured front teeth restored before a wedding')}</div><figcaption class="cap"><b>Fractured teeth before a wedding.</b> Two hybrid ceramic veneers.</figcaption></figure>
</div>
<div class="grid g3" style="margin-top:28px">
<figure style="margin:0" data-treatment="Invisalign">{ba('invisalign-case-2-pre','invisalign-case-2-post','Protruding teeth before Invisalign','Protrusion corrected with Invisalign')}<figcaption class="cap">Invisalign: protruding teeth corrected.</figcaption></figure>
<figure style="margin:0">{ba('veneer-case-1-pre','veneer-case-1-post','Imperfect front teeth before veneers','Front teeth after veneers')}<figcaption class="cap">Front-teeth veneers.</figcaption></figure>
<figure style="margin:0">{ba('invisalign-case-1-pre','invisalign-case-1-post','Gaps between teeth before Invisalign','Gaps closed with Invisalign')}<figcaption class="cap">Invisalign: gaps closed.</figcaption></figure>
</div></div></section>

<section class="section alt" id="treatments" aria-labelledby="t-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Treatments</p><h2 id="t-h">Whitening, veneers, alignment and replacement.</h2></div></div>
<div class="mosaic">
<a class="t2" href="#book" data-pick="Veneers" data-treatment="Veneers">{pic('veneer-tool','Dentist placing a porcelain veneer with a gloved hand')}<span><b>E.max porcelain veneers</b><i>Same or next day · ₹14,000 per tooth</i></span></a>
<a class="w2" href="#book" data-pick="Invisalign" data-treatment="Invisalign">{pic('aligner','Invisalign clear aligner in its case')}<span><b>Invisalign clear aligners</b><i>Free scan &amp; result simulation</i></span></a>
<a href="#book" data-pick="Teeth whitening" data-treatment="Teeth whitening">{pic('zoom','Philips Zoom whitening lamp and shade comparison')}<span><b>Philips Zoom whitening</b><i>About 45 minutes</i></span></a>
<a class="t2" href="#book" data-pick="Smile makeover">{pic('case5','Before and after: smile makeover')}<span><b>Smile makeover</b><i>Planned around your face</i></span></a>
<a href="#book" data-pick="Dental implants" data-treatment="Dental implants">{pic('implant-caption','Dental implant model')}<span><b>Dental implants</b><i>Nobel, Osstem, Straumann</i></span></a>
<a class="w2" href="#same-day">{pic('samedaycrown','Same-day dentistry equipment: scanner, milling and furnace')}<span><b>Same-day CAD/CAM crowns</b><i>Scan, design, mill in one visit</i></span></a>
<a href="#book" data-pick="Smile makeover">{pic('laser','Dental laser in use')}<span><b>Laser gum contouring</b><i>Gummy smile, depigmentation</i></span></a>
<a href="#book" data-pick="Teeth whitening">{pic('cleaning','EMS Airflow cleaning')}<span><b>EMS Airflow cleaning</b><i>Gentle stain removal</i></span></a>
</div></div></section>

<section class="section dark" id="same-day" aria-labelledby="sd-h"><div class="wrap split">
<div><p class="eyebrow">Same-day dentistry</p><h2 id="sd-h">Crowns and veneers in one visit.</h2>
<p class="lead">A digital scan replaces messy impressions. The crown or veneer is designed on screen with you, milled in the clinic and fitted the same day. No temporary tooth, no second trip.</p>
<ol class="steps" style="grid-template-columns:1fr 1fr;margin-top:18px"><li><h3>Scan</h3><p>Intraoral scanner, no impression trays.</p></li><li><h3>Design</h3><p>You see the shape and shade on screen.</p></li><li><h3>Mill</h3><p>CAD/CAM milling in the clinic.</p></li><li><h3>Fit</h3><p>Polished and bonded the same day.</p></li></ol>
<p class="small" style="margin-top:14px">Equipment named on the current site: CEREC CAD/CAM, dental microscopes, digital scanners. {flag('Confirm equipment list')}</p></div>
<div class="photo" style="aspect-ratio:1/1">{pic('digital-zone','Digital dentistry zone at Goel Dental with milling unit and scanner')}</div>
</div></section>

<section class="section" id="dr-goel" aria-labelledby="dr-h"><div class="wrap split">
<div class="photo" style="aspect-ratio:4/5;max-width:520px">{pic('dr-shikha-portrait','Dr Shikha Goel, cosmetic dentist')}</div>
<div><p class="eyebrow">Your cosmetic dentist</p><h2 id="dr-h">Dr Shikha Goel</h2>
<p class="lead">MDS, Conservative Dentistry &amp; Endodontics. Founder of Goel Dental. Trained in smile design, ceramics, Invisalign and digital implantology.</p>
<p class="muted">She plans every makeover herself: photos and shade first, then a mock-up you approve, then treatment.</p>
<div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:12px;margin-top:22px">{''.join(f'<figure style="margin:0"><div class="photo" style="aspect-ratio:3/4;background:#fff;border:1px solid var(--line)">{pic(c,a)}</div><figcaption class="cap" style="font-size:12px">{a}</figcaption></figure>' for c,a in certs)}</div>
<div class="btns"><a class="btn" href="#book" data-book data-cta="doctor">Book with Dr Goel</a></div></div>
</div></section>

<section class="section alt" id="prices" aria-labelledby="p-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Prices</p><h2 id="p-h">Cosmetic fees, published.</h2><p class="lead" style="margin:12px 0 0">From the clinic's 2026 price list. Your exact plan and fee come in writing after the free consultation.</p></div><span>{flag('Clinic to confirm')}</span></div>
<div class="grid g3">
<div class="tw"><table class="tbl"><thead><tr><th>Veneers &amp; bonding</th><th>Fee</th></tr></thead><tbody><tr><td>Edge bonding</td><td class="n">₹1,500</td></tr><tr><td>Gap closure, per tooth</td><td class="n">₹2,500</td></tr><tr><td>Composite veneer</td><td class="n">₹2,500</td></tr><tr><td>CAD/CAM composite veneer</td><td class="n">₹8,000</td></tr><tr><td>E.max / porcelain veneer</td><td class="n">₹14,000</td></tr></tbody></table></div>
<div class="tw"><table class="tbl"><thead><tr><th>Whitening &amp; crowns</th><th>Fee</th></tr></thead><tbody><tr><td>Pola Office whitening</td><td class="n">₹6,000</td></tr><tr><td>Dash whitening</td><td class="n">₹8,000</td></tr><tr><td>Philips Zoom whitening</td><td class="n">₹18,000</td></tr><tr><td>CAD/CAM crown</td><td class="n">₹12,000</td></tr><tr><td>Premium CAD/CAM crown</td><td class="n">₹14,000</td></tr></tbody></table></div>
<div class="tw"><table class="tbl"><thead><tr><th>Implants</th><th>Per implant</th></tr></thead><tbody><tr><td>Adin / Alpha Bio</td><td class="n">₹17,000</td></tr><tr><td>Osstem</td><td class="n">₹35,000</td></tr><tr><td>Nobel Biocare</td><td class="n">₹40–45,000</td></tr><tr><td>Straumann</td><td class="n">₹55,000</td></tr><tr><td>All-on-4 full arch</td><td class="n">₹90,000–1L</td></tr></tbody></table></div>
</div>
<p class="small muted" style="margin-top:16px">The current site lists written warranties (e.g. 10 years on E.max veneers, 5 years on lab crowns) with care conditions. {flag('Review warranty wording against DCI ethics & ad policy before use in ads')}</p>
</div></section>

<section class="section" aria-labelledby="tour-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">The clinic</p><h2 id="tour-h">Designed to calm, equipped to be precise.</h2></div></div>
<div class="mosaic">
<a class="w2 t2" href="#book">{pic('clinic-front','Reception area at Goel Dental')}<span><b>Reception</b></span></a>
<a href="#book">{pic('waiting','Waiting lounge')}<span><b>Lounge</b></span></a>
<a href="#book">{pic('consult-room','Consultation room')}<span><b>Smile design room</b></span></a>
<a class="w2" href="#book">{pic('operatory','Treatment operatories')}<span><b>Operatories</b></span></a>
</div></div></section>

<section class="section alt" aria-labelledby="rv-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">What patients say</p><h2 id="rv-h">In their words.</h2></div><a class="btn ghost sm" href="{MAPS}" data-cta="reviews">All 708 Google reviews</a></div>
<div class="grid g3">
<figure class="quote" style="margin:0"><blockquote>"I had been wanting a perfect smile for a very long time, all the more once I entered the fashion designing industry… I feel more confident now and don't hesitate from smiling for the camera."</blockquote><figcaption>Priyanshi Bindal · Ceramic veneers</figcaption></figure>
<figure class="quote" style="margin:0"><blockquote>"State of the art centre with readily available diagnostics, experts and implants, trained and courteous staff… a seamless, hassle-free and excellent experience."</blockquote><figcaption>Anubhav Srivastava · Implants</figcaption></figure>
<figure class="quote" style="margin:0"><blockquote>"Dr Shikha has a very good hand, you will really feel the difference, and all new technology. The staff is also responsible and knows the work."</blockquote><figcaption>Ginni G</figcaption></figure>
</div><p class="small muted" style="margin-top:14px">As published on delhidentalsmiles.com, shortened. {flag('Confirm source & consent')}</p>
</div></section>

<section class="section" aria-labelledby="faq-h"><div class="wrap split" style="align-items:start">
<div><p class="eyebrow">Questions</p><h2 id="faq-h">Before your consultation.</h2></div>
<div class="faq">
<details><summary>Is the cosmetic consultation free?</summary><div class="a">Yes, cosmetic and implant consultations are listed at ₹0 on the clinic's 2026 price list. X-rays or a CBCT scan, if needed, are charged separately.</div></details>
<details><summary>Do veneers damage my teeth?</summary><div class="a">Porcelain veneers usually need a thin layer of enamel removed. Composite and some CAD/CAM veneers need little or none. Dr Goel explains the trade-off for your teeth at the consultation.</div></details>
<details><summary>How white will whitening make my teeth?</summary><div class="a">It depends on your starting shade and the cause of staining. Your shade is recorded before and after. Fluorosis or tetracycline stains may respond better to veneers.</div></details>
<details><summary>Is the clinic a certified Invisalign provider?</summary><div class="a">The clinic offers Invisalign with a free intraoral scan and a simulation of the result. Provider tier to be confirmed.</div></details>
<details><summary>Can it be finished before my wedding?</summary><div class="a">Often, yes. Whitening, bonding and many veneer cases are completed within days. Tell us your date when you book.</div></details>
</div></div></section>

<section class="section dark" id="book" aria-labelledby="book-h"><div class="wrap split" style="align-items:start">
<div><p class="eyebrow">Free consultation</p><h2 id="book-h">See your new smile before you commit.</h2><p class="lead">Photos, shade and a plan with fees in writing. No cost for the consultation.</p>
<ul class="ticks" style="color:var(--on-night)"><li>Response within 30 minutes in clinic hours {flag('Confirm')}</li><li>Mock-up before any treatment</li><li>EMI available on leading credit cards</li></ul></div>
<div style="color:var(--ink)">{book_form(["Smile makeover","Veneers","Invisalign","Teeth whitening","Dental implants","Not sure yet"], title="Book a free cosmetic consultation")}</div>
</div></section>
</main>
<footer class="ft"><div class="wrap">
<div class="ft-grid">
<div><p class="logo" style="font-size:24px">Delhi Dental Smiles</p><p>By Goel Dental · 14/185, Ground Floor, Main Shivalik Road, Malviya Nagar, New Delhi 110017<br><a href="tel:{TEL}" data-cta="footer">{PHONE_DISPLAY}</a> · info@delhidentalsmiles.com</p><p class="small">Site says "since 2010"; goeldentalcare.com says founded 2011. {flag('Confirm year')}</p></div>
<div><h2>Treatments</h2><ul><li><a href="#treatments">E.max veneers</a></li><li><a href="#treatments">Invisalign</a></li><li><a href="#treatments">Zoom whitening</a></li><li><a href="#same-day">Same-day crowns</a></li><li><a href="#treatments">Implants</a></li></ul></div>
<div><h2>Prototype</h2><ul><li><a href="index.html">Project hub</a></li><li><a href="goel-dental-care.html">Goel Dental Care site</a></li><li><a href="strategy-and-google-ads.html">Strategy &amp; Google Ads review</a></li></ul></div>
</div>
<div class="ft-base"><span>© 2026 Goel Dental. Preview build prepared by Daniel Deepak; not the live site.</span><button type="button" data-tlog>Show tracking events</button></div>
</div></footer>
{mbar('Free consult')}
<script>window.GD_ROUTES={json.dumps(ROUTES)};</script>
<script>{tracking_js('delhi_dental_smiles')}</script>
</body></html>"""

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "delhi-dental-smiles.html"
    open(out, "w").write(page()); print("ok", out)
