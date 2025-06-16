import dht11
import time
import RPi.GPIO as GPIO

# GPIO-instellingen
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Pin waarop de sensor is aangesloten
sensor_pin = 4

# Initialiseer de sensor
sensor = dht11.DHT11(pin=sensor_pin)

def lees_sensor():
    # Probeer gegevens van de sensor te lezen
    result = sensor.read()
    
    if result.is_valid():
        temperatuur = result.temperature
        luchtvochtigheid = result.humidity
        return temperatuur, luchtvochtigheid
    else:
        return None, None

if __name__ == '__main__':
    while True:
        temp, hum = lees_sensor()
        if temp is not None and hum is not None:
            print(f"Temperatuur: {temp}°C, Luchtvochtigheid: {hum}%")
        else:
            print("Sensor fout! Probeer opnieuw...")
        time.sleep(5)
