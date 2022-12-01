from flask import Blueprint, render_template

# referencing the original static and template folders
# but it can be custom folders
second = Blueprint('second', __name__, static_folder='static', template_folder='templates')


# this function can be accesed by both of these different roots
@second.route('/home')
@second.route('/')
def home():
    return render_template('home.html')