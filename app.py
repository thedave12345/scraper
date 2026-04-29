import os
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/run")
def run_script():
    subprocess.run(["python", "scraper.py"])
    return "Scraping lancé"

@app.route("/")
def home():
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
