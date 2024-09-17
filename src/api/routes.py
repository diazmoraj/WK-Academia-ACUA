"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

from api.models import Administrator
from api.models import Professor
from api.models import Student
from api.models import Profile
from api.models import PaymentProfessor
from api.models import PaymentStudent
from api.models import CommentProfessor
from api.models import CommentStudent
from api.models import Post
from api.models import Event
from api.models import Address
from api.models import Invoice
from api.models import Instrument
from api.models import Course

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# Metodos GET de las tablas
@api.route('/api/administrator', methods=['GET'])
def get_all_administrator():
    all_administrators = Administrator.query.all()
    administrators_serialized = []
    for administrator in all_administrators:
        administrators_serialized.append(administrator.serialize())
        print(administrators_serialized)
    return jsonify({"data": administrators_serialized}), 200

@api.route('/api/professor', methods=['GET'])
def get_all_professor():
    all_professors = Professor.query.all()
    professors_serialized = []
    for professor in all_professors:
        professors_serialized.append(professor.serialize())
        print(professors_serialized)
    return jsonify({"data": professors_serialized}), 200

@api.route('/api/student', methods=['GET'])
def get_all_student():
    all_students = Student.query.all()
    students_serialized = []
    for student in all_students:
        students_serialized.append(student.serialize())
        print(students_serialized)
    return jsonify({"data": students_serialized}), 200

@api.route('/api/profile', methods=['GET'])
def get_all_profile():
    all_profiles = Profile.query.all()
    profiles_serialized = []
    for profile in all_profiles:
        profiles_serialized.append(profile.serialize())
        print(profiles_serialized)
    return jsonify({"data": profiles_serialized}), 200

@api.route('/api/paymentprofessor', methods=['GET'])
def get_all_paymentprofessor():
    all_paymentprofessors = PaymentProfessor.query.all()
    paymentprofesors_serialized = []
    for paymentprofessor in all_paymentprofessors:
        paymentprofesors_serialized.append(paymentprofessor.serialize())
        print(paymentprofesors_serialized)
    return jsonify({"data": paymentprofesors_serialized}), 200

@api.route('/api/paymentstudent', methods=['GET'])
def get_all_paymentstudent():
    all_paymentstudents = PaymentStudent.query.all()
    paymentstudents_serialized = []
    for paymentstudent in all_paymentstudents:
        paymentstudents_serialized.append(paymentstudent.serialize())
        print(paymentstudents_serialized)
    return jsonify({"data": paymentstudents_serialized}), 200

@api.route('/api/commentprofessor', methods=['GET'])
def get_all_commentprofessor():
    all_commentprofessors = CommentProfessor.query.all()
    commentprofessors_serialized = []
    for commentprofessor in all_commentprofessors:
        commentprofessors_serialized.append(commentprofessor.serialize())
        print(commentprofessors_serialized)
    return jsonify({"data": commentprofessors_serialized}), 200

@api.route('/api/commentstudent', methods=['GET'])
def get_all_commentstudent():
    all_commentstudents = CommentStudent.query.all()
    commentstudents_serialized = []
    for commentstudent in all_commentstudents:
        commentstudents_serialized.append(commentstudent.serialize())
        print(commentstudents_serialized)
    return jsonify({"data": commentstudents_serialized}), 200

@api.route('/api/post', methods=['GET'])
def get_all_post():
    all_post = Post.query.all()
    posts_serialized = []
    for post in all_post:
        posts_serialized.append(post.serialize())
        print(posts_serialized)
    return jsonify({"data": posts_serialized}), 200

@api.route('/api/event', methods=['GET'])
def get_all_event():
    all_event = Event.query.all()
    events_serialized = []
    for event in all_event:
        events_serialized.append(event.serialize())
        print(events_serialized)
    return jsonify({"data": events_serialized}), 200

@api.route('/api/address', methods=['GET'])
def get_all_address():
    all_address = Address.query.all()
    addresses_serialized = []
    for address in all_address:
        addresses_serialized.append(address.serialize())
        print(addresses_serialized)
    return jsonify({"data": addresses_serialized}), 200

@api.route('/api/invoice', methods=['GET'])
def get_all_invoice():
    all_invoice = Invoice.query.all()
    invoices_serialized = []
    for invoice in all_invoice:
        invoices_serialized.append(invoice.serialize())
        print(invoices_serialized)
    return jsonify({"data": invoices_serialized}), 200

@api.route('/api/instrument', methods=['GET'])
def get_all_instrument():
    all_instrument = Instrument.query.all()
    instruments_serialized = []
    for instrument in all_instrument:
        instruments_serialized.append(instrument.serialize())
        print(instruments_serialized)
    return jsonify({"data": instruments_serialized}), 200

@api.route('/api/course', methods=['GET'])
def get_all_course():
    all_course = Course.query.all()
    courses_serialized = []
    for course in all_course:
        courses_serialized.append(course.serialize())
        print(courses_serialized)
    return jsonify({"data": courses_serialized}), 200

# Metodos GET ID de las tablas
@api.route('/api/administrator/<int:number_cardID>', methods=['GET'])
def get_single_administrator(number_cardID):
    single_administrator = Administrator.query.filter_by(number_cardID = number_cardID).first()
    if single_administrator is None:
        return jsonify({"msg": "El administrador con el ID: {} no existe".format(number_cardID)}), 400
    return jsonify({"data": single_administrator.serialize()}), 200

@api.route('/api/professor/<int:number_cardID>', methods=['GET'])
def get_single_professor(number_cardID):
    single_professor = Professor.query.filter_by(number_cardID = number_cardID).first()
    if single_professor is None:
        return jsonify({"msg": "El profesor con el ID: {} no existe".format(number_cardID)}), 400
    return jsonify({"data": single_professor.serialize()}), 200

@api.route('/api/student/<int:number_cardID>', methods=['GET'])
def get_single_student(number_cardID):
    single_student = Student.query.filter_by(number_cardID = number_cardID).first()
    if single_student is None:
        return jsonify({"msg": "El estudiante con el ID: {} no existe".format(number_cardID)}), 400
    return jsonify({"data": single_student.serialize()}), 200

@api.route('/api/profile/<int:id>', methods=['GET'])
def get_single_profile(id):
    single_profile = Profile.query.get(id)
    if single_profile is None:
        return jsonify({"msg": "El perfil con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_profile.serialize()}), 200

@api.route('/api/paymentprofessor/<int:id>', methods=['GET'])
def get_single_paymentprofessor(id):
    single_paymentprofessor = PaymentProfessor.query.get(id)
    if single_paymentprofessor is None:
        return jsonify({"msg": "El pago de profesor con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_paymentprofessor.serialize()}), 200

@api.route('/api/paymentstudent/<int:id>', methods=['GET'])
def get_single_paymentstudent(id):
    single_paymentstudent = PaymentStudent.query.get(id)
    if single_paymentstudent is None:
        return jsonify({"msg": "El pago de estudiante con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_paymentstudent.serialize()}), 200

@api.route('/api/commentprofessor/<int:id>', methods=['GET'])
def get_single_commentprofessor(id):
    single_commentprofessor = CommentProfessor.query.get(id)
    if single_commentprofessor is None:
        return jsonify({"msg": "El comentario de profesor con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_commentprofessor.serialize()}), 200

@api.route('/api/commentstudent/<int:id>', methods=['GET'])
def get_single_commenttstudent(id):
    single_commentstudent = CommentStudent.query.get(id)
    if single_commentstudent is None:
        return jsonify({"msg": "El comentario de estudiante con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_commentstudent.serialize()}), 200

@api.route('/api/post/<int:id>', methods=['GET'])
def get_single_post(id):
    single_post = Post.query.get(id)
    if single_post is None:
        return jsonify({"msg": "El post con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_post.serialize()}), 200

@api.route('/api/event/<int:id>', methods=['GET'])
def get_single_event(id):
    single_event = Event.query.get(id)
    if single_event is None:
        return jsonify({"msg": "El evento con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_event.serialize()}), 200

@api.route('/api/address/<int:id>', methods=['GET'])
def get_single_address(id):
    single_address = Address.query.get(id)
    if single_address is None:
        return jsonify({"msg": "La direccion con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_address.serialize()}), 200

@api.route('/api/invoice/<int:id>', methods=['GET'])
def get_single_invoice(id):
    single_invoice = Invoice.query.get(id)
    if single_invoice is None:
        return jsonify({"msg": "La informacion de la factura electronica" +
                        "con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_invoice.serialize()}), 200

@api.route('/api/instrument/<int:id>', methods=['GET'])
def get_single_instrument(id):
    single_instrument = Instrument.query.get(id)
    if single_instrument is None:
        return jsonify({"msg": "El instrumento con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_instrument.serialize()}), 200

@api.route('/api/course/<int:id>', methods=['GET'])
def get_single_course(id):
    single_course = Course.query.get(id)
    if single_course is None:
        return jsonify({"msg": "El curso con el ID: {} no existe".format(id)}), 400
    return jsonify({"data": single_course.serialize()}), 200

# Metodos POST de las tablas
@api.route('/api/administrator', methods=['POST'])
def new_administrator():
    required_fields = ["name", "last_name1", "last_name2", "cardID_type",
                       "number_cardID", "birthday", "phone_number", 
                       "email", "password"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_administrator = Administrator()
    for field in required_fields:
        setattr(new_administrator, field, body[field])

    try:
        db.session.add(new_administrator)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/professor', methods=['POST'])
def new_professor():
    required_fields = ["name", "last_name1", "last_name2", "cardID_type",
                       "number_cardID", "birthday", "country", "phone_number", 
                       "email", "password"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_professor = Professor()
    for field in required_fields:
        setattr(new_professor, field, body[field])

    try:
        db.session.add(new_professor)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/student', methods=['POST'])
def new_student():
    required_fields = ["name", "last_name1", "last_name2", "cardID_type",
                       "number_cardID", "birthday", "phone_number", 
                       "responsable", "emergency_contact", "phone_emergency",
                       "diagnostic", "email", "password"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_student = Student()
    for field in required_fields:
        setattr(new_student, field, body[field])

    try:
        db.session.add(new_student)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/profile', methods=['POST'])
def new_profile():
    required_fields = ["profile"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_profile = Profile()
    for field in required_fields:
        setattr(new_profile, field, body[field])

    try:
        db.session.add(new_profile)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/paymentprofessor', methods=['POST'])
def new_paymentprofessor():
    required_fields = ["pay", "SINPE", "IBAN"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_paymentprofessor = PaymentProfessor()
    for field in required_fields:
        setattr(new_paymentprofessor, field, body[field])

    try:
        db.session.add(new_paymentprofessor)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/paymentstudent', methods=['POST'])
def new_paymentstudent():
    required_fields = ["pay_date", "limit_pay_date", "mount"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_paymentstudent = PaymentStudent()
    for field in required_fields:
        setattr(new_paymentstudent, field, body[field])

    try:
        db.session.add(new_paymentstudent)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/commentprofessor', methods=['POST'])
def new_commentprofessor():
    required_fields = ["comment_professor"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_commentprofessor = CommentProfessor()
    for field in required_fields:
        setattr(new_commentprofessor, field, body[field])

    try:
        db.session.add(new_commentprofessor)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/commentstudent', methods=['POST'])
def new_commentstudent():
    required_fields = ["comment_student"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_commentstudent = CommentStudent()
    for field in required_fields:
        setattr(new_commentstudent, field, body[field])

    try:
        db.session.add(new_commentstudent)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/post', methods=['POST'])
def new_post():
    required_fields = ["title", "author", "origin_date", "publish_date", "theme", "post"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_post = Post()
    for field in required_fields:
        setattr(new_post, field, body[field])

    try:
        db.session.add(new_post)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/event', methods=['POST'])
def new_event():
    required_fields = ["event_date", "place", "event"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_event = Event()
    for field in required_fields:
        setattr(new_event, field, body[field])

    try:
        db.session.add(new_event)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/address', methods=['POST'])
def new_address():
    required_fields = ["province", "canton", "district"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_address = Address()
    for field in required_fields:
        setattr(new_address, field, body[field])

    try:
        db.session.add(new_address)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/invoice', methods=['POST'])
def new_invoice():
    required_fields = ["name", "last_name1", "last_name2", "cardID_type",
                       "number_cardID", "phone_number", "email"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_invoice = Invoice()
    for field in required_fields:
        setattr(new_invoice, field, body[field])

    try:
        db.session.add(new_invoice)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200

@api.route('/api/instrument', methods=['POST'])
def new_instrument():
    required_fields = ["instrument"]
    
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({"msg": "Debes completar toda la informacion para continuar"}), 400
    
    missing_fields = [field for field in required_fields if field not in body]

    if missing_fields:
        return jsonify({"msg": f"Faltan los siguientes campos: {', '.join(missing_fields)}"}), 400
    
    new_instrument = Instrument()
    for field in required_fields:
        setattr(new_instrument, field, body[field])

    try:
        db.session.add(new_instrument)
        db.session.commit()
    except Exception as error:
        return jsonify({"msg": error.args[0]}), 500
    
    return jsonify({"msg": "OK"}), 200






from api.models import Course