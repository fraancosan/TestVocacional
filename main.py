import streamlit as st
import datos

def mostrarDatos(tabla, indice, color = "green", tipo= "aptitudes"):
  st.markdown(f"**[Segun tus {tipo} podrías dedicarte a:**")
  st.markdown(f"**:{color}[{tabla[0]}]**")
  for i in tabla[indice]:
    st.markdown(f"**:{color}[-{i}]**")

st.set_page_config(layout="centered", page_title="Test CHASIDE",page_icon="logo.png")
st.subheader("**:blue[Test Orientacion Vocacional CHASIDE:]**")
st.write("**[Con la finalidad de contribuir al proceso de la elección de una carrera universitaria, ponemos a disposición este test de orientación vocacional que consta de 98 preguntas relacionadas a tus intereses y aptitudes.]**")
st.write("**[Un test de orientación vocacional puede ser una herramienta útil, aunque no definitiva, para contar con una primera aproximación a la búsqueda vocacional. En base a tus respuestas, podrás tener una orientación, considerando intereses y aptitudes.]**")

preguntas = datos.obtenerPreguntas()
respuestas = []

with st.form("my_form"):
  for i in range(len(preguntas)):
    # Preguntas
    respuestas.append(st.radio(f"{preguntas[i]}", ("Si", "No"), key=f"{i+1}", horizontal=True, index=1))
  
  submitted = st.form_submit_button("Aceptar")

if submitted:
  intereses = [0,0,0,0,0,0,0]
  aptitudes = [0,0,0,0,0,0,0]
  for i in range(len(respuestas)):
    if respuestas[i] == "Si":
      #Se usa "i+1" dado que "i" tiene un valor menos que la pregunta
      #Con esto obtengo que tipo de aptitud e interes es la pregunta
      interes = datos.obtenerInteres(i+1)
      aptitud = datos.obtenerAptitudes(i+1)

      if interes == "C":
        intereses[0]+= 1
      if interes == "H":
        intereses[1]+= 1
      if interes == "A":
        intereses[2]+= 1
      if interes == "S":
        intereses[3]+= 1
      if interes == "I":
        intereses[4]+= 1
      if interes == "D":
        intereses[5]+= 1
      if interes == "E":
        intereses[6]+= 1

      if aptitud == "C":
        aptitudes[0]+= 1
      if aptitud == "H":
        aptitudes[1]+= 1
      if aptitud == "A":
        aptitudes[2]+= 1
      if aptitud == "S":
        aptitudes[3]+= 1
      if aptitud == "I":
        aptitudes[4]+= 1
      if aptitud == "D":
        aptitudes[5]+= 1
      if aptitud =="E":
        aptitudes[6]+= 1
  
  #Evaluo esto para que el programa no devuelva nada si es que ninguna pregunta fue contestada afirmativamente
  if max(intereses) == 0:
    interes = -1
  else:
    interes = intereses.index(max(intereses))
  if max(aptitudes) == 0:
    aptitud = -1
  else:
    aptitud = aptitudes.index(max(aptitudes))

  colInteres, colAptitud = st.columns(2)
  # Hacer q quede dividido en dos columnas y ver el tema de que muestre solo intereses o aptitudes dependiendo lo que toque
  with colInteres:
    if interes == 0:
      tabla = datos.administrativas()
      mostrarDatos(tabla, 1, "green", "intereses")

    if interes == 1:
      tabla = datos.humanisticas()
      mostrarDatos(tabla, 1, "green", "intereses")
    
    if interes == 2:
      tabla = datos.artisticas()
      mostrarDatos(tabla, 1, "green", "intereses")
    
    if interes == 3:
      tabla = datos.medicina()
      mostrarDatos(tabla, 1, "green", "intereses")

    if interes == 4:
      tabla = datos.ingenieria()
      mostrarDatos(tabla, 1, "green", "intereses")

    if interes == 5:
      tabla = datos.defensa()
      mostrarDatos(tabla, 1, "green", "intereses")
    
    if interes == 6:
      tabla = datos.ciencias()
      mostrarDatos(tabla, 1, "green", "intereses")

  with colAptitud:
    if aptitud == 0:
      tabla = datos.administrativas()
      mostrarDatos(tabla, 2, "orange", "aptitudes")

    if aptitud == 1:
      tabla = datos.artisticas()
      mostrarDatos(tabla, 2, "orange", "aptitudes")

    if aptitud == 2:
      tabla = datos.artisticas()
      mostrarDatos(tabla, 2, "orange", "aptitudes")
    
    if aptitud == 3:
      tabla = datos.medicina()
      mostrarDatos(tabla, 2, "orange", "aptitudes")

    if aptitud == 4:
      tabla = datos.ingenieria()
      mostrarDatos(tabla, 2, "orange", "aptitudes")

    if aptitud == 5:
      tabla = datos.defensa()
      mostrarDatos(tabla, 2, "orange", "aptitudes")
    
    if aptitud == 6:
      tabla = datos.ciencias()
      mostrarDatos(tabla, 2, "orange", "aptitudes")
