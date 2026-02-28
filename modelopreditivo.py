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
            st.metric("Acurácia Geral", "78.25%")
        with c2:
            st.metric("Estabilidade Média (CV)", "79.21%")
        
        st.write("""
        A consistência entre os dados de teste e a validação cruzada confirma que o modelo é **altamente confiável** sob a perspectiva de saúde populacional. Ele apresenta uma excelente capacidade de generalização, o que significa que está pronto para classificar novos perfis de usuários com um alto índice de assertividade, suportando decisões clínicas e de bem-estar.
        """)

    st.subheader("📈 Estabilidade via Validação Cruzada (Temporal)")
    with st.container(border=True):
        st.write("""
        O monitoramento por "folds" (divisões de dados) demonstra que o modelo mantém sua performance estável em diferentes cenários, reforçando a segurança biológica das previsões e a robustez dos indicadores de saúde analisados.
        """)
        try:
            img_cv = Image.open('cv_stability.png')
            st.image(img_cv, caption="Estabilidade da Acurácia em Diferentes Amostras de Dados", use_container_width=True)
        except:
            st.warning("Gráfico de estabilidade não encontrado.")

    st.divider()

    st.header("🔍 Direcionadores de Classificação")
    
    with st.container(border=True):
        st.write("""
        **💡 Diferencial Estratégico: Foco na Causa, não no Sintoma**
        
        Nossa inteligência foi treinada **removendo propositalmente as variáveis de Peso e Altura**. 
        Diferente de uma calculadora de IMC comum, desafiamos o modelo a identificar a obesidade através de padrões de **comportamento e genética**. 
        Isso valida nossa solução como uma ferramenta poderosa de **medicina preventiva e análise de risco**, capaz de prever tendências antes mesmo que o ganho de massa ocorra.
        """)

    st.write("""
    Abaixo, identificamos os fatores que mais influenciam o diagnóstico do modelo após essa filtragem estratégica.
    
    **O que essa análise mostra?**
    Isso mede o quanto cada variável contribuiu para reduzir a incerteza do modelo. Quanto maior a barra, mais vezes e com mais impacto essa característica foi determinante para decidir a categoria de obesidade de uma pessoa.
    """)

    try:
        img_importance = Image.open('feature_importance.png')
        st.image(img_importance, caption="Top 15 Indicadores de Saúde que Direcionam a Classificação", use_container_width=True)
    except:
        st.warning("Gráfico de importância de variáveis não encontrado.")

    st.subheader("📚 Insights Estratégicos baseados no Modelo")
    with st.container(border=True):
        st.write("""
        - **Histórico Familiar (Preditor Dominante)**: A genética e o ambiente familiar aparecem como o divisor de águas mais forte na predisposição à obesidade.
        - **Perfil de Gênero**: O modelo detecta variações metabólicas e comportamentais distintas que impactam o ganho de massa de forma diferenciada entre homens e mulheres.
        - **Hábito de Lanches (CAEC)**: A frequência de consumo extra-refeição é um "gatilho" crítico para o desequilíbrio calórico identificado pela IA.
        - **Consumo de Vegetais (FCVC)**: O fator com maior peso positivo em termos de proteção e controle metabólico nutricional.
        - **Mobilidade e Transporte Ativo**: A escolha do meio de condução (como caminhar) é um indicador comportamental de alto impacto na saúde preventiva.
        """)


    st.divider()

    st.header("📊 Matriz de Assertividade Clínica")
    
    st.subheader("📍 Realidade vs. Predição da IA")
    with st.container(border=True):
        st.write("""
        A Matriz de Confusão abaixo detalha o rigor do modelo em cada categoria:
        - **Concentração de Precisão**: A diagonal principal destaca onde o modelo acertou com exatidão o diagnóstico.
        - **Tendência de Erros Coerentes**: Quando ocorre divergência, o modelo tende a classificar para categorias vizinhas (ex: Sobrepeso para Obesidade I), o que mantém a coerência clínica da gravidade do quadro.
        """)
        try:
            st.image("confusion_matrix.png", use_container_width=True)
        except FileNotFoundError:
            st.warning("Gráfico da Matriz de Confusão não encontrado.")

    st.divider()
    st.info("""
    **💡 Visão Humanizada e Estratégica:**
    "Nosso modelo não olha apenas para o peso, mas para a **'jornada'** do indivíduo. Ele identifica que o histórico familiar e a frequência de lanches são tão determinantes quanto a atividade física no diagnóstico final."
    """)

if __name__ == "__main__":
    show()
else:
    show()
