from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json
import config

app = Flask(__name__)

# MQTT Client setup
mqtt_client = mqtt.Client(config.MQTT_CLIENT_ID_FLASK)

# TLS configuration
mqtt_client.tls_set()

# Callback when the client receives a message
def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    data = json.loads(payload)
    print(f"Received message from topic {msg.topic}: {data}")
    # Here you can process the sensor data (e.g., store it in a database)

mqtt_client.on_message = on_message
mqtt_client.connect(config.MQTT_BROKER, config.MQTT_PORT, 60)
mqtt_client.subscribe(config.MQTT_TOPIC_SENSOR)
mqtt_client.loop_start()

@app.route('/control_valve', methods=['POST'])
def control_valve():
    action = request.json.get('action')
    if action in ['open_valve', 'close_valve']:
        mqtt_client.publish(config.MQTT_TOPIC_CONTROL, action)
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error', 'message': 'Invalid action'}), 400

@app.route('/get_moisture', methods=['GET'])
def get_moisture():
    # This endpoint could return the latest sensor data from your storage
    # For example:
    # return jsonify({'moisture_data': latest_data})
    return jsonify({'message': 'This endpoint is not yet implemented'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
