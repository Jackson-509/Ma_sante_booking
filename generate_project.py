import os
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "composants" / "generator_templates_booking_services"

def create_project(nom_site, slug, couleur="#00838f"):
    base = Path(slug)
    folders = [
        base / "templates",
        base / "static" / "css",
        base / "static" / "img",
        base / "instance"
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    # index.html
    index_src = (TEMPLATE_DIR / "index.html").read_text(encoding="utf-8")
    (base / "templates" / "index.html").write_text(index_src.format(nom_site=nom_site), encoding="utf-8")

    # fiche_praticien.html
    index_src = (TEMPLATE_DIR / "fiche_praticien.html").read_text(encoding="utf-8")
    (base / "templates" / "fiche_praticien.html").write_text(index_src.format(nom_site=nom_site), encoding="utf-8")

    print(f"✅ Projet '{slug}' généré avec succès.")

if __name__ == "__main__":
    nom_site = input("Nom du site : ")
    slug = input("Nom du dossier (slug) : ")
    couleur = input("Couleur principale (hex) [#00838f] : ") or "#00838f"
    create_project(nom_site, slug, couleur)