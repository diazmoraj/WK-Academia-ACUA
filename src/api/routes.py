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