# python bridge..

import serial
import requests

ser = serial.Serial('COM10', 115200)

while True:
    line = ser.readline().decode().strip()

    print("Raw:", line)

    if line in ['0', '1']:
        motion = int(line)

        try:
            res = requests.post(
                "http://127.0.0.1:5000/add",
                json={"motion": motion}
            )

            print("Sent:", motion, "| Status:", res.status_code)

        except Exception as e:
            print("Error:", e)
