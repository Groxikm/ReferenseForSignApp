from flask import Flask, render_template, request, redirect, url_for, Response
from flask_cors import cross_origin, CORS
import datetime
from token_service import TokenServiceImpl
import security
from authorisation_service import authorisation_service as auth
from mongo_orm import mongo_db
from posts_service import service as posts_service_file
import settings

app = Flask(__name__)
token_service = TokenServiceImpl()
security_service = security.EndpointsSecurityService()
authorisation_service = auth.AutorisationServise()

# posts service setting
posts_service = posts_service_file.PostsService(
        mongo_db.MongoRepository(
            settings.DB_CONNECTION_STRING, "order_of_stake_db", "posts"))


CORS(app)


aboutDto = {
        "text": "The Order of Stake was founded in 2024 by individuals for individuals.",
        "slogan": "Brotherhood for friends, equality for foes!"
    }


#  Hello message
@app.route('/greets', methods=['GET'])
def greet():
    return {"greeting": "GREETS, ORDER!"}, 200


@app.route('/auth/token', methods=['GET'])
def validate_access_token():
    error_message = security_service.secure_by_validation_of_jwt(request.headers.get('accessToken'))
    if error_message == None:
        return {"message": "OK"}, 200


@app.route('/authorised/about', methods=['GET'])
def aboutOrder():
    error_message = security_service.secure_by_validation_of_jwt(request.headers.get('accessToken'))
    if error_message == None:
        return aboutDto, 200
    else: 
        return error_message, 401

@app.route('/auth/login', methods=['GET'])
def login():
    # Получение всех заголовков
    request_headers = request.headers

    # Пример получения конкретного заголовка
    username = "" + str(request_headers.get('username'))
    password = "" + str(request_headers.get('password'))

    if username == "": username = "null"
    if password == "": password = "null"


    if authorisation_service.check_credentials(username, password) == False:
        return security.ErrorMessage("Credentials check failed!").get_dto(), 403

    return {"accessToken": token_service.encode(username)}, 200


@app.route('/authorised/greet', methods=["GET"])
def auth_greet():
    error_message = security_service.secure_by_validation_of_jwt(request.headers.get('accessToken'))
    if error_message != None:
        return error_message, 401

    return {"greeting": "HELLO, KNIGHT!"}, 200


# Posts
@app.route('/authorised/posts', methods=["GET"])
def get_posts():
    # authentication check
    error_message = security_service.secure_by_validation_of_jwt(request.headers.get('accessToken'))
    if error_message != None:
        return error_message, 401
    
    arguments = request.args
    
    posts = posts_service.find_all_by_page(arguments.get("last_post_id"), int(arguments.get("page_size")))
    post_dtos = list()
    
    for post in posts:
        post_dtos.append(post.to_web_dto())
    
    return {"posts": post_dtos}, 200


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
