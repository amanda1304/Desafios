class CaixaEletronico:
    def __init__(self):
        self.__conta ='567'
        self.__senha = '234'
        self.__dinheiro = 600.0
    def _verificar_conta_senha(self, conta, senha):
        return conta == self.__conta and senha == self.__senha
    def conectado(self):
        conta_digitada = input("Digite o numero da conta:")
        senha_digitada = input("Digite a senha da conta:")
        if self._verificar_conta_senha(conta_digitada, senha_digitada):
            print("Bem Vindo!")
            self.menu()
        else:
            print("Senha ou número da conta invalido")
    def menu(self):
        while True:
            print("""
            =========================
            
                    [d]-Deposito
                    [s]-Sacar
                    [e]-Extrato
                    [t]-Trocar a Senha
                    [q]-Sair
                    
            =========================
                """)
            opcao = input("").lower()
            if opcao == 'd':
                valor = float(input("Digite o valor que deseja depositar: "))
                if valor > 0:
                    self.__dinheiro += valor
                    print(f" Depósito de R$ {valor:.2f} realizado.")
                else:
                    print(" Valor inválido.")

            elif opcao == 's':
                valor = float(input("Digite o valor que deseja Sacar: "))
                if 0 < valor <= self.__dinheiro:
                    self.__dinheiro -= valor
                    print(f" Saque de R$ {valor:.2f} realizado.")
                else:
                    print("Valor inválido ou saldo insuficiente.")

            elif opcao == 'e':
                print ("----------- Extrato ------------ \n")
                print (f" Extrato: R$ {self.__dinheiro:.2f}\n")
                print("---------------------------------")
            elif opcao == 't':
                 senha_atual = input("Digite sua senha atual: ")
                 if senha_atual == self.__senha:
                    novasenha = (input("Troca a Senha: "))
                    self.__senha = novasenha
                    print(f" Sua nova senha: {novasenha}")
                 else:
                     print("Senha atual incorreta.")
            elif opcao == 'q':
                print(" Saindo do Conta...")
                break

            else:
                print(" Opção inválida!")

caixa = CaixaEletronico()
caixa.conectado()