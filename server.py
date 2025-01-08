from flask import Flask, render_template, request, redirect, url_for, Response
from flask_cors import cross_origin, CORS
import datetime
from flask_cors import CORS
from token_service import TokenServiceImpl
import security
from authorisation_service import authorisation_service as auth
from mongo_orm import mongo_db
import settings
from flask import Flask, request, jsonify
from sign_service.signature import Signature
from lib.signature_comparison_method_circles_pithagorian import compare_two_signatures
app = Flask(__name__)
token_service = TokenServiceImpl()
security_service = security.EndpointsSecurityService()
authorisation_service = auth.AutorisationServise()


CORS(app)
from sign_service import service as service_s

signature_service = service_s.SignatureService(
        mongo_db.MongoRepository(
            settings.DB_CONNECTION_STRING, "Test_DB", "signature_collection"))


@app.route('/signature', methods=['POST'])
def save_signature():
    data = request.json
    sig = signature_service.add_new(data)

    return sig.to_web_dto(), 200

@app.route('/signature/compare', methods=['PUT'])
def compare_signatures():
    data = request.get_json()
    ethalon_signature = data["ethaloneSignature"]
    comparable_signature = data["comparableSignature"]
    tolerance = data["tolerance"]
    result = compare_two_signatures(ethalon_signature, comparable_signature, tolerance)

    return {"percentageOfMatch": result}, 200

@app.route('/signature/compare/server', methods=['PUT'])
def compare_signature_with():
    data = request.get_json()
    comparable_signature = data["comparingSignature"]
    tolerance = data["tolerance"]
    signature_id = data["signatureId"]

    ethalon_data = signature_service.find_by_id(signature_id)
    ethalon_signature = ethalon_data.signature

    result = compare_two_signatures(ethalon_signature, comparable_signature, tolerance)

    return {"percentageOfMatch": result}, 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

