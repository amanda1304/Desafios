class BancoSeguro:
    def __init__(self):
        self.__senha = '1234'
        self.__dinheiro = 2000.0
    def _verificar_senha(self, senha):
        return senha == self.__senha
    def abrir(self):
        senha_digitada = input("Digite a senha: ")
        if self._verificar_senha(senha_digitada):
            print("Canta aberto!")
            self.menu()
        else:
            print(" Senha incorreta! Canta bloqueado.")
    def menu(self):
        while True:
            print("""
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair
            """)
            opcao = input("=> ").lower()

            if opcao == 'd':
                valor = float(input("Insira o valor do depósito: "))
                if valor > 0:
                    self.__dinheiro += valor
                    print(f" Depósito de R$ {valor:.2f} realizado.")
                else:
                    print(" Valor inválido.")

            elif opcao == 's':
                valor = float(input("Insira o valor do saque: "))
                if 0 < valor <= self.__dinheiro:
                    self.__dinheiro -= valor
                    print(f" Saque de R$ {valor:.2f} realizado.")
                else:
                    print("Valor inválido ou saldo insuficiente.")

            elif opcao == 'e':
                print(f" Extrato: R$ {self.__dinheiro:.2f}")

            elif opcao == 'q':
                print(" Saindo do Conta...")
                break

            else:
                print(" Opção inválida!")

# Executando
cofre = BancoSeguro()
cofre.abrir()

