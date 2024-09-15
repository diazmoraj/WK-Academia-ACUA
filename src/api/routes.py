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