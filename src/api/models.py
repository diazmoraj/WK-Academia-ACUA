from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
class Administrator(db.Model):
    __tablename__ = 'administrator'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name1 = db.Column(db.String(50), nullable=False)
    last_name2 = db.Column(db.String(50), nullable=True)
    cardID_type = db.Column(db.String(25), nullable=False)
    number_cardID = db.Column(db.String(25), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    profile = db.relationship("Profile", back_populates="administrator")
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship("Address", back_populates="administrators")

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
            "birthday": self.birthday.isoformat() if self.birthday else None,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": self.address.serialize() if self.address else None
        }
    
class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String(25), nullable=False)
    
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    administrator = db.relationship("Administrator", back_populates="profile")

    def __repr__(self):
        return 'Profile: {}'.format(self.profile)
    
    def serialize(self):
        return{
            "id": self.id,
            "profile": self.profile
        }
    
class Professor(db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name1 = db.Column(db.String(50), nullable=False)
    last_name2 = db.Column(db.String(50), nullable=True)
    cardID_type = db.Column(db.String(25), nullable=False)
    number_cardID = db.Column(db.String(25), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    payment = db.relationship("Payment", back_populates="professor")
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship("Address", back_populates="professors")

    def __repr__(self):
        return 'Professor: {}'.format(self.name)
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "last_name1": self.last_name1,
            "last_name2": self.last_name2,
            "cardID_type": self.cardID_type,
            "number_cardID": self.number_cardID,
            "birthday": self.birthday.isoformat() if self.birthday else None,
            "country": self.country,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": self.address.serialize() if self.address else None
        }
    
class Payment(db.Model):
    __tablename__ = 'payment'

    id = db.Column(db.Integer, primary_key=True)
    pay = db.Column(db.String(15), nullable=False)
    SINPE = db.Column(db.String(25), nullable=True)
    IBAN = db.Column(db.String(50), nullable=True)

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship("Professor", back_populates="payment")

    def __repr__(self):
        return 'Payment: {}'.format(self.pay)
    
    def serialize(self):
        return{
            "id": self.id,
            "pay": self.pay,
            "SINPE": self.SINPE,
            "IBAN": self.IBAN
        }

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name1 = db.Column(db.String(50), nullable=False)
    last_name2 = db.Column(db.String(50), nullable=True)
    cardID_type = db.Column(db.String(25), nullable=False)
    number_cardID = db.Column(db.String(25), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(25), nullable=False)
    responsable = db.Column(db.String(75), nullable=True)
    emergency_contact = db.Column(db.String(50), nullable=False)
    phone_emergency = db.Column(db.String(25), nullable=False)
    diagnostic = db.Column(db.String(250), nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    invoice = db.relationship("Invoice", back_populates="student")
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship("Address", back_populates="students")
    comment = db.relationship("Comment", back_populates="student")

    def __repr__(self):
        return 'Student: {}'.format(self.name)
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "last_name1": self.last_name1,
            "last_name2": self.last_name2,
            "cardID_type": self.cardID_type,
            "number_cardID": self.number_cardID,
            "birthday": self.birthday.isoformat() if self.birthday else None,
            "phone_number": self.phone_number,
            "responsable": self.responsable,
            "emergency_contact": self.emergency_contact,
            "phone_emergency": self.phone_emergency,
            "diagnostic": self.diagnostic,
            "email": self.email,
            "address": self.address.serialize() if self.address else None
        }
    
class Invoice(db.Model):
    __tablename__ = 'invoice'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name1 = db.Column(db.String(50), nullable=False)
    last_name2 = db.Column(db.String(50), nullable=True)
    cardID_type = db.Column(db.String(25), nullable=False)
    number_cardID = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", back_populates="invoice")

    def __repr__(self):
        return 'Invoice: {}'.format(self.name)
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "last_name1": self.last_name1,
            "last_name2": self.last_name2,
            "cardID_type": self.cardID_type,
            "number_cardID": self.number_cardID,
            "phone_number": self.phone_number,
            "email": self.email
        }

class Instrument(db.Model):
    __tablename__ = 'instrument'

    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String(25), nullable=False)

    course = db.relationship("Course", back_populates="instrument")

    def __repr__(self):
        return 'Instrument: {}'.format(self.instrument)
    
    def serialize(self):
        return{
            "id": self.id,
            "instrument": self.instrument
        }
    
class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    modality = db.Column(db.String(15), nullable=False)

    instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'))
    instrument = db.relationship("Instrument", back_populates="course")
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", back_populates="course")
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship("Professor", back_populates="course")

    def __repr__(self):
        return 'Course: {}'.format(self.modality)
    
    def serialize(self):
        return{
            "id": self.id,
            "modality": self.modality
        }
    
class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(50), nullable=False)
    canton = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)

    administrators = db.relationship("Administrator", back_populates="address")
    professors = db.relationship("Professor", back_populates="address")
    students = db.relationship("Student", back_populates="address")

    def __repr__(self):
        return f'Address: {self.province}, {self.canton}, {self.district}'

    def serialize(self):
        return {
            "id": self.id,
            "province": self.province,
            "canton": self.canton,
            "district": self.district
        }
    
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", back_populates="comment")

    def __repr__(self):
        return 'Comment: {}'.format(self.comment)
    
    def serialize(self):
        return{
            "id": self.id,
            "comment": self.comment
        }