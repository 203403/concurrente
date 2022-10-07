import threading
import time
import random

PRODUCTORES = random.randint(1, 10)
CONSUMIDORES = PRODUCTORES
REPETICIONES = random.randint(20, 40)
MAX_SIZE_BODEGA = random.randint(50, 100)
BODEGA = []

class Productor(threading.Thread):
    producto = []
    conta = 0

    def __init__(self):
        super(Productor, self).__init__()
        self.id  = Productor.conta
        Productor.conta += 1
        Productor.producto.append(threading.Lock())

    
    def next(self):
        return (self.id + 1) % PRODUCTORES

    def espera(self):
        if self.id < self.next():
            Productor.producto[self.id].acquire()
            Productor.producto[self.next()].acquire()
            print(f"Productor {self.id} en espera...", end = ' ')
            print(f"Productor {self.next()} tambien esta en espera...")
        else:
            Productor.producto[self.next()].acquire()
            Productor.producto[self.id].acquire()
            print(f"Productor {self.next()} en espera...", end = ' ')
            print(f"Productor {self.id} tambien esta en espera...")
    
    def producir(self, cantidad):
        print(f"Productor {self.id} produciendo {cantidad} productos")
        for _ in range(cantidad):
            if(BODEGA.__len__() < (MAX_SIZE_BODEGA)):
                BODEGA.append(f"PRODUCTO {BODEGA.__len__()+1}")  
            else:
                break
        time.sleep(0.2)
        print(f"Productor {self.id} almaceno el/los productos producido(s)")

    def liberar(self):
        Productor.producto[self.id].release()
        Productor.producto[self.next()].release()
        
        
    
    def run(self):
        productos_random =  random.randint(1, 10)
        time.sleep(0.3)
        for i in range(REPETICIONES):
            self.espera()
            if (BODEGA.__len__() >= MAX_SIZE_BODEGA):
                print("ESPERANDO... BODEGA LLENA")
                time.sleep(1)  
            else:
                self.producir(productos_random)
            self.liberar()
                
            print(f"Cantidad de productos en la bodega: {BODEGA.__len__()}")  

class Consumidor(threading.Thread):
    producto = []
    conta = 0

    def __init__(self):
        super(Consumidor, self).__init__()
        self.id  = Consumidor.conta
        Consumidor.conta += 1
        Consumidor.producto.append(threading.Lock())

    
    def next(self):
        return (self.id + 1) % CONSUMIDORES

    def espera(self):
        if self.id < self.next():
            Consumidor.producto[self.id].acquire()
            Consumidor.producto[self.next()].acquire()
            print(f"Consumidor {self.id} en espera...", end = ' ')
            print(f"Consumidor {self.next()} tambien esta en espera...")
        else:
            Consumidor.producto[self.next()].acquire()
            Consumidor.producto[self.id].acquire()
            print(f"Consumidor {self.next()} en espera...", end = ' ')
            print(f"Consumidor {self.id} tambien esta en espera...")
    
    def consumir(self, cantidad):
        print(f"Consumidor {self.id} consumiendo {cantidad} productos")
        for _ in range(cantidad):
            if(BODEGA.__len__() > 0):
                BODEGA.pop() 
            else:
                break
        time.sleep(0.2)
        print(f"Consumidor {self.id} consumio los productos")

    def liberar(self):
        Consumidor.producto[self.id].release()
        Consumidor.producto[self.next()].release()
    
    def run(self):
        productos_random =  random.randint(1, 10)
        time.sleep(0.3)
        for i in range(REPETICIONES):
            self.espera()
            if (BODEGA.__len__() <= 0):
                print("ESPERANDO... BODEGA VACIA")
                time.sleep(1)
            else:
                self.consumir(productos_random)
            self.liberar()
            print(f"Cantidad de productos en la bodega: {BODEGA.__len__()}")  
              
def main():
    productores = []
    consumidores = []

    for i in range(PRODUCTORES):
        productores.append(Productor())
    
    for i in range(CONSUMIDORES):
        consumidores.append(Consumidor())

    for p in productores:
        if (p.is_alive() != True):
            p.start()
        
    for c in consumidores:
        if (c.is_alive() != True):
            c.start()

if __name__ == '__main__':
    print(f"Cantidad de Productores: {PRODUCTORES}")
    print(f"Cantidad de Consumidores: {CONSUMIDORES}")
    print(f"Repeticiones: {REPETICIONES}")
    print(f"Capacidad de la Bodega: {MAX_SIZE_BODEGA}")
    print(f"Cantidad Inicial de productos en la bodega: {BODEGA.__len__()}")
    time.sleep(2)  
    main()
