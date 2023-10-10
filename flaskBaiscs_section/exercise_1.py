from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Welcome to the webpage for converting names!</h2>'

def convert_func(value):
    if not value.endswith('y'):
        res = value + 'y'
    else:
        res = value[:-1] + 'iful'
    return res

@app.route('/puppy/<name>')
def convert_name(name):
    return f'<h3>{name} after conversion is: {convert_func(name)}.</h3>'

if __name__ == '__main__':
    app.run(debug=True)
    