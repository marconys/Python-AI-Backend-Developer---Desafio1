# DESAFIO
Fomos contratado por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeiro versão do sistema devemos implementar apenas 3 operações: depósisto, saque e extrato.

# OPERAÇÃO DE DEPÓSITO
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o números da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# OPERAÇÃO DE SAQUE
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saque devem ser armazenados em uma variável de exibidos na operação de extrato.

# OPERAÇÃO DE EXTRATO
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

## Precisamos deixar o nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visializar extrato. Além disso para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

# Função saque
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

# Função depósito
A função de depósito deve receber os argumentos apenas por posição (positional only). sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

# Função extrato
A função extrato deve receber os argumentos por posição (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

## precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções: exemplo: listar contas.

# Função cirar usuário (cliente)
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. o endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

# Função criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é conposta por: agência, número da conta e usuário. o número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.