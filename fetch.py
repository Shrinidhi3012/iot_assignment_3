import json
from datetime import datetime, timedelta

log_file = "sensor_log.json"

sensor_type = input("Enter sensor type (temperature/humidity/co2): ").strip().lower()
cutoff = datetime.utcnow() - timedelta(hours=5)

print(f"\nReading '{sensor_type}' values from the last 5 hours:\n")

try:
    with open(log_file, "r") as file:
        for line in file:
            try:
                record = json.loads(line)
                record_time = datetime.fromisoformat(record["timestamp"])

                if record_time >= cutoff and sensor_type in record:
                    print(f"{record_time}: {record[sensor_type]}")
            except Exception:
                continue
except FileNotFoundError:
    print(f"'{log_file}' not found. Please run the subscriber script first to generate logs.")
