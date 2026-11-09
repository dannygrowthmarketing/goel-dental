import subprocess, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), ".."))
for s, o in [("goel_site.py","goel-dental-care.html"),("dds_site.py","delhi-dental-smiles.html")]:
    subprocess.run([sys.executable, "src/"+s, o], check=True)
subprocess.run([sys.executable, "src/report.py"], check=True); subprocess.run([sys.executable, "src/hub.py"], check=True)
