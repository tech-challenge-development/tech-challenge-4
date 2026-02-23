import streamlit as st
import pandas as pd
import joblib
import os

st.markdown("<h1 style='color: #d94e41;'>Simulador Interativo</h1>", unsafe_allow_html=True)
st.divider()

st.write("""
Preencha o formulário abaixo com as características do paciente para obter uma predição sobre o nível de obesidade.
O modelo utiliza dados antropométricos e de hábitos de vida para classificar o risco.
""")

with st.form("form_predicao"):
    st.subheader("📋 Dados Pessoais")
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gênero", ["Masculino", "Feminino"])
        age = st.number_input("Idade", min_value=1, max_value=150, value=25)
        height = st.number_input("Altura (m)", min_value=0.00, max_value=3.00, value=1.70, step=0.01)
    
    with col2:
        weight = st.number_input("Peso (kg)", min_value=0.0, max_value=1000.0, value=70.0, step=0.1)
        family_history = st.selectbox("Histórico familiar de sobrepeso", ["Sim", "Não"])

    st.subheader("🍎 Hábitos Alimentares e Consumo")
    col3, col4 = st.columns(2)
    
    with col3:
        favc = st.selectbox("Consumo frequente de alimentos calóricos", ["Sim", "Não"])
        
        fcvc_opts = {1: "Raramente", 2: "Às vezes", 3: "Sempre"}
        fcvc = st.selectbox("Frequência de consumo de vegetais", options=list(fcvc_opts.keys()), format_func=lambda x: fcvc_opts[x])
        
        ncp = st.selectbox("Número de refeições principais", [1, 2, 3, 4])
        
        caec = st.selectbox("Consumo de alimentos entre as refeições", ["Não", "Às vezes", "Frequentemente", "Sempre"])

    with col4:
        ch2o_opts = {1: "Menos de 1 litro/dia", 2: "Entre 1 e 2 litros/dia", 3: "Mais de 2 litros/dia"}
        ch2o = st.selectbox("Consumo diário de água", options=list(ch2o_opts.keys()), format_func=lambda x: ch2o_opts[x])
        
        scc = st.selectbox("Monitoramento do consumo de calorias", ["Sim", "Não"])
        
        calc = st.selectbox("Consumo de álcool", ["Não", "Às vezes", "Frequentemente", "Sempre"])

    st.subheader("🏃 Estilo de Vida")
    col5, col6 = st.columns(2)
    
    with col5:
        smoke = st.selectbox("Fuma", ["Sim", "Não"])
        
        faf_opts = {0: "Nenhuma", 1: "1 a 2 vezes por semana", 2: "3 a 4 vezes por semana", 3: "5 vezes ou mais por semana"}
        faf = st.selectbox("Frequência de atividade física", options=list(faf_opts.keys()), format_func=lambda x: faf_opts[x])
    
    with col6:
        tue_opts = {0: "Até 2 horas por dia", 1: "De 3 a 5 horas por dia", 2: "Mais de 5 horas por dia"}
        tue = st.selectbox("Tempo diário em dispositivos eletrônicos", options=list(tue_opts.keys()), format_func=lambda x: tue_opts[x])
        
        mtrans = st.selectbox("Meio de transporte", ["Carro", "Moto", "Bicicleta", "Transporte público", "Caminhada"])

    submitted = st.form_submit_button("🔍 Analisar Risco")

if submitted:
    # Mapeamento para os valores esperados pelo modelo (inglês/original)
    map_gender = {"Masculino": "Male", "Feminino": "Female"}
    map_yes_no = {"Sim": "yes", "Não": "no"}
    map_caec_calc = {"Não": "no", "Às vezes": "Sometimes", "Frequentemente": "Frequently", "Sempre": "Always"}
    map_mtrans = {"Carro": "Automobile", "Moto": "Motorbike", "Bicicleta": "Bike", "Transporte público": "Public_Transportation", "Caminhada": "Walking"}

    # Preparar dados para o modelo (DataFrame com as colunas esperadas)
    data = {
        'Gender': [map_gender[gender]], 'Age': [age], 'Height': [height], 'Weight': [weight],
        'family_history': [map_yes_no[family_history]], 'FAVC': [map_yes_no[favc]], 'FCVC': [float(fcvc)],
        'NCP': [float(ncp)], 'CAEC': [map_caec_calc[caec]], 'SMOKE': [map_yes_no[smoke]], 'CH2O': [float(ch2o)], 'SCC': [map_yes_no[scc]],
        'FAF': [float(faf)], 'TUE': [float(tue)], 'CALC': [map_caec_calc[calc]], 'MTRANS': [map_mtrans[mtrans]]
    }
    df_input = pd.DataFrame(data)
    
    st.divider()
    st.markdown("### Resultado da Análise")
    
    model_path = 'modelo_obesity.joblib'
    le_path = 'label_encoder_obesity.joblib'

    try:
        # Carregar modelo e label encoder
        loaded_model = joblib.load(model_path)
        le = joblib.load(le_path)

        # Fazer a predição
        prediction = loaded_model.predict(df_input)
        prediction_proba = loaded_model.predict_proba(df_input)
        
        # Obter o rótulo da predição e a confiança
        confidence = max(prediction_proba[0]) * 100
        prediction_label = le.inverse_transform(prediction)[0]

        # Exibir o resultado
        st.metric("Nível de Obesidade Previsto", f"{prediction_label}", f"Confiança: {confidence:.2f}%")

        # Adicionar uma mensagem colorida com base no resultado
        if "Obesity" in prediction_label:
            st.error(f"O modelo indica um alto risco, classificando o paciente como: **{prediction_label}**.")
        elif "Overweight" in prediction_label:
            st.warning(f"O modelo indica um risco moderado, classificando o paciente como: **{prediction_label}**.")
        else:
            st.success(f"O modelo indica um baixo risco, classificando o paciente como: **{prediction_label}**.")

    except FileNotFoundError:
        st.error("ERRO: Arquivos do modelo ('modelo_obesity.joblib', 'label_encoder_obesity.joblib') não encontrados na pasta raiz do projeto.")
        st.info("Executando em modo de demonstração com base no IMC.")

    except Exception as e:
        st.error(f"Ocorreu um erro inesperado durante a predição: {e}")