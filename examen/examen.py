import threading, time

state = threading.Lock()

def comer(id):
    print("Persona " + str(id) + " tomo los dos palillos")
    list_1 = n_personas
    list_2 = [id]
    set_difference = set(list_1) - set(list_2)
    personas_esperando = list(set_difference)
    print(f"Personas esperando: {personas_esperando}")
    print("Persona " + str(id) + " comiendo...", end = ' ')
    time.sleep(2)
    
class Persona(threading.Thread):
    def __init__(self, id, ):
        threading.Thread.__init__(self)
        self.id = id
    
    def run(self):
        state.acquire()
        comer(self.id)
        state.release()
        print("Persona " + str(self.id) + "  termino de comer y dejo los palillos")
        

n_personas=[1,2,3,4,5,6,7,8]
personas = []

for x in n_personas:
    personas.append(Persona(n_personas[x-1]))

for p in personas:
    p.start()