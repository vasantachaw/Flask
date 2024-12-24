from flask import Flask, render_template, request
import joblib as jb

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    result = None
    if request.method == "POST":
        hour = request.form.get("hours")
        hr = float(hour)
        model = jb.load("static/Model/Student_mark_predictor_model.pkl")
        result = model.predict([[hr]])[0][0].round()
    return render_template("index.html", result=str(result) + "%")


if __name__ == "__main__":
    app.run(debug=True)
