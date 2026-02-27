import streamlit as st
import pandas as pd
from PIL import Image

def show():
    st.markdown("<h1 style='color: #d94e41; text-align: center;'>Modelo Preditivo</h1>", unsafe_allow_html=True)
    st.divider()

    st.write("""
    O objetivo foi um modelo de inteligência artificial capaz de classificar o nível de obesidade de um indivíduo com alta precisão, 
    baseando-se em seus hábitos de vida, características demográficas e físicas.
    """)

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

        ### Variável Alvo
        - **Obesity (Nível de Obesidade)**: 
            - *Insufficient_Weight* (Abaixo do peso)
            - *Normal_Weight* (Peso normal)
            - *Overweight_Level_I* (Sobrepeso I)
            - *Overweight_Level_II* (Sobrepeso II)
            - *Obesity_Type_I* (Obesidade I)
            - *Obesity_Type_II* (Obesidade II)
            - *Obesity_Type_III* (Obesidade III)
        """)

    st.divider()

    st.header("🤖 A Inteligência por trás da Decisão")
    with st.container(border=True):
        st.write("""
        Para este desafio, selecionamos o **XGBoost**, uma das machine learning mais avançadas e respeitadas em ciência de dados. 
        
        Imagine o XGBoost como um **"Conselho de Especialistas Digital"**.
        Em vez de uma única análise, ele cria centenas de pequenos analistas que trabalham em conjunto. 
        O grande diferencial é que cada novo "especialista" aprende com as dificuldades do anterior, refinando as previsões sucessivamente. 
        
        Essa abordagem de **Refinamento Contínuo** é o que permite ao modelo atingir uma precisão cirúrgica, sendo ideal para lidar com a complexidade dos múltiplos fatores que influenciam a saúde e o peso.
        """)

        try:
            img_xgboost = Image.open('xgboot.png')
            st.image(img_xgboost, caption="Funcionamento do algoritmo XGBoost", use_container_width=True)
        except Exception:
            st.warning("Imagem explicativa do XGBoost não encontrada.")

    st.divider()

    st.header("🏆 Performance e Estabilidade")
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Acurácia de Teste", "96.2%")
        with c2:
            st.metric("Acurácia Média (CV)", "96.3%")
        
        st.write("""
        A proximidade entre a acurácia de teste e a média da validação cruzada indica um modelo **robusto**, 
        que não sofre de overfitting (quando o modelo decora os dados mas não aprende de verdade).
        """)

    st.subheader("📈 Estabilidade do Modelo (Cross-Validation)")
    with st.container(border=True):
        st.write("""
        O gráfico abaixo mostra como o modelo se comportou em 5 diferentes "dobras" (folds) dos dados. 
        A consistência dos resultados (todos acima de 95%) prova que a inteligência é capaz de generalizar o conhecimento para novos perfis de pacientes.
        """)
        try:
            img_cv = Image.open('cv_stabilityv2.png')
            st.image(img_cv, caption="Consistência da Acurácia por Fold", use_container_width=True)
        except:
            st.warning("Gráfico de estabilidade não encontrado.")

    st.divider()

    st.header("🔍 O que mais influencia a classificação?")
    st.write("""
    Utilizamos algoritmos de importância de atributos para identificar quais comportamentos e características são os maiores direcionadores de obesidade no modelo. 
    """)

    try:
        img_importance = Image.open('feature_importancev2.png')
        st.image(img_importance, caption="Principais Fatores de Influência", use_container_width=True)
    except:
        st.warning("Imagem de importância das features não encontrada.")

    st.subheader("📚 Interpretação dos Principais Insights")
    with st.container(border=True):
        st.write("""
        - **Gênero e Peso**: Pilares fundamentais para a determinação biológica do nível de peso.
        - **Mobilidade Ativa (Walking)**: O uso de caminhada como transporte surge como um forte indicador de saúde e preditor importante no modelo refinado.
        - **Consumo entre refeições (CAEC)**: O hábito de "lanchar" frequentemente é um dos maiores divisores de águas no modelo.
        - **Consumo de Vegetais (FCVC)**: Reflete diretamente na saúde metabólica e controle calórico.
        """)


    st.divider()

    st.header("📊 Detalhamento de Assertividade")
    
    st.subheader("📍 Mapa de Diagnóstico (Real vs. Inteligência)")
    with st.container(border=True):
        st.write("""
        Este mapa mostra onde a inteligência acerta e onde ocorrem as raras "confusões".
        - **Acertos Implacáveis**: A linha diagonal mostra que quase todos os pacientes são classificados corretamente.
        - **Margem de Erro Coerente**: Quando o modelo erra, ele geralmente aponta para um nível vizinho (ex: confunde Obesidade I com II), nunca cometendo erros grosseiros (como confundir Peso Abaixo com Obesidade III).
        """)
        try:
            img_cm = Image.open('confusion_matrixv2.png')
            st.image(img_cm, caption="Matriz de Assertividade do Modelo", use_container_width=True)
        except:
            st.warning("Imagem da matriz de assertividade não encontrada.")

if __name__ == "__main__":
    show()
else:
    show()
