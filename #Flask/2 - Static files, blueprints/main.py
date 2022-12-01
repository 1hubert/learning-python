from flask import Flask

# importing folder admin as a package
import admin

app = Flask(__name__)
# the prefix is what has to come first to look at second.py
# in this case it's always looking at second.py for routes
# app.register_blueprint(second, url_prefix='')

app.register_blueprint(admin.second, url_prefix='/admin')

@app.route('/')
def test():
    return '<h1>Test</h1>'


if __name__ == '__main__':
    app.run(debug=True)