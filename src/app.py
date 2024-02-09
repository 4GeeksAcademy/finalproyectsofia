import streamlit as st
import pickle
import pandas as pd


# Cargar el modelo entrenado y el modelo escalado
ruta_modelo_original = 'models/randomforestmodel.pkl'
ruta_modelo_escalado = 'models/scaler_model.pkl'

with open(ruta_modelo_original, 'rb') as archivo_modelo_original:
    modelo_original = pickle.load(archivo_modelo_original)

with open(ruta_modelo_escalado, 'rb') as archivo_modelo_escalado:
    modelo_escalado = pickle.load(archivo_modelo_escalado)


page_gradient = """
<style>
[data-testid="stAppViewContainer"]{
    background: linear-gradient(to bottom, #ffb0b7, #e1faf2); /* Change colors according to your preferences */
    margin: 0;
    padding: 0;
}
</style>
"""

# Apply the style
st.markdown(page_gradient, unsafe_allow_html=True)

# Función para hacer predicciones
def hacer_prediccion(time_occ, area, crm_cd, vict_age, vict_sex, vict_descent, premis_cd, weapon_used_cd, status):
    # Crear un DataFrame con los nuevos datos
    nuevos_datos = {
        'TIME OCC': [time_occ],
        'AREA': [area],
        'Crm Cd': [crm_cd],
        'Vict Age': [vict_age],
        'Vict Sex': [vict_sex],
        'Vict Descent': [vict_descent],
        'Premis Cd': [premis_cd],
        'Weapon Used Cd': [weapon_used_cd],
        'Status': [status],
    }
    nuevos_datos_df = pd.DataFrame(nuevos_datos)

    # Escalar las características
    nuevos_datos_escalados = modelo_escalado.transform(nuevos_datos_df)

    # Hacer la predicción con el modelo original
    prediccion = modelo_original.predict(nuevos_datos_escalados)

    return prediccion[0]

# Interfaz de usuario con Streamlit
def main():
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    # Centrar el título y cambiar el color utilizando HTML
    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>Exploración del Comportamiento Criminal en Los Ángeles: Análisis y Predicciones</h1>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify; font-weight: bold;'>En este estudio hemos analizado la criminalidad de la Ciudad de Los Angeles California y lo hemos hecho realizando un modelo Machine Learning. Desarrollar un modelo de Machine Learning implica varios pasos. Debemos tener en cuenta que estos pasos pueden variar según el problema específico y los datos disponibles. Aquí estan los pasos que hemos seguido para nuestro estudio:</p>", unsafe_allow_html=True)

    st.write("<p style='text-align: justify; font-weight: bold;'> </p>", unsafe_allow_html=True)

    # Lista numerada de pasos
    pasos = [
        "DEFINICION DEL PROBLEMA",
        "RECOPILACIÓN DE DATOS",
        "EXPLORACIÓN Y ANÁLISIS DE DATOS ",
        "DIVISIÓN DE DATOS",
        "SELECCIÓN DEL MODELO",
        "PREPROCESAMIENTO DEL MODELO",   
        "ENTRENAMIENTO DEL MODELO",
        "EVALUACIÓN DEL MODELO, AJUSTE Y OPTIMIZACIÓN",
        "DESPLIEGUE DEL MODELO",
        "CONCLUSIONES",
    ]

    
    # Imprimir la lista numerada de pasos
    for i, paso in enumerate(pasos, 1):
        st.write(f"<b>{i}. {paso}</b>", unsafe_allow_html=True)

    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>La Ciudad del los Ángeles</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'>La Ciudad de Los Ángeles, comúnmente conocida como Los Ángeles o L.A., es la ciudad más grande del estado de California y la segunda ciudad más poblada de los Estados Unidos, después de Nueva York. Ubicada en la costa oeste del país, Los Ángeles es conocida por ser el centro de la industria del entretenimiento y alberga a Hollywood, que es la capital mundial del cine y la televisión.</p>", unsafe_allow_html=True)

    ruta_imagen = "images/12.jpg"

    st.image(ruta_imagen, use_column_width=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> La tasa de criminalidad en Los Ángeles puede variar según el tipo de delito y la ubicación específica dentro de la ciudad. Los delitos comunes incluyen asaltos, robos, robos de vehículos, vandalismo, delitos relacionados con drogas y otros. Es importante tener en cuenta que la ciudad es grande y diversa, y la incidencia de delitos puede variar considerablemente entre diferentes vecindarios.</p>", unsafe_allow_html=True)


    placeholder = st.empty()

    if st.button("Siguiente"):
        st.session_state.pagina_actual = "pagina_1"

    placeholder.text(" ")


def pagina_1():

    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>1 .- DEFINICIÓN DEL PROBLEMA</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'>  Nuestro objetivo de estudio ha sido el analisis de los datos recogidos que  reflejan incidentes delictivos en la ciudad de Los Ángeles que se remontan a 2020. Con la finalidad de crear un modelo de machine learning que pueda predecir la gravedad de los incidentes que ocurren en esta zona. </p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'>  Predecir la gravedad de los incidentes en una región tiene diversas aplicaciones y beneficios en diferentes contextos, como la gestión de la seguridad pública, la toma de decisiones gubernamentales, la asignación de recursos y la planificación de políticas. Algunas razones por las cuales predecir la gravedad de los incidentes puede ser crucial incluyen: </p>", unsafe_allow_html=True)

    beneficios = [
    "**-Gestión de Recursos de Seguridad**",
    "**-Prevención de Delitos**",
    "**-Mejora de la Respuesta a Emergencias**",
    "**-Planificación Urbana y Desarrollo**",
    "**-Distribución de Recursos de Salud**",
    "**-Desarrollo de Políticas Públicas**",
    "**-Seguridad Ciudadana**",
    "**-Eficiencia en la Justicia**",
    ]

# Mostrar la lista en Streamlit
    for beneficio in beneficios:
        st.markdown(beneficio, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>2 .- RECOPILACIÓN DE DATOS</h1>", unsafe_allow_html=True)

    url = "https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data"
    link_text = "(pincha aquí para acceder)"
    st.markdown(f"<p style='text-align: justify; font-weight: bold;'> Los datos han sido obtenidos de esta pagina web <a href='{url}' target='_blank'>{link_text}</a>. La información incluye detalles como la fecha del informe, la fecha del incidente, la hora, la ubicación, el tipo de crimen, la descripción del crimen, y mas variables que explicaremos a continuación que nos han servido para nuestro estudio</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>3 .- EXPLORACIÓN Y ANÁLISIS DE DATOS</h1>", unsafe_allow_html=True)
    # st.write("<p style='text-align: justify; font-weight: bold;'> </p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'>En este punto incluimos otros tres puntos claves para el desarrollo: </p>", unsafe_allow_html=True)
    pasos = [
        "INGESTION DE DATOS",
        "ANALISIS ESTADISTICO",
        "EDA ",
    ]
    
    # Imprimir la lista numerada de pasos
    for i, paso in enumerate(pasos, 1):
        st.write(f"<b>{i}. {paso}</b>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'>Centraremos nuestra explicacion en el EDA ya que es el paso mas importante antes de entrenar nuestro modelo. El primer paso del EDA ha sido ver el tamaño de nuestro dataframe , hemos obtenido un total del de   888472 filas y 28 de columnas . El sguiente paso ha sido definir las varibles con las que vamos a trabajar para poder valorar cuales son las mas relevantes, en nuestro caso son las siguientes: </p>", unsafe_allow_html=True)
    datos = {
    "DR_NO": "Número de informe del Departamento de Policía.",
    "Date Rptd": "Fecha en que se presentó el informe.",
    "DATE OCC": "Fecha en que ocurrió el incidente.",
    "TIME OCC": "Hora del día en que ocurrió el incidente.",
    "AREA": "Número de área en la que ocurrió el incidente.",
    "AREA NAME": "Nombre del área.",
    "Rpt Dist No": "Subárea de un área geográfica.",
    "Part 1-2": "Tipo de incidente. 1 para incidentes graves y 2 para incidentes menos graves.",
    "Crm Cd": "Código del delito.",
    "Crm Cd Desc": "Descripción del delito.",
    "Mocodes": "Estos códigos proporcionan información sobre la forma en que se llevó a cabo un crimen.",
    "Vict Age": "Edad de la víctima.",
    "Vict Sex": "Sexo de la víctima.",
    "Vict Descent": "Descendencia de la víctima.",
    "Descent Code": "Descripcion de los codigos de descendencia",
    "Premis Cd": "Código del tipo de lugar del incidente.",
    "Premis Desc": "Descripción del lugar del incidente.",
    "Weapon Used Cd": "Código del arma utilizada.",
    "Weapon Desc": "Descripción del arma utilizada.",
    "Status": "Estado del informe.",
    "Status Desc": "Descripción del estado del informe.",
    "Crm Cd 1, 2, 3, 4 ": "Códigos adicioanles de delitos.",
    "LOCATION": "Dirección del incidente.",
    "Cross Street": "Calle cruzada.",
    "LAT, LON": "Latitud y longitud del incidente."
    }

# Mostrar la lista en Streamlit
    # 0st.markdown("<h3 style='text-align: center;'>Información sobre los datos:</h3>", unsafe_allow_html=True)
    for clave, valor in datos.items():
        st.markdown(f"<p style='margin-bottom: 4px;'>- <strong>{clave}:</strong> {valor}</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


    st.write("<p style='text-align: justify; font-weight: bold;'>Tras estudiar nuestras variables nos quedamos finalmente con 20 de ellas las cuales son mas relevantes</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; font-size: 16px;'>ANALISIS UNIVARIANTE:</h3>", unsafe_allow_html=True)

    ruta_imagen1 = "images/imag1.png"
    st.write("<p style='text-align: justify; font-weight: bold;'> Variables numericas</p>", unsafe_allow_html=True)

    st.image(ruta_imagen1, width=800)

    insights_graves = [
    "Grave: Los delitos graves superan a los no graves",
    "Crm Cd: Los códigos de delitos más repetidos rondan alrededor del 510 que es el robo de vehiculos ",
    "Weapon Used Cd: El código de arma más utilizado es el 400, que es el uso de la fuerza física",
    "AREA: Las áreas más repetidas son la 1 y la 12, que son Central y 77th Street, respectivamente. Tampoco observamos valores atípicos",
    "Vict Age: El valor más repetido es 0, pero lo más seguro es que sean valores nulos. La mayoría de las víctimas se encuentran entre los 20 y 40 años. Observamos que aquí sí hay valores atípicos",
    "LAT y LON: Las coordenadas se sitúan cerca, esto se debe a que son de la misma ciudad de Los Ángeles. También hay valores atípicos",
    "Rpt Dist No: Las áreas subgráficas están repartidas, pero hay varias que destacan como el 162 y 645",
    "Premis Cd: El código de tipo de lugar más repetido es el 101, seguido del 501, en la calle y en vivienda unifamiliar"
    ]

# Muestra los insights sobre delitos graves en la aplicación Streamlit
    for insight in insights_graves:
        st.markdown(f"- {insight}", unsafe_allow_html=True)

    ruta_imagen2 = "images/imag2.png"
    st.write("<p style='text-align: justify; font-weight: bold;'> Variables categóricas</p>", unsafe_allow_html=True)

    st.image(ruta_imagen2, width=800)
    insights = [
        "Area Name: Las áreas donde ocurren un mayor número de incidentes son Central y 77th Street",
        "Status: El estado que más se repite es IC, es decir que la investigación está en curso",
        "VICT SEX: El número de hombres que sufren delitos es mayor que el de las mujeres. Hay géneros que no se indican y valores nulos",
        "Vict Descent: Según el origen étnico, la mayoría de las víctimas son hispanohablantes/latinos y blancos",
        "Time: La hora con más incidentes es a las 12:00 pm, y las 18:00 pm"
    ]

# Display insights in a Streamlit app
    
    for insight in insights:
        st.markdown(f"- {insight}", unsafe_allow_html=True)

    ruta_imagen3 = "images/imag3.png"
    st.write("<p style='text-align: justify; font-weight: bold;'> Variables temporales</p>", unsafe_allow_html=True)

    st.image(ruta_imagen3, width=800)

    insights_temporales = [
    "Casi todos los meses tienen la misma influencia, aunque podemos destacar que octubre es el que más sobresale",
    "Los días de la semana también tienen casi todos la misma distribución, pero destaca el Viernes",
    "Respecto a los días de los meses, los días que más se repiten son el 1 y el 31"
    ]
    
    for insight_temporal in insights_temporales:
     st.markdown(f"- {insight_temporal}", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center; font-size: 16px;'>ANALISIS MULTIVARIBALE:</h3>", unsafe_allow_html=True)

    ruta_imagen4 = "images/imag4.png"
    st.write("<p style='text-align: justify; font-weight: bold;'> Variables numericas con target</p>", unsafe_allow_html=True)

    st.image(ruta_imagen4, width=800)


    insights_correlacion = [
    "AREA: La correlación con el área es muy débil, casi nula",
    "Rpt Dist: Correlación débil, similar a la correlación con el área",
    "Crm Cd: Los códigos de delitos tienen una correlación de -0.70, sugiere una relación lineal negativa fuerte entre las dos variables. Esto significa que hay una tendencia clara de cambio en una variable cuando la otra cambia, y la magnitud de la correlación indica la fuerza de esa relación. Es esperable ya que entre menor sea el delito mayor numeración tendrá",
    "Vict Age: Obtenemos una correlación no muy significativa y negativa, entre más edad, menos tendencia a que suceda un incidente grave",
    "Premis Cd: Correlación notable pero no muy significativa. El tipo de lugar del incidente tiene que ver con que el delito sea grave o menos grave",
    "Weapon Used Cd: Los códigos de armas más utilizados también tienen una correlación negativa directa, no muy significativa pero mayor respecto a otras varibales ",
    "LAT y LON: Correlación débil, mismo número pero una positiva y otra negativa"
    ]

# Muestra los insights sobre correlación en la aplicación Streamlit
    for insight_correlacion in insights_correlacion:
        st.markdown(f"- {insight_correlacion}", unsafe_allow_html=True)


    ruta_imagen5 = "images/5.png"
    st.write("<p style='text-align: justify; font-weight: bold;'> Variables categóricas con target</p>", unsafe_allow_html=True)

    st.image(ruta_imagen5, width=800)

    insights_accidentes = [
    "AREA: En todas las áreas destaca un mayor numero de incidentes graves",
    "Status: En las investigaciones en curso, los accidentes graves son los que están en mayoría",
    "Vict Sex: Para las mujeres suceden más incidentes no graves que graves, al contrario que para los hombres",
    "Vict Descent: Para los orígenes étnicos, en los Hispano Latinos suceden más incidentes que en el resto, pero destacan los incidentes menos graves"
    ]

# Muestra los insights sobre accidentes en la aplicación Streamlit
    for insight_accidente in insights_accidentes:
        st.markdown(f"- {insight_accidente}", unsafe_allow_html=True)

    ruta_imagen6 = "images/imag6.png"
    st.write("<p style='text-align: justify; font-weight: bold;'> Variables temporales con target</p>", unsafe_allow_html=True)

    st.image(ruta_imagen6, width=800)

    insights_grafico = [
    "Como observamos en el gráfico de arriba, para todos los periodos, el número de incidentes graves es mayor que los no graves"
    ]

    for insight_grafico in insights_grafico:
        st.markdown(f"- {insight_grafico}", unsafe_allow_html=True)
 
    st.markdown("<h3 style='text-align: center; font-size: 16px;'>ANALISIS DE CORRELACIONES COMPLETO:</h3>", unsafe_allow_html=True)

    ruta_imagen7 = "images/imag7.png"
    st.write("<p style='text-align: justify; font-weight: bold;'> Variables temporales con target</p>", unsafe_allow_html=True)

    st.image(ruta_imagen7, width=800)

    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>4 .- DIVISION DE LOS DATOS</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> La división de datos en conjuntos de entrenamiento (train) y prueba (test) es una práctica común en el aprendizaje automático (machine learning). Esta técnica se utiliza para evaluar el rendimiento de un modelo entrenado en datos que no ha visto durante el proceso de entrenamiento.</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>5 .- SELECCIÓN DE LOS K - BEST</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> El objetivo es reducir la dimensionalidad del conjunto de características manteniendo solo las más relevantes para mejorar el rendimiento del modelo. Esta técnica es especialmente útil cuando se trabaja con conjuntos de datos con un gran número de características, y se busca mejorar la eficiencia computacional y la generalización del modelo..</p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> Nuestro seleccion k best ha seleccionado las 9 mejores varibles con las que entrenaremos nuestro modelo </p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>6 .- PREPROCESAMIENTO DEL MODELO</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> El objetivo principal de la normalización es llevar todas las características a una escala común sin distorsionar las diferencias en las gamas de valores originales. Esto es importante porque muchos algoritmos de aprendizaje automático son sensibles a la escala de las características y pueden tener dificultades para converger o proporcionar resultados precisos si las características tienen magnitudes muy diferentes. </p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    # Botones para navegar a otras páginas
    if st.button("Volver"):
        st.session_state.pagina_actual = "main"
    if st.button("Siguiente"):
        st.session_state.pagina_actual = "pagina_2"

def pagina_2():
    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>7 .- ENTRENAMIENTO DEL MODELO</h1>", unsafe_allow_html=True)
   
    modelos = [
    "**MODELO DE REGRESION LINEAL:**",
    "-La regresión logística es un modelo estadístico utilizado para problemas de clasificación binaria o multiclase. Algunas de sus características clave incluyen el uso de la función logística para transformar las salidas a un rango entre 0 y 1, capacidad para manejar clasificación binaria y multiclase, estimación de coeficientes y un intercepto para definir un hiperplano de separación en el espacio de características, el uso de la función de pérdida logarítmica para el entrenamiento, y la capacidad de producir probabilidades de pertenencia a una clase. Además, es computacionalmente eficiente, fácil de interpretar y se puede regularizar para evitar el sobreajuste",
    "**MODELO RANDOM FOREST:**",
    "- **Alta Precisión Predictiva:** Ofrece predicciones precisas y robustas.",
    "- **Robustez Frente a Sobreajuste:** Mitiga el sobreajuste gracias a su aleatorización.",
    "- **Manejo de Datos No Balanceados:** Funciona bien con conjuntos de datos desequilibrados.",
    "- **Manejo de Variables Categóricas y Numéricas:** Puede manejar ambos tipos de variables sin preprocesamiento adicional.",
    "- **Identificación de Importancia de Características:** Proporciona una medida de la importancia de las características.",
    "- **Manejo de Grandes Conjuntos de Datos:** Eficiente en conjuntos de datos grandes.",
    "- **Versatilidad para Regresión y Clasificación:** Aplicable a problemas de regresión y clasificación.",
    "- **Fácil de Configurar y Menos Sensible a Hiperparámetros:** Tiene pocos hiperparámetros y funciona bien con valores predeterminados.",
    "- **Resiliencia ante Datos Ruidosos y Atípicos:** Es resistente a datos ruidosos y atípicos debido a la agregación de múltiples árboles.",
    "- **Implementación Sencilla:** Fácil de implementar en comparación con modelos más complejos."
    ]

    for insight_accidente in modelos:
        st.markdown(insight_accidente, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>8 .- EVALUACIÓN DEL MODELO , AJUSTE Y OPTIMIZACIÓN</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> REGRESION LOGISTICA: Obtenemos un accuracy de 0.8861, procedemos a intantar mejorar este resulta, optimizamos los hiperparámetros y obtenemos un accuracy de 0.8864. </p>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> RANDOM FOREST: Obtenemos un accuracy de 0.99. Seleccionamos este modelo. </p>", unsafe_allow_html=True)


    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>9 .- DESPLIEGUE DEL MODELO DEL MODELO</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


    # Botones para navegar a otras páginas
    if st.button("Volver"):
        st.session_state.pagina_actual = "pagina_1"
    if st.button("Ir a la Prediccion"):
        st.session_state.pagina_actual = "pagina_3"

def pagina_3():

    st.markdown("<h1 style='text-align: center;'>Predice la gravedad del delito</h1>", unsafe_allow_html=True)
    # Recopila datos de entrada del usuario
    time_occ = st.number_input("Hora", min_value=1, max_value=24, step=1, value=1)
    area = st.selectbox('Indica el Area', ("Central","Rampart","Southwet","Hollenbeck","Harbor",
        "Hollywood","Wilshire", "West LA", "Van Nuys", "Wset Valley",
        "Northheast", "77th Street", "Newton", "Pacific", "N Hollywood",
        "Foothill", "Devonshire", "Southeast", "Mission", "Olympic",
        "Topanga"), index=0)
    crm_cd = st.selectbox('Codigo delito', ('BATTERY - SIMPLE ASSAULT', 'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE', 'VANDALISM - MISDEMEANOR ($399 OR UNDER)', 'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)', 'RAPE, FORCIBLE', 'SHOPLIFTING - PETTY THEFT ($950 & UNDER)', 'OTHER MISCELLANEOUS CRIME', 'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD', 'BURGLARY FROM VEHICLE', 'CRIMINAL THREATS - NO WEAPON DISPLAYED', 'ARSON', 'THEFT PLAIN - PETTY ($950 & UNDER)', 'ROBBERY', 'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT', 'BURGLARY', 'VEHICLE - STOLEN', 'BRANDISH WEAPON', 'INTIMATE PARTNER - SIMPLE ASSAULT', 'THEFT, PERSON', 'BATTERY WITH SEXUAL CONTACT', 'BIKE - STOLEN', 'INTIMATE PARTNER - AGGRAVATED ASSAULT', 'BATTERY POLICE (SIMPLE)', 'TRESPASSING', 'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)', 'THEFT FROM MOTOR VEHICLE - ATTEMPT', 'THROWING OBJECT AT MOVING VEHICLE', 'THEFT OF IDENTITY', 'BUNCO, GRAND THEFT', 'ATTEMPTED ROBBERY', 'OTHER ASSAULT', 'BOMB SCARE', 'VIOLATION OF RESTRAINING ORDER', 'SEXUAL PENETRATION W/FOREIGN OBJECT', 'VIOLATION OF COURT ORDER', 'SHOTS FIRED AT INHABITED DWELLING', 'BURGLARY, ATTEMPTED', 'FAILURE TO YIELD', 'PURSE SNATCHING', 'LETTERS, LEWD - TELEPHONE CALLS, LEWD', 'INDECENT EXPOSURE', 'VIOLATION OF TEMPORARY RESTRAINING ORDER', 'BUNCO, PETTY THEFT', 'KIDNAPPING - GRAND ATTEMPT', 'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)', 'RESISTING ARREST', 'DISCHARGE FIREARMS/SHOTS FIRED', 'KIDNAPPING', 'LEWD/LASCIVIOUS ACTS WITH CHILD', 'LEWD CONDUCT', 'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH', 'CHILD NEGLECT (SEE 300 W.I.C.)', 'CONTEMPT OF COURT', 'DOCUMENT FORGERY / STOLEN FELONY', 'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)', 'BUNCO, ATTEMPT', 'ORAL COPULATION', 'THEFT PLAIN - ATTEMPT', 'CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT', 'RAPE, ATTEMPTED', 'SHOPLIFTING - ATTEMPT', 'BOAT - STOLEN', 'EXTORTION', 'FALSE IMPRISONMENT', 'BURGLARY FROM VEHICLE, ATTEMPTED', 'THEFT FROM MOTOR VEHICLE - GRAND ($950.01 AND OVER)', 'THREATENING PHONE CALLS/LETTERS', 'VEHICLE - ATTEMPT STOLEN', 'PICKPOCKET', 'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)', 'UNAUTHORIZED COMPUTER ACCESS', 'COUNTERFEIT', 'DISTURBING THE PEACE', 'CREDIT CARDS, FRAUD USE ($950 & UNDER)', 'THEFT FROM PERSON - ATTEMPT', 'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT', 'CRIMINAL HOMICIDE', 'PROWLER', 'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $950 & UNDER', 'CHILD ANNOYING (17YRS & UNDER)', 'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER', 'CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)', 'CHILD PORNOGRAPHY', 'PEEPING TOM', 'SEX, UNLAWFUL(INC MUTUAL CONSENT, PENETRATION W/ FRGN OBJ', 'BATTERY ON A FIREFIGHTER', 'TILL TAP - PETTY ($950 & UNDER)', 'CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT', 'DRIVING WITHOUT OWNER CONSENT (DWOC)', 'LYNCHING - ATTEMPTED', 'STALKING', 'CHILD STEALING', 'CRUELTY TO ANIMALS', 'HUMAN TRAFFICKING - COMMERCIAL SEX ACTS', 'RECKLESS DRIVING', 'PURSE SNATCHING', 'ILLEGAL DUMPING', 'CREDIT CARDS, FRAUD USE ($950.01 & OVER)', 'BIKE - ATTEMPTED STOLEN', 'DOCUMENT WORTHLESS ($200 & UNDER)', 'FALSE POLICE REPORT', 'DOCUMENT WORTHLESS ($200.01 & OVER)', 'CONSPIRACY', 'CONTRIBUTING', 'DISHONEST EMPLOYEE - GRAND THEFT', 'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE', 'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)', 'LYNCHING', 'PIMPING', 'WEAPONS POSSESSION/BOMBING', 'DISRUPT SCHOOL', 'THEFT, COIN MACHINE - ATTEMPT', 'THEFT, COIN MACHINE - PETTY ($950 & UNDER)', 'VEHICLE, STOLEN - OTHER (MOTORIZED SCOOTERS, BIKES, ETC)', 'GRAND THEFT / INSURANCE FRAUD', 'CHILD ABANDONMENT', 'DISHONEST EMPLOYEE - PETTY THEFT', 'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $950.01', 'PANDERING', 'TILL TAP - GRAND THEFT ($950.01 & OVER)', 'TELEPHONE PROPERTY - DAMAGE', 'BIGAMY', 'GRAND THEFT / AUTO REPAIR', 'PICKPOCKET, ATTEMPT', 'BRIBERY', 'PETTY THEFT - AUTO REPAIR', 'INCITING A RIOT', 'DRUNK ROLL', 'MANSLAUGHTER, NEGLIGENT', 'TILL TAP - ATTEMPT', 'BESTIALITY, CRIME AGAINST NATURE SEXUAL ASSAULT WITH ANIMAL', 'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)', 'DRUGS, TO A MINOR', 'DISHONEST EMPLOYEE ATTEMPTED THEFT', 'INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)', 'FIREARMS EMERGENCY PROTECTIVE ORDER (FIREARMS EPO)', 'BLOCKING DOOR INDUCTION CENTER', 'FIREARMS RESTRAINING ORDER (FIREARMS RO)', 'BOAT - ATTEMPTED STOLEN', 'FAILURE TO DISPERSE'), index =0)


    vict_age = st.number_input("Edad", min_value=15, max_value=120, step=1, value=15)
    vict_sex = st.selectbox('Ingresa tu género', ("Male", "Female", "None"), index=0)
    vict_descent = st.selectbox('Descendencia étnica',('Otro asiático (Other Asian)', 'Negro (Black)', 'Chino (Chinese)', 'Camboyano (Cambodian)', 'Filipino', 'Guamaniano', 'Hispano/Latino/Mexicano (Hispanic/Latin/Mexican)', 'Indígena americano/alaska nativo (American Indian/Alaskan Native)', 'Japonés (Japanese)', 'Coreano (Korean)', 'Laosiano (Laotian)', 'Otro', 'Isleño del Pacífico (Pacific Islander)', 'Samoano', 'Hawaiano', 'Vietnamita', 'Blanco (White)', 'Desconocido (Unknown)', 'Indio asiático (Asian Indian)'), index=0)
    premis_cd = st.selectbox('Lugar del Incidente',("SINGLE FAMILY DWELLING", "SIDEWALK", "POLICE FACILITY", "MULTI-UNIT DWELLING (APARTMENT, DUPLEX, ETC)", "BEAUTY SUPPLY STORE", "NIGHT CLUB (OPEN EVENINGS ONLY)", "DEPARTMENT STORE", "STREET", "PARKING LOT", "HOTEL", "COFFEE SHOP (STARBUCKS, COFFEE BEAN, PEET'S, ETC.)", "ALLEY", "PUBLIC RESTROOM/OUTSIDE*", "GARAGE/CARPORT", "MTA BUS", "MINI-MART", "OTHER BUSINESS", "VEHICLE, PASSENGER/TRUCK", "OTHER STORE", "MTA - RED LINE - UNION STATION", "RESTAURANT/FAST FOOD", "MTA - RED LINE - PERSHING SQUARE", "DRUG STORE", "SINGLE RESIDENCE OCCUPANCY (SRO'S) LOCATIONS", "PARKING UNDERGROUND/BUILDING", "HOSPITAL", "MARKET", "LA UNION STATION (NOT LINE SPECIFIC)", "MISSIONS/SHELTERS", "BAR/COCKTAIL/NIGHTCLUB", "DETENTION/JAIL FACILITY", "OTHER PREMISE", "CLOTHING STORE", "BANK", "MTA - BLUE LINE - 7TH AND METRO CENTER", "OTHER/OUTSIDE", "STAPLES CENTER *", "CONSTRUCTION SITE", "MEDICAL/DENTAL OFFICES", "MTA - RED LINE - 7TH AND METRO CENTER", "LIQUOR STORE", "TOBACCO SHOP", "HIGH-RISE BUILDING", "MUNICIPAL BUS LINE INCLUDES LADOT/DASH", "OTHER RESIDENCE", "BUS STOP", "MTA - PURPLE LINE - PERSHING SQUARE", "BAR/SPORTS BAR (OPEN DAY & NIGHT)", "LIBRARY", "MTA - RED LINE - CIVIC CENTER/GRAND PARK", "GOVERNMENT FACILITY (FEDERAL,STATE, COUNTY & CITY)", "SEX ORIENTED/BOOK STORE/STRIP CLUB/GENTLEMAN'S CLUB", "MTA - PURPLE LINE - CIVIC CENTER/GRAND PARK", "UNDERPASS/BRIDGE*", "SHOPPING MALL (COMMON AREA)", "TRANSPORTATION FACILITY (AIRPORT)", "PARK/PLAYGROUND", "HEALTH SPA/GYM", "FRAT HOUSE/SORORITY/DORMITORY", "YARD (RESIDENTIAL/BUSINESS)", "MTA - GOLD LINE - UNION STATION", "BEAUTY/BARBER SHOP", "DRIVEWAY", "AMTRAK TRAIN", "FURNITURE STORE", "7TH AND METRO CENTER (NOT LINE SPECIFIC)", "PUBLIC STORAGE", "COLLEGE/JUNIOR COLLEGE/UNIVERSITY", "CONVENTION CENTER", "LAUNDROMAT", "OFFICE BUILDING/OFFICE", "ABANDONED BUILDING ABANDONED HOUSE", "ENTERTAINMENT/COMEDY CLUB (OTHER)", "MTA - EXPO LINE - 7TH AND METRO CENTER", "BASKETBALL COURTS", "OTHER RR TRAIN (UNION PAC, SANTE FE ETC", "MUSEUM", "HORSE RACING/SANTA ANITA PARK*", "TRUCK, COMMERICAL", "TUNNEL", "JEWELRY STORE", "CHURCH/CHAPEL (CHANGED 03-03 FROM CHURCH/TEMPLE)", "MTA PROPERTY OR PARKING LOT", "HIGH SCHOOL", "GAS STATION", "BUS-CHARTER/PRIVATE", "JUNIOR HIGH SCHOOL", "MTA - RED LINE - VERMONT/BEVERLY", "MTA - RED LINE - WESTLAKE/MACARTHUR PARK", "SWAP MEET", "STAIRWELL*", "FREEWAY", "ELEMENTARY SCHOOL", "MTA - RED LINE - VERMONT/SANTA MONICA", "NURSING/CONVALESCENT/RETIREMENT HOME", "DIY CENTER (LOWE'S,HOME DEPOT,OSH,CONTRACTORS WAREHOUSE)", "VALET", "SPECIALTY SCHOOL/OTHER", "AUTO REPAIR SHOP", "DISCOUNT STORE (99 CENT,DOLLAR,ETC.)", "CELL PHONE STORE", "MOTEL", "STORAGE SHED", "PORCH, RESIDENTIAL", "MAIL BOX", "MOBILE HOME/TRAILERS/CONSTRUCTION TRAILERS/RV'S/MOTORHOME", "APARTMENT/CONDO COMMON LAUNDRY ROOM", "CONDOMINIUM/TOWNHOUSE", "AUTO DEALERSHIP (CHEVY, FORD, BMW, MERCEDES, ETC.)", "MTA - EXPO LINE - EXPO/WESTERN", "AUTO SUPPLY STORE*", "DELIVERY SERVICE (FED EX, UPS, COURIERS,COURIER SERVICE)*", "RECYCLING CENTER", "MTA - EXPO LINE - EXPO/CRENSHAW", "MTA - EXPO LINE - EXPO/LA BREA", "NAIL SALON", "GROUP HOME", "HOSPICE", "TRANSITIONAL HOUSING/HALFWAY HOUSE", "DAY CARE/CHILDREN*", "CAR WASH", "MTA - EXPO LINE - JEFFERSON/USC", "COLISEUM", "MTA - EXPO LINE - EXPO/VERMONT", "WAREHOUSE", "MTA - EXPO LINE - EXPO PARK/USC", "MTA - GOLD LINE - LINCOLN/CYPRESS", "TELECOMMUNICATION FACILITY/LOCATION", "STUDIO (FILM/PHOTOGRAPHIC/MUSIC)", "CHECK CASHING*", "PET STORE", "PATIO*", "BEACH", "TRANSIENT ENCAMPMENT", "TOW YARD*", "MTA - SILVER LINE - HARBOR GATEWAY TRANSIT CTR", "VACANT LOT", "SLIPS/DOCK/MARINA/BOAT", "BALCONY*", "AUTOMATED TELLER MACHINE (ATM)", "PHARMACY INSIDE STORE OR SUPERMARKET*", "MANUFACTURING COMPANY", "PAWN SHOP", "VISION CARE FACILITY*", "ELECTRONICS STORE (IE:RADIO SHACK, ETC.)", "FIRE STATION", "AUTO SALES LOT", "MTA - SILVER LINE - PACIFIC COAST HWY", "PRIVATE SCHOOL/PRESCHOOL", "DAY CARE/ADULTS*", "OIL REFINERY", "TV/RADIO/APPLIANCE", "MTA - GOLD LINE - SOTO", "ABORTION CLINIC/ABORTION FACILITY*") ,index=0)
    weapon_used_cd = st.selectbox('Arma Usada',('STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE)', 'UNKNOWN WEAPON/OTHER WEAPON', 'ROCK/THROWN OBJECT', 'VERBAL THREAT', 'FOLDING KNIFE', 'BLUNT INSTRUMENT', 'BOTTLE', 'SEMI-AUTOMATIC PISTOL', 'OTHER CUTTING INSTRUMENT', 'HAND GUN', 'PHYSICAL PRESENCE', 'VEHICLE', 'SCISSORS', 'STICK', 'MACHETE', 'OTHER KNIFE', 'ICE PICK', 'KNIFE WITH BLADE 6INCHES OR LESS', 'FIRE', 'GLASS', 'SIMULATED GUN', 'KNIFE WITH BLADE OVER 6 INCHES IN LENGTH', 'DEMAND NOTE', 'BOMB THREAT', 'PIPE/METAL PIPE', 'UNKNOWN FIREARM', 'MACE/PEPPER SPRAY', 'HAMMER', 'BELT FLAILING INSTRUMENT/CHAIN', 'UNKNOWN TYPE CUTTING INSTRUMENT', 'SCREWDRIVER', 'KITCHEN KNIFE', 'AIR PISTOL/REVOLVER/RIFLE/BB GUN', 'BRASS KNUCKLES', 'REVOLVER', 'SWITCH BLADE', 'CLUB/BAT', 'STUN GUN', 'AXE', 'RIFLE', 'ASSAULT WEAPON/UZI/AK47/ETC', 'OTHER FIREARM', 'SHOTGUN', 'ANTIQUE FIREARM', 'FIXED OBJECT', 'SEMI-AUTOMATIC RIFLE', 'BOARD', 'CAUSTIC CHEMICAL/POISON', 'CONCRETE BLOCK/BRICK', 'EXPLOXIVE DEVICE', 'DIRK/DAGGER', 'SYRINGE', 'TIRE IRON', 'SCALDING LIQUID', 'RAZOR BLADE', 'CLEAVER', 'DOG/ANIMAL (SIC ANIMAL ON)', 'TOY GUN', 'MARTIAL ARTS WEAPONS', 'SWORD', 'SAWED OFF RIFLE/SHOTGUN', 'BOWIE KNIFE', 'RAZOR', 'STRAIGHT RAZOR', 'LIQUOR/DRUGS', 'AUTOMATIC WEAPON/SUB-MACHINE GUN', 'STARTER PISTOL/REVOLVER', 'UZI SEMIAUTOMATIC ASSAULT RIFLE', 'UNK TYPE SEMIAUTOMATIC ASSAULT RIFLE', 'BOW AND ARROW', 'BLACKJACK', 'HECKLER & KOCH 93 SEMIAUTOMATIC ASSAULT RIFLE', 'MAC-11 SEMIAUTOMATIC ASSAULT WEAPON', 'ROPE/LIGATURE', 'MAC-10 SEMIAUTOMATIC ASSAULT WEAPON', 'RELIC FIREARM', 'HECKLER & KOCH 91 SEMIAUTOMATIC ASSAULT RIFLE', 'M-14 SEMIAUTOMATIC ASSAULT RIFLE'), index=0)
    status = st.selectbox('Estado',('Adult Other', 'Invest Cont', 'Adult Arrest', 'Juv Arrest', 'Juv Other', 'UNK') ,index=0)

    # Botón para realizar la predicción
    if st.button('Realizar Predicción'):
        # Realiza la predicción y muestra el resultado
        # resultado_prediccion = hacer_prediccion(time_occ, area, crm_cd, vict_age, vict_sex, vict_descent, premis_cd, weapon_used_cd, status)
        # st.success(f'La predicción de área es: {resultado_prediccion}')
        area_dict = {"Central": 1, 
                     "Rampart": 2,
                     "Southwest": 3,
                     "Hollenbeck": 4, 
                     "Harbor": 5,
                     "Hollywood": 6,
                     "Wilshire": 7, 
                     "West LA": 8,
                     "Van Nuys": 9,
                     "Wset Valley": 10, 
                     "Northheast": 11,
                     "77th Street": 12,
                     "Newton": 13,
                     "Pacific": 14, 
                     "N Hollywood": 15,
                     "Foothill": 16,
                     "Devonshire": 17,
                     "Southeast": 18, 
                     "Mission": 19,
                     "Olympic": 20,
                     "Topanga": 21,
                     }
        delitos_dict = {
        'BATTERY - SIMPLE ASSAULT': 624,
        'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE': 845,
        'VANDALISM - MISDEMEANOR ($399 OR UNDER)': 745,
        'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)': 740,
        'RAPE, FORCIBLE': 121,
        'SHOPLIFTING - PETTY THEFT ($950 & UNDER)': 442,
        'OTHER MISCELLANEOUS CRIME': 946,
        'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD': 341,
        'BURGLARY FROM VEHICLE': 330,
        'CRIMINAL THREATS - NO WEAPON DISPLAYED': 930,
        'ARSON': 648,
        'THEFT PLAIN - PETTY ($950 & UNDER)': 440,
        'ROBBERY': 210,
        'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT': 230,
        'BURGLARY': 310,
        'VEHICLE - STOLEN': 510,
        'BRANDISH WEAPON': 761,
        'INTIMATE PARTNER - SIMPLE ASSAULT': 626,
        'THEFT, PERSON': 350,
        'BATTERY WITH SEXUAL CONTACT': 860,
        'BIKE - STOLEN': 480,
        'INTIMATE PARTNER - AGGRAVATED ASSAULT': 236,
        'BATTERY POLICE (SIMPLE)': 623,
        'TRESPASSING': 888,
        'THEFT FROM MOTOR VEHICLE - PETTY ($950 & UNDER)': 420,
        'THEFT FROM MOTOR VEHICLE - ATTEMPT': 421,
        'THROWING OBJECT AT MOVING VEHICLE': 647,
        'THEFT OF IDENTITY': 354,
        'BUNCO, GRAND THEFT': 662,
        'ATTEMPTED ROBBERY': 220,
        'OTHER ASSAULT': 625,
        'BOMB SCARE': 755,
        'VIOLATION OF RESTRAINING ORDER': 901,
        'SEXUAL PENETRATION W/FOREIGN OBJECT': 815,
        'VIOLATION OF COURT ORDER': 900,
        'SHOTS FIRED AT INHABITED DWELLING': 251,
        'BURGLARY, ATTEMPTED': 320,
        'FAILURE TO YIELD': 890,
        'PURSE SNATCHING': 351,
        'LETTERS, LEWD  -  TELEPHONE CALLS, LEWD': 956,
        'INDECENT EXPOSURE': 850,
        'VIOLATION OF TEMPORARY RESTRAINING ORDER': 902,
        'BUNCO, PETTY THEFT': 664,
        'KIDNAPPING - GRAND ATTEMPT': 920,
        'SHOPLIFTING-GRAND THEFT ($950.01 & OVER)': 343,
        'RESISTING ARREST': 437,
        'DISCHARGE FIREARMS/SHOTS FIRED': 753,
        'KIDNAPPING': 910,
        'LEWD/LASCIVIOUS ACTS WITH CHILD': 760,
        'LEWD CONDUCT': 762,
        'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH': 821,
        'CHILD NEGLECT (SEE 300 W.I.C.)': 237,
        'CONTEMPT OF COURT': 903,
        'DOCUMENT FORGERY / STOLEN FELONY': 649,
        'EMBEZZLEMENT, GRAND THEFT ($950.01 & OVER)': 668,
        'BUNCO, ATTEMPT': 666,
        'ORAL COPULATION': 820,
        'THEFT PLAIN - ATTEMPT': 441,
        'CHILD ABUSE (PHYSICAL) - SIMPLE ASSAULT': 627,
        'RAPE, ATTEMPTED': 122,
        'SHOPLIFTING - ATTEMPT': 443,
        'BOAT - STOLEN': 487,
        'EXTORTION': 940,
        'FALSE IMPRISONMENT': 434,
        'BURGLARY FROM VEHICLE, ATTEMPTED': 410,
        'THEFT FROM MOTOR VEHICLE - GRAND ($950.01 AND OVER)': 331,
        'THREATENING PHONE CALLS/LETTERS': 928,
        'VEHICLE - ATTEMPT STOLEN': 520,
        'PICKPOCKET': 352,
        'EMBEZZLEMENT, PETTY THEFT ($950 & UNDER)': 670,
        'UNAUTHORIZED COMPUTER ACCESS': 661,
        'COUNTERFEIT': 660,
        'DISTURBING THE PEACE': 886,
        'CREDIT CARDS, FRAUD USE ($950 & UNDER)': 654,
        'THEFT FROM PERSON - ATTEMPT': 450,
        'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT': 250,
        'CRIMINAL HOMICIDE': 110,
        'PROWLER': 933,
        'DEFRAUDING INNKEEPER/THEFT OF SERVICES, $950 & UNDER': 951,
        'CHILD ANNOYING (17YRS & UNDER)': 813,
        'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER': 231,
        'CRM AGNST CHLD (13 OR UNDER) (14-15 & SUSP 10 YRS OLDER)': 812,
        'CHILD PORNOGRAPHY': 814,
        'PEEPING TOM': 932,
        'SEX, UNLAWFUL(INC MUTUAL CONSENT, PENETRATION W/ FRGN OBJ': 810,
        'BATTERY ON A FIREFIGHTER': 622,
        'TILL TAP - PETTY ($950 & UNDER)': 471,
        'CHILD ABUSE (PHYSICAL) - AGGRAVATED ASSAULT': 235,
        'DRIVING WITHOUT OWNER CONSENT (DWOC)': 433,
        'LYNCHING - ATTEMPTED': 436,
        'STALKING': 763,
        'CHILD STEALING': 922,
        'CRUELTY TO ANIMALS': 943,
        'HUMAN TRAFFICKING - COMMERCIAL SEX ACTS': 822,
        'RECKLESS DRIVING': 438,
        'PURSE SNATCHING': 451,
        'ILLEGAL DUMPING': 949,
        'CREDIT CARDS, FRAUD USE ($950.01 & OVER)': 653,
        'BIKE - ATTEMPTED STOLEN': 485,
        'DOCUMENT WORTHLESS ($200 & UNDER)': 652,
        'FALSE POLICE REPORT': 439,
        'DOCUMENT WORTHLESS ($200.01 & OVER)': 651,
        'CONSPIRACY': 944,
        'CONTRIBUTING': 954,
        'DISHONEST EMPLOYEE - GRAND THEFT': 345,
        'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE': 921,
        'THEFT, COIN MACHINE - GRAND ($950.01 & OVER)': 473,
        'LYNCHING': 435,
        'PIMPING': 805,
        'WEAPONS POSSESSION/BOMBING': 756,
        'DISRUPT SCHOOL': 880,
        'THEFT, COIN MACHINE - ATTEMPT': 475,
        'THEFT, COIN MACHINE - PETTY ($950 & UNDER)': 474,
        'VEHICLE, STOLEN - OTHER (MOTORIZED SCOOTERS, BIKES, ETC)': 522,
        'GRAND THEFT / INSURANCE FRAUD': 347,
        'CHILD ABANDONMENT': 870,
        'DISHONEST EMPLOYEE - PETTY THEFT': 444,
        'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER $950.01': 950,
        'PANDERING': 806,
        'TILL TAP - GRAND THEFT ($950.01 & OVER)': 470,
        'TELEPHONE PROPERTY - DAMAGE': 924,
        'BIGAMY': 948,
        'GRAND THEFT / AUTO REPAIR': 349,
        'PICKPOCKET, ATTEMPT': 452,
        'BRIBERY': 942,
        'PETTY THEFT - AUTO REPAIR': 446,
        'INCITING A RIOT': 882,
        'DRUNK ROLL': 353,
        'MANSLAUGHTER, NEGLIGENT': 113,
        'TILL TAP - ATTEMPT': 472,
        'BESTIALITY, CRIME AGAINST NATURE SEXUAL ASSAULT WITH ANIMAL': 840,
        'REPLICA FIREARMS(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE)': 931,
        'DRUGS, TO A MINOR': 865,
        'DISHONEST EMPLOYEE ATTEMPTED THEFT': 445,
        'INCEST (SEXUAL ACTS BETWEEN BLOOD RELATIVES)': 830,
        'FIREARMS EMERGENCY PROTECTIVE ORDER (FIREARMS EPO)': 904,
        'BLOCKING DOOR INDUCTION CENTER': 432, 'FIREARMS RESTRAINING ORDER (FIREARMS RO)': 906,
        'BOAT - ATTEMPTED STOLEN': 491, 'FAILURE TO DISPERSE': 884
            }

 

        sex_parse_dict = {"Male": 1, "Female": 2}
        vict_descent_dict  = {'Otro asiático (Other Asian)': 0,'Negro (Black)': 1,'Chino (Chinese)': 2,
            'Camboyano (Cambodian)': 3,'Filipino': 4,'Guamaniano': 5,'Hispano/Latino/Mexicano (Hispanic/Latin/Mexican)': 6,
            'Indígena americano/alaska nativo (American Indian/Alaskan Native)': 7,'Japonés (Japanese)': 8,'Coreano (Korean)': 9,'Laosiano (Laotian)': 10,'Otro': 11,'Isleño del Pacífico (Pacific Islander)': 12,'Samoano': 13,'Hawaiano': 14,'Vietnamita': 15, 'Blanco (White)': 16, 'Desconocido (Unknown)': 17, 'Indio asiático (Asian Indian)': 18
        }

        premis_cd_dict = {"SINGLE FAMILY DWELLING": 501, "SIDEWALK": 102, "POLICE FACILITY": 726, "MULTI-UNIT DWELLING (APARTMENT, DUPLEX, ETC)": 502, "BEAUTY SUPPLY STORE": 409, "NIGHT CLUB (OPEN EVENINGS ONLY)": 735, "DEPARTMENT STORE": 404, "STREET": 101, "PARKING LOT": 108, "HOTEL": 503, "COFFEE SHOP (STARBUCKS, COFFEE BEAN, PEET'S, ETC.)": 252, "ALLEY": 103, "PUBLIC RESTROOM/OUTSIDE*": 148, "GARAGE/CARPORT": 707, "MTA BUS": 801, "MINI-MART": 401, "OTHER BUSINESS": 203, "VEHICLE, PASSENGER/TRUCK": 122, "OTHER STORE": 406, "MTA - RED LINE - UNION STATION": 900, "RESTAURANT/FAST FOOD": 210, "MTA - RED LINE - PERSHING SQUARE": 902, "DRUG STORE": 403, "SINGLE RESIDENCE OCCUPANCY (SRO'S) LOCATIONS": 516, "PARKING UNDERGROUND/BUILDING": 123, "HOSPITAL": 701, "MARKET": 402, "LA UNION STATION (NOT LINE SPECIFIC)": 834, "MISSIONS/SHELTERS": 517, "BAR/COCKTAIL/NIGHTCLUB": 207, "DETENTION/JAIL FACILITY": 753, "OTHER PREMISE": 710, "CLOTHING STORE": 405, "BANK": 602, "MTA - BLUE LINE - 7TH AND METRO CENTER": 931, "OTHER/OUTSIDE": 116, "STAPLES CENTER *": 741, "CONSTRUCTION SITE": 118, "MEDICAL/DENTAL OFFICES": 719, "MTA - RED LINE - 7TH AND METRO CENTER": 903, "LIQUOR STORE": 202, "TOBACCO SHOP": 244, "HIGH-RISE BUILDING": 744, "MUNICIPAL BUS LINE INCLUDES LADOT/DASH": 802, "OTHER RESIDENCE": 504, "BUS STOP": 124, "MTA - PURPLE LINE - PERSHING SQUARE": 917, "BAR/SPORTS BAR (OPEN DAY & NIGHT)": 733, "LIBRARY": 738, "MTA - RED LINE - CIVIC CENTER/GRAND PARK": 901, "GOVERNMENT FACILITY (FEDERAL,STATE, COUNTY & CITY)": 725, "SEX ORIENTED/BOOK STORE/STRIP CLUB/GENTLEMAN'S CLUB": 706, "MTA - PURPLE LINE - CIVIC CENTER/GRAND PARK": 916, "UNDERPASS/BRIDGE*": 152, "SHOPPING MALL (COMMON AREA)": 727, "TRANSPORTATION FACILITY (AIRPORT)": 212, "PARK/PLAYGROUND": 109, "HEALTH SPA/GYM": 717, "FRAT HOUSE/SORORITY/DORMITORY": 508, "YARD (RESIDENTIAL/BUSINESS)": 121, "MTA - GOLD LINE - UNION STATION": 966, "BEAUTY/BARBER SHOP": 218, "DRIVEWAY": 104, "AMTRAK TRAIN": 810, "FURNITURE STORE": 413, "7TH AND METRO CENTER (NOT LINE SPECIFIC)": 835, "PUBLIC STORAGE": 221, "COLLEGE/JUNIOR COLLEGE/UNIVERSITY": 722, "CONVENTION CENTER": 713, "LAUNDROMAT": 222, "OFFICE BUILDING/OFFICE": 702, "ABANDONED BUILDING ABANDONED HOUSE": 506, "ENTERTAINMENT/COMEDY CLUB (OTHER)": 703, "MTA - EXPO LINE - 7TH AND METRO CENTER": 940, "BASKETBALL COURTS": 757, "OTHER RR TRAIN (UNION PAC, SANTE FE ETC": 811, "MUSEUM": 754, "HORSE RACING/SANTA ANITA PARK*": 715, "TRUCK, COMMERICAL": 113, "TUNNEL": 106, "JEWELRY STORE": 201,"CHURCH/CHAPEL (CHANGED 03-03 FROM CHURCH/TEMPLE)": 708, "MTA PROPERTY OR PARKING LOT": 135, "HIGH SCHOOL": 721, "GAS STATION": 301, "BUS-CHARTER/PRIVATE": 111, "JUNIOR HIGH SCHOOL": 720, "MTA - RED LINE - VERMONT/BEVERLY": 906, "MTA - RED LINE - WESTLAKE/MACARTHUR PARK": 904, "SWAP MEET": 216, "STAIRWELL*": 138, "FREEWAY": 110, "ELEMENTARY SCHOOL": 704, "MTA - RED LINE - VERMONT/SANTA MONICA": 907, "NURSING/CONVALESCENT/RETIREMENT HOME": 510, "DIY CENTER (LOWE'S,HOME DEPOT,OSH,CONTRACTORS WAREHOUSE)": 243, "VALET": 156, "SPECIALTY SCHOOL/OTHER": 729, "AUTO REPAIR SHOP": 217, "DISCOUNT STORE (99 CENT,DOLLAR,ETC.)": 242, "CELL PHONE STORE": 248, "MOTEL": 505, "STORAGE SHED": 120, "PORCH, RESIDENTIAL": 119, "MAIL BOX": 145, "MOBILE HOME/TRAILERS/CONSTRUCTION TRAILERS/RV'S/MOTORHOME": 509, "APARTMENT/CONDO COMMON LAUNDRY ROOM": 515, "CONDOMINIUM/TOWNHOUSE": 507, "AUTO DEALERSHIP (CHEVY, FORD, BMW, MERCEDES, ETC.)": 255, "MTA - EXPO LINE - EXPO/WESTERN": 946, "AUTO SUPPLY STORE*": 408, "DELIVERY SERVICE (FED EX, UPS, COURIERS,COURIER SERVICE)*": 232, "RECYCLING CENTER": 251, "MTA - EXPO LINE - EXPO/CRENSHAW": 947, "MTA - EXPO LINE - EXPO/LA BREA": 949, "NAIL SALON": 220, "GROUP HOME": 514, "HOSPICE": 237, "TRANSITIONAL HOUSING/HALFWAY HOUSE": 518, "DAY CARE/CHILDREN*": 231, "CAR WASH": 247, "MTA - EXPO LINE - JEFFERSON/USC": 943, "COLISEUM": 712, "MTA - EXPO LINE - EXPO/VERMONT": 945, "WAREHOUSE": 213, "MTA - EXPO LINE - EXPO PARK/USC": 944, "MTA - GOLD LINE - LINCOLN/CYPRESS": 968, "TELECOMMUNICATION FACILITY/LOCATION": 238, "STUDIO (FILM/PHOTOGRAPHIC/MUSIC)": 254, "CHECK CASHING*": 229, "PET STORE": 411, "PATIO*": 146, "BEACH": 117, "TRANSIENT ENCAMPMENT": 158, "TOW YARD*": 151, "MTA - SILVER LINE - HARBOR GATEWAY TRANSIT CTR": 897, "VACANT LOT": 107, "SLIPS/DOCK/MARINA/BOAT": 705, "BALCONY*": 140, "AUTOMATED TELLER MACHINE (ATM)": 605, "PHARMACY INSIDE STORE OR SUPERMARKET*": 235, "MANUFACTURING COMPANY": 204, "PAWN SHOP": 211, "VISION CARE FACILITY*": 236, "ELECTRONICS STORE (IE:RADIO SHACK, ETC.)": 412, "FIRE STATION": 752, "AUTO SALES LOT": 208, "MTA - SILVER LINE - PACIFIC COAST HWY": 898, "PRIVATE SCHOOL/PRESCHOOL": 723, "DAY CARE/ADULTS*": 230, "OIL REFINERY": 303, "TV/RADIO/APPLIANCE": 206, "MTA - GOLD LINE - SOTO": 962, "ABORTION CLINIC/ABORTION FACILITY*": 227 }
        status_dict = {'Adult Other': 0, 'Invest Cont': 1, 'Adult Arrest': 2, 'Juv Arrest': 3, 'Juv Other': 4, 'UNK': 5}

        weapon_used_dict = {'STRONG-ARM (HANDS, FIST, FEET OR BODILY FORCE)': 400, 'UNKNOWN WEAPON/OTHER WEAPON': 500, 'ROCK/THROWN OBJECT': 306, 'VERBAL THREAT': 511, 'FOLDING KNIFE': 204, 'BLUNT INSTRUMENT': 302, 'BOTTLE': 212, 'SEMI-AUTOMATIC PISTOL': 109, 'OTHER CUTTING INSTRUMENT': 218, 'HAND GUN': 102, 'PHYSICAL PRESENCE': 515, 'VEHICLE': 307, 'SCISSORS': 216, 'STICK': 308, 'MACHETE': 215, 'OTHER KNIFE': 207, 'ICE PICK': 214, 'KNIFE WITH BLADE 6INCHES OR LESS': 200, 'FIRE': 506, 'GLASS': 221, 'SIMULATED GUN': 113, 'KNIFE WITH BLADE OVER 6 INCHES IN LENGTH': 201, 'DEMAND NOTE': 504, 'BOMB THREAT': 501, 'PIPE/METAL PIPE': 312, 'UNKNOWN FIREARM': 106, 'MACE/PEPPER SPRAY': 512, 'HAMMER': 311, 'BELT FLAILING INSTRUMENT/CHAIN': 301, 'UNKNOWN TYPE CUTTING INSTRUMENT': 223, 'SCREWDRIVER': 219, 'KITCHEN KNIFE': 205, 'AIR PISTOL/REVOLVER/RIFLE/BB GUN': 114, 'BRASS KNUCKLES': 303, 'REVOLVER': 101, 'SWITCH BLADE': 206, 'CLUB/BAT': 304, 'STUN GUN': 513, 'AXE': 211, 'RIFLE': 103, 'ASSAULT WEAPON/UZI/AK47/ETC': 115, 'OTHER FIREARM': 107, 'SHOTGUN': 104, 'ANTIQUE FIREARM': 116, 'FIXED OBJECT': 305, 'SEMI-AUTOMATIC RIFLE': 110, 'BOARD': 309, 'CAUSTIC CHEMICAL/POISON': 503, 'CONCRETE BLOCK/BRICK': 310, 'EXPLOXIVE DEVICE': 505, 'DIRK/DAGGER': 203, 'SYRINGE': 220, 'TIRE IRON': 514, 'SCALDING LIQUID': 510, 'RAZOR BLADE': 210, 'CLEAVER': 213, 'DOG/ANIMAL (SIC ANIMAL ON)': 516, 'TOY GUN': 112, 'MARTIAL ARTS WEAPONS': 508, 'SWORD': 217, 'SAWED OFF RIFLE/SHOTGUN': 105, 'BOWIE KNIFE': 202, 'RAZOR': 208, 'STRAIGHT RAZOR': 209, 'LIQUOR/DRUGS': 507, 'AUTOMATIC WEAPON/SUB-MACHINE GUN': 108, 'STARTER PISTOL/REVOLVER': 111, 'UZI SEMIAUTOMATIC ASSAULT RIFLE': 118, 'UNK TYPE SEMIAUTOMATIC ASSAULT RIFLE': 117, 'BOW AND ARROW': 502, 'BLACKJACK': 300, 'HECKLER & KOCH 93 SEMIAUTOMATIC ASSAULT RIFLE': 122, 'MAC-11 SEMIAUTOMATIC ASSAULT WEAPON': 120, 'ROPE/LIGATURE': 509, 'MAC-10 SEMIAUTOMATIC ASSAULT WEAPON': 119, 'RELIC FIREARM': 125, 'HECKLER & KOCH 91 SEMIAUTOMATIC ASSAULT RIFLE': 121, 'M-14 SEMIAUTOMATIC ASSAULT RIFLE': 124}

        area = area_dict[area]
        crm_cd = delitos_dict[crm_cd]
        vict_sex = sex_parse_dict[vict_sex]
        vict_descent = vict_descent_dict[vict_descent]
        premis_cd = premis_cd_dict[premis_cd]
        weapon_used_cd = weapon_used_dict[weapon_used_cd]
        status = status_dict[status]

        row = [time_occ, area, crm_cd, vict_age, vict_sex, vict_descent, premis_cd, weapon_used_cd, status]
        scaled_row = modelo_escalado.transform([row])
        predicted = modelo_original.predict(scaled_row)[0]
        gravedad_dict = {0: 'Leve', 1: 'Grave: Si un delito conlleva la aplicación de una pena grave como castigo, se puede hablar de un delito grave'}
        st.success(f'- {gravedad_dict[predicted]}')


    st.markdown("<h1 style='color: #9D1B28; text-align: center;'>10 .- CONCLUSIONES</h1>", unsafe_allow_html=True)
    st.write("<p style='text-align: justify; font-weight: bold;'> </p>", unsafe_allow_html=True)

    if st.button("Ir a la Página Principal"):
         st.session_state.pagina_actual = "main"



if "pagina_actual" not in st.session_state:
    st.session_state.pagina_actual = "main"

# Lógica de navegación basada en el estado actual
if st.session_state.pagina_actual == "main":
    main()
elif st.session_state.pagina_actual == "pagina_1":
    pagina_1()
elif st.session_state.pagina_actual == "pagina_2":
    pagina_2()
elif st.session_state.pagina_actual == "pagina_3":
    pagina_3()
