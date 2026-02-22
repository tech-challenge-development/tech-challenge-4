import streamlit as st

st.markdown("<h1 style='color: #d94e41;'>Obesidade e seus Fatores (OMS)</h1>", unsafe_allow_html=True)
st.divider()

st.header("O que é a Obesidade segundo a OMS?")
st.write("""
A **Organização Mundial da Saúde (OMS)** define a obesidade como uma **doença crônica** caracterizada pelo acúmulo anormal ou excessivo de gordura corporal que pode prejudicar a saúde. 

Desde 1990, a prevalência de obesidade adulta mais que dobrou, e a adolescente quadruplicou. Em 2022, estima-se que **uma em cada oito pessoas** no mundo vivia com obesidade.
""")

st.header("📊 Panorama Global em Números (2022)")
met_col1, met_col2, met_col3 = st.columns(3)

with met_col1:
    st.metric(label="Adultos com Sobrepeso", value="2.5 Bilhões", delta="43% da pop. adulta")
    st.caption("Aumento de 25% (1990) para 43% (2022)")

with met_col2:
    st.metric(label="Adultos com Obesidade", value="890 Milhões", delta="16% da pop. global")
    st.caption("Taxa que mais que dobrou desde 1990")

with met_col3:
    st.metric(label="Crianças e Adolescentes", value="160 Milhões", delta="Obesidade")
    st.caption("390 milhões no total possuem sobrepeso")

st.write("""
Além dos adultos, a situação entre os jovens é preocupante: em 2022, mais de **390 milhões** de crianças e adolescentes (5-19 anos) estavam acima do peso, sendo **160 milhões** diagnosticados com obesidade.
""")


st.header("Principais Fatores Causais")
st.write("""
As causas do sobrepeso e da obesidade são multifatoriais, resultando principalmente de um **desequilíbrio entre a ingestão de energia (dieta) e o gasto energético (atividade física)**.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🍎 Dieta e Hábitos")
    st.write("""
    * Consumo elevado de alimentos ultraprocessados (ricos em gordura e açúcar).
    * Acesso facilitado a alimentos de alta densidade energética mas baixa qualidade nutricional.
    * Marketing agressivo de alimentos não saudáveis.
    """)
    
    st.markdown("### 🧬 Genética e Biologia")
    st.write("""
    * A genética influencia como o corpo armazena e processa energia.
    * Interações complexas entre neurobiologia e comportamentos alimentares.
    """)

with col2:
    st.markdown("### 🏃 Sedentarismo")
    st.write("""
    * Redução da atividade física devido à natureza sedentária de muitos trabalhos.
    * Mudanças nos meios de transporte e urbanização crescente.
    """)
    
    st.markdown("### 🏙️ Fatores Ambientais")
    st.write("""
    * "Ambientes Obesogênicos" que dificultam escolhas saudáveis.
    * Fatores socioeconômicos (acesso a alimentos frescos e áreas de lazer).
    """)

st.divider()

st.header("🩺 Impactos e Riscos para a Saúde")
st.write("""
A obesidade não é apenas uma preocupação estética; ela é um fator determinante para a morbidade e mortalidade prematura. Segundo a **OMS**, o risco de problemas de saúde aumenta progressivamente conforme o grau da obesidade.
""")

risk_col1, risk_col2 = st.columns(2)

with risk_col1:
    st.markdown("### 🫀 Doenças Cardiovasculares")
    st.write("""
    Aumento significativo do risco de doenças cardíacas, hipertensão arterial e Acidentes Vasculares Cerebrais (**AVC**).
    """)
    
    st.markdown("### 🩸 Diabetes Tipo 2")
    st.write("""
    A obesidade é a principal causa evitável do diabetes tipo 2, que pode levar a problemas renais, amputações e perda de visão.
    """)

    st.markdown("### 🦴 Problemas Musculoesqueléticos")
    st.write("""
    Sobrecarga nas articulações, resultando em doenças degenerativas como a **osteoartrite**.
    """)

with risk_col2:
    st.markdown("### 🎗️ Câncer")
    st.write("""
    Maior probabilidade de desenvolver diversos tipos de câncer, incluindo os de **mama, cólon, endométrio e rins**.
    """)
    
    st.markdown("### 🫁 Distúrbios Respiratórios")
    st.write("""
    Dificuldade respiratória crônica, asma e **apneia do sono**.
    """)

    st.markdown("### 🧠 Saúde Mental")
    st.write("""
    Impactos psicológicos profundos, como **baixa autoestima, ansiedade e depressão**, que podem dificultar ainda mais o tratamento.
    """)

st.divider()
st.caption("Fonte: Organização Mundial da Saúde (OMS) - World Health Organization")
