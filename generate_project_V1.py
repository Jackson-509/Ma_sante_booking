import os
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "composants" / "generator_templates_booking_services"

def create_project(nom_site, slug, couleur="#00838f"):
    base = Path(slug)
    folders = [
        base / "templates",
        base / "static" / "css",
        base / "static" / "img",
        base / "static" / "js",
        base / "instance"
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    # app.py
    app_src = (TEMPLATE_DIR / "app.py").read_text(encoding="utf-8")
    (base / "app.py").write_text(app_src, encoding="utf-8")

    # config.py
    config_src = (TEMPLATE_DIR / "config.py").read_text(encoding="utf-8")
    (base / "config.py").write_text(config_src, encoding="utf-8")

    # index.html
    index_src = (TEMPLATE_DIR / "index.html").read_text(encoding="utf-8")
    (base / "templates" / "index.html").write_text(index_src, encoding="utf-8")

    # fiche_praticien.html
    fiche_src = (TEMPLATE_DIR / "fiche_praticien.html").read_text(encoding="utf-8")
    (base / "templates" / "fiche_praticien.html").write_text(fiche_src, encoding="utf-8")

    # praticiens.html
    praticiens_src = (TEMPLATE_DIR / "praticiens.html").read_text(encoding="utf-8")
    (base / "templates" / "praticiens.html").write_text(praticiens_src, encoding="utf-8")

    # style.css
    style_src = (TEMPLATE_DIR / "style.css").read_text(encoding="utf-8")
    style_src = style_src.replace("#00838f", couleur)
    (base / "static" / "css" / "style.css").write_text(style_src, encoding="utf-8")

    # README.md
    readme_src = (TEMPLATE_DIR / "README.md").read_text(encoding="utf-8")
    (base / "README.md").write_text(readme_src.format(nom_site=nom_site, couleur=couleur, slug=slug), encoding="utf-8")

    # .gitignore, Procfile, requirements.txt
    requirements_src = (TEMPLATE_DIR / "requirements.txt").read_text(encoding="utf-8")
    procfile_src = (TEMPLATE_DIR / "Procfile").read_text(encoding="utf-8")
    gitignore_src = (TEMPLATE_DIR / "gitignore").read_text(encoding="utf-8")
    (base / "requirements.txt").write_text(requirements_src, encoding="utf-8")
    (base / "Procfile").write_text(procfile_src, encoding="utf-8")
    (base / ".gitignore").write_text(gitignore_src, encoding="utf-8")

    # Images vides
    for img in ["logo.png", "banner.jpg", "service1.jpg", "service2.jpg"]:
        (base / "static" / "img" / img).touch()

    # Pages légales HTML
    for page in ["cgu.html", "mentions-legales.html", "politique-confidentialite.html", "parametres-cookies.html"]:
        content = (TEMPLATE_DIR / page).read_text(encoding="utf-8")
        (base / "templates" / page).write_text(content, encoding="utf-8")

    # Footer HTML (à injecter dans toutes les pages principales)
    footer = (TEMPLATE_DIR / "footer.html").read_text(encoding="utf-8")
    for html_file in [
        "index.html", "fiche_praticien.html", "praticiens.html",
        "cgu.html", "mentions-legales.html", "politique-confidentialite.html", "parametres-cookies.html"
    ]:
        html_path = base / "templates" / html_file
        if html_path.exists():
            with open(html_path, "a", encoding="utf-8") as f:
                f.write("\n" + footer.strip())

    print(f"✅ Projet '{slug}' généré avec succès.")

if __name__ == "__main__":
    nom_site = input("Nom du site : ")
    slug = input("Nom du dossier (slug) : ")
    couleur = input("Couleur principale (hex) [#00838f] : ") or "#00838f"
    create_project(nom_site, slug, couleur)
