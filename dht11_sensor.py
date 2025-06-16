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
    print("[DEBUG] lees_sensor() aangeroepen")
    # Probeer gegevens van de sensor te lezen
    result = sensor.read()
    print(f"[DEBUG] Raw sensor result: {result}")
    if result.is_valid():
        temperatuur = result.temperature
        luchtvochtigheid = result.humidity
        print(f"[DEBUG] Geldige data: Temp={temperatuur}, Hum={luchtvochtigheid}")
        return temperatuur, luchtvochtigheid
    else:
        print("[DEBUG] Ongeldige sensor data!")
        return None, None

if __name__ == '__main__':
    while True:
        temp, hum = lees_sensor()
        if temp is not None and hum is not None:
            print(f"Temperatuur: {temp}°C, Luchtvochtigheid: {hum}%")
        else:
            print("Sensor fout! Probeer opnieuw...")
        time.sleep(5)
