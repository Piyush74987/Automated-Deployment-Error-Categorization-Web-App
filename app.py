from flask import Flask, render_template, request
from error_anaylsis import analyze_error_with_nlp

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        error_text = request.form["error_text"]
        category, reason, resolution, prevention = analyze_error_with_nlp(error_text)
        result = {
            "category": category,
            "reason": reason,
            "resolution": resolution,
            "prevention": prevention
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
