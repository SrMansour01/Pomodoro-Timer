import time
import os

def pomodoro(tempo_trabalho, tempo_pausa_curta, tempo_pausa_longa, ciclos):
    for ciclo in range(ciclos):
        # Trabalho
        print(f"Começando o ciclo {ciclo + 1} de trabalho.")
        countdown(tempo_trabalho)
        os.system("clear")  # Limpa o terminal (Linux/macOS)
        
        # Pausa curta
        print("Hora de uma pausa curta.")
        countdown(tempo_pausa_curta)
        os.system("clear")
        
        # Pausa longa (após 4 ciclos de trabalho)
        if ciclo < ciclos - 1:
            print("Hora de uma pausa longa.")
            countdown(tempo_pausa_longa)
            os.system("clear")

def countdown(tempo_em_minutos):
    tempo_em_segundos = tempo_em_minutos * 60
    while tempo_em_segundos > 0:
        minutos, segundos = divmod(tempo_em_segundos, 60)
        print(f"{minutos:02}:{segundos:02}", end="\r")
        time.sleep(1)
        tempo_em_segundos -= 1
    print("00:00")

if __name__ == "__main__":
    tempo_trabalho = 25
    tempo_pausa_curta = 5
    tempo_pausa_longa = 15
    ciclos = 4
    
    pomodoro(tempo_trabalho, tempo_pausa_curta, tempo_pausa_longa, ciclos)
