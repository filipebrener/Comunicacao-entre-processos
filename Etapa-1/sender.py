import signal
import os
import time
import argparse

parser = argparse.ArgumentParser(description='Recebimento do PID')
# Adicionar argumento com o método add_argument()
parser.add_argument('-p','--pid',type=int, help='PID do processo')
argument = parser.parse_args()
pid = argument.pid

if __name__ =='__main__':
    time.sleep(3)
    os.kill(int(pid), signal.SIGUSR1)
    time.sleep(3)
    os.kill(int(pid), signal.SIGUSR2)
    time.sleep(3)
    os.kill(int(pid), signal.SIGKILL)