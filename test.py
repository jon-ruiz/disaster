from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    casualties = pd.read_csv("/Users/jonruiz/testflask/data/casualties.csv")
    caution_advice = pd.read_csv("/Users/jonruiz/testflask/data/caution_advice.csv")
    donations = pd.read_csv("/Users/jonruiz/testflask/data/donations.csv")
    info_source = pd.read_csv("/Users/jonruiz/testflask/data/info_source.csv")
    return render_template("home.html",casualties=casualties, caution_advice=caution_advice, donations=donations, info_source=info_source)

if __name__ == '__main__':
    app.run(debug=True)
