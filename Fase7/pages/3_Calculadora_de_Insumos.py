import streamlit as st
import math
import pandas as pd

# Inicializa logs em session_state
if "logs" not in st.session_state:
    st.session_state.logs = []

st.title("📦 Cálculo e Gerenciamento de Insumos Agrícolas")

st.write("Insira as informacões de qual cultura e área(m²) que deseja cultivar e receba as informações de quantidade de insumos que serão usadas para cada item!")


# -----------------------------------------------------------
# Função para calcular insumos
# -----------------------------------------------------------
def calcular_insumos(area, cultura):
    # Batata: 5L/1m
    quantidade_insumo_batata_aplicacao = (math.sqrt(area) * 5) / 1000
    quantidade_insumo_batata_total = quantidade_insumo_batata_aplicacao * 5

    # Morango: 2.5L/1m
    quantidade_insumo_morango_aplicacao = (math.sqrt(area) * 2.5) / 1000
    quantidade_insumo_morango_total = quantidade_insumo_morango_aplicacao * 5

    return {
        "area": area,
        "cultura": cultura,
        "quant_insumo_batata": quantidade_insumo_batata_total,
        "quant_aplicacao_batata": quantidade_insumo_batata_aplicacao,
        "quant_insumo_morango": quantidade_insumo_morango_total,
        "quant_aplicacao_morango": quantidade_insumo_morango_aplicacao,
    }


# -----------------------------------------------------------
# Cadastro de novos registros
# -----------------------------------------------------------
st.subheader("➕ Registrar novos dados")

area = st.number_input("Área da plantação (m²)", min_value=1, step=1)
cultura = st.selectbox("Selecione a cultura", ["Batata", "Morango"])
cultura_valor = 1 if cultura == "Batata" else 2

if st.button("Registrar"):
    registro = calcular_insumos(area, cultura_valor)
    st.session_state.logs.append(registro)
    st.success("Registro adicionado com sucesso!")


# -----------------------------------------------------------
# Exibição dos registros
# -----------------------------------------------------------
st.subheader("📋 Registros cadastrados")

if len(st.session_state.logs) == 0:
    st.info("Nenhum registro cadastrado ainda.")
else:
    df = pd.DataFrame(st.session_state.logs)
    df["cultura"] = df["cultura"].map({1: "Batata", 2: "Morango"})
    st.dataframe(df)


# -----------------------------------------------------------
# Atualização de registros
# -----------------------------------------------------------
# -----------------------------------------------------------
# Atualização de registros
# -----------------------------------------------------------
st.subheader("✏ Atualizar um registro")

if len(st.session_state.logs) > 0:
    idx_atualizar = st.number_input(
        "Número do registro para atualizar",
        min_value=0,
        max_value=len(st.session_state.logs) - 1,
        step=1,
    )

    nova_area = st.number_input("Nova área (m²)", min_value=1, step=1)
    nova_cultura = st.selectbox(
        "Nova cultura",
        ["Batata", "Morango"],
        key="atualizar"
    )
    nova_cultura_valor = 1 if nova_cultura == "Batata" else 2

    if st.button("Atualizar registro"):
        novo = calcular_insumos(nova_area, nova_cultura_valor)
        st.session_state.logs[idx_atualizar] = novo
        st.success(f"Registro {idx_atualizar} atualizado com sucesso!")
        st.rerun()   

# -----------------------------------------------------------
# Remover registros
# -----------------------------------------------------------
st.subheader("🗑 Remover um registro")

if len(st.session_state.logs) > 0:
    idx_remover = st.number_input(
        "Número do registro para remover",
        min_value=0,
        max_value=len(st.session_state.logs) - 1,
        step=1,
        key="remover"
    )

    if st.button("Remover registro"):
        st.session_state.logs.pop(idx_remover)
        st.success("Registro removido com sucesso!")
        st.rerun()

