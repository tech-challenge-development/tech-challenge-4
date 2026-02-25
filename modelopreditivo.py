import streamlit as st
import pandas as pd
from PIL import Image

def show():
    st.markdown("<h1 style='color: #d94e41; text-align: center;'>Modelo Preditivo</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>Traduzindo dados científicos em insights estratégicos para a saúde.</p>", unsafe_allow_html=True)
    st.divider()

    st.write("""
    O objetivo foi um modelo de inteligência artificial capaz de classificar o nível de obesidade de um indivíduo com alta precisão, 
    baseando-se em seus hábitos de vida, características demográficas e físicas.
    """)

    # --- Resumo Executivo ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Modelo", "XGBoost")
    with col2:
        st.metric("Acurácia Geral", "96%", "+1.5%")
    with col3:
        st.metric("Confiabilidade", "Excelente")

    st.divider()

    # --- Dicionário de Dados ---
    st.header("📖 Dicionário de Dados")
    with st.container(border=True):
        st.markdown("""
        ### Características Pessoais e Demográficas
        - **Gender (Gênero)**: Sexo biológico (Female, Male).
        - **Age (Idade)**: Idade em anos (14–61).
        - **Height (Altura)**: Altura em metros (1.45–1.98 m).
        - **Weight (Peso)**: Peso em quilogramas (39–173 kg).
        - **family_history (Histórico Familiar)**: Histórico familiar de excesso de peso (yes/no).

        ### Hábitos Alimentares e Estilo de Vida
        - **FAVC (Alimentos Calóricos)**: Consumo frequente de alimentos muito calóricos (yes/no).
        - **FCVC (Vegetais)**: Frequência de consumo de vegetais (1: raramente, 2: às vezes, 3: sempre).
        - **NCP (Refeições Principais)**: Número de refeições principais por dia (1 a 4 ou mais).
        - **CAEC (Lanches entre Refeições)**: Frequência de lanches entre as refeições (no, Sometimes, Frequently, Always).
        - **SMOKE (Fumante)**: Hábito de fumar (yes/no).
        - **CH2O (Água)**: Consumo diário de água (1: < 1L, 2: 1–2L, 3: > 2L).
        - **SCC (Monitoramento Calórico)**: Monitora a ingestão calórica diária (yes/no).
        - **FAF (Atividade Física)**: Frequência semanal de atividade física (0: nenhuma, 1: 1–2x, 2: 3–4x, 3: 5x+).
        - **TUE (Dispositivos Eletrônicos)**: Tempo diário usando eletrônicos (0: 0–2h, 1: 3–5h, 2: > 5h).
        - **CALC (Álcool)**: Consumo de bebida alcoólica (no, Sometimes, Frequently, Always).
        - **MTRANS (Transporte)**: Meio de transporte habitual (Automobile, Motorbike, Bike, Public_Transportation, Walking).

        ### Variável Alvo (Label)
        - **Obesity (Nível de Obesidade)**: 
            - *Insufficient_Weight* (Abaixo do peso)
            - *Normal_Weight* (Peso normal)
            - *Overweight_Level_I* (Sobrepeso I)
            - *Overweight_Level_II* (Sobrepeso II)
            - *Obesity_Type_I* (Obesidade I)
            - *Obesity_Type_II* (Obesidade II)
            - *Obesity_Type_III* (Obesidade III)
        """)


    # --- O Que Direciona o Modelo? ---
    st.header("🔍 O que mais influencia a classificação?")
    st.write("""
    Utilizamos algoritmos de importância de atributos para identificar quais comportamentos e características são os maiores direcionadores de obesidade no modelo. 
    Entender esses fatores é crucial para direcionar intervenções de saúde pública ou personalizadas.
    """)

    try:
        img_importance = Image.open('feature_importance.png')
        st.image(img_importance, caption="Top 10 Fatores de Influência", use_container_width=True)
    except:
        st.warning("Imagem de importância das features não encontrada.")

    st.subheader("📚 Interpretação dos Principais Insights")
    with st.container(border=True):
        st.write("""
        - **Gênero e Peso**: Como esperado, são pilares fundamentais para a determinação do IMC e do nível de obesidade associado.
        - **Consumo entre refeições (CAEC)**: O hábito de não comer entre as refeições apareceu como um forte diferencial na estabilidade do peso.
        - **Consumo de Vegetais (FCVC)**: A frequência de consumo de vegetais é um dos indicadores dietéticos mais fortes para a saúde metabólica.
        - **Atividade Física (FAF) e Hidratação (CH2O)**: Embora em escalas menores, estes fatores completam o perfil de risco do indivíduo.
        """)


    st.divider()

    # --- Desempenho Técnico ---
    st.header("📊 Confiabilidade e Precisão do Modelo")
    
    st.write("""
    Para garantir que o modelo é seguro para tomada de decisão, avaliamos seu desempenho sob duas perspectivas principais: 
    a **assertividade por categoria** e a **qualidade geral das previsões**.
    """)

    # --- Container 1: Matriz de Confusão ---
    st.subheader("📍 Mapa de Assertividade (Real vs. Predito)")
    with st.container(border=True):
        st.write("""
        Este mapa (conhecido tecnicamente como Matriz de Confusão) mostra o cruzamento entre o que o indivíduo **realmente é** e o que o modelo **previu**. 
        - **Na diagonal central**: Estão os acertos (onde o modelo e a realidade coincidem).
        - **Fora da diagonal**: Estão os raros casos de erro, geralmente confundindo categorias vizinhas (ex: Sobrepeso I com Sobrepeso II), o que demonstra que o modelo é coerente mesmo quando erra.
        """)
        try:
            img_cm = Image.open('confusion_matrix.png')
            st.image(img_cm, caption="Visualização da Precisão por Nível de Peso", use_container_width=True)
        except:
            st.warning("Imagem da matriz de assertividade não encontrada.")

    # --- Container 2: Relatório de Classificação ---
    st.subheader("📈 Métricas de Qualidade por Categoria")
    with st.container(border=True):
        st.write("""
        Aqui detalhamos a "nota" do modelo para cada classe de peso. Utilizamos dois indicadores principais:
        1. **Confiança (Precisão)**: Quando o modelo diz que é "Obesidade I", qual a chance de ele estar certo? (No nosso caso, entre 83% e 100%).
        2. **Abrangência (Recall)**: De todos os casos reais de "Peso Normal", quantos o modelo conseguiu identificar corretamente?
        """)
        
        # Static table based on notebook results
        report_data = {
            'Nível de Peso': ['Abaixo do Peso', 'Peso Normal', 'Sobrepeso I', 'Sobrepeso II', 'Obesidade I', 'Obesidade II', 'Obesidade III'],
            'Confiança (Precisão)': ['96%', '83%', '97%', '98%', '100%', '98%', '98%'],
            'Abrangência (Recall)': ['91%', '95%', '99%', '98%', '98%', '90%', '98%']
        }
        st.table(pd.DataFrame(report_data))
        
        st.write("**Conclusão**: O modelo demonstra uma performance excepcional, especialmente para identificar níveis críticos de obesidade, onde a precisão chega a 100%.")
if __name__ == "__main__":
    show()
else:
    show()
