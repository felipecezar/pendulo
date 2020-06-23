import RPi.GPIO as GPIO
import time
import csv

t0 = time.time()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

dados = []

def gravarDados():
    with open('dados.csv','w',newline='') as f:
        arquivo = csv.writer(f)
        for dado in dados:
            arquivo.writerow([dado])

def calcularPeriodo(channel):
    global t0
    GPIO.remove_event_detect(17)  
    global dados
    tempo = time.time() - t0
    dados.append(f'{tempo:.3f}')
    print(f'{tempo:.3f}')
    GPIO.add_event_detect(17,GPIO.BOTH,callback = calcularPeriodo, bouncetime = 10)
   
GPIO.add_event_detect(17,GPIO.BOTH,callback=calcularPeriodo,bouncetime=10)

print('Pressione ctrl+c para sair')
try:
    while True:
       print('Aguardando evento...')
       time.sleep(5)

except KeyboardInterrupt:
    pass

gravarDados()
print('\nExecução Finalizada!')
GPIO.cleanup()
