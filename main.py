import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(17,IO.IN)

tempo_inicial = time.time()

valores = []
flag = False

try:
    while True:

        if not IO.input(17):
            if flag:
                flag = False
                tempo_atual = time.time()
                tempo = tempo_atual - tempo_inicial
                valores.append(tempo)
                print(tempo)
        else:
            flag = True

except:
    IO.cleanup()
