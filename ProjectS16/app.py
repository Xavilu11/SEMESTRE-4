from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template("index.html")

# Página "Acerca de"
@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)