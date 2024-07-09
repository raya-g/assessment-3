from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Mock data for quizzes (replace with actual data retrieval logic)
quizzes = [
    {"name": "Quiz 1", "url": "/quiz1"},
    {"name": "Quiz 2", "url": "/quiz2"},
    {"name": "Quiz 3", "url": "/quiz3"}
]

# Home page route
@app.route('/')
def home():
    return render_template('index.html')

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Profile page route (example)
@app.route('/profile')
def profile():
    # Example: Check if user is logged in, redirect to login if not
    if 'username' not in session:
        return redirect(url_for('login'))
    # Render profile page
    return render_template('profile.html')

# API endpoint to fetch quizzes
@app.route('/api/quizzes', methods=['GET'])
def get_quizzes():
    return jsonify({"success": True, "quizzes": quizzes})

if __name__ == '__main__':
    app.run(debug=True)
