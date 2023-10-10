from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    var = 'Amir'
    return render_template('basic.html', var=var)

if __name__ == '__main__':
    app.run(debug=True)