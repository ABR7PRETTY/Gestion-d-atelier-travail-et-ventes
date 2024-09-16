from michelin import api_michelin_bp
from michelin.controllers.CategorieController import CategorieController
from michelin.controllers.ArticleController import ArticleController
from michelin.controllers.ApprentiController import ApprentiController
from michelin.controllers.AtelierController import AtelierController
from michelin.controllers.VenteController import VenteController
from michelin.controllers.DepenseController import DepenseController
from michelin.controllers.DesignationController import Designation_journaliereController


categorie_controller = CategorieController()
article_controller = ArticleController()
atelier_controller = AtelierController()
apprenti_controller = ApprentiController()
designation_controller = Designation_journaliereController()
vente_controller = VenteController()
depense_controller = DepenseController()


@api_michelin_bp.route("/categories", methods=['POST'])
def add_category():
    return categorie_controller.create()

@api_michelin_bp.route("/categories", methods=['GET'])
def list_categories():
    return categorie_controller.all()

@api_michelin_bp.route("/updateCategorie/<int:id>", methods=["PUT"])
def update_categorie(id):
    return categorie_controller.update(id)


@api_michelin_bp.route("/deleteCategorie/<int:id>", methods=["DELETE"])
def delete_categorie(id):
    return categorie_controller.delete(id)

@api_michelin_bp.route("/articles", methods=['POST'])
def add_article():
    return article_controller.create()

@api_michelin_bp.route("/articles", methods=['GET'])
def list_article():
    return article_controller.all()

@api_michelin_bp.route("/deleteArticle/<int:article_id>", methods=["DELETE"])
def delete_article(article_id):
    return article_controller.delete(article_id)


@api_michelin_bp.route("/updateArticle/<int:article_id>", methods=["PUT"])
def update_article(article_id):
    return article_controller.update(article_id)

@api_michelin_bp.route("/apprentis", methods=['POST'])
def add_apprenti():
    return apprenti_controller.create()

@api_michelin_bp.route("/apprentis", methods=['GET'])
def list_apprentis():
    return apprenti_controller.all()

@api_michelin_bp.route("/updateApprenti/<int:id>", methods=["PUT"])
def update_apprenti(id):
    return apprenti_controller.update(id)


@api_michelin_bp.route("/deleteApprenti/<int:id>", methods=["DELETE"])
def delete_apprenti(id):
    return apprenti_controller.delete(id)

@api_michelin_bp.route("/ateliers", methods=['POST'])
def add_atelier():
    return atelier_controller.create()

@api_michelin_bp.route("/ateliers", methods=['GET'])
def list_atelier():
    return atelier_controller.all()

@api_michelin_bp.route("/deleteAtelier/<int:atelier_id>", methods=["DELETE"])
def delete_atelier(atelier_id):
    return atelier_controller.delete(atelier_id)


@api_michelin_bp.route("/updateAtelier/<int:atelier_id>", methods=["PUT"])
def update_atelier(atelier_id):
    return atelier_controller.update(atelier_id)

@api_michelin_bp.route("/ventes", methods=['POST'])
def add_vente():
    return vente_controller.create()

@api_michelin_bp.route("/ventes", methods=['GET'])
def list_ventes():
    return vente_controller.all()

@api_michelin_bp.route("/updateVente/<int:id>", methods=["PUT"])
def update_vente(id):
    return vente_controller.update(id)


@api_michelin_bp.route("/deleteVente/<int:id>", methods=["DELETE"])
def delete_vente(id):
    return vente_controller.delete(id)

@api_michelin_bp.route("/designations", methods=['POST'])
def add_designation():
    return designation_controller.create()

@api_michelin_bp.route("/designations", methods=['GET'])
def list_designation():
    return designation_controller.all()

@api_michelin_bp.route("/deleteDesignation/<int:designation_id>", methods=["DELETE"])
def delete_designation(designation_id):
    return designation_controller.delete(designation_id)


@api_michelin_bp.route("/updateDesignation/<int:designation_id>", methods=["PUT"])
def update_designation(designation_id):
    return designation_controller.update(designation_id)

@api_michelin_bp.route("/depenses", methods=['POST'])
def add_depense():
    return depense_controller.create()

@api_michelin_bp.route("/depenses", methods=['GET'])
def list_depense():
    return depense_controller.all()

@api_michelin_bp.route("/deleteDepense/<int:depense_id>", methods=["DELETE"])
def delete_depense(depense_id):
    return depense_controller.delete(depense_id)


@api_michelin_bp.route("/updateDepense/<int:depense_id>", methods=["PUT"])
def update_depense(depense_id):
    return depense_controller.update(depense_id)
