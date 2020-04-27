from flask import Blueprint, url_for, flash, request
from app.handlers.users import UserHandler
from app.handlers.user_category import UserCategoryHandler
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        return UserHandler().add_user(request.form) #Done
    else:
        if not request.args:
            return UserHandler().get_all_users() #DONE
        else:
            return UserHandler().search_users(request.args)

@user_bp.route('/<int:user_id>', methods=['GET', 'DELETE'])
def get_user(user_id):
    if request.method == 'GET':
        return UserHandler().getUserById(user_id) #Done
    elif request.method == 'DELETE':
        return UserHandler().delete_user_byid(user_id)


@user_bp.route('/categories', methods=['GET']) #Done
def get_ranks():
    if request.method == 'GET':
        return UserCategoryHandler().get_all_categories() #DONE

@user_bp.route('/categories/<string:category>', methods=['GET']) #Done
def get_users_from_ranks(category):
    if request.method == 'GET':
        return UserHandler().getUsersByCategory(category) #Done

@user_bp.route('/categories/count', methods=['GET']) #Done
def count_ranks():
    if request.method == 'GET':
        return UserCategoryHandler().countCategories() #Done

# @app.route('/login', methods=['POST'])
# def login():
#     if request.method == 'POST':
#         if current_user.is_authenticated:
#             return redirect(url_for('index'))
#         form = LoginForm()
#         if form.validate_on_submit():
#             user = User.query.filter_by(username=form.username.data).first()
#             if user is None or not user.check_password(form.password.data):
#                 flash('Invalid username or password')
#                 return redirect(url_for('login'))
#             login_user(user, remember=form.remember_me.data)
#             return redirect(url_for('index'))

@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        return UserHandler().logout_user(request.form)

@user_bp.route('/delete', methods=['DELETE'])
def deleteuser():
    if request.method == 'DELETE':
        return UserHandler().delete_user(request.form)

@user_bp.route('/update/{uid}', methods=['PUT'])
def settings(uid):
    if request.method == 'PUT':
        return UserHandler().update_user(uid, request.form)

@user_bp.route('/count', methods=['GET'])
def count_users():
    if request.method == 'GET':
        return UserHandler().count_users()



