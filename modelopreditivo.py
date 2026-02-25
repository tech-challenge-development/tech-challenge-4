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
    st.header("📊 Detalhamento Técnico")
    
    tab1, tab2 = st.tabs(["Matriz de Confusão", "Relatório de Classificação"])
    
    with tab1:
        st.write("A matriz abaixo mostra onde o modelo acerta e onde ocorrem as raras confusões entre categorias próximas.")
        try:
            img_cm = Image.open('confusion_matrix.png')
            st.image(img_cm, caption="Precisão por Categoria (Real vs Predito)", use_container_width=True)
        except:
            st.warning("Imagem da matriz de confusão não encontrada.")
            
    with tab2:
        st.write("O modelo apresenta um **F1-Score médio de 0.96**, indicando um ótimo equilíbrio entre sensibilidade e precisão em todas as 7 classes de peso.")
        
        # Static table based on notebook results
        report_data = {
            'Categoria': ['Insuficiente', 'Normal', 'Sobrepeso I', 'Sobrepeso II', 'Obesidade I', 'Obesidade II', 'Obesidade III'],
            'Precisão': ['0.96', '0.83', '0.97', '0.98', '1.00', '0.98', '0.98'],
            'Recall': ['0.91', '0.95', '0.99', '0.98', '0.98', '0.90', '0.98']
        }
        st.table(pd.DataFrame(report_data))

    st.info("💡 **Ação**: Utilize estes insights para focar em políticas de conscientização sobre o consumo de vegetais e a redução de lanches entre as refeições.")

if __name__ == "__main__":
    show()
else:
    show()
