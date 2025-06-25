from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Jenkins + Docker App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                text-align: center;
                padding-top: 100px;
            }
            .container {
                background: white;
                padding: 40px;
                margin: auto;
                width: 60%;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 1.2em;
                color: #555;
            }
            .footer {
                margin-top: 50px;
                font-size: 0.9em;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Welcome to My Jenkins + Docker Flask App</h1>
            <p>This app was built using:</p>
            <ul style="text-align:left; display:inline-block;">
                <li>Python & Flask for the web server</li>
                <li>Docker to containerize the application</li>
                <li>Jenkins for Continuous Integration</li>
                <li>GitHub as the source code repository</li>
            </ul>
            <p>Every time I push code, Jenkins builds & deploys automatically!</p>
            <div class="footer">
                Built by Suffyan Ali — CI/CD Enthusiast
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

