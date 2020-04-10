import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)

t0 = time.time()
flag = False

def calcularPeriodo(channel):

    GPIO.remove_event_detect(17)
    
    global t0
    global flag

    if flag:
        tempo = time.time() - t0
        print(f'Intervalo : {tempo:.3f}')
        t0 = time.time()

        flag = False
    else:
        flag = True

    GPIO.add_event_detect(17,GPIO.BOTH,callback = calcularPeriodo, bouncetime = 10)
   
GPIO.add_event_detect(17,GPIO.BOTH,callback=calcularPeriodo,bouncetime=10)

print('Pressione ctrl+c para sair')
try:
    while True:
       print('Aguardando evento...')
       time.sleep(5)

except KeyboardInterrupt:
    pass

print('\nExecução Finalizada!')
GPIO.cleanup()
