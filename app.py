# Calculadora de Consumo de Energia Elétrica

print("=== Calculadora de Consumo de Energia ===")

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts - W): "))
horas_dia = float(input("Digite o tempo de uso diário (em horas): "))

# Cálculo do consumo mensal (kWh)
consumo_mensal = (potencia * horas_dia * 30) / 1000

# (Opcional) cálculo de custo
tarifa = 0.75  # valor do kWh em reais
custo = consumo_mensal * tarifa

# Saída formatada
print("\n=== Resultado ===")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}/mês")

# Calculadora de Consumo de Energia Elétrica
