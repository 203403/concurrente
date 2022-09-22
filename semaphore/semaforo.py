from threading import Thread, Semaphore
semaforo = Semaphore(1) # Crea la variable semaforo

# wait (s) Decrementa el valor de s si este es mayor que cero
# signal (s) Desbloqua algún proceso bloqueado en s, y en el caso
# de que no haya ningún proceso incrementa el valor de s

def critico(id):
    global x;
    x = x + id
    print("Hilo =" + str(id) + " =>" + str(x))
    x = 1

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        
    def run(self):
        semaforo.acquire() # Inicializa semaforo, lo adquiere
        critico(self.id)
        semaforo.release() # Libera un semaforo e incrementa la variable semáforo
    
threads_semaphore = [Hilo(1), Hilo(2), Hilo(3)]
x = 1;
for t in threads_semaphore:
    t.start()