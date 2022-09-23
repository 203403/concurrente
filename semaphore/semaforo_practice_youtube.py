import pytube
from threading import Thread, Semaphore
semaforo = Semaphore(1) # Crea la variable semaforo


def critico(id):
    global x;
    x = x + id
    print("Hilo =" + str(id) + " =>" + str(x))
    x = 1

def download_videos(id):
    video_urls = [
    'https://youtu.be/1rZsW0IWdIs',
    'https://youtu.be/AbCO4lW0G60',
    'https://youtu.be/Fw0-51X0t8I',
    'https://youtu.be/dnnh8unDP4Y',
    'https://youtu.be/ZF-w__uUs8c'
    ]
    pytube.YouTube(video_urls[id-1]).streams.first().download()
    print(f'{video_urls[id-1]} was downloaded...')  

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        
    def run(self):
        semaforo.acquire() # Inicializa semaforo, lo adquiere
        critico(self.id)
        download_videos(self.id)
        semaforo.release() # Libera un semaforo e incrementa la variable semáforo
    
threads_semaphore = [Hilo(1), Hilo(2), Hilo(3), Hilo(4), Hilo(5)]
x = 1;
for t in threads_semaphore:
    t.start()