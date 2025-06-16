# dht11_reader.py
# Dit script leest de temperatuur van een DHT11 sensor uit.
# Zorg dat je de benodigde bibliotheken hebt geïnstalleerd: Adafruit_DHT

import Adafruit_DHT
import time

# Stel het type sensor in
DHT_SENSOR = Adafruit_DHT.DHT11
# Stel de GPIO pin in waarop de DHT11 is aangesloten (bijvoorbeeld 4)
DHT_PIN = 4

def lees_temperatuur():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temp={temperature:.1f}C  Luchtvochtigheid={humidity:.1f}%")
        return temperature
    else:
        print("Sensor niet gevonden of fout bij uitlezen!")
        return None

if __name__ == "__main__":
    while True:
        lees_temperatuur()
        time.sleep(2)
