import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------

st.set_page_config(
    page_title="CUIDADO OPERATIVO 360°",
    page_icon="🩺",
    layout="centered"
)

# ---------------------------------------------------------
# INFORMACIÓN BASE DEL PROYECTO
# ---------------------------------------------------------

CONTENIDO_PROYECTO = """
CUIDADO OPERATIVO 360° es un programa integral orientado a la
promoción de la salud laboral y prevención de riesgos ergonómicos
y cardiovasculares en trabajadores operativos.

El proyecto contempla:

- Diagnóstico basal en salud laboral.
- Tamizaje cardiovascular.
- Seguimiento de indicadores ergonómicos.
- Intervenciones educativas.
- Pausas activas dirigidas.
- Higiene postural.
- Prevención de lesiones.
- Estrategias de microeducación digital.
- Registro de dolor lumbar.
- Registro de dolor cervical.
- Registro de fatiga laboral.
- Registro de realización de pausas activas.
- Registro de horas de trabajo en postura prolongada.
- Presión arterial.
- Peso.
- Talla.
- IMC.
- Perímetro abdominal.
- Indicadores institucionales.
- Cobertura de trabajadores evaluados.
- Participación en pausas activas.
- Comparativos mensuales.

El proyecto también contempla conceptualmente una aplicación móvil
para el monitoreo de la salud laboral.
"""

# ---------------------------------------------------------
# TÍTULO
# ---------------------------------------------------------

st.title("🩺 CUIDADO OPERATIVO 360°")

st.write(
    "### Tutor conversacional educativo sobre salud laboral"
)

st.info(
    "Puedes escribir tu pregunta directamente. "
    "No necesitas seleccionar una opción de un menú."
)

# ---------------------------------------------------------
# MEMORIA DE LA CONVERSACIÓN
# ---------------------------------------------------------

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# ---------------------------------------------------------
# RESPUESTAS DEL TUTOR
# ---------------------------------------------------------

def responder(pregunta):

    texto = pregunta.lower()

    if "qué es cuidado operativo" in texto or "que es cuidado operativo" in texto:

        return """
**CUIDADO OPERATIVO 360°** es un programa orientado a la promoción
de la salud laboral y a la prevención de riesgos ergonómicos y
cardiovasculares en trabajadores operativos.

Su propuesta combina diagnóstico, seguimiento, educación y
estrategias preventivas.

Por ejemplo, contempla el diagnóstico basal, el tamizaje
cardiovascular, el seguimiento de indicadores ergonómicos y
las pausas activas.

¿Quieres que te explique ahora **cómo funciona el diagnóstico
basal**?
"""

    elif "diagnóstico basal" in texto or "diagnostico basal" in texto:

        return """
El **diagnóstico basal en salud laboral** corresponde a la etapa
inicial del proyecto.

Su finalidad es obtener información inicial sobre el estado de
salud laboral de los trabajadores.

Dentro del proyecto se contemplan:

- Encuestas estructuradas.
- Peso.
- Talla.
- IMC.
- Perímetro abdominal.

Después de obtener esta información se pueden desarrollar
estrategias de intervención y seguimiento.

¿Quieres que te haga una pregunta para comprobar si lo entendiste?
"""

    elif "pausa activa" in texto or "pausas activas" in texto:

        return """
Las **pausas activas** forman parte de las estrategias de
intervención de CUIDADO OPERATIVO 360°.

El proyecto contempla su implementación como una estrategia
preventiva dentro de la salud laboral.

Además, el proyecto plantea registrar la realización de pausas
activas para poder hacer seguimiento.

💡 **Pregunta para ti:**

¿Por qué crees que es importante realizar pausas activas durante
una jornada laboral?

Respóndeme con tus propias palabras y te daré retroalimentación.
"""

    elif "higiene postural" in texto:

        return """
La **higiene postural** es uno de los componentes de intervención
del proyecto.

CUIDADO OPERATIVO 360° contempla capacitación en higiene postural
y prevención de lesiones.

La finalidad educativa es ayudar a los trabajadores a reconocer
y prevenir situaciones relacionadas con posturas inadecuadas
durante las actividades laborales.

¿Quieres que te explique esto mediante un ejemplo de un trabajador
operativo?
"""

    elif "dolor lumbar" in texto:

        return """
El **dolor lumbar** aparece dentro del módulo diagnóstico del
proyecto.

La aplicación conceptual contempla registrar este indicador para
realizar seguimiento de aspectos relacionados con la salud laboral.

No se trata solamente de registrar el dato: el proyecto busca
generar información que permita orientar estrategias preventivas.

¿Quieres que continuemos con el **dolor cervical y la fatiga laboral**?
"""

    elif "dolor cervical" in texto:

        return """
El **dolor cervical** también forma parte de los indicadores
contemplados en el módulo diagnóstico.

Su registro permite recopilar información relacionada con las
condiciones de salud laboral de los trabajadores.

¿Quieres que ahora revisemos qué otros indicadores contempla
el módulo diagnóstico?
"""

    elif "fatiga" in texto:

        return """
La **fatiga laboral** es otro de los elementos que el proyecto
plantea registrar dentro del módulo diagnóstico.

Esto permite recopilar información relacionada con la situación
laboral de los trabajadores y posteriormente realizar seguimiento.

¿Quieres que te haga una pregunta sobre este tema?
"""

    elif "imc" in texto:

        return """
El **IMC (índice de masa corporal)** aparece dentro de las
mediciones contempladas en la etapa diagnóstica.

Para obtenerlo se utilizan el peso y la talla.

En CUIDADO OPERATIVO 360° estos datos hacen parte del diagnóstico
basal y del registro de información de salud laboral.

Si quieres, puedo explicarte **paso a paso cómo se relacionan
peso, talla e IMC dentro del proyecto**.
"""

    elif "presión arterial" in texto or "presion arterial" in texto:

        return """
La **presión arterial** forma parte del registro clínico
contemplado en el proyecto.

CUIDADO OPERATIVO 360° incluye este dato dentro del componente
relacionado con el seguimiento de la salud laboral y el tamizaje
cardiovascular.

¿Quieres que te explique qué papel cumple el **tamizaje
cardiovascular** dentro del proyecto?
"""

    elif "tamizaje cardiovascular" in texto:

        return """
El **tamizaje cardiovascular** es uno de los componentes de la
propuesta de CUIDADO OPERATIVO 360°.

Está orientado a identificar información relacionada con factores
de riesgo cardiovascular en trabajadores operativos.

El proyecto contempla, entre otros datos, el registro de presión
arterial, peso, talla, IMC y perímetro abdominal.

¿Quieres que te haga una pregunta sobre el tamizaje cardiovascular?
"""

    elif "perímetro abdominal" in texto or "perimetro abdominal" in texto:

        return """
El **perímetro abdominal** es una de las mediciones contempladas
en el proyecto.

Se encuentra dentro de los datos que pueden registrarse durante
el diagnóstico y seguimiento de la salud laboral.

Junto con otros datos, permite disponer de indicadores para el
seguimiento institucional.

¿Quieres que repasemos cuáles son todas las mediciones que
contempla el proyecto?
"""

    elif "aplicación" in texto or "app" in texto:

        return """
El proyecto contempla conceptualmente una **aplicación móvil**
orientada al monitoreo de la salud laboral.

Entre sus funcionalidades planteadas están:

1. Módulo diagnóstico.
2. Registro clínico.
3. Panel administrativo.

El panel administrativo permitiría visualizar información como
la cobertura de trabajadores evaluados, indicadores institucionales,
participación en pausas activas y comparativos mensuales.

¿Quieres que te explique cada módulo?
"""

    elif "enfermería" in texto or "enfermeria" in texto:

        return """
El proyecto resalta el papel de **enfermería** en los procesos
de innovación, gestión del riesgo y transformación de entornos
laborales saludables.

Dentro del proyecto, el personal de enfermería también participa
en el componente de registro clínico.

¿Quieres que hablemos sobre el papel de enfermería dentro de
CUIDADO OPERATIVO 360°?
"""

    elif (
        "úlcera" in texto
        or "ulcera" in texto
        or "medicamento" in texto
        or "dosis" in texto
        or "herida" in texto
    ):

        return """
Ese tema específico **no está desarrollado en el contenido del
proyecto CUIDADO OPERATIVO 360° que estamos utilizando como base**.

Por eso no voy a inventar información y presentarla como si
formara parte del proyecto.

Sí puedo ayudarte con los temas que sí contempla, como:

- Riesgos ergonómicos.
- Riesgos cardiovasculares.
- Pausas activas.
- Higiene postural.
- Prevención de lesiones.
- Diagnóstico basal.
- Tamizaje cardiovascular.
- Indicadores de salud laboral.
"""

    elif "pregunta" in texto or "quiz" in texto or "evalúame" in texto:

        return """
🧠 **Vamos a comprobar tus conocimientos.**

**Pregunta 1:**

¿Cuál es uno de los principales objetivos de CUIDADO OPERATIVO
360°?

A. Diagnosticar enfermedades infecciosas.

B. Promover la salud laboral y prevenir riesgos ergonómicos y
cardiovasculares.

C. Realizar únicamente tratamientos farmacológicos.

Escribe **A, B o C** y te explicaré tu respuesta.
"""

    elif texto.strip() == "b":

        return """
🎉 **¡Correcto!**

La respuesta es **B**.

CUIDADO OPERATIVO 360° está orientado a la promoción de la
salud laboral y a la prevención de riesgos ergonómicos y
cardiovasculares en trabajadores operativos.

Vamos con una segunda pregunta:

**¿Cuál de estos elementos forma parte del diagnóstico del proyecto?**

A. Peso, talla e IMC.

B. Tratamiento antibiótico.

C. Administración de medicamentos.

¿Cuál eliges?
"""

    else:

        return f"""
Entiendo tu pregunta:

> {pregunta}

Para responder de forma fiel al proyecto, necesito relacionarla
con los contenidos de **CUIDADO OPERATIVO 360°**.

Los principales temas que podemos estudiar son:

• Diagnóstico basal en salud laboral  
• Tamizaje cardiovascular  
• Riesgos ergonómicos  
• Pausas activas  
• Higiene postural  
• Prevención de lesiones  
• Dolor lumbar y cervical  
• Fatiga laboral  
• IMC  
• Presión arterial  
• Perímetro abdominal  
• Aplicación de monitoreo de salud laboral  
• Indicadores institucionales  
• Papel de enfermería

Puedes preguntarme directamente, por ejemplo:

**"Explícame las pausas activas"**

o:

**"Hazme preguntas sobre el proyecto"**
"""

# ---------------------------------------------------------
# MOSTRAR CONVERSACIÓN
# ---------------------------------------------------------

for mensaje in st.session_state.mensajes:

    with st.chat_message(mensaje["rol"]):
        st.markdown(mensaje["contenido"])

# ---------------------------------------------------------
# CAJA DE PREGUNTAS
# ---------------------------------------------------------

pregunta = st.chat_input(
    "Escribe aquí tu pregunta..."
)

if pregunta:

    st.session_state.mensajes.append(
        {
            "rol": "user",
            "contenido": pregunta
        }
    )

    respuesta = responder(pregunta)

    st.session_state.mensajes.append(
        {
            "rol": "assistant",
            "contenido": respuesta
        }
    )

    st.rerun()
