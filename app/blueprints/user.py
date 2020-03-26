from flask import Blueprint, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

user_bp = Blueprint('user', __name__)


user_ranks = {
    1: 'admin',
    2: 'provider',
    3: 'supplier',
    4: 'user'
}

@user_bp.route('/')
def index():
    return "Welcome to user"

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if(user_id in users):
        return users[user_id]
    return {'error': "User not found"}

@user_bp.route('/check_user_categories/<int:user_id>', methods=['GET'])
def check_rank(user_id):
    pass

@user_bp.route('/register', methods=['POST'])
def register():
    password_hash = generate_password_hash(password)
    pass

    # return render_template('login.html', title='Sign In', form=form)
# @user_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     if(check_password_hash(self.password_hash, password)):
#         return True
#     else:
#         return False
#     pass

@user_bp.route('/logout', methods=['GET', 'POST'])
def login():
    pass


@user_bp.route('/activate', methods=['POST'])
def activate():
    pass

@user_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    pass
