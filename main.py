import utime
from machine import Pin, SPI
import sdcard
import os
import busio
import RPi.GPIO as GPIO
import time
import digitalio
import board
import adafruit_ssd1306
import adafruit_sdcard
import adafruit_rfm9x

# Inicializando o buzzer
buzzer = Pin(13, Pin.OUT)
buzzer.value(1)
utime.sleep(1)
buzzer.value(0)

# Inicializando o módulo LoRa
spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
cs = digitalio.DigitalInOut(board.GP17)
reset = digitalio.DigitalInOut(board.GP20)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)

# Inicializando o cartão microSD
spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP12)
cs = digitalio.DigitalInOut(board.GP9)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = os.VfsFat(sdcard)
os.mount(vfs, "/sd")

#definindo pino do sensor
SENSOR_PIN = (número do pino não achei pcb)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

while True:
    if GPIO.input(SENSOR_PIN):
    time.sleep(0.1)

    # Envio dos dados via LoRa
    rfm9x.send(bytes("Dados do sensor", "utf-8"))

    # Salvando os dados no cartão microSD
    with open("/sd/dados.txt", "a") as arquivo:
        arquivo.write("Dados do sensor\n")

    # Aguardando 5 segundos
    utime.sleep(5)
