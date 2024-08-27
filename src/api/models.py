from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Administrator(db.Model):
    __tablename__ = 'administrator'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name1 = db.Column(db.String(50), nullable=False)
    last_name2 = db.Column(db.String(50), nullable=True)
    cardID_type = db.Column(db.String(25), nullable=False)
    number_cardID = db.Column(db.BigInteger, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.BigInteger, nullable=False)
    province = db.Column(db.String(50), nullable=False)
    canton = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'Administrator: {}'.format(self.name)
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "last_name1": self.last_name1,
            "last_name2": self.last_name2,
            "cardID_type": self.cardID_type,
            "number_cardID": self.number_cardID,
            "birthday": self.birthday,
            "phone_number": self.phone_number,
            "province": self.province,
            "canton": self.canton,
            "district": self.district,
            "email": self.email
        }