import threading, time

state = threading.Lock()

def eat(id):
    list_perE.append(id)
    list_1 = n_personas
    list_2 = list_perE
    set_difference = set(list_1) - set(list_2)
    personas_waiting = list(set_difference)
    print("Persona " + str(id) + " comiendo...", end = ' ')
    print(f"Personas esperando: {personas_waiting}")

def take_chopsticks(id, chopsticks_left, chopsticks_right):
    msg = f"Persona {id} tomando los palillos" 
    print("-" * len(msg) + "\n" + msg)
    chopsticks_left += 1
    chopsticks_right += 1
    chopsticks_total = chopsticks_left + chopsticks_right
    if (chopsticks_total == 2):
        msg = "Persona " + str(id) + " tomo los dos palillos"
        print(msg)
        eat(id)
    else:
        print(f"La persona {id} no tomo los palillos")
    
    
class Persona(threading.Thread):
    def __init__(self, id, chopsticks_left, chopsticks_right):
        threading.Thread.__init__(self)
        self.id = id
        self.chopsticks_left = chopsticks_left
        self.chopsticks_right = chopsticks_right
    
    def run(self):
        state.acquire()
        take_chopsticks(self.id, self.chopsticks_left, self.chopsticks_right)
        time.sleep(3)
        state.release()
        print("Persona " + str(self.id) + " termino de comer y dejo los palillos")
        

n_personas=[1,2,3,4,5,6,7,8]
personas = []
list_perE = []

for x in n_personas:
    personas.append(Persona(n_personas[x-1], 0, 0))

for p in personas:
    p.start()