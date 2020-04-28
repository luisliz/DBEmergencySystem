from flask import Flask
from flask_restful import Resource, Api
from app.blueprints import dashboard, payment, user, resources, transaction, resource_category, request

app = Flask(__name__)

api = Api(app)

app.register_blueprint(user.user_bp,                           url_prefix="/users")  # Register supplier, admin, need
app.register_blueprint(resources.resources_bp,                 url_prefix="/resources")
app.register_blueprint(resource_category.resource_category_bp, url_prefix="/categories")
app.register_blueprint(dashboard.dashboard_bp,                 url_prefix="/dashboard")
app.register_blueprint(payment.payment_bp,                     url_prefix="/payment")
app.register_blueprint(transaction.transaction_bp,             url_prefix="/transaction")
app.register_blueprint(request.request_bp,                     url_prefix="/requests")

@app.route('/')
def hello_world():
    return 'Welcome to Emergency System app'

def main():
    app.run()


if __name__ == '__main__':
    main()
