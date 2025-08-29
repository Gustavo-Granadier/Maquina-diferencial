def babbage(eixo_y, tam):
    n = len(eixo_y)
    tabela = [eixo_y]
    for i in range(tam):
        linha = []
        for j in range(n - i - 1):
            d = tabela[i][j+1] - tabela[i][j]
            linha.append(d)
        tabela.append(linha)
    return tabela


def polinomio(x, coeficientes):
    soma = 0
    grau = len(coeficientes) - 1
    for i in range(grau + 1):
        soma += coeficientes[i] * (x ** (grau - i))
    return soma


def maquina_diferencial(tabela_diferencas):
    grau = len(tabela_diferencas) - 1
    tabela_extrapolada = [list(row) for row in tabela_diferencas]
    for i in range(grau - 1, -1, -1):
        proximo_valor_linha_abaixo = tabela_extrapolada[i+1][-1]
        ultimo_valor_linha_atual = tabela_extrapolada[i][-1]
        novo_valor_linha_atual = ultimo_valor_linha_atual + proximo_valor_linha_abaixo
        tabela_extrapolada[i].append(novo_valor_linha_atual)
    return tabela_extrapolada[0][-1]


coeficientes = [9, -3, 2, 9, 2, 4]
eixo_x = list(range(10))
eixo_y = [polinomio(x, coeficientes) for x in eixo_x]

diffs = babbage(eixo_y, len(coeficientes) - 1)

print("Valores de x:", eixo_x)
print("Valores de y:", eixo_y)
print("\nTabela de Diferenças:")
for i, diff in enumerate(diffs):
    print(f"Diferença {i}: {diff}")

proximo_x = eixo_x[-1] + (eixo_x[1] - eixo_x[0])
proximo_y_extrapolado = maquina_diferencial(diffs)

print(f"\nPróximo x esperado: {proximo_x}")
print(f"Próximo y extrapolado: {proximo_y_extrapolado}")

proximo_y_real = polinomio(proximo_x, coeficientes)
print(f"Próximo y real (verificação): {proximo_y_real}")
