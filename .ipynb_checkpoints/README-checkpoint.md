# Projeto - Escrevendo nossa própria "BioPython"

Para treinar o que aprendemos durante o curso, vamos criar algumas classes e funções inpirados na biblioteca BioPython. 
E podemos usá-la para resolver alguns problemas de Bioinformática.

Vai ser algo simplificado, apenas com o intuito de treinarmos algumas coisas que aprendemos em sala de aula.

--------------------------

## Para ser criado

### Função ler_fasta

Esta função se inpira na SeqIo.parse. 
Ela lerá um arquivo "fasta" e o transformará em uma lista de objetos OrganismoFasta, 
para ser mais facilmente manipulado no código.

### Classe OrganismoFasta

Esta classe se inspira na SeqRecord deverá ler ter como um atributo um id, um nome e uma sequência como atributos. 

Você receberá tanto o id, quanto o nome, quanto a sequencia como string. 

Porém, salvará a sequencia como um objeto da classe Sequencia, que será o coração do nosso projeto.

### Classe Sequencia

Esta classe vai ser a principal do projeto e vai conter as funcionalida de sequencia.

Ela deve ter pelo menos um atributo que é a própria Sequencia.

Essa classe deve ter os seguintes métodos:

- .complementar() - Inspirado no método Seq().complement()
  - Retorna outro objeto sequencia, com a sequencia complementar.

  
- .complementar_reversa() - Inspirado no método Seq.reverse_complement()
  - Retorna outro objeto sequencia, com a sequencia complementar reversa.


- .transcrever - Inspirado no método Seq.transcribe()
  - Retorna outro objeto sequencia, com a sequencia resultado da transcricao daquela sequencia.


- .traduzir(parar=False) - Inspirado no método Seq().translate()
  - Retorna uma string com a tradução da sequencia para uma proteína.
  - Exemplo: "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG" -> "MAIVMGR*KGAR*"
  - Essa função receberá um argumento parar. Se ele for true, sua tradução deve parar no stop codon. Se ela for False, deve continuar e marcar os stop códons como * e varrer até o final.
  - Para fazer essa função, está disponibilizado um dicionário no arquivo constantes.py DNA_PARA_AMINOACIDO que você pode importar.
  - Caso a trinca de codon não esteja nesse dicionário, é porque a sequencia tem uma base indefinida. Nessa caso, marque a proteína como X, indicando que não tem como sabe-la.

- .calcular_percentual(bases)
  - Esse método foi inventado. Ele vai receber uma lista de bases e calcular o percentual daquelas bases na composição da Sequencia.
  - Ex: Sequencia("ATCGAAA").calcular_percentual(bases=["A"]) = 0.5 (pois há 4 As num total de 8 bases)
  - Ex: Sequencia("ATCGCC").calcular_percentual(bases=["C", "G"]) = 0.66 (pois há 4 Cs e Gs num total de 8 bases)

----------------------

### Usando

Para testar, vamos tentar resolver alguns problemas usando essas suas classes!

Esses problemas estão descritos na pasta problema.

-----------------------

## Avaliação

Diferente das nossas tarefas de casa, não terá avaliação automática. Eu vou ler e avaliar e dar uma nota com cuidado.

Então mesmo se não funcionar 100%, eu vou conseguir dar nota de acordo com a solução.
