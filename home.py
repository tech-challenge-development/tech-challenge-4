import streamlit as st

st.set_page_config(page_title="Data Analytics - Turma 10DTAT - Grupo 56", layout="wide")

pg = st.navigation([
    st.Page("introducao.py", title="Introdução", icon="📖"),
    st.Page("oms.py", title="Obesidade e seus Fatores (OMS)", icon="⚕️"),
    st.Page("analisexploratoriadedados.py", title="Analise Exploratória de Dados (EDA)", icon="📊"),
    st.Page("modelopreditivov2.py", title="Modelo Preditivo", icon="📝"),
    st.Page("simulador.py", title="Simulador Interativo", icon="💻"),
    st.Page("conclusao.py", title="Conclusão", icon="🎯")
])

with st.sidebar:
    st.markdown("<h3 style='margin-bottom: 0px; padding-bottom: 0px;'>Data Analytics - Turma 10DTAT - Grupo 56 - Tech Challenge 4</h3>", unsafe_allow_html=True)
    st.divider()
    st.markdown("""
    *Evandro Anholeto*  
    *Pedro Alencar*  
    *Renan Ribas*
    """)

pg.run()