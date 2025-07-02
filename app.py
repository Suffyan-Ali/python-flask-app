from flask import Flask, render_template_string

app = Flask(__name__)

# Bootstrap HTML base template
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
        <li class="nav-item">
          <a class="nav-link{% if active=='home' %} active{% endif %}" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link{% if active=='about' %} active{% endif %}" href="/about">About</a>
        </li>
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
            <p class="mt-3">Thiss web app was automatically built and deployed using Jenkins whenever code is pushed to GitHub.</p>
            <p>Created by <strong>Suffyan Ali</strong>, a passionate learner of DevOps and CI/CD practices.</p>
        </div>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

