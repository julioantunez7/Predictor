import numpy as np
import pickle
import requests
import streamlit as st

import pip
pip.main(["install", "scikit-learn"])

# loading the saved model

url = 'https://raw.githubusercontent.com/julioantunez7/Predictor/main/trained_model.sav'
response = requests.get(url)
# Verificar si la descarga fue exitosa
if response.status_code == 200:
    # Cargar el modelo utilizando pickle
    binary_data = response.content
    loaded_model = pickle.loads(binary_data)
# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(input_Data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_Data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def main():

    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA DE PREDICCION DE COMPRA DE MATERIA PRIMA </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Lecctura de datos
    # Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    dato1 = st.text_input('Inventario actual')
    if dato1.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato1_numeric = int(dato1)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Inventario actual'")
    else:
        st.error("Por favor ingrese un valor para 'Inventario actual'")
    dato2 = st.text_input('Tiempo de espera del producto (Horas)')
    if dato2.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato22 = int(dato2)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Tiempo de espera del producto'")
    else:
        st.error("Por favor ingrese un valor para 'Tiempo de espera del producto'")
    dato3 = st.text_input('Cantidad en transito')
    if dato3.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato33 = int(dato3)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Cantidad en transito'")
    else:
        st.error("Por favor ingrese un valor para 'Cantidad en transito'")
    dato4 = st.text_input('Ventas de 1 mes')
    if dato4.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato44 = int(dato4)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Ventas de 1 mes'")
    else:
        st.error("Por favor ingrese un valor para 'Ventas de 1 mes'")

    dato5 = st.text_input('Ventas de 3 meses')
    if dato5.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato55 = int(dato5)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Ventas de 3 meses'")
    else:
        st.error("Por favor ingrese un valor para 'Ventas de 3 meses'")
    dato6 = st.text_input('Ventas de 6 meses')
    if dato6.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato66 = int(dato6)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Ventas de 6 meses'")
    else:
        st.error("Por favor ingrese un valor para 'Ventas de 6 meses'")

    dato7 = st.text_input('Ventas de 9 meses')
    if dato7.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato77 = int(dato7)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Ventas de 9 meses'")
    else:
        st.error("Por favor ingrese un valor para 'Ventas de 9 meses'")
    dato8 = st.text_input('Inventario minimo')
    if dato8.strip():  # Si la cadena tiene contenido (ignorando espacios en blanco)
        try:
            dato88 = int(dato8)
            # Aquí puedes usar dato1_numeric en tus operaciones posteriores
        except ValueError:
            st.error("Por favor ingrese un valor numérico para 'Inventario minimo'")
    else:
        st.error("Por favor ingrese un valor para 'Inventario minimo'")

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Result'):
        diagnosis = model_prediction(
            [dato1_numeric,dato22,dato33,dato44,dato55,dato66,dato77,dato88])

        valor = str(diagnosis)
        print("Valor a pasar a st.success:", valor)  # Verificar el valor antes de pasarlo a st.success()
        st.success("Resultado exitoso")
        st.text("La predicción a 3 meses es:" + str(diagnosis[0][0]))  # Acceder al primer elemento de la primera fila
        st.text("La predicción a 6 meses es:" + str(diagnosis[0][1]))  # Acceder al segundo elemento de la primera fila
        st.text("La predicción a 9 meses es:" + str(diagnosis[0][2]))

if __name__ == '__main__':
    main()