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
    app.run()
