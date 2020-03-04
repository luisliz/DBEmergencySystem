from flask import Flask 
from flask_restful import Resource, Api
from handlers import user, resources, dashboard

app = Flask(__name__)
api = Api(app)

app.register_blueprint(url_prefix="/user") #Register supplier, admin, need
app.register_blueprint(url_prefix="/resources")
app.register_blueprint(url_prefix="/dashboard")

if __name__ == '__main__': 
    app.run()
