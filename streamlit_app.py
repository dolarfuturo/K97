import streamlit as st
import pandas as pd
from datetime import datetime, timezone
import hashlib

# --- CONFIGURAÇÃO DE UI E ENGINE ---
st.set_page_config(page_title="K97 TERMINAL", layout="wide", initial_sidebar_state="expanded")

# CSS para Menu e Cards de Dados
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #050a15; border-right: 1px solid #10b981; }
    .stMetric { background-color: #0f172a; border: 1px solid #1e293b; padding: 20px; border-radius: 12px; }
    .main { background-color: #020617; }
    </style>
    """, unsafe_allow_html=True)

# --- NÚCLEO TÉCNICO (RESET VWAP 00:00 UTC) ---
now_utc = datetime.now(timezone.utc)
if 'vendas' not in st.session_state:
    st.session_state.vendas = []

# --- MENU LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
    st.title("K97 CORE")
    st.divider()
    menu = st.radio("MENU DE COMANDO", ["📊 Dashboard", "💸 Operacional", "🔒 Auditoria", "💬 Chat Interno"])
    st.divider()
    st.info(f"SINC: {now_utc.strftime('%H:%M:%S')} UTC")
    st.caption("Reset Binance: 00:00:00")

# --- LÓGICA DAS PÁGINAS ---

# 1. DASHBOARD (VISÃO GERAL)
if menu == "📊 Dashboard":
    st.markdown("<h1 style='color: #10b981;'>ESTATÍSTICAS REAL-TIME</h1>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    faturamento = sum([v['valor'] for v in st.session_state.vendas])
    
    c1.metric("FATURAMENTO (VWAP)", f"R$ {faturamento:,.2f}")
    c2.metric("TICKET MÉDIO", f"R$ {faturamento/len(st.session_state.vendas) if st.session_state.vendas else 0:,.2f}")
    c3.metric("CONEXÃO", "STABLE", delta="LATÊNCIA 14ms")

    st.subheader("Fluxo de Atendimento")
    chart_data = pd.DataFrame({"Hora": range(24), "Volume": [2, 5, 1, 0, 0, 0, 0, 4, 8, 12, 10, 15, 18, 14, 2
