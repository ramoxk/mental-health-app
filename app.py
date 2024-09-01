from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Detailed Check-In
@app.route('/checkin', methods=['GET', 'POST'])
def checkin():
    if request.method == 'POST':
        mood = request.form['mood']
        return redirect(url_for('guide', mood=mood))
    return render_template('checkin.html')

# Step-by-Step Guide
@app.route('/guide/<mood>')
def guide(mood):
    exercises = {
        "happy": [
            "Keep up your positive habits!",
            "Share your joy with others.",
            "Consider setting new goals to maintain your happiness."
        ],
        "sad": [
            "Write down what's troubling you in your journal.",
            "Try a grounding exercise: Name 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste.",
            "Consider reaching out to a loved one or a professional."
        ],
        "anxious": [
            "Try deep breathing: Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds.",
            "Write down your worries and then challenge them with rational responses.",
            "Practice mindfulness by focusing on the present moment."
        ],
        "angry": [
            "Engage in physical activity: Go for a run, do some push-ups, or simply take a walk.",
            "Practice deep breathing to calm your nervous system.",
            "Identify the source of your anger and write down possible solutions."
        ]
    }
    return render_template('guide.html', mood=mood, exercises=exercises.get(mood, []))

# Meditation/Breathing Exercises
@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

# Journaling Section
@app.route('/journal', methods=['GET', 'POST'])
def journal():
    if request.method == 'POST'):
        entry = request.form['entry']
        # Save the entry to a file or database (not implemented here)
        return render_template('journal.html', success=True)
    return render_template('journal.html')

# Emergency Contact Information
@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
