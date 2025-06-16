# dht11_reader.py
# Dit script leest de temperatuur van een DHT11 sensor uit met gpiozero

try:
    from gpiozero import DHT11
    from time import sleep

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
    print("gpiozero niet gevonden. Installeer met: pip3 install gpiozero")
    exit(1)
