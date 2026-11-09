from shared import *

TOK = ("--ink:#13201F;--ink-2:#2B3836;--mute:#56625F;--line:rgba(19,32,31,.13);--line-2:rgba(19,32,31,.26);"
       "--paper:#FAF8F4;--ivory:#F1EEE7;--sand:#E3DED3;--white:#fff;--accent:#E8792B;--accent-dark:#B85A17;--accent-text:#9A4A10;"
       "--accent-soft:rgba(232,121,43,.12);--on-accent:#1A0E04;--night:#0F1918;--on-night:#F4F1EA;--on-night-mute:#B9C2BE;"
       "--display:'Fraunces',Georgia,'Times New Roman',serif;--sans:'Inter','Helvetica Neue',Arial,sans-serif;--gut:clamp(16px,4vw,48px);"
       "--maxw:1240px;--read:68ch;--r:2px;--shadow:0 1px 2px rgba(0,0,0,.04),0 10px 30px rgba(19,32,31,.07);color-scheme:light;"
       "--hero-op:.62;--hero-grad:linear-gradient(90deg,rgba(15,25,24,.94) 0%,rgba(15,25,24,.72) 48%,rgba(15,25,24,.25) 100%)")
FONTS = "family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600"

SCHEMA = [{"@context": "https://schema.org", "@type": "Dentist", "name": "Goel Dental", "url": "https://www.goeldentalcare.com/",
  "telephone": TEL, "email": "info@goeldentalcare.com", "foundingDate": "2011-01-01",
  "address": {"@type": "PostalAddress", "streetAddress": "14/185, Main Shivalik Road", "addressLocality": "Malviya Nagar, New Delhi", "postalCode": "110017", "addressRegion": "Delhi", "addressCountry": "IN"},
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "09:30", "closes": "20:00"}],
  "areaServed": ["Malviya Nagar","Saket","Shivalik","Sheikh Sarai","Chhattarpur","Munirka","Vasant Kunj","Hauz Khas","South Delhi"],
  "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "708"}}]

ROUTES = {
 "pain": {"t": "Tooth pain", "u": 1, "lvl": "Same day if severe · Endodontist", "d": "Pain that wakes you, swelling or a bad taste usually means infection near the nerve. An exam and X-ray decide between a filling, a root canal or an extraction.", "go": "#root-canal"},
 "broken": {"t": "Broken or chipped tooth", "u": 1, "lvl": "Within 24–48 hours", "d": "Keep any fragment in milk and chew on the other side. Small chips are bonded the same day; bigger breaks may need a crown.", "go": "#emergency"},
 "gums": {"t": "Bleeding gums", "lvl": "Book this week · Periodontist", "d": "Bleeding when brushing is the most common early sign of gum disease. A cleaning and gum check come first.", "pick": "Cleaning / gums"},
 "wisdom": {"t": "Wisdom tooth pain", "lvl": "Within a few days · Oral surgeon", "d": "An OPG X-ray (on site) shows the tooth's position. Many are monitored; some need removal.", "pick": "Extraction / wisdom tooth"},
 "missing": {"t": "Missing tooth", "lvl": "Planned consultation", "d": "Implant, bridge or denture. Implant consultations are listed free on the clinic's 2026 fee list.", "go": "#implants", "pick": "Implants"},
 "crooked": {"t": "Crooked or gapped teeth", "lvl": "Planned consultation · Orthodontist", "d": "Braces or Invisalign clear aligners for teens and adults. A scan shows which suits you.", "pick": "Braces / aligners"},
 "stained": {"t": "Stained or yellow teeth", "lvl": "Planned consultation", "d": "Cleaning first, then whitening, bonding or veneers. See the cosmetic site for real cases.", "pick": "Cosmetic / whitening"},
 "child": {"t": "My child", "lvl": "Book this week", "d": "Separate children's room, fluoride, sealants and laughing-gas sedation for anxious kids.", "pick": "Child's check-up"},
}

def page():
    P = []
    P.append(head("Goel Dental | Dentist in Malviya Nagar, South Delhi",
        "Goel Dental, Main Shivalik Road, Malviya Nagar. Root canals, implants, braces and Invisalign, kids' dentistry and emergencies. 4.8★ from 708 Google reviews. Fees published.",
        "https://www.goeldentalcare.com/", TOK, FONTS, SCHEMA))
    P.append(f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="preview"><b>Preview build for Dr Goel.</b> Orange badges mark details still to be confirmed. Photos are from goeldentalcare.com and delhidentalsmiles.com.</div>
<header class="hd"><div class="wrap">
<a class="logo" href="#top">Goel Dental <small>Malviya Nagar</small></a>
<nav class="nav" aria-label="Main"><a href="#treatments">Treatments</a><a href="#emergency">Emergency</a><a href="#fees">Fees</a><a href="#doctors">Doctors</a><a href="#clinic">Clinic</a><a href="#visit">Visit</a><a href="tel:{TEL}" data-cta="header">{PHONE_DISPLAY}</a></nav>
<a class="btn sm accent hd-cta" href="#book" data-book data-cta="header">Book</a>
<button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
</div><nav class="drawer" id="drawer" aria-label="Mobile"><a href="#treatments">Treatments</a><a href="#emergency">Emergency</a><a href="#fees">Fees</a><a href="#doctors">Doctors</a><a href="#clinic">Clinic tour</a><a href="#visit">Visit us</a><a href="#book">Book appointment</a></nav></header>
<main id="main">
<section class="hero" id="top" aria-labelledby="h1">{pic('clinic-front','Reception and treatment area at Goel Dental, Malviya Nagar', eager=True)}
<div class="wrap">
<p class="eyebrow">Dental clinic · Main Shivalik Road, Malviya Nagar</p>
<h1 id="h1">Dentist in Malviya Nagar. Six specialists, one clinic.</h1>
<p class="lead">Root canals under a microscope, implants, braces and Invisalign, gum and children's care. The right specialist plans your treatment, and the fee is in writing before anything starts.</p>
<div class="btns"><a class="btn accent" href="#book" data-book data-cta="hero">Book appointment</a><a class="btn ghost" href="tel:{TEL}" data-cta="hero">{ICON['phone']} {PHONE_DISPLAY}</a><a class="btn wa" href="#" data-wa data-cta="hero">{ICON['wa']} WhatsApp</a></div>
<div class="stats"><div><b>4.8★</b><span>708 Google reviews</span></div><div><b>2011</b><span>On Main Shivalik Road</span></div><div><b>6</b><span>Dentists &amp; specialists</span></div><div><b>₹0</b><span>Implant consultation</span></div></div>
</div></section>

<section class="section alt" aria-labelledby="router-h" data-router><div class="wrap">
<div class="head"><div><p class="eyebrow">Start here</p><h2 id="router-h">What brings you in?</h2><p class="lead" style="margin:12px 0 0">Pick the closest match. You'll see how soon to come, who you'll see, and the next step.</p></div></div>
<div class="chips" role="group" aria-label="Choose a symptom">{''.join(f'<button class="chip" type="button" aria-pressed="false" data-r="{k}">{v["t"]}</button>' for k,v in ROUTES.items())}</div>
<div class="router-out" aria-live="polite" hidden></div>
</div></section>

<section class="section" id="treatments" aria-labelledby="tx-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Treatments</p><h2 id="tx-h">Everyday care and planned treatment.</h2></div><a class="btn ghost sm" href="delhi-dental-smiles.html">Cosmetic &amp; smile makeovers →</a></div>
<div class="mosaic">
<a class="t2" href="#root-canal" data-treatment="Root canal treatment">{pic('micro-rct','Dental operating microscope used for root canal treatment')}<span><b>Root canal treatment</b><i>Single-sitting · microscope-assisted</i></span></a>
<a class="w2" href="#implants" data-treatment="Dental implants">{pic('implant-caption','Dental implant model showing the implant, abutment and crown')}<span><b>Dental implants</b><i>Free consultation · CBCT planning</i></span></a>
<a href="#emergency">{pic('rct-model','Model of a tooth showing the root canals')}<span><b>Toothache &amp; emergencies</b><i>Call first</i></span></a>
<a href="#book" data-pick="Braces / aligners">{pic('aligner','Invisalign clear aligner in its case at Goel Dental')}<span><b>Invisalign &amp; braces</b><i>Two orthodontists</i></span></a>
<a href="#book" data-pick="Cleaning / gums">{pic('cleaning','Scaling and polishing')}<span><b>Cleaning &amp; gums</b><i>EMS Airflow cleaning</i></span></a>
<a class="t2" href="#book" data-pick="Child's check-up">{pic('kids','Child smiling during a dental check-up')}<span><b>Children's dentistry</b><i>Separate kids' room</i></span></a>
<a href="#book" data-pick="Extraction / wisdom tooth">{pic('opg','OPG full-mouth X-ray machine in the clinic imaging corner')}<span><b>Wisdom teeth &amp; extractions</b><i>OPG on site</i></span></a>
<a class="w2" href="delhi-dental-smiles.html">{pic('zoom','Philips Zoom whitening lamp with before and after shade comparison')}<span><b>Whitening, veneers, smile design</b><i>On the Delhi Dental Smiles site</i></span></a>
</div></div></section>

<section class="section alt" id="emergency" aria-labelledby="em-h"><div class="wrap split">
<div class="urgent"><p class="eyebrow">Dental emergency</p><h2 id="em-h" style="font-size:clamp(28px,3vw,40px)">In pain now? Call before you come.</h2>
<ul class="ticks"><li>Severe toothache or pain that wakes you</li><li>Swelling of the gum or face</li><li>Broken, cracked or knocked-out tooth</li><li>Bleeding that won't stop after an extraction</li></ul>
<p class="small">Swelling spreading to the eye or neck, fever, or trouble breathing or swallowing: go to a hospital emergency department now.</p>
<div class="btns"><a class="btn urgent" href="tel:{TEL}" data-cta="emergency">{ICON['phone']} Call {PHONE_DISPLAY}</a><a class="btn wa" href="#" data-wa data-cta="emergency" data-t="Emergency">{ICON['wa']} WhatsApp a photo</a></div></div>
<div><h3>First aid while you travel</h3>
<div class="faq"><details><summary>Knocked-out adult tooth</summary><div class="a">Hold it by the crown, not the root. Rinse briefly in milk. Put it back in the socket if you can, or keep it in milk, and come in straight away. The first hour matters most.</div></details>
<details><summary>Broken or chipped tooth</summary><div class="a">Rinse with warm water, keep any piece in milk, use a cold compress on the cheek, and avoid chewing on that side.</div></details>
<details><summary>Severe toothache</summary><div class="a">Rinse with warm salt water, floss gently to remove trapped food, and take ordinary pain relief as directed on the pack. Don't put aspirin on the gum.</div></details>
<details><summary>Bleeding after an extraction</summary><div class="a">Bite firmly on folded gauze for 30 minutes without checking. Sit upright and avoid rinsing or hot drinks. Call if it doesn't settle.</div></details></div>
<p class="small muted" style="margin-top:16px">Open hours: Mon–Sat 9:30 am–8 pm on most listings; Delhi Dental Smiles says "Open on Saturday &amp; Sunday". {flag('Confirm Sunday')}</p></div>
</div></section>

<section class="section" id="root-canal" data-treatment="Root canal treatment" aria-labelledby="rct-h"><div class="wrap split">
<div class="photo" style="aspect-ratio:1/1">{pic('dr-shikha-reception','Dr Shikha Goel, endodontist, at the Goel Dental reception')}</div>
<div><p class="eyebrow">Root canal treatment</p><h2 id="rct-h">Save the tooth. Often in one sitting.</h2>
<p class="lead">Done by Dr Shikha Goel, MDS in Conservative Dentistry &amp; Endodontics, with an operating microscope (4–25× magnification), rotary files, an apex locator and digital X-ray in the room.</p>
<ul class="ticks"><li>Single-sitting root canals when the tooth allows</li><li>Microscope-assisted for molars, re-treatments and cracked teeth</li><li>Same-day CAD/CAM crown available, so the tooth is finished in one visit</li><li>Local anaesthetic; laughing gas for anxious patients</li></ul>
<div class="btns"><a class="btn" href="#book" data-book data-pick="Root canal" data-cta="rct">Book a root canal consultation</a><a class="btn ghost" href="#fees">See root canal fees</a></div></div>
</div></section>

<section class="section dark" id="implants" data-treatment="Dental implants" aria-labelledby="imp-h"><div class="wrap split r">
<div class="photo" style="aspect-ratio:4/5;max-height:640px">{pic('dr-shikha-implant','Dr Shikha Goel, implantologist, in the clinic')}</div>
<div><p class="eyebrow">Dental implants</p><h2 id="imp-h">Replace a missing tooth with a fixed one.</h2>
<p class="lead">Free implant consultation with a CBCT 3D scan for planning. You choose the implant system; the fee for each is published.</p>
<div class="tw" style="margin:22px 0;border-color:rgba(255,255,255,.18)"><table class="tbl" style="background:transparent;color:var(--on-night)"><thead><tr><th style="background:rgba(255,255,255,.06);color:var(--on-night-mute)">Implant system</th><th style="background:rgba(255,255,255,.06);color:var(--on-night-mute)">Per implant</th></tr></thead><tbody>
<tr><td>Adin / Alpha Bio</td><td class="n">₹17,000</td></tr><tr><td>Osstem</td><td class="n">₹35,000</td></tr><tr><td>Nobel Biocare</td><td class="n">₹40,000–45,000</td></tr><tr><td>Straumann</td><td class="n">₹55,000</td></tr><tr><td>All-on-4 (full arch)</td><td class="n">₹90,000–1,00,000</td></tr></tbody></table></div>
<p class="small">Crown on the implant is separate (₹8,500 PFM to ₹17,000 same-day CAD/CAM). Source: clinic's published 2026 fee list. {flag('Confirm before ads quote it')}</p>
<div class="btns"><a class="btn accent" href="#book" data-book data-pick="Implants" data-cta="implants">Book free implant consultation</a><a class="btn wa" href="#" data-wa data-t="Dental implants" data-cta="implants">{ICON['wa']} Ask on WhatsApp</a></div></div>
</div></section>

<section class="section" id="fees" aria-labelledby="fee-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Fees</p><h2 id="fee-h">Prices, published before you visit.</h2><p class="lead" style="margin:12px 0 0">No surprises at the counter. These are the clinic's published fees; your exact fee comes in writing after the exam.</p></div></div>
<div class="grid g2">
<div class="tw"><table class="tbl"><thead><tr><th>Consultation &amp; general</th><th>Fee</th></tr></thead><tbody>
<tr><td>Implant / cosmetic consultation</td><td class="n">₹0</td></tr><tr><td>General consultation</td><td class="n">₹500</td></tr><tr><td>X-ray, 1–3 teeth / full mouth (OPG)</td><td class="n">₹150 / ₹500</td></tr><tr><td>CBCT scan</td><td class="n">₹2,500–4,500</td></tr><tr><td>Scaling &amp; polishing</td><td class="n">₹2,500</td></tr><tr><td>Tooth filling</td><td class="n">from ₹800</td></tr></tbody></table></div>
<div class="tw"><table class="tbl"><thead><tr><th>Root canal &amp; crowns</th><th>Fee</th></tr></thead><tbody>
<tr><td>Root canal: front / premolar / molar</td><td class="n">₹4,500 / 5,500 / 6,500</td></tr><tr><td>Single-sitting root canal</td><td class="n">₹7,500</td></tr><tr><td>Microscopic root canal</td><td class="n">₹8,500</td></tr><tr><td>Metal-ceramic crown</td><td class="n">₹6,500</td></tr><tr><td>Metal-free zirconia crown</td><td class="n">₹8,000</td></tr><tr><td>Same-day CAD/CAM crown</td><td class="n">₹12,000–14,000</td></tr></tbody></table></div>
</div>
<p class="small muted" style="margin-top:14px">From the clinic's published 2026 price list. Final fee is confirmed in writing after the exam. EMI on leading credit cards. {flag('Clinic to confirm all fees')}</p>
</div></section>

<section class="section alt" id="doctors" aria-labelledby="doc-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Clinical team</p><h2 id="doc-h">The dentists you'll meet.</h2></div><span>{flag('Confirm current team')}</span></div>
<div class="grid g4">
<article class="doc"><div class="photo">{pic('dr-shikha-portrait','Dr Shikha Goel')}</div><p class="role">Director · Endodontist &amp; cosmetic dentist</p><h3>Dr Shikha Goel</h3><p class="cred">MDS, Conservative Dentistry &amp; Endodontics, Bapuji Dental College (2010). Former Research Officer, AIIMS. Registered with the Delhi Dental Council.</p></article>
<article class="doc"><div class="photo">{pic('dr-kohli','Dr Sanchaita Kohli')}</div><p class="role">Oral &amp; maxillofacial surgeon</p><h3>Dr Sanchaita Kohli</h3><p class="cred">MDS. 13+ years at Maulana Azad Institute of Dental Sciences. ATLS provider; AOCMF trauma certified.</p></article>
<article class="doc"><div class="photo">{pic('dr-nisheet','Dr Nisheet Sharma')}</div><p class="role">Orthodontist</p><h3>Dr Nisheet Sharma</h3><p class="cred">MDS Orthodontics, IDST Muradnagar. Complex alignment, relapse cases, invisible and lingual braces.</p></article>
<article class="doc"><div class="photo">{pic('dr-akansha','Dr Akansha Uniyal')}</div><p class="role">In-house dentist</p><h3>Dr Akansha Uniyal</h3><p class="cred">BDS, MDS Oral Pathology, Maulana Azad Dental College, New Delhi.</p></article>
</div>
<div class="grid g2" style="margin-top:28px">
<div class="card"><p class="role eyebrow" style="margin:0">Periodontist · gum specialist</p><h3 style="margin:0">Dr Ambica Sharma</h3><p class="small muted" style="margin:0">MDS, Govt Dental College Ahmedabad (2011); 3 years Senior Resident, AIIMS. {flag('Photo needed')}</p></div>
<div class="card"><p class="role eyebrow" style="margin:0">Orthodontist</p><h3 style="margin:0">Dr Parag Gupta</h3><p class="small muted" style="margin:0">Trained at I.T.S-CDSR Muradnagar; member, Indian Orthodontic Society. {flag('Photo needed')}</p></div>
</div></div></section>

<section class="section" aria-labelledby="cases-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Real cases</p><h2 id="cases-h">Results from this clinic.</h2><p class="lead" style="margin:12px 0 0">Drag to compare. Cases as published on the clinic's own websites. Results vary between patients.</p></div><span>{flag('Confirm patient consent')}</span></div>
<div class="grid g3">
<figure style="margin:0">{ba('ems-gbt-case-1-pre','ems-gbt-case-1-post','Heavy deposits on teeth before cleaning','Teeth after EMS Airflow cleaning')}<figcaption class="cap">EMS Airflow cleaning: heavy deposits removed in one visit.</figcaption></figure>
<figure style="margin:0">{ba('invisalign-case-3-pre','invisalign-case-3-post','Wide gaps between front teeth before treatment','Gaps closed after Invisalign')}<figcaption class="cap">Invisalign: wide front-teeth gaps closed.</figcaption></figure>
<figure style="margin:0">{ba('veneer-case-2-pre','veneer-case-2-post','Uneven front teeth before treatment','Front teeth after E.max veneers')}<figcaption class="cap">E.max veneers on uneven front teeth.</figcaption></figure>
</div></div></section>

<section class="section alt" id="clinic" aria-labelledby="clinic-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Clinic tour</p><h2 id="clinic-h">Inside Goel Dental, Malviya Nagar.</h2></div></div>
<div class="mosaic">
<a class="w2 t2" href="#visit">{pic('operatory','Treatment operatories with dental chairs')}<span><b>Operatories</b><i>Separate rooms, natural light</i></span></a>
<a href="#visit">{pic('entrance','Clinic entrance corridor')}<span><b>Entrance</b></span></a>
<a href="#visit">{pic('waiting','Reception and waiting area')}<span><b>Waiting lounge</b></span></a>
<a class="w2" href="#visit">{pic('digital-zone','Digital dentistry zone with scanner and milling unit')}<span><b>Digital dentistry zone</b><i>Scan, design, mill on site</i></span></a>
<a href="#visit">{pic('opg','OPG machine')}<span><b>Imaging corner</b><i>OPG and CBCT</i></span></a>
<a href="#visit">{pic('steril','Sterilisation room')}<span><b>Sterilisation room</b></span></a>
<a class="w2" href="#visit">{pic('consult-room','Consultation room')}<span><b>Consultation room</b><i>Plans and fees explained here</i></span></a>
</div></div></section>

<section class="section" aria-labelledby="rv-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">Patient reviews</p><h2 id="rv-h">4.8 on Google, from 708 reviews.</h2></div><a class="btn ghost sm" href="{MAPS}" data-cta="reviews">Read them on Google</a></div>
<div class="grid g3">
<figure class="quote" style="margin:0"><blockquote>"I visited Dr Shikha Goel due to severe tooth pain. She explained the cause and treatment in detail. I got one wisdom tooth removed and one root canal done… I got a single-day crown also in 1 hour, which saved me a visit."</blockquote><figcaption>Rekha Uniyal · Root canal &amp; extraction</figcaption></figure>
<figure class="quote" style="margin:0"><blockquote>"I went for an RCT. Full treatment was done in a single sitting, and even the crown was delivered the same day. Dr Shikha involved me in designing my crown."</blockquote><figcaption>Sandeep Goyal · Single-sitting RCT</figcaption></figure>
<figure class="quote" style="margin:0"><blockquote>"My son is currently undergoing treatment for teeth alignment with Dr Shikha Goel… I've also had my own teeth cleaned by her, and the experience was wonderful."</blockquote><figcaption>Richa Hora · Kids' orthodontics &amp; cleaning</figcaption></figure>
</div>
<p class="small muted" style="margin-top:14px">Testimonials as published on delhidentalsmiles.com, shortened. Production pulls reviews live from the Google Business Profile. {flag('Confirm source & consent')}</p>
</div></section>

<section class="section alt" aria-labelledby="how-h"><div class="wrap">
<div class="head"><div><p class="eyebrow">How a visit works</p><h2 id="how-h">From first message to follow-up.</h2></div></div>
<ol class="steps"><li><h3>Tell us the problem</h3><p>Call, WhatsApp or book here. Name and mobile is enough.</p></li><li><h3>We confirm a time</h3><p>The front desk calls back and books the right specialist.</p></li><li><h3>Exam and written plan</h3><p>X-ray if needed. Options and fees in writing.</p></li><li><h3>Treatment</h3><p>Only after you agree. Local anaesthetic; sedation if needed.</p></li><li><h3>Aftercare</h3><p>Written aftercare and a review visit.</p></li></ol>
</div></section>

<section class="section" aria-labelledby="faq-h"><div class="wrap split" style="align-items:start">
<div><p class="eyebrow">Questions</p><h2 id="faq-h">Before you book.</h2><p class="lead">Still unsure? <a href="#" data-wa data-cta="faq">Ask on WhatsApp</a>.</p></div>
<div class="faq">
<details><summary>How much does a root canal cost?</summary><div class="a">From ₹4,500 for a front tooth to ₹6,500 for a molar; ₹7,500 single-sitting; ₹8,500 microscopic. A crown is usually advised for back teeth. You get the exact fee after the exam.</div></details>
<details><summary>Is the implant consultation really free?</summary><div class="a">Yes, per the clinic's published 2026 fee list. A CBCT scan, if needed for planning, is ₹2,500–4,500.</div></details>
<details><summary>Can I be seen the same day for tooth pain?</summary><div class="a">Call first. Urgent cases are fitted in the same day whenever the schedule allows.</div></details>
<details><summary>Do you treat children?</summary><div class="a">Yes, in a separate children's room, with fluoride, sealants, kids' root canals and laughing-gas sedation for anxious children.</div></details>
<details><summary>Do you offer EMI?</summary><div class="a">Yes, on leading credit cards. Ask the front desk which cards and tenures apply.</div></details>
<details><summary>How do I get there by metro?</summary><div class="a">Malviya Nagar station (Yellow Line), Gate 1, then about 10 minutes' walk on Main Shivalik Road, next to Sunil Hospital.</div></details>
</div></div></section>

<section class="section alt" id="book" aria-labelledby="book-h"><div class="wrap split" style="align-items:start">
<div><p class="eyebrow">Book appointment</p><h2 id="book-h">Book in under a minute.</h2><p class="lead">No payment to book. The front desk confirms the time and the right dentist.</p>
<ul class="ticks"><li>Call-back within 30 minutes in clinic hours {flag('Confirm SLA')}</li><li>Fee confirmed in writing before treatment</li><li>Your reference number links this request to your visit</li></ul>
<p>Prefer to talk? <a href="tel:{TEL}" data-cta="book_section">{PHONE_DISPLAY}</a></p></div>
{book_form(["Tooth pain / check-up","Root canal","Implants","Braces / aligners","Cleaning / gums","Extraction / wisdom tooth","Child's check-up","Cosmetic / whitening"])}
</div></section>

<section class="section" id="visit" aria-labelledby="visit-h"><div class="wrap split">
<div><p class="eyebrow">Visit us</p><h2 id="visit-h">On Main Shivalik Road, Malviya Nagar.</h2>
<p class="lead" style="margin-bottom:10px">Goel Dental<br>14/185, Ground Floor {flag('Ground vs Lower Ground')}<br>Main Shivalik Road, Malviya Nagar<br>New Delhi 110017</p>
<p class="muted">Next to Sunil Hospital, near the Liberty showroom. 10 minutes from Malviya Nagar metro, Gate 1. Patients come from Shivalik, Saket, Sheikh Sarai, Chhattarpur, Munirka, Vasant Kunj and Hauz Khas.</p>
<p><b>Mon–Sat, 9:30 am – 8:00 pm</b> {flag('Confirm hours & Sunday')}</p>
<div class="btns"><a class="btn" href="{MAPS}" rel="noopener" data-cta="visit">Get directions</a><a class="btn ghost" href="tel:{TEL}" data-cta="visit">{ICON['phone']} Call</a></div></div>
<div class="photo" style="aspect-ratio:4/3">{pic('happy-patient','Patient and dentist at Goel Dental')}</div>
</div></section>
</main>
<footer class="ft"><div class="wrap">
<div class="ft-grid">
<div><p class="logo" style="font-size:26px">Goel Dental</p><p class="nap">14/185, Main Shivalik Road, Malviya Nagar, New Delhi 110017<br><a href="tel:{TEL}" data-cta="footer">{PHONE_DISPLAY}</a> · info@goeldentalcare.com</p></div>
<div><h2>General</h2><ul><li><a href="#root-canal">Root canal treatment</a></li><li><a href="#emergency">Dental emergency</a></li><li><a href="#book">Cleaning &amp; gums</a></li><li><a href="#book">Wisdom teeth</a></li><li><a href="#book">Kids dentistry</a></li></ul></div>
<div><h2>Planned treatment</h2><ul><li><a href="#implants">Dental implants</a></li><li><a href="#book">Invisalign &amp; braces</a></li><li><a href="delhi-dental-smiles.html">Veneers &amp; smile design</a></li><li><a href="#fees">Fees</a></li></ul></div>
<div><h2>Prototype</h2><ul><li><a href="index.html">Project hub</a></li><li><a href="strategy-and-google-ads.html">Strategy &amp; Google Ads review</a></li><li><a href="delhi-dental-smiles.html">Delhi Dental Smiles site</a></li></ul></div>
</div>
<div class="ft-base"><span>© 2026 Goel Dental. Preview build prepared by Daniel Deepak; not the live site.</span><button type="button" data-tlog>Show tracking events</button></div>
</div></footer>
{mbar()}
<script>window.GD_ROUTES={json.dumps(ROUTES)};</script>
<script>{tracking_js('goel_dental_care')}</script>
</body></html>""")
    return "".join(P)

if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "goel-dental-care.html"
    open(out, "w").write(page()); print("ok", out)
