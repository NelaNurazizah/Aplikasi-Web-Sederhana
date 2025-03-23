from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    nama = None
    pesan = None

    if request.method == "POST":
        nama = request.form.get("nama")
        pesan = request.form.get("pesan")

    return render_template("index.html", nama=nama, pesan=pesan)

if __name__ == "__main__":
    app.run(debug=True)
