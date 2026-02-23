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
        'family_history_with_overweight': [map_yes_no[family_history]], 'FAVC': [map_yes_no[favc]], 'FCVC': [fcvc],
        'NCP': [ncp], 'CAEC': [map_caec_calc[caec]], 'SMOKE': [map_yes_no[smoke]], 'CH2O': [ch2o], 'SCC': [map_yes_no[scc]],
        'FAF': [faf], 'TUE': [tue], 'CALC': [map_caec_calc[calc]], 'MTRANS': [map_mtrans[mtrans]]
    }
    df_input = pd.DataFrame(data)
    
    st.divider()
    st.markdown("### Resultado da Análise")
    
    # Fallback: Cálculo de IMC simples para demonstração
    imc = weight / (height ** 2)
    st.info("Modo de Demonstração (Modelo não carregado)")
    st.metric("IMC Calculado", f"{imc:.2f}")

    print(smoke)
    
    if imc < 18.5: st.warning("Classificação IMC: Abaixo do peso")
    elif imc < 25: st.success("Classificação IMC: Peso normal")
    elif imc < 30: st.warning("Classificação IMC: Sobrepeso")
    else: st.error("Classificação IMC: Obesidade")