# Máquina Diferencial

## Introdução
A Máquina Diferencial foi idealizada por **Charles Babbage** no século XIX como um dispositivo mecânico capaz de calcular automaticamente tabelas de funções polinomiais.  
Seu funcionamento se baseia no **método das diferenças finitas**, que permite calcular novos valores de uma função utilizando apenas **operações de soma**.

## Funcionamento
- Constrói-se uma **tabela de diferenças**, onde:
  - A primeira linha contém os valores conhecidos de uma função \(y\).
  - As linhas seguintes contêm as diferenças sucessivas entre os valores anteriores.
- Para polinômios de grau \(n\), a \(n\)-ésima diferença é **constante**.
- A máquina utiliza essa propriedade para **extrapolar valores futuros** sem necessidade de multiplicações ou potências.

## Ideia Principal
1. Define-se um conjunto de pontos \(x\) igualmente espaçados e calcula-se os valores \(y = f(x)\).  
2. Constrói-se a tabela de diferenças sucessivas até que uma linha constante apareça.  
3. Para calcular novos valores, a máquina soma os termos das diferenças **de baixo para cima**, propagando até a primeira linha.  
4. O valor resultante corresponde ao próximo \(y\) da função.

## Códigos
- O arquivo **`babage`** contém o código mais completo, que cobre a **nota 100** do trabalho.  
- O arquivo **`babage80`** é uma versão anterior do programa, que cobre apenas a **nota 80**.
