from typing import List


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


def maquina_diferencial(tabela_diferencas, eixo_x=None, x_alvo=None):
    tabela_extrapolada = [list(row) for row in tabela_diferencas]
    grau = len(tabela_extrapolada) - 1

    h = eixo_x[1] - eixo_x[0]
    passos = int(round((x_alvo - eixo_x[-1]) / h))

    for _ in range(passos):
        for i in range(grau - 1, -1, -1):
            valor_linha_abaixo = tabela_extrapolada[i+1][-1]
            valor_linha_atual = tabela_extrapolada[i][-1]
            novo_valor_linha_atual = valor_linha_atual + valor_linha_abaixo
            tabela_extrapolada[i].append(novo_valor_linha_atual)
    return tabela_extrapolada


coeficientes = [4, 3, 2, 9, 2]
eixo_x = list(range(9))
eixo_y = [polinomio(x, coeficientes) for x in eixo_x]

diffs = babbage(eixo_y, len(coeficientes) - 1)

print("Valores de x:", eixo_x)
print("Valores de y:", eixo_y)
print("\nTabela de Diferencas (original):")
for i, linha in enumerate(diffs):
    print(f"Diferenca {i}: {linha}")


x_alvo = 9
tabela_nova = maquina_diferencial(diffs, eixo_x, x_alvo)
print(f"\nTabela de Diferencas (atualizada ate x= {x_alvo}):")

for i, linha in enumerate(tabela_nova):
    print(f"Diferenca {i}: {linha}")

y_alvo = tabela_nova[0][-1]
print(f"\nValor em x= {x_alvo} pela maquina diferencial: {y_alvo}")
print(f"Valor em x= {x_alvo} prova real: {polinomio(x_alvo, coeficientes)}")
