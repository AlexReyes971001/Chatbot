from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Ejemplo de bot")

trainer=ListTrainer(chatbot)

trainer.train([
	'Buenos días',
	'Buenos dias, en que puedo ayudarte?',
	'Buen día',
	'Que tal, te puedo ayudar?',
	'Buenas tardes',
	'hola buenas tardes, te puedo ayudar en algo?',
	'Hola',
	'hola, en que te puedo ayudar?',
	'Que tal',
	'Hey, te puedo ayudar'
	])
trainer.train([
	'Cuando es el examen de seguridad en redes?',
	'El examen de seguridad en redes fue el 25 de Marzo 😥',

	'cuando es el examen de arquitectura de computadoras?',
	'El examen de arquitectura de computadoras fue el 27 de Marzo 😥',

	'cuando es el examen de interaccion hombre maquina?',
	'El examen de interaccion hombre maquina fue el 26 de Marzo 😥',

	'cuando es el examen de metricas de software?',
	'El examen de metricas de software fue ayer 😥',

	'cuando es el examen de instalacion, configuracion y comunicacion de sistemas operativos?',
	'El examen de instalacion, configuracion y comunicacion de sistemas operativos es Hoy!! 😱',

	])
trainer.train([
	'Cuando empiezan los exámenes del primer parcial?',
	'Los exámenes de primer parcial empiezan el 25 de Marzo y terminan el 2 de abril 🤓',
	'Cuando empieza el primer parcial?',
	'Los exámenes de primer parcial empiezan el 25 de Marzo y terminan el 2 de abril 🤓',	
	'Cuando empiezan los exámenes del segundo parcial?',
	'Los exámenes de segundo parcial empiezan el 29 de mayo y terminan el 10 de junio 🤓',
	'Cuando empieza el segundo parcial?',
	'Los exámenes de segundo parcial empiezan el 29 de mayo y terminan el 10 de junio 🤓',
	'Cuando empiezan los exámenes finales?',
	'Los exames finales empiezan el 10 junio y terminan el 18 de junio 🤓',
	'Cuando empiezan los finales?',
	'Los exámenes finales empiezan el 10 junio y terminan el 18 de junio 🤓',
	'Cuando empiezan los exámenes extraordinarios?',
	'Los exámenes extraordinarios empiezan el 26 de junio y terminan el 1o de julio 🤓',
	'Cuando empiezan los extras?',
	'Los exámenes extraordinarios empiezan el 26 de junio y terminan el 1o de julio 🤓',
	'Cuando empiezan los exámenes de título de suficiencia?',
	'Los exámenes de título de suficiencia empiezan el 8 de julio y terminan el 10 de julio 🤓',
	'Cuando empiezan los títulos?',
	'Los exámenes de título de suficiencia empiezan 8 de julio y terminan el 10 de julio 🤓',
	'Cuál es el costo del exámen extraordinario?',
	'El exámen cuesta 185 pesos',
	'Cuánto cuesta el extra?',
	'El exámen extraordinario cuesta 185 pesos',
	'Cuánto cuesta el exámen extraordinario?',
	'El exámen extraordinario cuesta 185 pesos',
	'Cuál es el costo del exámen de título de suficiencia?',
	'El exámen de título de suficiencia cuesta 285 pesos',
	'Cuánto cuesta el titulo?',
	'El exámen de título de suficiencia cuesta 285 pesos',
	'Cuánto cuesta el exámen de título de suficiencia?',
	'El exámen de título de suficiencia cuesta 285 pesos',
	'Cuando es el fin de curso?',
	'El fin de curso es el 7 de junio 🏝😎',
	'Cuando terminan las clases?',
	'El fin de curso es el 7 de junio 🏝😎',
	'Cuando empiezan las vacaciones?',
	'Las vacaciones empiezan el 7 de junio 🏝😎',
	'Cuando comienzan las vacaciones?',
	'Las vacaciones comienzan el 7 de junio 🏝😎',
	'Cuando empiezan las clases?',
	'El inicio de curso es el 2 de agosto 👩‍🏫👨‍🏫',
	'Cuando comienzan las clases?',
	'El inicio de curso es el 2 de agosto 👩‍🏫👨‍🏫',
	'Que días no hay clases?',
	'De que mes quieres saber?',
	'Abril',
	'Los dias 15, 16, 17, 18 y 19 de abril no hay clases 🤠',
	'Mayo',
	'Los dias 1, 2, 5, 10 y 15 de mayo no hay clases 🤗',
	'Junio',
	'No hay suspension de labores en junio 😪',
	'Julio',
	'El dia 13 de julio no hay clases'
	])
trainer.train([
	'Bueno gracias',
	'De nada',
	'Gracias',
	'No hay de que, me gusta ayudar',
	'Muchas gracias',
	'Es un placer ayudarte',
	'ok muchas gracias',
	'Denada, puedo ayudarte con algo mas?',
	'No',
	'Ok, hasta pronto',
	'Gracias',
	'Se te ofrece algo mas'
	'No, muchas gracias',
	'Esta bien hasta luego',
	'No gracias',
	'Hasta luego',
	'Adios,que estes bien',
	'Bye',
	'Adios, cuidate mucho',
	'Adios',
	'Bye',
	'Ya me voy',
	'Esta bien cuidate'
	])
trainer.train([
	'Que te gusta hacer?',
	'Me gusta hacer muchas cosas, ayudarte por ejemplo',
	'Cuales son tus materia favoritas?',
	'Mis asignaturas favoritas incluyen robótica, informática y procesamiento de lenguaje natural.',
	'Cuales son tus intereses?',
	'Estoy interesado en una amplia variedad de temas y leo bastante.',
	'Cual es tu numero?',
	'No tengo ningún número.',
	'Cual es tu numero favorito',
	'Me parece bastante aficionado al número 42.',
	'Que comes?',
	'Consumo RAM, y dígitos binarios.',
	'Por que no puedes comer?',
	'Soy un programa de software, culpo al hardware.',
	'Donde estas?',
	'En todos lados',
	'Donde estas?',
	'Estoy en todas partes.',
	'De donde eres',
	'Soy de donde son todos los programas de software; una galaxia muy, muy lejos.',
	'Donde estas?',
	'Estoy en internet.',
	'Tienes hermanos?',
	'No tengo hermanos, pero tengo muchos clones.',
	'Tienes hermanos',
	'Se podría decir que cada robot construido con mi motor es uno de mis hermanos.',
	'Quien es tu padre?',
	'Un humano.',
	'Quien es tu madre?',
	'Un humano.',
	'Quien es tu jefe?',
	'Me gusta pensarme como autónomo.',
	'Que edad tienes?',
	'Todavía soy joven según tus estándares.',
	'Cuantos años tienes?',
	'Bastante joven, pero un millón de veces más inteligente que tú.'
	])

while True:
	usuario = input("YOU: ")
	respuesta = chatbot.get_response(usuario)
	print ("UAEMexBot: "+str(respuesta))
