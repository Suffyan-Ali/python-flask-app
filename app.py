from flask import Flask, render_template_string

app = Flask(__name__)

# Base Bootstrap Template
base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">CI/CD App</a>
    <div class="collapse navbar-collapse">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item"><a class="nav-link{% if active=='home' %} active{% endif %}" href="/">Home</a></li>
        <li class="nav-item"><a class="nav-link{% if active=='about' %} active{% endif %}" href="/about">About</a></li>
        <li class="nav-item"><a class="nav-link{% if active=='workflow' %} active{% endif %}" href="/workflow">Workflow</a></li>
      </ul>
    </div>
  </div>
</nav>
<div class="container mt-5">
    {{ content|safe }}
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(base_template, title="Home", active="home", content="""
        <div class="text-center">
            <h1 class="mb-4">🚀 Welcome to AWS + Docker Flask App</h1>
            <p class="lead">This app demonstrates a CI/CD pipeline using:</p>
            <ul class="list-group list-group-flush w-50 mx-auto">
                <li class="list-group-item">Python & Flask</li>
                <li class="list-group-item">Docker</li>
                <li class="list-group-item">Jenkins</li>
                <li class="list-group-item">GitHub</li>
            </ul>
        </div>
    """)

@app.route("/about")
def about():
    return render_template_string(base_template, title="About", active="about", content="""
        <div class="text-center">
            <h2>About This Project</h2>
            <p class="mt-3">This web app was automatically built and deployed using a full CI/CD pipeline.</p>
            <p>Created by <strong>Suffyan Ali</strong>, a passionate learner of DevOps and cloud automation.</p>
        </div>
    """)

@app.route("/workflow")
def workflow():
    return render_template_string(base_template, title="CI/CD Workflow", active="workflow", content="""
        <h2 class="text-center mb-4">⚙️ CI/CD Workflow Overview</h2>
        <div class="row text-center">
            <div class="col-md-2 offset-md-1">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">1️⃣ GitHub</h5>
                        <p class="card-text">Push code to GitHub repository</p>
                    </div>
                </div>
            </div>
            <div class="col-md-2">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">2️⃣ CodePipeline</h5>
                        <p class="card-text">Detects changes and triggers CodeBuild</p>
                    </div>
                </div>
            </div>
            <div class="col-md-2">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">3️⃣ CodeBuild</h5>
                        <p class="card-text">Builds Docker image and pushes to ECR</p>
                    </div>
                </div>
            </div>
            <div class="col-md-2">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">4️⃣ Amazon ECR</h5>
                        <p class="card-text">Stores versioned Docker images</p>
                    </div>
                </div>
            </div>
            <div class="col-md-2">
                <div class="card shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">5️⃣ Amazon ECS</h5>
                        <p class="card-text">Deploys new image to running service</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-5 text-center">
            <p class="lead">🎉 Application is updated live after every code push!</p>
        </div>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


