IoT Assignment 3 – CIS600 Spring 2025

This project simulates a cloud-based IoT system using AWS IoT Core. It includes virtual sensors, MQTT-based data publishing, data logging, and historical data retrieval.

Files
- AWS files that will be use for access to aws
- `python_script.py` – Publishes random sensor data (temperature, humidity, CO2) to AWS IoT using MQTT.
- `subscribe.py` – Subscribes to the topic and logs incoming data with timestamps to `sensor_log.json`.
- `fetch.py` – Fetches and displays data for a specified sensor from the last 5 hours by reading `sensor_log.json`.
- 'sensor_log.json' store the values from subscribe.py

Features
- Uses AWS IoT Core with X.509 certificate-based authentication.
- Simulates a virtual environmental station with realistic sensor values.
- Logs timestamped sensor data locally.
- Allows time-based filtering of sensor values.

Setup
1. Configure AWS IoT Core with a Thing and certificates.
2. Replace file paths and credentials in all scripts (`endpoint`, `certificate`, `private_key`, etc.).
3. Run `python_script.py` to start publishing data.
4. In a separate terminal, run `subscribe.py` to log incoming data.
5. Use `fetch.py` to query data for the last 5 hours.
