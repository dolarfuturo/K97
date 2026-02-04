import streamlit as st
import pandas as pd
from datetime import datetime, timezone
import time

# --- CONFIGURAÇÃO INTERFACE K97 ---
st.set_page_config(page_title="K97 TERMINAL", layout="wide", initial_sidebar_state="collapsed")

# Estilo CSS para visual "Dark Terminal"
st.markdown("""
    <style>
    .main { background-color: #020617; color: #f8fafc; }
    .stMetric { background-color: #0f172a; border: 1px solid #1e293b; padding: 15px; border_radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TEMPO (REGRAS DO USUÁRIO) ---
# Reset VWAP configurado para 00:00 UTC (Abertura Binance)
now_utc = datetime.now(timezone.utc)
st.sidebar.subheader("📡 STATUS DO SISTEMA")
st.sidebar.write(f"Relógio UTC: {now_utc.strftime('%H:%M:%S')}")
st.sidebar.write(f"Reset em: 00:00:00 UTC")

# --- INTERFACE DO TERMINAL ---
st.markdown("<h1 style='color: #10b981; font-family: monospace;'>📟 K97_CORE_v1.0</h1>", unsafe_allow_html=True)

# Simulador de Dados (Substituiremos por Banco de Dados no próximo passo)
# Aqui é onde o faturamento "ganha vida"
faturamento_simulado = 12450.75 

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("FATURAMENTO (VWAP)", f"R$ {faturamento_simulado:,.2f}", delta="LIVE")

with col2:
    st.metric("CADEIRAS ATIVAS", "4 / 5", delta="-1")

with col3:
    st.metric("TICKET MÉDIO", "R$ 840,00")

st.markdown("---")

# --- ÁREA DE COMANDOS DO GERENTE ---
st.subheader("🛠️ COMANDOS DE OPERAÇÃO")

c1, c2, c3 = st.columns(3)

if c1.button("⚡ GERAR PIX DINÂMICO"):
    st.warning("Gerando Payload BRCode...")
    # Lógica de cripto/pix futura entra aqui
    st.code("00020126330014BR.GOV.BCB.PIX0111CLINICAK97...6304", language="text")

if c2.button("📑 AUDITORIA DO DIA"):
    st.info("Compilando logs de transação da recepção...")

if c3.button("🔄 FORCE RESET VWAP"):
    st.error("Resetando métricas para 0.00 (Manual)")

# --- TABELA DE FLUXO DE CAIXA ---
st.markdown("### 📊 ÚLTIMAS ENTRADAS")
# Simulação de dados para visualização no tablet
df_vendas = pd.DataFrame({
    "HORA (UTC)": ["23:45", "23:10", "22:50", "22:15"],
    "PROCEDIMENTO": ["Implante", "Limpeza", "Avaliação", "Prótese"],
    "VALOR": [4500.00, 250.00, 0.00, 1800.00],
    "STATUS": ["PAGO", "PAGO", "PENDENTE", "PAGO"]
})
st.table(df_vendas)

# Rodapé Técnico
st.markdown("---")
st.caption("K97 Terminal - Conexão Criptografada via Streamlit Cloud")
