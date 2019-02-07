import time
import sys
import json
import paho.mqtt.client as mqtt

def blink_led(n_times):
	try:
		from gpiozero import LED
		from gpiozero.exc import BadPinFactory
		led = gpiozero.LED(17)
		print("Blink!")
		for i in range(n_times):
			led.on()
			time.sleep(0.5)
			led.off()
			time.sleep(0.5)
	except BadPinFactory as e:
		print(e)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	on_connect_msg = f'Connected with result code {rc}'
	print(on_connect_msg)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
	client.subscribe("aindustriosa/blink")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	decode_data = msg.payload.decode("utf-8","ignore")
	data = json.loads(decode_data)
	blink_data = data.get("blink", None)
	if blink_data:
		blink_msg = f'{msg.topic} {str(msg.payload)}'
		print(blink_msg)
		blink_led(blink_data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()