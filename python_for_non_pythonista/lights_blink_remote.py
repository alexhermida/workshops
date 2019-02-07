import paho.mqtt.client as mqtt

import argparse
import json

def publish():
    client = mqtt.Client()
    client.connect("test.mosquitto.org", 1883, 60)

    data = json.dumps({"blink": args.times})

    
    client.publish("aindustriosa/blink", data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blink leds!.')
    parser.add_argument('times', type=int, help='Number of times to blink')
    args = parser.parse_args()

    publish()
