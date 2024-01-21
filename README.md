# Projeto 1: Fundamentos da Programação - IST

## Descrição

Neste projeto de Fundamentos da Programação, parte integrante do curso de Engenharia Informática no Instituto Superior Técnico (IST) de Lisboa, os alunos desenvolverão funções para obter informações sobre o estado de um território retangular composto por caminhos verticais e horizontais. Estes caminhos podem conter interseções ocupadas por montanhas, formando cadeias de montanhas e vales.

### Descrição de um Território

Um território é uma estrutura retangular formada por caminhos verticais e horizontais. Os caminhos verticais são identificados por letras maiúsculas de A a Z, e os caminhos horizontais são identificados por números inteiros de 1 a 99. Cada interseção é identificada pelos identificadores dos caminhos que a formam.

### Conexões, Cadeias de Montanhas e Vales

Duas interseções ocupadas (ou livres) estão conectadas se for possível traçar um percurso entre elas passando por interseções adjacentes. Cadeias de montanhas são conjuntos de interseções ocupadas conectadas entre si, enquanto vales são conjuntos de interseções livres adjacentes a uma montanha.

## Trabalho a Realizar

O objetivo é escrever um programa em Python que forneça informações sobre o estado do território, conforme descrito. O projeto inclui a definição de várias funções relacionadas à manipulação do território.

### Representação do Território e das Interseções

O território é representado internamente como um tuplo de tuplos, e as interseções são representadas como tuplos de dois elementos. Funções auxiliares devem ser implementadas para validar interseções, verificar a validade do território, obter a última interseção e muito mais.

## Funções Principais
- `eh_territorio`: Verifica se a entrada é um território válido.
- `obtem_ultima_intersecao`: Obtém a última interseção do território.
- `eh_intersecao`: Verifica se a entrada é uma interseção válida.
- ...

## Funções de Cadeias de Montanhas e Vales
- `obtem_cadeia`: Obtém a cadeia conectada à interseção fornecida.
- `obtem_vale`: Obtém o vale conectado à montanha da interseção fornecida.
- ...

## Funções de Informação do Território
- `verifica_conexao`: Verifica se duas interseções estão conectadas.
- `calcula_numero_montanhas`: Calcula o número de interseções ocupadas por montanhas.
- `calcula_numero_cadeias_montanhas`: Calcula o número de cadeias de montanhas.
- `calcula_tamanho_vales`: Calcula o tamanho total dos vales.
- ...

## Testes Privados (FP2324P1)

Para executar os testes privados usando o módulo pytest do Python, utilize o seguinte comando em um terminal:

```bash
pytest -vv test_private.py
