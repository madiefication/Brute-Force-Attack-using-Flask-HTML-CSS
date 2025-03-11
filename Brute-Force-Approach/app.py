from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Random credentials for demonstration
USERNAME = 'admin'
PASSWORD = 'letmein'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('success'))
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
