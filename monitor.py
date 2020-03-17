import time
import subprocess

import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


RST = 24
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height

image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()
font = ImageFont.truetype('Montserrat-Medium.ttf', 16)
while True:

    draw.rectangle((0,0,width,height), outline=0, fill=0)

#    cmd = "hostname -I | cut -d' \' -f1 | head --bytes -1"
#    IP = subprocess.check_output(cmd, shell = True )
#    draw.text((0, height//2), str(IP),  font=font, fill=255)
    draw.text((0, height//2), "Teste na Tela",  font=font, fill=255)

    disp.image(image)
    disp.display()
    time.sleep(5)
