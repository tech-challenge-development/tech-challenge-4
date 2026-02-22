import streamlit as st

st.set_page_config(page_title="Data Analytics - Turma 10DTAT - Grupo 56", layout="wide")

pg = st.navigation([
    st.Page("introducao.py", title="Introdução ao Tech Challenge 4", icon="📖"),
    st.Page("metricasdeobesidade.py", title="Métricas de Obesidade (OMS)", icon="⚕️"),
    st.Page("analisexploratoriadedados.py", title="Analise Exploratória de Dados (EDA)", icon="📊"),
    st.Page("modelopreditivo.py", title="Modelo Preditivo", icon="💻"),
    st.Page("conclusao.py", title="Conclusão", icon="🎯")
])

with st.sidebar:
    st.markdown("<h3 style='margin-bottom: 0px; padding-bottom: 0px;'>Data Analytics - Turma 10DTAT - Grupo 56</h3>", unsafe_allow_html=True)
    st.divider()
    st.markdown("""
    *Evandro Anholeto*  
    *Pedro Alencar*  
    *Renan Ribas*
    """)

pg.run()