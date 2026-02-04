from flask import Flask, render_template_string
import socket

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }
        h1 { color: #667eea; }
        .info { color: #666; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 DevOps Project</h1>
        <p>Application déployée avec succès !</p>
        <div class="info">
            <p>Hostname: {{ hostname }}</p>
            <p>Version: 1.0.0</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, hostname=hostname)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
