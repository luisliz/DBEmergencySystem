from flask import Flask
from flask_restful import Resource, Api
from handlers import user, resources, dashboard

app = Flask(__name__)
api = Api(app)

app.register_blueprint(user.user_bp, url_prefix="/user") #Register supplier, admin, need
app.register_blueprint(resources.resources_bp, url_prefix="/resources")
app.register_blueprint(dashboard.dashboard_bp, url_prefix="/dashboard")


def main():
    app.run()

if __name__ == '__main__':
    main()
