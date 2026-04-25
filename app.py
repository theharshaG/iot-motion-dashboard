#flask and database..

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    motion = db.Column(db.Integer)

# Create DB
with app.app_context():
    db.create_all()

# -------------------------------
# RECEIVE DATA FROM PYTHON
# -------------------------------
@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    motion = data.get('motion')

    new_data = Sensor(motion=motion)
    db.session.add(new_data)
    db.session.commit()

    return jsonify({"message": "Saved"})

# -------------------------------
# GET DATA
# -------------------------------
@app.route('/data')
def get_data():
    records = Sensor.query.order_by(Sensor.id.desc()).limit(10).all()

    return jsonify([
        {"id": r.id, "motion": r.motion}
        for r in records
    ])

# -------------------------------
# DASHBOARD
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
