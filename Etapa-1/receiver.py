import signal
import os
import threading

def init_python3_process(process_name, pid):
    chamada = 'python3 ' + process_name + ' -p ' + str(pid)
    os.system(chamada)

def receive_sigusr1(signum, stack):
    print('Recebido o sinal do usuário 1')
    signal.pause()

def receive_sigusr2(signum, stack):
    print('Recebido o sinal do usuário 2')
    signal.pause()

if __name__ =='__main__':
    os.system('clear')
    signal.signal(signal.SIGUSR1, receive_sigusr1)
    signal.signal(signal.SIGUSR2, receive_sigusr2)
    pid = os.getpid()
    t1 = threading.Thread(target=init_python3_process, args=('sender.py', pid,))
    t1.start()
    signal.pause()
