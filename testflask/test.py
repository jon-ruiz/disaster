from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    data = pd.read_csv("/Users/jonruiz/Downloads/Advertising.csv")
    mean_whole = round(data.radio.mean(), 3)
    return render_template("home.html",mean_whole=mean_whole)

if __name__ == '__main__':
    app.run(debug=True)
