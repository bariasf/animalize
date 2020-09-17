#pip install streamlit

import streamlit as st
import numpy as np
 
st.title('ANIMALIZE')
st.header("Bienvenido a nuestra aplicación.")

mascota = st.multiselect("¿Que tipo de mascota tienes?",("perro","gato","pájaro/canario"))
st.write("Espero que esté muy bien tu {}, pronto te ayudaremos con él." .format(','.join(mascota)))
wild = st.selectbox("¿Te interesan los animales salvajes?",("Sí, claro.","No, la verdad."))
wild2 = str(wild)
if wild2 == "Sí, claro.":
    st.write("¡Qué bien!, aquí conocerás sobre ellos")
else:
    st.write("Lástima, porque aquí encontrarás cosas sobre ellos.")
