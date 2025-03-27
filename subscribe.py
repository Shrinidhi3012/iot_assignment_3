from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
from datetime import datetime

client_id = "assignment_3_subscriber"
endpoint = "a2j9tq5ho5rt78-ats.iot.us-east-2.amazonaws.com"
root_ca = "AmazonRootCA1.pem"
private_key = "c610b9c254393f1ff9da6a083348aa6f9abcd4aa57ddc4e37247a6f993ad640e-private.pem.key"
certificate = "c610b9c254393f1ff9da6a083348aa6f9abcd4aa57ddc4e37247a6f993ad640e-certificate.pem.crt"

topic = "iot/env/station1"
log_file = "sensor_log.json"

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        data["timestamp"] = datetime.utcnow().isoformat()

        with open(log_file, "a") as f:
            f.write(json.dumps(data) + "\n")

        print(f"Logged: {data}")
    except Exception as e:
        print(f"Failed to log message: {e}")

mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint(endpoint, 8883)
mqtt_client.configureCredentials(root_ca, private_key, certificate)

mqtt_client.connect()
mqtt_client.subscribe(topic, 1, on_message)

print(f"Subscribed to {topic}. Logging incoming data...")
while True:
    pass
