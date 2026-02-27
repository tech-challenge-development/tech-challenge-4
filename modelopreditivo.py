import streamlit as st
import pandas as pd
from PIL import Image

def show():
    st.markdown("<h1 style='color: #d94e41; text-align: center;'>Modelo Preditivo</h1>", unsafe_allow_html=True)
    st.divider()

    st.write("""
    Desenvolvemos um modelo de inteligência artificial de alta performance para classificar o nível de obesidade de forma precisa. 
    A solução integra características físicas, hábitos alimentares e estilo de vida para fornecer um diagnóstico automatizado e confiável.
    """)

    st.header("📖 Dicionário de Variáveis")
    with st.container(border=True):
        st.markdown("""
        ### Perfil Demográfico e Físico
        - **Gender (Gênero)**: Identificação biológica (Female/Male).
        - **Age (Idade)**: Faixa etária analisada (14–61 anos).
        - **Height (Altura)**: Estatura em metros (1.45–1.98 m).
        - **Weight (Peso)**: Massa corporal em quilogramas (39–173 kg).
        - **family_history (Histórico Familiar)**: Presença de casos de excesso de peso na família.

        ### Comportamentos e Estilo de Vida
        - **FAVC (Alimentos Calóricos)**: Consumo frequente de alimentos com alta densidade energética.
        - **FCVC (Vegetais)**: Frequência de ingestão de vegetais (1: Raramente a 3: Sempre).
        - **NCP (Refeições)**: Número de refeições principais ao longo do dia.
        - **CAEC (Lanches)**: Frequência de consumo de alimentos entre as refeições principais.
        - **SMOKE (Tabagismo)**: Hábito de fumar.
        - **CH2O (Hidratação)**: Consumo diário de água (1: < 1L a 3: > 2L).
        - **SCC (Monitoramento)**: Hábito de monitorar a ingestão calórica diária.
        - **FAF (Atividade Física)**: Frequência semanal de exercícios (0: Nenhuma a 3: Alta).
        - **TUE (Eletrônicos)**: Tempo diário dedicado ao uso de dispositivos tecnológicos.
        - **CALC (Álcool)**: Hrequência de consumo de bebidas alcoólicas.
        - **MTRANS (Transporte)**: Meio de locomoção predominante (Caminhada, Transporte Público, Particular, etc.).

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

    st.header("🤖 Inteligência da Solução: O Algoritmo XGBoost")
    with st.container(border=True):
        st.write("""
        A solução utiliza o **XGBoost (Extreme Gradient Boosting)**, um dos algoritmos de aprendizado de máquina mais robustos e eficientes do mercado.
        
        **Como ele decide?**
        Visualize o XGBoost como uma **comissão técnica altamente especializada**. Em vez de uma única decisão isolada, o modelo constrói uma sequência de modelos preditivos onde cada um corrige os erros do anterior. 
        Este processo de refinamento iterativo garante que a classificação final considere a interdependência complexa entre todos os hábitos do indivíduo, resultando em uma assertividade superior.
        """)

        try:
            img_xgboost = Image.open('xgboot.png')
            st.image(img_xgboost, caption="Arquitetura de decisão sequencial do XGBoost", use_container_width=True)
        except Exception:
            st.warning("Diagrama do XGBoost não encontrado.")

    st.divider()

    st.header("🏆 Performance e Confiabilidade")
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Acurácia Geral", "96.21%")
        with c2:
            st.metric("Estabilidade Média (CV)", "96.33%")
        
        st.write("""
        A consistência entre os dados de teste e a validação cruzada confirma que o modelo é **altamente confiável**. Ele possui uma excelente capacidade de generalização, o que significa que está pronto para classificar novos perfis de usuários com o mesmo nível de precisão.
        """)

    st.subheader("📈 Estabilidade via Validação Cruzada (Temporal)")
    with st.container(border=True):
        st.write("""
        O monitoramento por "folds" (divisões de dados) demonstra que o modelo mantém sua performance acima de 95% em diferentes cenários, reforçando a segurança biológica das previsões.
        """)
        try:
            img_cv = Image.open('cv_stability.png')
            st.image(img_cv, caption="Estabilidade da Acurácia em Diferentes Amostras", use_container_width=True)
        except:
            st.warning("Gráfico de estabilidade não encontrado.")

    st.divider()

    st.header("🔍 Direcionadores de Classificação")
    st.write("""
    Identificamos os fatores que mais pesam na decisão do modelo. Compreender esses direcionadores é fundamental para entender o comportamento da IA.
    """)

    try:
        img_importance = Image.open('feature_importance.png')
        st.image(img_importance, caption="Top 15 Fatores que Direcionam a Classificação", use_container_width=True)
    except:
        st.warning("Gráfico de importância de variáveis não encontrado.")

    st.subheader("📚 Insights Estratégicos")
    with st.container(border=True):
        st.write("""
        - **Peso e Gênero**: Como esperado, são os indicadores estruturais mais fortes.
        - **Influência do Meio de Transporte**: A locomoção ativa (como caminhar) aparece como um preditor positivo de saúde extremamente relevante.
        - **Hábito de Lanches (CAEC)**: A frequência de alimentação entre as refeições principais é um divisor crítico entre os níveis de sobrepeso e obesidade.
        - **Consumo de Vegetais e Hidratação**: Fatores que o modelo identifica como cruciais para a estabilidade metabólica.
        """)


    st.divider()

    st.header("📊 Matriz de Assertividade")
    
    st.subheader("📍 Realidade vs. Predição")
    with st.container(border=True):
        st.write("""
        A Matriz de Confusão abaixo detalha o rigor do modelo em cada categoria:
        - **Diagonal Dominante**: A concentração maciça na diagonal prova a alta taxa de acerto em todas as classes.
        - **Consistência em Erros**: Nos raros casos de erro, o modelo classifica para categorias adjacentes (ex: confundindo Obesidade I com II), o que indica uma interpretação coerente das tendências de massa corporal.
        """)
        try:
            img_cm = Image.open('confusion_matrix.png')
            st.image(img_cm, caption="Matriz de Confusão: Detalhamento de Acertos por Classe", use_container_width=True)
        except:
            st.warning("Matriz de assertividade não encontrada.")

if __name__ == "__main__":
    show()
else:
    show()
