import sqlite3
import time

from fingerprint_sensor import FingerprintSensor  # Replace with actual library for your sensor

# Initialize the fingerprint sensor
sensor = FingerprintSensor()

# Connect to the SQLite database
conn = sqlite3.connect('fingerprints.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS fingerprints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fingerprint_data BLOB NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

def save_fingerprint(data):
    cursor.execute('INSERT INTO fingerprints (fingerprint_data) VALUES (?)', (data,))
    conn.commit()

try:
    while True:
        print("Waiting for fingerprint...")
        fingerprint_data = sensor.read_fingerprint()
        
        if fingerprint_data:
            print("Fingerprint detected, saving to database...")
            save_fingerprint(fingerprint_data)
            print("Fingerprint saved.")
        
        time.sleep(1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    print("Exiting...")

finally:
    conn.close()
    sensor.close()