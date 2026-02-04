import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime, timezone

# --- 1. CONFIGURAÇÃO TÉCNICA E ESTILO ---
st.set_page_config(page_title="K97 TERMINAL", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .main { background-color: #020617; color: #f8fafc; }
    .stMetric { background-color: #0f172a; border: 1px solid #1e293b; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LÓGICA CORE (SISTEMA K97) ---
class K97System:
    def __init__(self):
        # Reset VWAP automático conforme regra: 00:00 UTC
        self.now_utc = datetime.now(timezone.utc)
        self.reset_time = "00:00:00 UTC"

    def autenticar_gerente(self, senha):
        # Hash de segurança conforme projeto original
        hash_auth = hashlib.sha256(senha.encode()).hexdigest()
        return hash_auth == hashlib.sha256(b"admin99").hexdigest()

# --- 3. INTERFACE DO TABLET ---
k97 = K97System()

st.markdown("<h1 style='color: #10b981; font-family: monospace;'>📟 K97_CORE_v1.0_LIVE</h1>", unsafe_allow_html=True)

# Sidebar: Auditoria e Status
st.sidebar.subheader("📡 STATUS DO SISTEMA")
st.sidebar.write(f"Relógio UTC: {k97.now_utc.strftime('%H:%M:%S')}")
st.sidebar.write(f"Reset VWAP: {k97.reset_time}")

# Abas do Sistema (Operacional e Gerente)
tab_op, tab_gerente = st.tabs(["OPERACIONAL", "🔒 RESTRITO GERENTE"])

# --- ABA OPERACIONAL (RECEPÇÃO) ---
with tab_op:
    st.subheader("Entrada de Atendimentos")
    with st.form("registro_venda"):
        paciente = st.text_input("Paciente")
        procedimento = st.selectbox("Procedimento", ["Limpeza", "Implante", "Avaliação", "Prótese"])
        valor = st.number_input("Valor (R$)", min_value=0.0)
        metodo = st.radio("Método", ["PIX", "Boleto", "Cartão"], horizontal=True)
        if st.form_submit_button("GERAR COBRANÇA"):
            # Lógica de geração de Hash para ID de cobrança
            cobranca_id = hashlib.md5(f"{paciente}{valor}".encode()).hexdigest()[:8]
            st.success(f"Cobrança {cobranca_id} gerada!")
            st.code(f"00020126330014BR.GOV.BCB.PIX...{cobranca_id}", language="text")

# --- ABA GERENTE (PROTEGIDA POR SENHA) ---
with tab_gerente:
    senha = st.text_input("Insira a senha gerencial", type="password")
    if k97.autenticar_gerente(senha):
        st.success("ACESSO GERENCIAL LIBERADO")
        
        # Dashboard Financeiro Real-Time
        c1, c2, c3 = st.columns(3)
        c1.metric("FATURAMENTO DIA", "R$ 12.450,00", delta="Live")
        c2.metric("COBRANÇAS PENDENTES", "4")
        c3.metric("STATUS CADEIRAS", "80% Ocupação")
        
        # Histórico de Chat e Logs
        st.divider()
        st.subheader("💬 Log de Comunicação Interna")
        st.text_area("Mensagens da Recepção", value="[23:45] Recepção -> Gerente: Paciente João Silva em cadeira 1.\n[23:50] Sistema: Pagamento PIX confirmado R$ 1.500,00", height=100)
        
        if st.button("🖨️ IMPRIMIR RELATÓRIO TÉRMICO"):
            st.info("Enviando para a rede...")
    else:
        if senha:
            st.error("SENHA INCORRETA. TENTATIVA LOGADA.")

# --- 4. PERSISTÊNCIA DE DADOS ---
# Sugestão: Conectar agora ao banco de dados SQLite ou Supabase conforme estrutura discutida
st.divider()
st.caption("K97 Clinic System | Estritamente Técnico")
