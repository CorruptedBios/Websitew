from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
users = [
    {'username': 'user1', 'password': 'pass1'},
    {'username': 'user2', 'password': 'pass2'}
]

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('video'))
        
        return redirect(url_for('login'))
    
    return render_template('login.html')

# Video page
@app.route('/video')
def video():
    return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=True)