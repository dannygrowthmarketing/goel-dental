from shared import *
from goel_site import TOK, FONTS
def page():
    cards=[("goel-dental-care.html","clinic-front","Goel Dental Care","goeldentalcare.com · general dentistry, 5–8 km","goel-dental-care.pdf"),
           ("delhi-dental-smiles.html","hero-smile","Delhi Dental Smiles","delhidentalsmiles.com · cosmetic, South Delhi","delhi-dental-smiles.pdf"),
           ("strategy-and-google-ads.html","digital-zone","Strategy & Google Ads review","₹24.9L ad history, keywords, competitors, page plan","strategy-and-google-ads.pdf")]
    c="".join(f'<article class="card" style="padding:0;overflow:hidden"><a href="{h}" style="text-decoration:none"><div class="photo" style="aspect-ratio:16/10">{pic(i,t)}</div></a><div style="padding:22px 24px 26px;display:grid;gap:8px"><h3 style="margin:0"><a href="{h}" style="text-decoration:none">{t}</a></h3><p class="small muted" style="margin:0">{d}</p><div class="btns" style="margin-top:8px"><a class="btn sm" href="{h}">Open site</a><a class="btn sm ghost" href="{p}">PDF</a></div></div></article>' for h,i,t,d,p in cards)
    return head("Goel Dental Prototypes","Website prototypes and strategy review for Goel Dental, Malviya Nagar.","https://dannygrowthmarketing.github.io/goel-dental/",TOK,FONTS,[])+f"""<body><div class="preview"><b>Prepared for Dr Saurabh Goel &amp; Dr Shikha Goel</b> by Daniel Deepak · 9 November 2026</div>
<main><section class="section"><div class="wrap"><p class="eyebrow">Goel Dental · Patient acquisition system</p><h1 style="max-width:18ch">Two websites and the plan behind them.</h1><p class="lead">Built with the clinic's own photos, doctors and cases. Every enquiry on both sites is tracked from ad click to treatment. Orange badges mark details for the clinic to confirm.</p>
<div class="grid g3" style="margin-top:48px">{c}</div></div></section></main></body></html>"""
open("index.html","w").write(page()); print("ok")
