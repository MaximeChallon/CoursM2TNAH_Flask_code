from ..app import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    prenom = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(80), nullable=False)

    @staticmethod
    def identification(mail, password):
        utilisateur = Users.query.filter(Users.mail == mail).first()
        if utilisateur and check_password_hash(utilisateur.password, password):
            return utilisateur
        return None

    @staticmethod
    def ajout(prenom, password, mail):
        erreurs = []
        if not prenom:
            erreurs.append("Le prénom est vide")
        if not password or len(password) < 6:
            erreurs.append("Le mot de passe est vide ou trop court")
        if not mail :
            erreurs.append("Le mail est vide")

        unique = Users.query.filter(
            db.or_(Users.mail == mail)
        ).count()
        if unique > 0:
            erreurs.append("L'utilisateur existe déjà avec le mail "+mail)

        if len(erreurs) > 0:
            return False, erreurs
        
        utilisateur = Users(
            prenom=prenom,
            password=generate_password_hash(password),
            mail=mail
        )

        try:
            db.session.add(utilisateur)
            db.session.commit()
            return True, utilisateur
        except Exception as erreur:
            return False, [str(erreur)]

    def get_id(self):
        return self.id

    @login.user_loader
    def get_user_by_id(id):
        return Users.query.get(int(id))