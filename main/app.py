from flask import Flask
from task import bp as task_bp

app = Flask(__name__)
app.register_blueprint(task_bp, url_prefix='/task')

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
