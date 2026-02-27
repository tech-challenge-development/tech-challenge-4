import streamlit as st

st.markdown("<h1 style='color: #d94e41;'>Análise Exploratória</h1>", unsafe_allow_html=True)
st.divider()

st.markdown("### 🎯 Objetivo da Análise")

st.write("""
O painel analítico foi desenvolvido para apoiar a equipe médica na identificação de padrões comportamentais 
associados ao excesso de peso na população analisada.

A análise permite compreender o perfil atual dos pacientes, identificar fatores modificáveis 
e direcionar estratégias preventivas baseadas em dados.
""")

st.markdown("### 🧩 Principais Insights Obtidos")

st.write("""
• Alta prevalência de sobrepeso e obesidade na base analisada.  
• Redução progressiva da atividade física conforme aumento da classificação de peso.  
• Maior frequência de consumo de alimentos hipercalóricos nos grupos com obesidade.  
• Padrões alimentares entre refeições associados ao excesso de peso.

Além dos principais Insights descritos acima, o relatório possui indicadores de correlação e intensidade para cada um dos fatores presentes na pesquisa, mas não identificados como relevantes no momento.
Esses indicadores permitirão o acompanhamento frequente de novas variáveis e a identificação de padrões de comportamento que possam alterar o resultado na população diagnosticada.
""")

st.divider()

st.markdown("### 📊 Acessar Painel Analítico")

dashboard_url = "https://app.powerbi.com/links/j-Wq19ONy3?ctid=11dbbfe2-89b8-4549-be10-cec364e59551&pbi_source=linkShare"

st.link_button("🔎 Visualizar Dashboard Interativo", dashboard_url)
st.caption("Para acessar o painel é necessário o login com um usuário com domínio FIAP.com.br")
