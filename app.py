from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    roll = request.form.get('roll')
    section = request.form.get('section')
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Append student data to a single CSV file
    with open('students.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_datetime, name, roll, section])

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
