from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>Python Flask Demo</title></head>
    <body style="text-align:center; font-family:Arial; padding:80px;">
        <h1>🚀 Python Flask CI/CD</h1>
        <h2>Successfully Deployed!</h2>
        <p>Powered by Huawei Cloud CodeArts</p>
        <h3>Version 1.0</h3>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
