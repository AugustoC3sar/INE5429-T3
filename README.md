# Trabalho Individual sobre Números Primos

## Descrição

A atividade consiste, basicamente, na implementação de dois algoritmos geradores de números pseudo-aleatórios e dois algoritmos de teste de primalidade, e realizar experimentos com estes algoritmos, gerando número de tamanhos variados de bits e analisando o tempo decorrido para tal.

## Estrutura do repositório

- Na pasta **src** estão os códigos dos respectivos algoritmos, implementados na linguagem Python.
- Na pasta **tests** estão as implementações de experimentos utilizadas.
- Para executar todos os testes, basta executar o arquivo **main.py**
- As tabelas resultantes serão exportadas na pasta **output** que será criada no início da execução

## Geração de números pseudo-aleatórios

Para esta etapa, foram escolhidos os algoritmos **Multiply-With-Carry Generator** (MWC) e **Additive Lagged Fibonacci Generator** (ALF).

### Implementação

Para cada gerador, implementou-se uma classe, com um método **next**, responsável por gerar os números pseudo-aleatórios. Seguiu-se a descrição dos algoritmos de acordo com a bibliografia listada no relatório.

O MWC obrigatoriamente deve receber uma seed de entrada, enquanto a configuração dos outros parâmetros (**carry**, **a** e **bits**) são opcionais. Caso não sejam configurados, os valores padrão são
- carry = 0
- a = 4294957665
- bits = 64 (m = 2^bits)

Da mesma forma, o ALFG também deve receber uma lista de seeds iniciais obrigatórias. A lista deve ter tamanho >= j. A configuração dos demais parâmetros também é opcional, mas caso não sejam configurados, eles assumem os seguintes valores:
- j = 55
- k = 24
- bits = 64 (m = 2^bits)

### Experimentos

Para cada gerador, implementou-se uma classe de teste, responsável por definir os experimentos realizados. O experimento principal, neste caso, consiste na geração de **k** números de **n** bits, com **n** e **k** fornecidos através de uma lista, e observação do tempo necessário para finalizar a execução de cada iteração. Utilizou-se seeds fixas para ambos os algoritmos, com o intuito, realmente, de observar a qualidade de um gerados com base nas seed fornecidas.
- K = [1, 50, 100, 500, 1000, 5000]
- N = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

As tabelas exportadas são construídas com base no índice **n** e na coluna **k**. cada célula possui o tempo médio, em milissegundos, necessário para a finalização do loop de execução.

## Teste de primalidade

Para esta etapa, além do algortimo obrigatório de **Miller-Rabin**, foi escolhido o algortimo **Teste de Fermat** para a implementação.

### Implementação
Para cada teste de primalidade, implementou-se uma classe, com um método **is_prime**, responsável pela verificação da primalidade de um dado número **n**. Novamente, seguiu-se a descrição dos algortimos de acordo com a bibliografia listada no relatório.

O Algoritmo de Miller-Rabin recebe como entrada um número **n**, aplica o algortimo e retorna o se o número é provavelmente primo (True) ou composto (False). Ainda foi implementado um método que permite a **k** realizações do teste.

O Algoritmo do teste de Fermat segue o mesmo padrão, recebendo como entrada um número **n**, mas, nesse caso, também recebendo como entrada um número **k** de vezes que o teste deve ser realizado.

### Experimentos
Para cada teste de primalidade, considerando:
- N = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

1. Para cada **n** em N
    1.1 Configura-se um valor de seed, de **n bits**, utilizando o random do python, com seed fixa
    1.2 Cria-se um gerador de números Pseudo-Aleatórios MWC, com a seed gerada
    1.3 Marca-se o tempo inicial, em milissegundos
    1.4 Enquanto verdadeiro
        1.4.1 Gera-se um novo número **num** até que ele seja impar e tenha exatos **n** bits significativos
        1.4.2 Se **num** passar no teste 5 vezes
            1.4.2.1 Finaliza o loop
    1.5 Calcula-se o tempo de execução, em milissegundos
    1.5 Adiciona-se na tabela de resultados os valores de número gerado e tempo decorrido para a sua geração

