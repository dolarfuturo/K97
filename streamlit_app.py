import streamlit as st
import pandas as pd
from datetime import datetime, timezone

# Configuração Técnica do Terminal
st.set_page_config(page_title="K97 TERMINAL", layout="wide")

# Reset Automático VWAP (Abertura Binance 00:00 UTC)
now_utc = datetime.now(timezone.utc)
st.sidebar.info(f"Sincronização: {now_utc.strftime('%H:%M:%S')} UTC")

st.markdown("<h1 style='color: #10b981;'>📟 K97 GERENCIAL</h1>", unsafe_allow_html=True)

# Painel de Auditoria
c1, c2 = st.columns(2)
c1.metric("Faturamento Dia", "R$ 0,00", help="Zera automaticamente às 00:00 UTC")
c2.metric("Status do Sistema", "ONLINE")

st.divider()

# Comandos de Operação
st.subheader("Ações Rápidas")
col_a, col_b = st.columns(2)
if col_a.button("⚡ GERAR PIX"):
    st.code("00020126330014BR.GOV.BCB.PIX...", language="text")
if col_b.button("🖨️ RECIBO TÉRMICO"):
    st.success("Comando enviado para a recepção.")

# Log de Dados
st.subheader("Últimas Movimentações")
st.dataframe(pd.DataFrame(columns=["Hora", "Paciente", "Valor", "Status"]), use_container_width=True)
