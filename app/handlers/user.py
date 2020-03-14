from flask import Blueprint

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    return "Welcome to user"

@user_bp.route('/user/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id): 
    pass 

@user_bp.route('/login', methods=['GET', 'POST'])
def login(): 
    pass

@user_bp.route('/register', methods=['POST'])
def register(): 
    pass 

@user_bp.route('/activate', methods=['POST'])
def activate():
    pass 

@user_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    pass
