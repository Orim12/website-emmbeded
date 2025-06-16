# dht11_reader.py
# Leest DHT11 sensor uit via pigpio en dht11 community module
# Zorg dat pigpio draait: sudo systemctl start pigpiod
# Installeer de dht11 module: pip3 install dht11 pigpio

import pigpio
import dht11
import time

DHT_PIN = 4

pi = pigpio.pi()
sensor = dht11.DHT11(pi, DHT_PIN)

def lees_temperatuur():
    result = sensor.read()
    if result.is_valid():
        print(f"Temp={result.temperature}C  Luchtvochtigheid={result.humidity}%")
        return result.temperature
    else:
        print("Sensor niet gevonden of fout bij uitlezen!")
        return None

if __name__ == "__main__":
    while True:
        lees_temperatuur()
        time.sleep(2)
