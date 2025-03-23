from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.jinja_env.globals.update(enumerate=enumerate)  # Tambahkan ini

messages = []  # Menyimpan pesan yang dikirim

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form["nama"]
        pesan = request.form["pesan"]
        messages.append({"nama": nama, "pesan": pesan})  # Simpan pesan

    return render_template("index.html", messages=messages)

@app.route("/hapus/<int:index>")
def hapus_pesan(index):
    if 0 <= index < len(messages):  # Pastikan indeks valid
        messages.pop(index)  # Hapus pesan berdasarkan indeks
    return redirect(url_for("index"))  # Redirect ke halaman utama

if __name__ == "__main__":
    app.run(debug=True)
