"""
[Exercício 112]
    Dentro do pacote utilidadesCeV que criamos no DESAFIO 111, temos um módulo chamado dado.
    Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.

OBS do aluno: valores float representados com vírgula devem ser considerados na função leiaDinheiro()
              isso o método replace() resolve
              da mesma forma, a tabela gerada pela função resumo() também poderia utilizar vírgula nos números float
              no entanto,a fim de simplificar e utilizar o padrão (nativo), preferi utilizar o ponto
              já que em todos os demais exercícios utilizei o ponto para exibir números float
"""
from utilidadesCeV import dado, moeda

valor = dado.leiaDinheiro('Digite o valor: R$')
moeda.resumo(valor, 35, 22)