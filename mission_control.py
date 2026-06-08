"""
MISSION CONTROL AI
Sistema de monitoramento inteligente para missão espacial experimental
"""

# ============================================================
# CONFIGURAÇÕES DA MISSÃO
# ============================================================
NOME_MISSAO = "Astral Hunters"
NOME_EQUIPE = "Phantom Crew"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# ============================================================
# FUNÇÕES DE ANÁLISE INDIVIDUAL
# ============================================================

def analisar_temperatura(valor):
    if valor > 35:
        return "CRÍTICO", f"Risco de superaquecimento ({valor}°C)", 2
    elif valor < 18 or (valor > 30 and valor <= 35):
        return "ATENÇÃO", f"Temperatura elevada/baixa ({valor}°C)", 1
    else:
        return "NORMAL", f"Temperatura estável ({valor}°C)", 0

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", f"Comunicação com a base em nível crítico ({valor}%)", 2
    elif valor < 60:
        return "ATENÇÃO", f"Comunicação instável ({valor}%)", 1
    else:
        return "NORMAL", f"Comunicação estável ({valor}%)", 0

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", f"Bateria em nível crítico ({valor}%)", 2
    elif valor < 50:
        return "ATENÇÃO", f"Bateria abaixo do recomendado ({valor}%)", 1
    else:
        return "NORMAL", f"Energia estável ({valor}%)", 0

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", f"Oxigênio em nível crítico ({valor}%)", 2
    elif valor < 90:
        return "ATENÇÃO", f"Oxigênio abaixo do ideal ({valor}%)", 1
    else:
        return "NORMAL", f"Oxigênio adequado ({valor}%)", 0

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", f"Estabilidade operacional crítica ({valor}%)", 2
    elif valor < 70:
        return "ATENÇÃO", f"Estabilidade operacional reduzida ({valor}%)", 1
    else:
        return "NORMAL", f"Estabilidade operacional adequada ({valor}%)", 0

def classificar_ciclo(dados_ciclo):
    resultados = []
    pontuacao_total = 0
    
    funcs = [
        analisar_temperatura,
        analisar_comunicacao,
        analisar_bateria,
        analisar_oxigenio,
        analisar_estabilidade
    ]
    
    for i, func in enumerate(funcs):
        classificacao, mensagem, pontos = func(dados_ciclo[i])
        resultados.append({
            'area': areas_monitoradas[i],
            'valor': dados_ciclo[i],
            'classificacao': classificacao,
            'mensagem': mensagem,
            'pontos': pontos
        })
        pontuacao_total += pontos
    
    if pontuacao_total <= 2:
        classificacao_geral = "MISSÃO ESTÁVEL"
        recomendacao = "Manter operação normal e continuar monitoramento."
    elif pontuacao_total <= 5:
        classificacao_geral = "MISSÃO EM ATENÇÃO"
        recomendacao = "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        classificacao_geral = "MISSÃO CRÍTICA"
        recomendacao = "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
    
    return resultados, pontuacao_total, classificacao_geral, recomendacao

def exibir_ciclo(numero, resultados, pontuacao, classificacao, recomendacao):
    print("=" * 45)
    print(f"CICLO {numero}")
    print("-" * 45)
    
    for res in resultados:
        print(f"{res['area']}: {res['valor']} | {res['classificacao']} | {res['mensagem']}")
    
    print(f"\nPontuação de risco do ciclo: {pontuacao}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}\n")

def analisar_tendencia(pontuacoes):
    primeiro = pontuacoes[0]
    ultimo = pontuacoes[-1]
    
    if ultimo > primeiro:
        return "A missão apresentou tendência de PIORA."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de MELHORA."
    else:
        return "A missão permaneceu ESTÁVEL em relação ao início."

def identificar_area_mais_afetada(pontuacoes_acumuladas):
    max_pontos = max(pontuacoes_acumuladas)
    indices_maiores = [i for i, p in enumerate(pontuacoes_acumuladas) if p == max_pontos]
    
    if len(indices_maiores) == 1:
        return areas_monitoradas[indices_maiores[0]]
    else:
        return ", ".join([areas_monitoradas[i] for i in indices_maiores])

def gerar_relatorio_final(dados_missao, todas_classificacoes, pontuacoes_por_ciclo, pontuacoes_acumuladas):
    num_ciclos = len(dados_missao)
    
    medias = [0, 0, 0, 0, 0]
    for ciclo in dados_missao:
        for i in range(5):
            medias[i] += ciclo[i]
    medias = [m / num_ciclos for m in medias]
    
    maior_pontuacao = max(pontuacoes_por_ciclo)
    ciclo_mais_critico = pontuacoes_por_ciclo.index(maior_pontuacao) + 1
    
    qtd_ciclos_criticos = sum(1 for p in pontuacoes_por_ciclo if p >= 6)
    
    risco_medio = sum(pontuacoes_por_ciclo) / num_ciclos
    
    tendencia = analisar_tendencia(pontuacoes_por_ciclo)
    
    area_mais_afetada = identificar_area_mais_afetada(pontuacoes_acumuladas)
    
    ultima_classificacao = todas_classificacoes[-1]
    
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"\nQuantidade de ciclos analisados: {num_ciclos}")
    
    print(f"\nMédia de temperatura: {medias[0]:.2f} °C")
    print(f"Média de comunicação: {medias[1]:.2f}%")
    print(f"Média de bateria: {medias[2]:.2f}%")
    print(f"Média de oxigênio: {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%")
    
    print(f"\nCiclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_pontuacao}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_ciclos_criticos}")
    
    print(f"\nTendência da missão: {tendencia}")
    
    print("\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontuacoes_acumuladas[i]} pontos")
    
    print(f"\nÁrea mais afetada: {area_mais_afetada}")
    
    print(f"\nClassificação final da missão: {ultima_classificacao}")
    
    print("\nConclusão:")
    if ultima_classificacao == "MISSÃO ESTÁVEL":
        print("A missão transcorreu dentro dos parâmetros normais. Todos os sistemas operam adequadamente.")
    elif ultima_classificacao == "MISSÃO EM ATENÇÃO":
        print("A missão apresentou instabilidade relevante durante a operação. Apesar da tentativa de recuperação, ainda existem sistemas em atenção e a equipe deve manter o plano de contingência ativo.")
    else:
        print("A missão enfrentou problemas críticos em múltiplos sistemas. Recomenda-se revisão completa dos protocolos de segurança e intervenção imediata.")
    
    print("=" * 60 + "\n")

def main():
    print("\n" + "=" * 45)
    print("MISSION CONTROL AI")
    print("=" * 45)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    
    pontuacoes_por_ciclo = []
    todas_classificacoes = []
    pontuacoes_acumuladas = [0, 0, 0, 0, 0]
    
    for i, dados_ciclo in enumerate(dados_missao):
        resultados, pontuacao_total, classificacao_geral, recomendacao = classificar_ciclo(dados_ciclo)
        
        for j, res in enumerate(resultados):
            pontuacoes_acumuladas[j] += res['pontos']
        
        pontuacoes_por_ciclo.append(pontuacao_total)
        todas_classificacoes.append(classificacao_geral)
        
        exibir_ciclo(i + 1, resultados, pontuacao_total, classificacao_geral, recomendacao)
    
    gerar_relatorio_final(dados_missao, todas_classificacoes, pontuacoes_por_ciclo, pontuacoes_acumuladas)

if __name__ == "__main__":
    main()