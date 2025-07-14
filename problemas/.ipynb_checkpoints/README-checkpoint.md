## Problema 1: Análise de Composição de Nucleotídeos

Tarefa: Escreva um script que:

1) Faça o parse do arquivo multiFASTA, usando a função ler_fasta.
2) Imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo GC (percentual de C + G) para cada sequência.  

Dica: Use sua classe Sequencia e sua função .calcular_percentual(bases)

---------------------------

## Problema 2: Tradução de Sequências de Nucleotídeos para Sequências de Proteínas

Objetivo: Traduzir sequências de nucleotídeos para sequências de proteínas.

Tarefa: Escreva um script em Python para:

1) Fazer o parse do arquivo multiFASTA.
2) Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente.
3) Imprimir as sequências de proteínas.  

Dica: Use sua classe Sequencia e sua função de traduzir

---------------------------

## Problema 3: Identificação de Mutação em Genomas Virais

#### Contexto

Você está colaborando com uma equipe de virologistas que está estudando mutações específicas em genomas de vírus da família Flaviviridae. Eles identificaram uma mutação de interesse que ocorre na posição 1000 das sequências, onde o nucleotídeo 'A' é substituído por 'G'. Seu trabalho é identificar se essa mutação está presente nas sequências fornecidas e gerar um relatório. Esta análise é crucial para entender a evolução dos vírus e suas possíveis implicações na virulência e resistência a tratamentos.

#### Objetivo
Aprender a usar Python para procurar mutações específicas em sequências de DNA e gerar relatórios detalhados.

### Tarefa - Fazer script que:

1. Faça o parse do arquivo multiFASTA contendo os genomas virais.
2. Verifique se a mutação específica (substituição de nucleotídeo) na posição 1000 está presente em cada sequência.
3. Gerar um relatório que indique quais sequências possuem a mutação e quais não possuem.