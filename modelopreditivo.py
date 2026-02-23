import streamlit as st

st.markdown("<h1 style='color: #d94e41;'>Modelo Preditivo</h1>", unsafe_allow_html=True)
st.divider()

st.write("""
Nesta seção, detalhamos a construção, treinamento e avaliação do modelo de Machine Learning desenvolvido para prever os níveis de obesidade.
""")

st.subheader("🛠️ Arquitetura do Modelo")
st.write("Detalhes sobre o algoritmo escolhido (XGBoost), hiperparâmetros e pipeline de pré-processamento.")

st.subheader("📊 Métricas de Desempenho")
st.write("Resultados obtidos nos dados de teste, incluindo Acurácia, Precision, Recall, F1-Score, desvio padrão e/ou validação cruzada.")

st.info("Para testar o modelo com novos dados, acesse a página **Simulador Interativo** no menu lateral.")
