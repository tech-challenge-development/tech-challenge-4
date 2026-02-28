import streamlit as st

st.markdown("<h1 style='color: #d94e41;'>Conclusão</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("### 🎯 Objetivo do Projeto")

st.write("""
O presente estudo teve como objetivo desenvolver uma solução analítica e preditiva 
para apoiar a equipe médica na identificação de fatores associados ao excesso de peso, 
utilizando técnicas de machine learning aplicadas a dados comportamentais e antropométricos.
""")

st.markdown("### 🤖 Modelo Preditivo")

st.write("""
A partir da etapa de feature engineering, foram tratadas inconsistências da base, 
padronizadas variáveis categóricas e estruturadas novas representações numéricas 
para otimização do desempenho do modelo.

O modelo XGBoost foi selecionado por sua robustez e capacidade de capturar 
relações não lineares entre variáveis, alcançando performance superior a 75% 
de acurácia, superando o critério mínimo exigido.
""")

st.markdown("### 📊 Principais Insights Analíticos")

st.write("""
A análise exploratória evidenciou que:

• A população apresenta alta prevalência de sobrepeso e obesidade.  
• A redução da atividade física está fortemente associada ao aumento da severidade do peso.  
• O consumo frequente de alimentos hipercalóricos se destaca nos grupos com obesidade.  
""")

st.markdown("### 🔎 Integração entre Modelo e Dashboard")

st.write("""
A convergência entre análise exploratória e modelo preditivo reforça a consistência dos achados. 

Enquanto o modelo permite a classificação e priorização de risco individual, 
o dashboard fornece contexto estratégico para a tomada de decisão clínica.
""")

st.markdown("### 🩺 Aplicação Estratégica")

st.write("""
A solução desenvolvida permite:

• Triagem preditiva de pacientes com maior risco.  
• Direcionamento de intervenções preventivas.  
• Apoio à construção de programas estruturados de promoção à saúde.  

A integração entre modelagem preditiva e análise estratégica de dados 
representa uma ferramenta relevante para apoiar equipes médicas 
na atuação preventiva e na otimização de recursos.
""")
