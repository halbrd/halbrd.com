from flask import Flask, render_template

from views.bumps import bumps

app = Flask(__name__)

app.register_blueprint(bumps)

@app.route('/')
def index():
    return render_template('index/index.html')

if __name__ == '__main__':
    # debug mode - not for production
    app.run(host='0.0.0.0', debug=True, port=5000)
