import streamlit as st

st.markdown("# 📈 Trading App: Inteligencia de Mercados")
st.markdown("""
**Plataforma de análisis cuantitativo diseñada para evaluar tendencias del mercado de valores global y respaldar decisiones financieras basadas en datos empíricos.**
""")

st.divider()

# 2. Características Técnicas (Lo que evaluará el banco)
st.markdown("### Capacidades Core del Sistema")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Análisis Técnico Dinámico**
    Cálculo de RSI, MACD y Medias Móviles optimizado para baja latencia, procesando el historial completo de la acción seleccionada.
    """)

with col2:
    st.success("""
    **Ingeniería de Series de Tiempo**
    Extracción, limpieza y reestructuración de datos financieros en tiempo real mediante la API de Yahoo Finance y Pandas.
    """)

with col3:
    st.warning("""
    **Visualización de Alta Fidelidad**
    Gráficos interactivos construidos con Plotly, permitiendo inspección de velas japonesas y líneas de tendencia con precisión milimétrica.
    """)

st.divider()

st.markdown("### Arquitectura y Desarrollo")
col_img, col_text, col_trad = st.columns([1, 2.2, 1.5], vertical_alignment="center")

with col_img:
    # Sin parámetros extra. Streamlit lo escala al ancho de esta columna (proporción 1)
    st.image("attachments/profile.png") 

with col_text:
    st.markdown("""
    Desarrollado aplicando rigor analítico y metodologías de las **ciencias exactas y la física** al ecosistema de la ciencia de datos financieros. 
    
    Este proyecto demuestra la capacidad de construir herramientas robustas desde cero, priorizando la estabilidad del código, la fricción cero en el despliegue de software y la claridad en la inteligencia de negocios.
    
    **Conecta conmigo:**
    * 🔗 [LinkedIn](https://www.linkedin.com/in/acxelcalle)
    * 💻 [GitHub](https://github.com/AcxelCalle)
    """)
    
with col_trad:
    # Al estar en la columna 3 (proporción 1.5), será ligeramente más ancha que tu perfil
    st.image("attachments/tradingInit.jpg")
    
st.divider()
st.caption("""
**Aviso Legal / Disclaimer:** Esta aplicación es un proyecto de demostración (Portfolio Project) desarrollado exclusivamente con fines académicos y de exhibición técnica. No constituye asesoramiento financiero, recomendación de inversión, ni tiene fines comerciales. Los datos son extraídos de fuentes públicas (Yahoo Finance) y pueden presentar latencia.
""")

st.markdown("<br>", unsafe_allow_html=True)
if st.button("Comenzar Análisis ➡️", use_container_width=True, type="primary"):
    st.switch_page("pages/Análisis_de_acciones.py")
