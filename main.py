import RPi.GPIO as GPIO
import time

"""
import Adafruit_SSD1306 as SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
disp = SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()
font = ImageFont.truetype('Montserrat-Medium.ttf', 16)

"""

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)

tempoInicio = time.time()
iniciarContagem = True

def calcularTempo(channel):
    GPIO.remove_event_detect(17)
    
    global tempoInicio
    global iniciarContagem

    if iniciarContagem:
        tempoDecorrido = time.time() - tempoInicio
        print(f'Intervalo {tempoDecorrido:.3f}')
        tempoInicio = time.time()
        iniciarContagem = False
    else:
        iniciarContagem = True

    GPIO.add_event_detect(17,GPIO.BOTH,callback = calcularTempo, bouncetime = 10)
   
GPIO.add_event_detect(17,GPIO.BOTH,callback=calcularTempo,bouncetime=10)

print('Pressione ctrl+c para sair')
try:
    while True:
       # draw.rectangle((0,0,width,height), outline=0, fill=0)
       # draw.text((0, height//2), f'Teste',  font=font, fill=255)
       # disp.image(image)
       # disp.display()
       print('Aguardando evento...')
       time.sleep(5)

except KeyboardInterrupt:
    pass

print('\nExecução Finalizada!')
GPIO.cleanup()
