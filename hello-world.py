from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open("version.txt", 'r') as f:
        version = f.read()

    return f'Hello From sckn.dev !<br><b>Build Number:</b> <span style="color:red">{version}</span>'

app.run(host='0.0.0.0',debug=True, port=5000)
