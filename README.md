# Otimizando um Sistema Bancário com Funções Python

## Objetivo do desafio

Este projeto tem por objetivo implementar o desafio de projeto "Otimizando um Sistema Bancário com Funções Python" no âmbito do Bootcamp "Luizalabas - Back-End com Python" realizado pela DIO.

## O Desafio

O desafio consiste em otimizar e extender o código inicial disponibilizado no arquivo desafio.py. O código inicial implementa as funcionalidades para depositar, sacar e emitir extrato. Solicita-se otimizar o código inicial empregando funções e extendê-lo implementando novas funcionalidades para cadastrar e listar usuários e contas bancárias.

## Features
[d]  Depositar
[s]  Sacar
[e]  Extrato
[u]  Cadastrar Cliente/Usuário
[lu] Listar Clientes/Usuários
[c]  Cadastrar Conta Bancária
[lc] Listar Contas Bancárias
[q]  Sair

## Como?
a) Criar funções para implementar as operações existentes de saque, depósito e extrato. Cada operação com sua própria função.

b) Implementar duas novas operações usando funções Python para cadastrar novo cliente/usuário e cadastrar nova conta bancária.

c) Cada função deverá estabelecer suas regras de passagem de parâmetros (/,*/*args,*kwargs) assim como o retorno.

d) A função saque deverá receber os argumentos apenas por nome (*,arg1,arg2,argn). A sugestão de argumentos inclui saldo, valor, extrato, limite, número de saques e limite de saques. A sugestão de retorno inclui saldo e extrato.

e) A função depósito deverá receber os argumentos apenas por posição (arg1, arg2, argn,/). A susgestão de argumentos inclui saldo, valor e extrato, enquanto a sugestão de retorno inclui saldo e extrato.

f) A função extrato deverá receber o argumento saldo por posição e extrato nomeado.

g) Criar, no mínimo, duas novas funcionalidades: criar cliente/usuário e criar conta bancária. Ficar a vontade para criar outras funcionalidades a exemplo de listar as contas bancárias já cadastradas.

h) Os novos clientes/usuários deverão ser armazenados em uma lista contendo nome, data de nascimento, cpf e endereço. O Endereço deve ser armazenado no formato "<logradouro, número, complemento> - <bairro> - <cidade/UF>". Deverá armazenar apenas os números do CPF, sem caracteres de formatação. Não poderão ser cadastrados mais de um usuário para o mesmo cpf. Os dados de cada usuário devem ser armazenados no formato chave-valor, o que implica utilizar a estrutura dicionário para cada usuário e a lista terá como ocorrências os dicionários correspondentes a cada usuário. usuarios =[{...}, {...},{...}, ...].

i) As contas bancárias deverão ser armazenadas em uma lista e deverão conter agência, conta e cliente/usuário, no formato chave-valor, assim como para usuários. O número da conta será sequencial iniciando em 000001. O número da agência será fixado em 0001. Um usuário/cliente poderá ter mais de uma conta. Uma conta deverá pertencer obrigatóriamente a um e somente um cliente/usuário válido, isto é, existente na lista de clientes/usuários cadastrados.

## Tecnologias empregadas
- Python: tipos de dados, variáveis, estruturas de dados (listas, dicionários, tuplas). Funções built-in input e print. Comandos de decisão e repetição (if, for, break), interpolação, funções(declaração, passagem de parâmetros e retorno).
- VSCode como IDE para edição e testes.

  ## Author
  Sérgio Santa Catarina.

