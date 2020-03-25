from flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
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
