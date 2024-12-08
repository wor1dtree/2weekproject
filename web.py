from flask import Flask, render_template, request
app = Flask(__name__)
userdata = "admin"
pddata = "admin"

@app.route('/', methods=['get'])
def main():
    return render_template('main.html')
    
@app.route('/', methods=['post'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if (userdata == username and pddata == password):
        return render_template('login.html')
    else:
        return render_template('main.html')

app.run(host = '0.0.0.0', port = 5000 )