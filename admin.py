from flask import Flask, render_template, request, jsonify, redirect, url_for, session

app = Flask(__name__)

# Set your admin credentials (for demonstration purposes)
admin_credentials = {
    'username': 'admin',
    'password': 'password123'  # In production, store hashed passwords
}

# Admin login route
@app.route('/admin_login', methods=['POST'])
def admin_login():
    data = request.json
    entered_username = data.get('username')
    entered_password = data.get('password')
    
    if entered_username == admin_credentials['username'] and entered_password == admin_credentials['password']:
        # Store username in session
        session['username'] = entered_username
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

# Admin dashboard route requiring authentication
@app.route('/admin')
def admin_dashboard():
    # Check if user is logged in
    if 'username' not in session:
        return redirect(url_for('admin_login'))
    
    # Render admin dashboard
    return render_template('admin_dashboard.html')

# Admin logout route
@app.route('/admin_logout')
def admin_logout():
    # Clear the session
    session.pop('username', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
