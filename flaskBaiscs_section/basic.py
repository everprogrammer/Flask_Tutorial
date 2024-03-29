from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy<h1>'

@app.route('/information')
def info():
    return '<h2>Puppies are great</h2>'

@app.route('/puppy/<name>')
def puppy(name):
    return f"<h3>This is a page for {name.upper()}!</h3>"

if __name__ == '__main__':
    app.run(debug=True)
