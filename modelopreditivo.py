import streamlit as st
import pandas as pd
from PIL import Image

def show():
    st.markdown("<h1 style='color: #d94e41; text-align: center;'>Modelo Preditivo de Obesidade</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em;'>Traduzindo dados científicos em insights estratégicos para a saúde.</p>", unsafe_allow_html=True)
    st.divider()

    st.write("""
    O objetivo desta etapa foi desenvolver um modelo de inteligência artificial capaz de classificar o nível de obesidade de um indivíduo com alta precisão, 
    baseando-se em seus hábitos de vida, características demográficas e físicas.
    """)

    # --- Resumo Executivo ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Acurácia Geral", "96%", "+1.5%")
    with col2:
        st.metric("Modelo", "XGBoost", help="Algoritmo de Gradient Boosting de alto desempenho")
    with col3:
        st.metric("Confiabilidade", "Excelente", help="Consistência demonstrada em validação cruzada")

    st.divider()

    # --- O Que Direciona o Modelo? ---
    st.header("🔍 O que mais influencia a classificação?")
    st.write("""
    Utilizamos algoritmos de importância de atributos para identificar quais comportamentos e características são os maiores "drivers" de obesidade no modelo. 
    Entender esses fatores é crucial para direcionar intervenções de saúde pública ou personalizadas.
    """)

    try:
        img_importance = Image.open('feature_importance.png')
        st.image(img_importance, caption="Top 10 Fatores de Influência", use_container_width=True)
    except:
        st.warning("Imagem de importância das features não encontrada.")

    with st.expander("📚 Interpretação dos Principais Insights"):
        st.write("""
        - **Gênero e Peso**: Como esperado, são pilares fundamentais para a determinação do IMC e do nível de obesidade associado.
        - **CAEC (Consumo entre refeições)**: O hábito de não comer entre as refeições (`CAEC_no`) apareceu como um forte diferencial na estabilidade do peso.
        - **FCVC (Consumo de Vegetais)**: A frequência de consumo de vegetais é um dos indicadores dietéticos mais fortes para a saúde metabólica no conjunto de dados.
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
