# -*- coding: utf-8 -*-

from random import randint
from random import seed


pacientes = []

class Paciente(object):
    def __init__(self, id):
        self.id = id

    def en_consulta(self):
        print ("El paciente {} esta siento atendido".format(self.id))

    def llegada(self):
        return  randint(1, 10)

def asignar_paciente(paciente):
    global pacientes
    aux = paciente.llegada()
    pacientes.append((paciente, aux))
    pacientes = sorted(pacientes, key=lambda tup: tup[1], reverse= True)


def atender():
    global ocupado
    if ocupado == 0:
        if len(pacientes) != 0:
            p = pacientes[0]
            ocupado = p[1]
            p[0].en_consulta()
            pacientes.pop(0)

ocupado = 0
time_simulation = 36
id_r = 1
seed(35)
for i in range(0, time_simulation):
  if i%3 == 0:
    id_r += 1
    test = Paciente(id_r)
    asignar_paciente(test)
  
  atender()
  ocupado -= 1


