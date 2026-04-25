# iot-motion-dashboard

IoT Motion Detection Dashboard (ESP32 + Flask Project)

## Overview

This project is a complete IoT-based Motion Detection System using ESP32, PIR sensor, and a Flask backend. The ESP32 reads motion data from a PIR sensor and sends it to a Python script via serial communication. The Python script forwards the data to a Flask API, which stores it in a database and displays it on a live web dashboard.

## Features

Real-time motion detection using PIR sensor
ESP32 to PC serial communication
Python API to send data to server
Flask backend with database storage
Live dashboard with auto-refresh
Recent motion data retrieval
End-to-end IoT pipeline

## Technologies Used

ESP32 (Arduino / PlatformIO)
PIR Motion Sensor
Python
Flask
Flask-SQLAlchemy
SQLite Database
HTML (Dashboard)
Serial Communication

## Project Structure

iot-motion-dashboard/
│
├── src/
│ └── main.cpp
│
├── app.py
├── api.py
├── iot.db
│
├── templates/
│ └── index.html
│
└── README.md

## How to Run

install python (VS Code)
Install required libraries:
pip install flask flask_sqlalchemy requests pyserial

Upload code to ESP32

Connect ESP32 to PC (check COM port)

Run Flask server:
python app.py

Run API script (serial to server):
python api.py

Open browser:
http://127.0.0.1:5000/

## How It Works

ESP32 reads PIR sensor value:
1 → Motion detected
0 → No motion

Data is sent via serial to Python script

api.py reads serial data and sends it to Flask API

Flask server receives data and stores it in SQLite database

Dashboard fetches latest data every 2 seconds

Displays:
Motion detected → Alert message
No motion → Safe status

API Endpoints

POST /add → Save motion data
GET /data → Get latest motion records
GET / → Dashboard UI

## Future Improvements

Add real-time notifications (Telegram / Email)
Add camera integration for security system
Deploy on cloud server
Add multiple sensor support
Add data analytics and logs
Integrate with mobile app

## Author
Harsha G
Learning Python | Embedded Systems | IoT
