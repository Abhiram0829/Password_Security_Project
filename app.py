from flask import Flask, render_template, request
import password_checker  # your existing password_checker.py

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form["password"]
        score, risk, breached = password_checker.calculate_risk(password)

        result = {
            "score": score,
            "breached": breached,
            "risk": risk
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
