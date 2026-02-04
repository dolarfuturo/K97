import datetime
import hashlib

class K97Terminal:
    def __init__(self):
        self.user_level = 0  # 0: Operacional, 99: Gerente
        self.logs = []
        self.chat_history = []
        self.financeiro = {"vendas_dia": 0.0, "cobranças_pendentes": []}
        self.pacientes_ativos = {}
        
    def reset_vwap_time(self):
        """Reset automático baseado no horário de abertura Binance (00:00 UTC)"""
        now = datetime.datetime.utcnow()
        return now.replace(hour=0, minute=0, second=0, microsecond=0)

    def autenticar(self, senha):
        # Hash simples para exemplo técnico
        if hashlib.sha256(senha.encode()).hexdigest() == hashlib.sha256(b"admin99").hexdigest():
            self.user_level = 99
            print("[K97] ACESSO GERENCIAL LIBERADO. ABAS RESTRITAS ATIVAS.")
        else:
            self.user_level = 0
            print("[K97] ACESSO OPERACIONAL PADRÃO.")

    def gerar_cobranca(self, paciente, valor, tipo="PIX"):
        """Gera link de cobrança e QR Code fictício"""
        status = "PENDENTE"
        cobranca_id = hashlib.md5(f"{paciente}{valor}".encode()).hexdigest()[:8]
        payload = {"id": cobranca_id, "paciente": paciente, "valor": valor, "tipo": tipo, "status": status}
        self.financeiro["cobranças_pendentes"].append(payload)
        
        print(f"\n[K97-PAY] COBRANÇA GERADA - ID: {cobranca_id}")
        print(f"Link: https://k97.pay/checkout/{cobranca_id}")
        print(f"QRCODE {tipo}: [IMAGE_DATA_SIMULATED]")
        return cobranca_id

    def aba_gerente(self):
        """Aba restrita com histórico e monitoramento real-time"""
        if self.user_level < 99:
            print("[ERRO] ACESSO NEGADO. PRIVILÉGIOS INSUFICIENTES.")
            return

        print("\n" + "="*50)
        print(f"K97 - DASHBOARD GERENCIAL | {datetime.datetime.now()}")
        print("="*50)
        print(f"FATURAMENTO REAL-TIME: R$ {self.financeiro['vendas_dia']:.2f}")
        print(f"COBRANÇAS ATIVAS: {len(self.financeiro['cobranças_pendentes'])}")
        print("\n--- ÚLTIMAS MENSAGENS DO CHAT ---")
        for msg in self.chat_history[-5:]:
            print(msg)
        print("="*50)

    def enviar_mensagem(self, destinatario, texto):
        remetente = "GERENTE" if self.user_level == 99 else "FUNCIONÁRIO"
        timestamp = datetime.datetime.now().strftime("%H:%M")
        entry = f"[{timestamp}] {remetente} -> {destinatario}: {texto}"
        self.chat_history.append(entry)
        print("[K97-CHAT] Mensagem enviada e logada.")

    def imprimir_documento(self, doc_id):
        print(f"\n[K97-PRINT] ENVIANDO PARA IMPRESSORA TÉRMICA...")
        print(f"Documento ID: {doc_id} | Status: OK")

# --- EXECUÇÃO DO SISTEMA K97 ---

terminal = K97Terminal()

# 1. Fluxo Operacional (Funcionário)
terminal.enviar_mensagem("GERENTE", "Paciente João Silva chegou para implante.")
terminal.gerar_cobranca("João Silva", 1500.00, "PIX")

# 2. Fluxo Gerencial (Acesso Restrito)
terminal.autenticar("admin99") # Simulação de login
terminal.financeiro["vendas_dia"] = 1500.00 # Atualização Real-time
terminal.aba_gerente()

# 3. Comando de Impressão
terminal.imprimir_documento("TX-9982")
