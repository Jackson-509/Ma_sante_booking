from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def index():
    return render_template("index.html", nom_site="MaSanté")

@app.route("/liste-praticiens")
def liste_praticiens():
    return render_template("praticiens.html", nom_site="MaSanté")

@app.route("/reserver/<int:id>", methods=["GET", "POST"])
def reserver(id):
    praticien = {
        "id": id,
        "nom": "Dr Jaou Belkacem",
        "specialite": "Médecin généraliste",
        "adresse": "7 bis Avenue Gaston Chauvin, 93600 Aulnay-sous-Bois",
        "tarif": "Conventionné secteur 1"
    }

    planning = [
        {"nom": "lundi", "date": "10 juin", "creneaux": ["09:00", "09:30", "10:00"]},
        {"nom": "mardi", "date": "11 juin", "creneaux": ["09:45", "10:15", "10:45"]},
        {"nom": "mercredi", "date": "12 juin", "creneaux": ["09:30", "10:00"]},
        {"nom": "jeudi", "date": "13 juin", "creneaux": []},
        {"nom": "vendredi", "date": "14 juin", "creneaux": ["11:00", "11:30"]},
        {"nom": "samedi", "date": "15 juin", "creneaux": []},
        {"nom": "dimanche", "date": "16 juin", "creneaux": []}
    ]

    return render_template("reserver.html", praticien=praticien, planning=planning, nom_site="MaSanté")

@app.route("/confirmer/<int:id>", methods=["POST"])
def confirmer_rdv(id):
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    email = request.form["email"]
    date = request.form["date"]
    heure = request.form["heure"]

    # Tu peux ici enregistrer le rdv (dans un fichier, BDD ou juste afficher un message)
    flash(f"Rendez-vous confirmé pour {prenom} {nom} le {date} à {heure} avec le praticien #{id}", "success")
    return redirect(url_for("index"))

@app.route("/login")
def login():
    return "<h1>Page de connexion à venir</h1>"
@app.route("/cgu")
def cgu():
    return render_template("cgu.html", nom_site="MaSanté")

@app.route("/mentions-legales")
def mentions_legales():
    return render_template("mentions-legales.html", nom_site="MaSanté")

@app.route("/confidentialite")
def politique_confidentialite():
    return render_template("confidentialite.html", nom_site="MaSanté")

@app.route("/cookies")
def parametres_cookies():
    return render_template("cookies.html", nom_site="MaSanté")



if __name__ == "__main__":
    app.run(debug=True)
