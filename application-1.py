from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Web App!</h1><p>This is your first Flask app.</p>"

if __name__ == "__main__":
    app.run(debug=True)

