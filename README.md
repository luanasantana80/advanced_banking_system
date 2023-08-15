
# Sistema Simples de Contas Correntes em Python

Este é um sistema simples de contas correntes implementado em Python. Ele permite aos usuários se cadastrarem, fazerem login, criar e acessar contas correntes, realizar operações como depósito e saque, e visualizar extratos.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

- **Cadastro de Usuário:** Os usuários podem se cadastrar fornecendo informações como nome, senha, endereço, CPF, entre outros. O CPF é verificado para garantir que não seja repetido.

- **Login:** Os usuários cadastrados podem fazer login no sistema fornecendo nome e senha.

- **Criação de Conta Corrente:** Os usuários logados podem criar contas correntes, que são numeradas automaticamente a partir do número 0001.

- **Acesso a Conta Corrente:** Os usuários podem acessar suas contas correntes informando o número da conta.

- **Depósito:** Os usuários podem fazer depósitos em suas contas correntes, aumentando o saldo e registrando o valor depositado.

- **Saque:** Os usuários podem fazer saques de suas contas correntes, desde que o saldo seja suficiente. O número de saques é limitado a 3.

- **Extrato:** Os usuários podem visualizar o saldo atual, o valor total depositado, o valor total sacado e a quantidade de saques restantes em suas contas correntes.

- **Listagem de Contas Correntes:** Os usuários podem ver uma lista de todas as suas contas correntes associadas ao seu CPF.

## Utilização

1. Execute o programa no terminal.
2. Siga as instruções exibidas no menu inicial para se cadastrar, fazer login ou sair do sistema.
3. Ao fazer login, siga as opções disponíveis para criar contas correntes, acessar contas existentes e realizar operações nelas.

## Observações

- Este é um exemplo simples e não possui validações avançadas ou recursos de segurança. Para um sistema real, considere implementar tratamentos de erro mais abrangentes e proteções de segurança.

- Este sistema foi criado como uma demonstração didática e não deve ser usado em produção sem melhorias substanciais.

---

Lembre-se de que você pode personalizar este README de acordo com suas necessidades e adicionar mais detalhes sobre como usar o código e suas funcionalidades.
