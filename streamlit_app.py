import numpy as np

def prob_sucesso_cobranca(hora_envio):
    """
    Modelo matemático simples de probabilidade de conversão por hora.
    """
    # Distribuição normal simulando picos às 10h e 14h
    picos = [10, 14]
    prob = max([np.exp(-0.5 * ((hora_envio - p) / 2)**2) for p in picos])
    return round(prob, 4)

# Gerando estatística para o terminal
for h in [8, 10, 12, 14, 18, 21]:
    print(f"Hora: {h}h | Probabilidade Estatística de Sucesso: {prob_sucesso_cobranca(h) * 100}%")
