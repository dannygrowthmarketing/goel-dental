from shared import *

TOK = ("--ink:#13201F;--ink-2:#2B3836;--mute:#56625F;--line:rgba(19,32,31,.13);--line-2:rgba(19,32,31,.26);"
       "--paper:#FAF8F4;--ivory:#F1EEE7;--sand:#E3DED3;--white:#fff;--accent:#E8792B;--accent-dark:#B85A17;--accent-text:#9A4A10;"
       "--accent-soft:rgba(232,121,43,.12);--on-accent:#1A0E04;--night:#0F1918;--on-night:#F4F1EA;--on-night-mute:#B9C2BE;"
       "--display:'Fraunces',Georgia,serif;--sans:'Inter','Helvetica Neue',Arial,sans-serif;--gut:clamp(16px,4vw,48px);"
       "--maxw:1180px;--read:70ch;--r:2px;--shadow:none;color-scheme:light;--hero-op:.35;--hero-grad:linear-gradient(90deg,rgba(15,25,24,.95),rgba(15,25,24,.7))")
FONTS = "family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600"

EXTRA = """
.num{font:500 clamp(54px,7vw,104px)/.9 var(--display);letter-spacing:-.03em;color:var(--ink)}
.sec-no{font:500 clamp(64px,9vw,128px)/.8 var(--display);color:var(--accent);opacity:.9}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:28px}
.kpis div{border-top:2px solid var(--ink);padding-top:14px;display:grid;gap:8px}
.kpis b{font:500 clamp(34px,4vw,52px)/1 var(--display);letter-spacing:-.02em}
.kpis span{font-size:14px;color:var(--mute)}
.bars{display:grid;gap:10px}
.bar{display:grid;grid-template-columns:minmax(120px,240px) 1fr auto;gap:14px;align-items:center;font-size:14.5px}
.bar i{display:block;height:18px;background:var(--ink)}
.bar i.good{background:#1F6B4C}.bar i.bad{background:#A8361F}.bar i.acc{background:var(--accent)}
.bar em{font-style:normal;font-variant-numeric:tabular-nums;font-weight:600;white-space:nowrap}
.bar .lab{min-width:0}
@media(max-width:640px){.bar{grid-template-columns:1fr auto}.bar .track{grid-column:1/-1;order:3}}
.alert{border-left:4px solid #A8361F;background:#FBEDE8;padding:22px 26px}
.ok{border-left:4px solid #1F6B4C;background:#E8F2EC;padding:22px 26px}
.tag{display:inline-block;font:600 10.5px var(--sans);letter-spacing:.12em;text-transform:uppercase;padding:4px 8px;border-radius:2px}
.tag.v{background:#E8F2EC;color:#1F6B4C}.tag.a{background:var(--accent-soft);color:var(--accent-text)}.tag.r{background:#FBEDE8;color:#A8361F}
"""

def bars(rows, maxv, fmt, cls=""):
    out = []
    for lab, v, extra, c in rows:
        w = max(1.5, 100 * v / maxv)
        out.append(f'<div class="bar"><span class="lab">{lab}</span><span class="track"><i class="{c or cls}" style="width:{w:.1f}%"></i></span><em>{fmt(v)}{extra}</em></div>')
    return '<div class="bars">' + "".join(out) + "</div>"

inr = lambda v: "₹" + (f"{v/1e5:.2f}L" if v >= 1e5 else f"{v:,.0f}")

def page():
    camp = [("General Dentistry MN", 1089590, " · 341 conv", ""), ("General Dentist Near Me", 577526, " · 129 conv", ""), ("General Dentistry – Weekend MN", 422689, " · 113 conv", ""),
            ("Root Canal Treatment", 190833, " · 41 conv", ""), ("General Dentistry KB (Karol Bagh)", 108134, " · 35 conv", ""), ("Dental Veneers – Apr 2023", 37783, " · 0 conv", "bad"),
            ("Dental Implants", 18357, " · 1 conv", "bad"), ("CGHS Dental – Kalkaji", 9714, " · 1 conv", ""), ("Wisdom teeth", 6013, " · 6 conv", "good"), ("5 others", 6266, " · 0 conv", "")]
    cpc_good = [("goel dental (brand search)", 548, " · 3.0% CVR", "good"), ("fix my teeth near me", 676, "", "good"), ("dentist near me with fees", 885, " · 3.1% CVR", "good"),
                ("dentist in malviya nagar (search term)", 960, " · 2.9% CVR", "good"), ("\"dentist in malviya nagar\" (phrase)", 1334, " · 2.1% CVR", "good"),
                ("teeth cleaning price delhi", 1220, "", "good"), ("dental implants new delhi", 1445, "", "good"), ("dental treatment in delhi", 2149, " · 84 conv", "")]
    cpc_bad = [("\"dentist south delhi\"", 20430, "", "bad"), ("[root canal treatment] exact", 20095, "", "bad"), ("Dental Implants campaign", 18357, " · ads disapproved", "bad"),
               ("\"dental clinic in\" (phrase)", 7912, "", "bad"), ("dentist near me (broad)", 6516, "", "bad"), ("\"dentist in south delhi\" (broad)", 6216, "", "bad"),
               ("Veneers campaign: ₹37,783 spent", 37783, " · 0 conv", "bad")]
    return head("Goel Dental: Strategy & Google Ads Review", "Google Ads history, keyword evidence, competitor research and the page plan for goeldentalcare.com and delhidentalsmiles.com.",
                "https://dannygrowthmarketing.github.io/goel-dental/strategy-and-google-ads.html", TOK, FONTS, []).replace("</style>", EXTRA + "</style>") + f"""<body>
<div class="preview"><b>Prepared for Dr Saurabh Goel</b> · Daniel Deepak · 9 November 2026 · Read-only review; nothing in the ad account was changed.</div>
<header class="hd"><div class="wrap"><a class="logo" href="#top">Goel Dental <small>Strategy &amp; Ads review</small></a>
<nav class="nav" aria-label="Sections"><a href="#s1">Ads history</a><a href="#s2">Keywords</a><a href="#s3">Page plan</a><a href="#s4">Competitors</a><a href="#s5">Two sites</a><a href="#s6">Tracking</a></nav>
<a class="btn sm accent hd-cta" href="index.html">Project hub</a></div></header>
<main id="main">
<section class="hero" id="top" aria-labelledby="h1">{pic('operatory','Goel Dental operatories', eager=True)}<div class="wrap">
<p class="eyebrow">Google Ads · Keywords · Competitors · Website plan</p>
<h1 id="h1">₹24.9 lakh spent on Google Ads. No way to tell which patients it bought.</h1>
<p class="lead">Ten years of account history, read in full. The spend found real demand. What failed was measurement: none of the 19 conversion actions is recording today, and the ads have been off since the balance went overdue.</p>
<div class="stats"><div><b>₹24.88L</b><span>All-time spend, Dec 2015 – Nov 2026</span></div><div><b>82,947</b><span>Clicks</span></div><div><b>677</b><span>"Conversions" (unverified)</span></div><div><b>0 / 19</b><span>Conversion actions recording</span></div></div>
</div></section>

<section class="section" id="s1" aria-labelledby="s1h"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:40px"><div><span class="sec-no">01</span><h2 id="s1h">The account, all time.</h2></div><p class="lead">Data read from the Goel Dental Google Ads account (598-498-3497) on 9 Nov 2026. <span class="tag v">Verified</span></p></div>
<div class="kpis"><div><b>₹29.99</b><span>Average cost per click</span></div><div><b>7.21%</b><span>Click-through rate. Strong for dental.</span></div><div><b>0.82%</b><span>Click to "conversion" rate</span></div><div><b>₹3,672</b><span>Cost per "conversion"</span></div></div>
<div class="grid g2" style="margin-top:56px;align-items:start">
<div><h3>Spend by campaign</h3>{bars(camp, 1089590, inr)}<p class="small muted" style="margin-top:12px">Three "General Dentistry" campaigns took 85% of all spend. Treatment campaigns (implants, veneers, root canal) got 10%.</p></div>
<div class="grid" style="gap:18px">
<div class="alert"><h3 style="margin-top:0">Status today</h3><ul class="ticks" style="margin:0"><li>All campaigns paused. "Make a payment to restart your ads": ₹29,296.99 overdue.</li><li>Conversion tracking: 4 tags inactive, 15 actions with no recent conversions, 0 recording.</li><li>Goals marked "Misconfigured": Submit lead form, Store visit, Download.</li><li>21 "Page views" counted as results. Page views are not patients.</li><li>Ads disapproved in 3 campaigns (Dental Implants: all ads).</li><li>Live ad copy uses "Painless Procedures" and "Sunday Open". Both need checking against policy and real hours.</li></ul></div>
<div class="card"><h3 style="margin:0">What "677 conversions" means</h3><p class="small muted" style="margin:0">They mix calls from ads, form fills, page views and other actions, with no link to booked or treated patients. Use them as a rough intent signal only. The ₹1.5 lakh figure from our call is likely a recent period; a spend-by-year split is the first thing to pull in week 1. <span class="tag a">To confirm</span></p></div>
</div></div>
</div></section>

<section class="section alt" id="s2" aria-labelledby="s2h"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:40px"><div><span class="sec-no">02</span><h2 id="s2h">What the keywords say.</h2></div><p class="lead">Cost per conversion by keyword and search term, all time. Green paid back best; red burned budget.</p></div>
<div class="grid g2" style="align-items:start">
<div><h3>Cheapest results</h3>{bars(cpc_good, 2149, inr)}</div>
<div><h3>Most expensive</h3>{bars(cpc_bad, 37783, inr)}</div>
</div>
<div class="grid g3" style="margin-top:56px">
<div class="card"><span class="tag v">Finding</span><h3 style="margin:0">Local beats "Delhi"</h3><p class="small muted" style="margin:0">"dentist in malviya nagar" converted at 2–3% for ₹960–1,334. "dentist south delhi" cost ₹20,430 per conversion. The catchment is real and narrow.</p></div>
<div class="card"><span class="tag v">Finding</span><h3 style="margin:0">People want prices</h3><p class="small muted" style="margin:0">"dentist near me with fees", "teeth cleaning price delhi", "tooth cap price", "implant cost in delhi" are recurring searches with high CTR. Both new sites publish fees.</p></div>
<div class="card"><span class="tag v">Finding</span><h3 style="margin:0">Premium never had a page</h3><p class="small muted" style="margin:0">Implant searches clicked at 21–31% CTR but implant ads were disapproved and veneer traffic (₹37,783) produced zero conversions with no dedicated landing page.</p></div>
<div class="card"><span class="tag v">Finding</span><h3 style="margin:0">Areas that searched</h3><p class="small muted" style="margin:0">Saket, Chhattarpur, Munirka, Vasant Kunj, Kalkaji and Karol Bagh all appear in search terms. Karol Bagh is ~15 km away; its campaign had most ads disapproved.</p></div>
<div class="card"><span class="tag v">Finding</span><h3 style="margin:0">Brand is cheap</h3><p class="small muted" style="margin:0">"goel dental", "goel dental clinic malviya nagar": ₹548–2,060 per conversion. A small brand campaign protects it from competitors.</p></div>
<div class="card"><span class="tag v">Finding</span><h3 style="margin:0">Quality Score drag</h3><p class="small muted" style="margin:0">Near-me exact and root canal keywords show "Rarely shown (low Quality Score)" and below first-page bid. Better landing pages lower the price per click.</p></div>
</div>
</div></section>

<section class="section" id="s3" aria-labelledby="s3h"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:40px"><div><span class="sec-no">03</span><h2 id="s3h">Searches mapped to pages.</h2></div><p class="lead">Each page exists because people searched for it and paid clicks proved intent. Built sections are live in the two prototypes.</p></div>
<div class="tw"><table class="tbl"><thead><tr><th>Search cluster (from the account)</th><th>Evidence</th><th>Page / section</th><th>Site</th><th>Status</th></tr></thead><tbody>
<tr><td>dentist / dental clinic in malviya nagar, near me</td><td>Best local CPA, ₹960–1,334</td><td>Homepage hero + visit section</td><td>Goel Dental Care</td><td><span class="tag v">Built</span></td></tr>
<tr><td>dentist near me with fees / prices, cleaning price, tooth cap price</td><td>3.1% CVR</td><td>Fees section → /fees/ page</td><td>Both</td><td><span class="tag v">Built</span></td></tr>
<tr><td>toothache, dental pain, root canal treatment, rct near me</td><td>₹1.9L spent, QS low</td><td>Root canal section → /root-canal-treatment/</td><td>Goel Dental Care</td><td><span class="tag v">Built</span></td></tr>
<tr><td>dental implants new delhi, implant cost, single tooth implant cost</td><td>21–31% CTR</td><td>Implants + brand price table</td><td>Both</td><td><span class="tag v">Built</span></td></tr>
<tr><td>veneers cost, smile makeover, cosmetic dental</td><td>₹38k, 0 conv, no page</td><td>Smile journeys + veneers</td><td>Delhi Dental Smiles</td><td><span class="tag v">Built</span></td></tr>
<tr><td>invisalign cost in delhi</td><td>41.7% CTR, 1.3% CVR</td><td>Invisalign section + free scan</td><td>Delhi Dental Smiles</td><td><span class="tag v">Built</span></td></tr>
<tr><td>wisdom tooth removal / cost</td><td>₹976 per conversion</td><td>Wisdom teeth page</td><td>Goel Dental Care</td><td><span class="tag a">Next</span></td></tr>
<tr><td>dentist in saket / chhattarpur / munirka / vasant kunj</td><td>Recurring terms</td><td>Directions content (no doorway pages)</td><td>Goel Dental Care</td><td><span class="tag v">Built</span></td></tr>
<tr><td>cghs dental treatment</td><td>26.8% CTR, Kalkaji</td><td>CGHS page, only if Kalkaji is active</td><td>Goel Dental Care</td><td><span class="tag a">Confirm</span></td></tr>
<tr><td>kids dentist, child dental</td><td>15.9% CTR, small volume</td><td>Kids section</td><td>Goel Dental Care</td><td><span class="tag a">Next</span></td></tr>
</tbody></table></div>
<h3 style="margin-top:48px">Relaunch keyword structure</h3>
<div class="grid g3">
<div class="card"><span class="tag a">Search · Local core</span><p class="small" style="margin:0">[dentist in malviya nagar] · "dental clinic in malviya nagar" · "dentist near me" (5 km radius) · "dentist in saket" · "dentist near me with fees"</p></div>
<div class="card"><span class="tag a">Search · Root canal &amp; pain</span><p class="small" style="margin:0">"root canal treatment" · "root canal cost" · "toothache dentist" · "single sitting root canal" → root canal section, call extension during hours</p></div>
<div class="card"><span class="tag a">Search · Implants</span><p class="small" style="margin:0">"dental implants" · "implant cost" · "single tooth implant" · "straumann implant delhi" → implants page, 8 km radius</p></div>
<div class="card"><span class="tag a">Search · Cosmetic (DDS)</span><p class="small" style="margin:0">"veneers cost" · "smile makeover delhi" · "invisalign cost delhi" · "teeth whitening delhi" → Delhi Dental Smiles, wider South Delhi radius</p></div>
<div class="card"><span class="tag a">Search · Brand</span><p class="small" style="margin:0">goel dental · dr shikha goel · delhi dental smiles</p></div>
<div class="card"><span class="tag r">Negatives from day one</span><p class="small" style="margin:0">free · govt · hospital · college · course · jobs · aiims · karol bagh (unless branch active) · far suburbs · "dentist" alone on broad</p></div>
</div>
</div></section>

<section class="section alt" id="s4" aria-labelledby="s4h"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:40px"><div><span class="sec-no">04</span><h2 id="s4h">Competitors, checked the same way.</h2></div><p class="lead">Nine homepages loaded in a real browser on 9 Nov. Single load, so speed is indicative. <span class="tag v">Verified</span></p></div>
<div class="tw"><table class="tbl"><thead><tr><th>Clinic</th><th>Tier</th><th>Server response</th><th>WhatsApp</th><th>GTM / GA4 / Ads / Meta</th><th>Schema</th><th>Note</th></tr></thead><tbody>
<tr><td>Clove Dental, Saket</td><td>A</td><td class="n">2.1 s</td><td>Script</td><td>✓ / ✓ / ✓ / ✓</td><td>LocalBusiness</td><td>Chain claims, weekend hours</td></tr>
<tr><td>Smile Delhi</td><td>A</td><td class="n">0.8 s</td><td>✓</td><td>✓ / ✓ / ✓ / ✓</td><td>Dentist</td><td>Ranks for implants + Invisalign; cost &amp; case pages</td></tr>
<tr><td>Ark Dental, GK-1</td><td>A</td><td class="n">4.4 s</td><td>7 links</td><td>– / – / ✓ / ✓</td><td>Dentist, FAQ</td><td>Sticky "Book consult", before/after, brands named</td></tr>
<tr><td>Geetanjali Dental Options</td><td>B</td><td class="n">0.2 s</td><td>✓</td><td>– / ✓ / – / –</td><td>LocalBusiness</td><td>1,439 Google reviews; no lead form</td></tr>
<tr><td>Dr Shruti Dental</td><td>B</td><td class="n">2.2 s</td><td>4 links</td><td>– / – / ✓ / –</td><td>Dentist</td><td>Running Google Ads on "malviya nagar"</td></tr>
<tr><td>South Point Dentistry</td><td>B</td><td class="n">5.6 s</td><td>2 links</td><td>– / – / ✓ / –</td><td>Dentist</td><td>All images missing alt text</td></tr>
<tr><td>Dr Shilpa's</td><td>C</td><td class="n">5.3 s</td><td>✓</td><td>– / ✓ / – / –</td><td>–</td><td>No H1, no call links</td></tr>
<tr><td>Centre for Dental Implant</td><td>C</td><td class="n">10.6 s</td><td>Script</td><td>– / – / – / –</td><td>–</td><td>Very slow</td></tr>
<tr><td><b>goeldentalcare.com today</b></td><td>C</td><td class="n">4.0 s</td><td>None</td><td>– / ✓ / ✓ / –</td><td>–</td><td>136 scripts, 28/30 images no alt</td></tr>
</tbody></table></div>
<p class="small muted" style="margin-top:14px">Google review counts (audit, 6 Nov): Geetanjali 1,439 · Clove Saket 1,099 · Goel 708 · Shining Smiles 624. Nobody checked routes by symptom or ties WhatsApp chats to their ad source. Both prototypes do.</p>
</div></section>

<section class="section" id="s5" aria-labelledby="s5h"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:40px"><div><span class="sec-no">05</span><h2 id="s5h">Two sites, two jobs.</h2></div><p class="lead">Both run on one phone number, one CRM and one tracking setup, so every lead lands in the same place.</p></div>
<div class="grid g2">
<a class="card" href="goel-dental-care.html" style="text-decoration:none;padding:0;overflow:hidden"><div class="photo" style="aspect-ratio:16/9">{pic('clinic-front','Goel Dental Care prototype')}</div><div style="padding:24px 28px 28px;display:grid;gap:8px"><span class="tag a">goeldentalcare.com</span><h3 style="margin:0">Goel Dental Care</h3><p class="small muted" style="margin:0">Problem-led, 5–8 km radius. Pain, root canal, cleaning, wisdom teeth, implants, kids. Primary action: call or book.</p><b class="small">Open prototype →</b></div></a>
<a class="card" href="delhi-dental-smiles.html" style="text-decoration:none;padding:0;overflow:hidden"><div class="photo" style="aspect-ratio:16/9">{pic('hero-smile','Delhi Dental Smiles prototype')}</div><div style="padding:24px 28px 28px;display:grid;gap:8px"><span class="tag a">delhidentalsmiles.com</span><h3 style="margin:0">Delhi Dental Smiles</h3><p class="small muted" style="margin:0">Cosmetic, wider South Delhi. Veneers, Invisalign, Zoom, same-day crowns, real smile journeys. Primary action: free consultation.</p><b class="small">Open prototype →</b></div></a>
</div>
</div></section>

<section class="section dark" id="s6" aria-labelledby="s6h"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:40px"><div><span class="sec-no">06</span><h2 id="s6h">From click to revenue.</h2></div><p class="lead">Every stage gets a number. The prototypes already fire these events; open "Show tracking events" in either site's footer.</p></div>
<div class="tw" style="border-color:rgba(255,255,255,.16)"><table class="tbl" style="background:transparent;color:var(--on-night)"><thead><tr><th style="background:rgba(255,255,255,.06);color:var(--on-night-mute)">Stage</th><th style="background:rgba(255,255,255,.06);color:var(--on-night-mute)">Event / source</th><th style="background:rgba(255,255,255,.06);color:var(--on-night-mute)">Leak today</th></tr></thead><tbody>
<tr><td>Traffic</td><td>UTM + gclid/fbclid captured, first &amp; last touch</td><td>Untagged GBP clicks; Delhi-wide targeting</td></tr>
<tr><td>Landing</td><td>treatment_view</td><td>Generic homepage for treatment ads</td></tr>
<tr><td>Enquiry</td><td>click_call · click_whatsapp (with GD-XXXXX ref) · lead_generated</td><td>Two phone numbers; WhatsApp not tracked</td></tr>
<tr><td>Lead</td><td>CRM record: source, campaign, keyword, treatment</td><td>Enquiries not logged</td></tr>
<tr><td>Appointment → visit</td><td>CRM status Booked → Came</td><td>No follow-up or reminder</td></tr>
<tr><td>Treatment → revenue</td><td>CRM value in ₹ → offline conversion to Google Ads</td><td>Ads optimised on page views and form fills</td></tr>
</tbody></table></div>
</div></section>

<section class="section" id="s7" aria-labelledby="s7h"><div class="wrap">
<div class="split" style="align-items:end;margin-bottom:40px"><div><span class="sec-no">07</span><h2 id="s7h">Before ads restart.</h2></div><p class="lead">Restarting campaigns on today's tracking would repeat the last ten years. Fix first, then spend.</p></div>
<div class="grid g3">
<div class="card"><span class="tag r">Week 1</span><h3 style="margin:0">Clean the account</h3><p class="small muted" style="margin:0">Clear the overdue balance only when ready to relaunch. Remove page views as conversions; one primary conversion: qualified lead. Fix disapprovals and claims.</p></div>
<div class="card"><span class="tag r">Week 1–2</span><h3 style="margin:0">Install measurement</h3><p class="small muted" style="margin:0">GTM, GA4 key events, call tracking, WhatsApp ref codes, CRM. Test 20 enquiries end to end.</p></div>
<div class="card"><span class="tag a">Week 3–4</span><h3 style="margin:0">Relaunch narrow</h3><p class="small muted" style="margin:0">Local core + root canal + implants on the new pages, 5–8 km, during staffed hours. Cosmetic on DDS after.</p></div>
</div>
<h3 style="margin-top:48px">Needs Dr Goel's input</h3>
<div class="grid g2"><ul class="ticks"><li>Which phone number is primary; WhatsApp Business number</li><li>Floor (Ground vs Lower Ground) and real hours, incl. Sunday (DDS says open)</li><li>Founded 2010 or 2011</li><li>Which branches are active: Kalkaji (CGHS), Kirti Nagar, Kaushambi</li><li>Current team and photos for Dr Ambica Sharma, Dr Parag Gupta</li></ul>
<ul class="ticks"><li>Confirm every fee on the 2026 list before ads quote them</li><li>Consent for each before/after case and testimonial</li><li>Warranty wording, "painless", "best": DCI ethics and ad-policy review</li><li>Invisalign provider tier; CEREC and CBCT in-house</li><li>Spend by year for the ₹1.5L period discussed; who answers enquiries</li></ul></div>
</div></section>
</main>
<footer class="ft"><div class="wrap"><div class="ft-base" style="margin-top:0;border-top:0;padding-top:0"><span>Prepared by Daniel Deepak for Goel Dental · 9 Nov 2026 · Google Ads data read-only from account 598-498-3497 · Competitor data verified 9 Nov 2026.</span></div></div></footer>
</body></html>"""

if __name__ == "__main__":
    open("strategy-and-google-ads.html", "w").write(page()); print("ok")
