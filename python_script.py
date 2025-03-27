from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import random
import json
import time

client_id = "assignment_3_thing"
endpoint = "a2j9tq5ho5rt78-ats.iot.us-east-2.amazonaws.com"
root_ca = "AmazonRootCA1.pem"
private_key = "c610b9c254393f1ff9da6a083348aa6f9abcd4aa57ddc4e37247a6f993ad640e-private.pem.key"
certificate = "c610b9c254393f1ff9da6a083348aa6f9abcd4aa57ddc4e37247a6f993ad640e-certificate.pem.crt"

mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint(endpoint, 8883)
mqtt_client.configureCredentials(root_ca, private_key, certificate)
mqtt_client.configureOfflinePublishQueueing(-1)
mqtt_client.configureDrainingFrequency(2)

mqtt_client.connect()

def generate_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": round(random.uniform(300, 2000), 2)
    }

while True:
    payload = json.dumps(generate_data())
    mqtt_client.publish("iot/env/station1", payload, 1)
    print(f"Published: {payload}")
    time.sleep(15)
