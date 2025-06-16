# dht11_reader.py
# Dit script leest de temperatuur van een DHT11 sensor uit.
# Zorg dat je de benodigde bibliotheken hebt geïnstalleerd: Adafruit_DHT of gpiozero

# Gebruik Adafruit_DHT bibliotheek (voorheen)
try:
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

# Alternatief: gebruik de gpiozero bibliotheek met een DHT11 breakout (vanaf gpiozero 2.0)
# Let op: gpiozero ondersteunt DHT11 alleen op een Raspberry Pi met de juiste hardware
except ImportError:
    print("Adafruit_DHT niet gevonden. Probeer gpiozero in plaats daarvan.")
    try:
        from gpiozero import DHT11
        from time import sleep
        import board
        import digitalio

        # Stel de GPIO pin in waarop de DHT11 is aangesloten (bijvoorbeeld 4)
        dht_pin = 4
        sensor = DHT11(dht_pin)

        def lees_temperatuur():
            temp = sensor.temperature
            humidity = sensor.humidity
            if temp is not None and humidity is not None:
                print(f"Temp={temp:.1f}C  Luchtvochtigheid={humidity:.1f}%")
                return temp
            else:
                print("Sensor niet gevonden of fout bij uitlezen!")
                return None

        if __name__ == "__main__":
            while True:
                lees_temperatuur()
                sleep(2)

    except ImportError:
        print("gpiozero of benodigde modules niet gevonden. Installeer met: pip3 install gpiozero")
        exit(1)
