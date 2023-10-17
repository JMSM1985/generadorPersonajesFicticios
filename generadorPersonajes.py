#Primero importamos el módulo time para poder hacer una breve demostración posteriormente:

import time

#Luego definimos las clases para los distintos personajes:

class magoOscuro():
	def __init__(self, nombre, edad, hechizoPrincipal, hechizoSecundario, breveBio):
		self.nombre = nombre
		self.edad = edad
		self.hechizoPrincipal = hechizoPrincipal
		self.hechizoSecundario = hechizoSecundario
		self.breveBio = breveBio
		
class monjeSanador():
	def __init__(self, nombre, edad, hechizoPrincipal, hechizoSecundario, breveBio):
		self.nombre = nombre
		self.edad = edad
		self.hechizoPrincipal = hechizoPrincipal
		self.hechizoSecundario = hechizoSecundario
		self.breveBio = breveBio
		
class guerrero():
	def __init__(self, nombre, edad, armaPrincipal, armaSecundaria, breveBio):
		self.nombre = nombre
		self.edad = edad
		self.armaPrincipal = armaPrincipal
		self.armaSecundaria = armaSecundaria
		self.breveBio = breveBio
		
class vampiro():
	def __init__(self, nombre, edad, habilidadPrincipal, habilidadSecundaria, breveBio):
		self.nombre = nombre
		self.edad = edad
		self.habilidadPrincipal = habilidadPrincipal
		self.habilidadSecundaria = habilidadSecundaria
		self.breveBio = breveBio
		
class hombreLobo():
	def __init__(self, nombre, edad, habilidadPrincipal, habilidadSecundaria, breveBio):
		self.nombre = nombre
		self.edad = edad
		self.habilidadPrincipal = habilidadPrincipal
		self.habilidadSecundaria = habilidadSecundaria
		self.breveBio = breveBio
		
#Ahora asignamos los personajes, tanto sus tipos como sus atributos para la pequeña demostración posterior:
		
personaje1 = magoOscuro("Aureliano Nocta", 55, "Muerte instantánea", "Maldición", "Mago europeo. Se cree que nació en España, aunque nadie ha vivido lo suficiente como para averiguarlo...")
personaje2 = monjeSanador("Felipe San Agustín", 32, "Curación total", "Curar herida", "Monje jesuita nacido en España. Misionero e incansable viajero, consiguió sus dones de sanación cuando en el Santuario de Fátima la misma Virgen se los dió...")
personaje3 = guerrero("Alfonso Castilla", 37, "Espada Ropera", "Daga", "Ex soldado español. En los Tercios de Flandes aprendió a manejarse como nadie en los asuntos de la guerra, pero la envidia y la traición le obligaron a volver a la península. Ahora espera pacientemente completar su venganza...")
personaje4 = vampiro("Juan Tepes", "Desconocida", "Invisibilidad", "Metamorfosis", "Hijo de un famoso vampiro, concebido en uno de los muchos viajes de su padre. Reina en las noches de Europa Occidental, aunque su ambición podría llevarle algún día a conquistar el trono de toda Europa...")
personaje5 = hombreLobo("Carlos de Tolouse", 66, "Garra de Acero", "Diente desgarrador", "Nacido en un pequeño pueblo de los Pirineos españoles, emigró siendo un niño a Tolouse cuando su familia buscaba un futuro mejor. Sin embargo, una terrible noche de luna llena en la que estaba perdido sufrió un ataque feroz por parte de un hombre lobo de la zona y ya nada se pudo hacer...")

#Aquí se decide el personaje para la breve demostración:

personajeElegido = input("Elige un personaje: 1-Mago Oscuro, 2-Monje Sanador, 3-Guerrero, 4-Vampiro, 5-Hombre Lobo\n")

#A continuación, en función del personaje elegido, se presenta su información:

if personajeElegido == "1":
	print("Has elegido al mago oscuro...")
	time.sleep(2)
	print("Su nombre es... " + personaje1.nombre)
	time.sleep(2)
	print("Su edad es... " + str(personaje1.edad))
	time.sleep(2)
	print("Su hechizo principal es... " + personaje1.hechizoPrincipal)
	time.sleep(2)
	print("Su hechizo secundario es... " + personaje1.hechizoSecundario)
	time.sleep(2)
	print("Su breve presentación es..." + personaje1.breveBio)
	time.sleep(2)
	
if personajeElegido == "2":
	print("Has elegido al monje sanador...")
	time.sleep(2)
	print("Su nombre es... " + personaje2.nombre)
	time.sleep(2)
	print("Su edad es... " + str(personaje2.edad))
	time.sleep(2)
	print("Su hechizo principal es... " + personaje2.hechizoPrincipal)
	time.sleep(2)
	print("Su hechizo secundario es... " + personaje2.hechizoSecundario)
	time.sleep(2)
	print("Su breve presentación es..." + personaje2.breveBio)
	time.sleep(2)
	
if personajeElegido == "3":
	print("Has elegido al guerrero...")
	time.sleep(2)
	print("Su nombre es... " + personaje3.nombre)
	time.sleep(2)
	print("Su edad es... " + str(personaje3.edad))
	time.sleep(2)
	print("Su arma principal es... " + personaje3.armaPrincipal)
	time.sleep(2)
	print("Su arma secundaria es... " + personaje3.armaSecundaria)
	time.sleep(2)
	print("Su breve presentación es..." + personaje3.breveBio)
	time.sleep(2)
	
if personajeElegido == "4":
	print("Has elegido al vampiro...")
	time.sleep(2)
	print("Su nombre es... " + personaje4.nombre)
	time.sleep(2)
	print("Su edad es... " + str(personaje4.edad))
	time.sleep(2)
	print("Su habilidad principal es... " + personaje4.habilidadPrincipal)
	time.sleep(2)
	print("Su habilidad secundaria es... " + personaje4.habilidadSecundaria)
	time.sleep(2)
	print("Su breve presentación es..." + personaje4.breveBio)
	time.sleep(2)
	
if personajeElegido == "5":
	print("Has elegido al hombre lobo...")
	time.sleep(2)
	print("Su nombre es... " + personaje5.nombre)
	time.sleep(2)
	print("Su edad es... " + str(personaje5.edad))
	time.sleep(2)
	print("Su habilidad principal es... " + personaje5.habilidadPrincipal)
	time.sleep(2)
	print("Su habilidad secundaria es... " + personaje5.habilidadSecundaria)
	time.sleep(2)
	print("Su breve presentación es..." + personaje5.breveBio)
	time.sleep(2)
	
#Y por último... Gracias!!!
	
print("Gracias por usar el creador de personajes!!!")
	

	




	
