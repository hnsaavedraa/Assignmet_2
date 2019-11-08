# Assignmet_2

## Integrantes
* Jose Fernando Morantes Florez
* Johan Sebastian Salamanca Gonzalez
* Harold Nicolas Saavedra Alvarado

# Patron usado: Hollywood ()

Se implemento un simulador de colas para un hospital, donde durante un tiempo dado se simulara la llegada de pacientes y se realizara una valoracion inicial donde se asignara un valor de prioridad y posteriormente seran atendidos de acuerdo a
esta prioridad. 

En la construccion de este simulador aplicamos el principio de Hollywood, este metodo nos ayuda a estructurar nuestro codigo para evitar
realizar comprobaciones innecesarias una y otra vez, en caso de no usarlo tendriamos que iterar cada minuto para validar que la funcion atender se este ejecutando en el momento correcto.
