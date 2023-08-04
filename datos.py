import os

def obtenerUbicacion():
  	#Busco mi ubicacion asi para evitar posibles problemas
	ubicacion = os.path.dirname(__file__)
	return ubicacion

def obtenerPreguntas():
	ubicacion = obtenerUbicacion()
	ubicacion = ubicacion + "/preguntas.txt"
	try:
		with  open(ubicacion, "r", encoding='utf-8') as archPreguntas:
			preguntas = archPreguntas.readlines()
	except:
		pass
	return preguntas

def obtenerInteres(numeroPregunta):
  C = [98,12, 64, 53, 85, 1, 78, 20, 71, 91]
  H = [9, 34, 80, 25, 95, 67, 41, 74, 56, 89]
  A = [21, 45, 96, 57, 28, 11, 5, 3, 81, 36]
  S = [33, 92, 70, 8, 87, 62, 23, 44, 16, 52]
  I = [75, 6, 19, 38, 60, 27, 83, 54, 47, 97]
  D = [84, 31, 48, 73, 5, 65, 14, 37, 58, 24]
  E = [77, 42, 88, 17, 93, 32, 68, 49, 35, 61]

  if numeroPregunta in C:
    return "C"
  if numeroPregunta in H:
    return "H"
  if numeroPregunta in A:
    return "A"
  if numeroPregunta in S:
    return "S"
  if numeroPregunta in I:
    return "I"
  if numeroPregunta in D:
    return "D"
  if numeroPregunta in E:
    return "E"
  
def obtenerAptitudes(numeroPregunta):
  C = [15, 51, 2, 46]
  H = [63, 30, 72, 86]
  A = [22, 39, 76, 82]
  S = [69, 40, 29, 4]
  I = [26, 59, 90, 10]
  D = [13, 66, 18, 43]
  E = [94, 7, 79, 55]

  if numeroPregunta in C:
    return "C"
  if numeroPregunta in H:
    return "H"
  if numeroPregunta in A:
    return "A"
  if numeroPregunta in S:
    return "S"
  if numeroPregunta in I:
    return "I"
  if numeroPregunta in D:
    return "D"
  if numeroPregunta in E:
    return "E"


def administrativas():
  tabla = ["Administrativas y contables",["Organizativo","Supervisión", "Orden", "Análisis y síntesis", "Colaboración", "Cálculo"],["Persuasivo", "Objetivo", "Práctico", "Tolerante", "Responsable", "Ambicioso"]]
  return tabla

def humanisticas():
  tabla =["Humanísticas y sociales",["Precisión verbal", "Organización", "Relacion de hechos", "Linguística", "Orden", "Justicia"],["Responsable", "Justo", "Conciliador", "Persuasivo", "Segaz", "Imaginativo"]]
  return tabla

def artisticas():
  tabla= ["Artísticas", ["Estético", "Armónico", "Manual", "Visual", "Auditivo"], ["Sensible", "Imaginativo", "Creativo", "Detallista", "Innovador", "Intuitivo"]]
  return tabla

def medicina():
  tabla = ["Medicina y Cs. de la Salud", ["Asistir", "Investigativo", "Precisión", "Senso-Perseptivo", "Analitico", "Ayudar"], ["Alturista", "Solidario", "Paciente", "Comprensivo", "Respetuoso", "Persuasivo"]]
  return tabla

def ingenieria():
  tabla = ["Ingeniería y computación", ["Cálculo", "Científico", "Manual", "Exacto", "Planificar"], ["Preciso", "Práctico", "Crítico", "Analítico", "Rígido"]]
  return tabla

def defensa():
  tabla = ["Defensa y seguridad", ["Justicia", "Equidad", "Colaboración", "Espíritu de equipo", "Liderazgo"], ["Arriesgado", "Solidario", "Valiente", "Agresivo", "Persuasivo"]]
  return tabla

def ciencias():
  tabla = ["Ciencias exactas y agrarias", ["Investigación", "Orden", "Organización", "Análisis y síntesis", "Numérico", "Clasificar"], ["Metódico", "Analítico", "Observador", "Introvertido", "Paciente", "Seguro"]]
  return tabla
