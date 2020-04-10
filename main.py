import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)

tempoInicio = time.time()
registrar = False

def calcularTempo(channel):

    GPIO.remove_event_detect(17)
    
    global tempoInicio
    global registrar

    if registrar:
        tempoDecorrido = time.time() - tempoInicio
        print(f'Intervalo : {tempoDecorrido:.3f}')
        tempoInicio = time.time()

        registrar = False
    else:
        registrar = True

    GPIO.add_event_detect(17,GPIO.BOTH,callback = calcularTempo, bouncetime = 10)
   
GPIO.add_event_detect(17,GPIO.BOTH,callback=calcularTempo,bouncetime=10)

print('Pressione ctrl+c para sair')
try:
    while True:
       print('Aguardando evento...')
       time.sleep(5)

except KeyboardInterrupt:
    pass

print('\nExecução Finalizada!')
GPIO.cleanup()
