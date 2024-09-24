from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
# Tabla para registrar los administradores
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
    email = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    profile = db.relationship("Profile", back_populates="administrator", lazy="joined")

    address = db.relationship("Address", back_populates="administrator", lazy="joined")

    def __repr__(self):
        return f'Administrator: {self.name}'
    
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
            "profile": self.profile.serialize() if self.profile else None,
            "address": self.address.serialize() if self.address else None,
            "is_active": self.is_active
        }

# Tabla para registrar los perfiles de los administradores 
class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String(25), nullable=False)
    
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    administrator = db.relationship("Administrator", back_populates="profile", lazy="joined")

    def __repr__(self):
        return f'Profile: {self.profile}'
    
    def serialize(self):
        return{
            "id": self.id,
            "profile": self.profile,
            "administrator": self.administrator.serialize() if self.administrator else None,
        }

# Tabla para registrar los profesores 
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
    email = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    paymentprofessor = db.relationship("PaymentProfessor", back_populates="professor", lazy="joined")

    address = db.relationship("Address", back_populates="professors", lazy="joined")

    commentprofessor = db.relationship("CommentProfessor", back_populates="professor", lazy="joined")

    course = db.relationship("Course", back_populates="professor", lazy="joined")

    def __repr__(self):
        return f'Professor: {self.name}'
    
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
            "paymentprofessor":self.paymentprofessor.serialize() if self.paymentprofessor else None,
            "address": self.address.serialize() if self.address else None,
            "commentprofessor": self.commentprofessor.serialize() if self.commentprofessor else None,
            "course": self.course.serialize() if self.course else None,
            "is_active": self.is_active
        }

# Tabla para registrar los tipos de pagos a los profesores 
class PaymentProfessor(db.Model):
    __tablename__ = 'paymentprofessor'

    id = db.Column(db.Integer, primary_key=True)
    pay = db.Column(db.String(15), nullable=False)
    SINPE = db.Column(db.String(25), nullable=True)
    IBAN = db.Column(db.String(50), nullable=True)

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship("Professor", back_populates="paymentprofessor")

    def __repr__(self):
        return f'PaymentProfessor: {self.pay}'
    
    def serialize(self):
        return{
            "id": self.id,
            "pay": self.pay,
            "SINPE": self.SINPE,
            "IBAN": self.IBAN,
            "professor": self.professor.serialize() if self.professor else None
        }

# Tabla para registrar los estudiantes
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
    email = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    invoice = db.relationship("Invoice", back_populates="student", lazy="joined")

    address = db.relationship("Address", back_populates="students", lazy="joined")

    commentstudent = db.relationship("CommentStudent", back_populates="student", lazy="joined")

    paymentstudent = db.relationship("PaymentStudent", back_populates="student", lazy="joined")
    
    course = db.relationship("Course", back_populates="student", lazy="joined")

    def __repr__(self):
        return f'Student: {self.name}'
    
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
            "is_active": self.is_active,
            "invoice": self.invoice.serialize() if self.invoice else None,
            "address": self.address.serialize() if self.address else None,
            "commentstudent": self.commentstudent.serialize() if self.commentstudent else None,
            "paymentstudent": self.paymentstudent.serialize() if self.paymentstudent else None,
            "course": self.course.serialize() if self.course else None
        }
    
# Tabla para registrar la factura electronica de los estudiantes 
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
        return f'Invoice: {self.name}'
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "last_name1": self.last_name1,
            "last_name2": self.last_name2,
            "cardID_type": self.cardID_type,
            "number_cardID": self.number_cardID,
            "phone_number": self.phone_number,
            "email": self.email,
            "student": self.student.serialize() if self.student else None
        }
    
# Tabla para registrar los tipos de pagos a los estudiantes 
class PaymentStudent(db.Model):
    __tablename__ = 'paymentstudent'

    id = db.Column(db.Integer, primary_key=True)
    pay_date = db.Column(db.Date, nullable=False)
    limit_pay_date = db.Column(db.Date, nullable=False)
    mount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", back_populates="paymentstudent")

    def __repr__(self):
        return f'PaymentStudent: {self.mount}'
    
    def serialize(self):
        return{
            "id": self.id,
            "pay_date": self.pay_date,
            "limit_pay_date": self.limit_pay_date,
            "mount": self.mount,
            "student": self.student.serialize() if self.student else None
        }
    
# Tabla para registrar los instrumentos que se imparten
class Instrument(db.Model):
    __tablename__ = 'instrument'

    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String(25), nullable=False)

    course = db.relationship("Course", back_populates="instrument")

    def __repr__(self):
        return f'Instrument: {self.instrument}'
    
    def serialize(self):
        return{
            "id": self.id,
            "instrument": self.instrument,
            "course": self.course.serialize() if self.course else None
        }

# Tabla para registrar los cursos matriculados
class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    modality = db.Column(db.String(15), nullable=False)

    instrument_id = db.Column(db.Integer, db.ForeignKey('instrument.id'))
    instrument = db.relationship("Instrument", back_populates="course")

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", back_populates="course", lazy="joined")

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship("Professor", back_populates="course", lazy="joined")

    def __repr__(self):
        return f'Course: {self.modality}'
    
    def serialize(self):
        return{
            "id": self.id,
            "modality": self.modality,
            "instrument": self.instrument.serialize() if self.instrument else None,
            "student": self.student.serialize() if self.instrument else None,
            "professor": self.professor.serialze() if self.professor else None
        }

# Tabla para registrar las direcciones de todo el personal
class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(50), nullable=False)
    canton = db.Column(db.String(50), nullable=False)
    district = db.Column(db.String(50), nullable=False)

    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    administrator = db.relationship("Administrator", back_populates="profile", lazy="joined")
    
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship("Professor", back_populates="address", lazy="joined")

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", back_populates="address", lazy="joined")

    def __repr__(self):
        return f'Address: {self.province}, {self.canton}, {self.district}'

    def serialize(self):
        return {
            "id": self.id,
            "province": self.province,
            "canton": self.canton,
            "district": self.district,
            "administrator": self.administrator.serialize() if self.administrator else None,
            "professor": self.professor.serialize() if self.professor else None,
            "student": self.student.serialize() if self.student else None
        }

# Tabla para registrar comentarios de los estudiantes a los profesores
class CommentStudent(db.Model):
    __tablename__ = 'commentstudent'

    id = db.Column(db.Integer, primary_key=True)
    comment_student = db.Column(db.String(255), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    student = db.relationship("Student", back_populates="commentstudent")

    def __repr__(self):
        return f'CommentStudent: {self.comment_student}'
    
    def serialize(self):
        return{
            "id": self.id,
            "comment_student": self.comment_student,
            "student": self.student.serialize() if self.student else None
        }

# Tabla para registrar comentarios de los profesores a los estudiantes
class CommentProfessor(db.Model):
    __tablename__ = 'commentprofessor'

    id = db.Column(db.Integer, primary_key=True)
    comment_professor = db.Column(db.String(255), nullable=False)

    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship("Professor", back_populates="commentprofessor")

    def __repr__(self):
        return f'CommentProfessor: {self.comment_professor}'
    
    def serialize(self):
        return{
            "id": self.id,
            "comment_professor": self.comment_professor,
            "professor": self.professor.serialize() if self.professor else None
        }
    
# Tabla para registrar los proximos eventos de ACUA o aliados
class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.Date, nullable=False)
    place = db.Column(db.String(50), nullable=False)
    event = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return f'Event: {self.event}'
    
    def serialize(self):
        return{
            "id": self.id,
            "event_date": self.event_date.isoformat() if self.event_date else None,
            "place": self.place,
            "event": self.event
        }
    
# Tabla para registrar post en el blog
class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    origin_date = db.Column(db.Date, nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    theme = db.Column(db.String(250), nullable=False)
    post = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'Post: {self.title}'
    
    def serialize(self):
        return{
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "origin_date": self.origin_date.isoformat() if self.origin_date else None,
            "publish_date": self.publish_date.isoformat() if self.publish_date else None,
            "theme": self.theme,
            "post": self.post
        }