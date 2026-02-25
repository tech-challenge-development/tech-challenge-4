import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("Obesity.csv")
    df["BMI"] = df["Weight"] / (df["Height"] ** 2)
    
    def risk_group(row):
        if row["Obesity"] in ["Insufficient_Weight", "Normal_Weight"]:
            return "Baixo Risco"
        elif row["Obesity"] in ["Overweight_Level_I", "Overweight_Level_II"]:
            return "Risco Moderado"
        else:
            return "Alto Risco"
    
    df["Risk_Group"] = df.apply(risk_group, axis=1)
    return df

df = load_data()

##==##

st.sidebar.header("Filtros Clínicos")

gender = st.sidebar.multiselect(
    "Gênero",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

df = df[df["Gender"].isin(gender)]

##==##

st.title("Painel Clínico de Avaliação de Risco de Obesidade")
st.markdown("Sistema de apoio à decisão médica")
st.markdown("---")

##===##

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Pacientes", len(df))

alto_risco = df[df["Risk_Group"] == "Alto Risco"]

col2.metric("% Alto Risco", f"{round(len(alto_risco)/len(df)*100,1)}%")

col3.metric("BMI Médio", round(df["BMI"].mean(),2))

col4.metric("Idade Média Alto Risco", round(alto_risco["Age"].mean(),1))

##==##

st.subheader("Distribuição de Risco Clínico")

fig = px.pie(df, names="Risk_Group",
             title="Classificação de Risco da População Avaliada")

st.plotly_chart(fig, use_container_width=True)

##==##

st.subheader("Impacto da Atividade Física no Risco")

fig2 = px.box(
    df,
    x="Risk_Group",
    y="FAF",
    title="Redução da Atividade Física nos Grupos de Maior Risco"
)

st.plotly_chart(fig2, use_container_width=True)

##==##

st.subheader("Tempo de Tela e Severidade")

fig3 = px.box(
    df,
    x="Risk_Group",
    y="TER",
    title="Aumento do Tempo de Tela nos Grupos de Alto Risco"
)

st.plotly_chart(fig3, use_container_width=True)

##==##

st.subheader("Correlação entre Variáveis Numéricas")

corr = df.corr(numeric_only=True)

fig4 = px.imshow(corr, text_auto=True)

st.plotly_chart(fig4, use_container_width=True)

##==##

st.subheader("Perfil Estatístico - Pacientes Alto Risco")

st.dataframe(alto_risco.describe())
