from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("boston_prediction")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index", methods=["GET", "POST"])
def get_values():

    if request.method == "POST":

        rm = float(request.form["rm"])
        pt = float(request.form["pt"])
        lstat = float(request.form["lstat"])

        prediction = model.predict([[rm, pt, lstat]])

        return render_template(
            "result.html",
            prediction=float(prediction[0]),
            rm=rm,
            pt=pt,
            lstat=lstat
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
