from datetime import datetime

class AnotacoesSecretas:
    def __init__(self):
        self.__senha = '123'
        self.__anotacoes = []

    def verificar_digitada(self, senha):
        return self.__senha == senha

    def ativo(self):
        senha_digitada = input('Digite a senha para efetuar o login: ')
        if self.verificar_digitada(senha_digitada):
            print('Bem Vindo!')
            self.menu()
        else:
            print("Senha ou número da conta invalido")
            return AnotacoesSecretas()

    def menu(self):
        while True:
            print("""
               =========================

                       [1]- Adicionar nota
                       [2]- Ver notas
                       [3]- Excluir nota
                       [4]- Trocar a Senha
                       [5]- Exportar notas (.txt)
                       [6]- Sair

               =========================
                   """)
            opcao = input('').lower()

            if opcao == '1':
                if len(self.__anotacoes) >= 10:
                    print("Você atingiu o limite de 10 anotações.")
                    continue
                nota = input('Digite sua nota: ')
                data = datetime.now().strftime("%d/%m/%Y %H:%M")
                self.__anotacoes.append(f"[{data}] {nota}")
            elif opcao == '2':
                if not self.__anotacoes:
                    print("Nenhuma anotação encontrada.")
                else:
                    print("\nSuas Anotações:")
                    for i, nota in enumerate(self.__anotacoes, start=1):
                        print(f"{i}. {nota}")

            elif opcao == '3':
                if not self.__anotacoes:
                    print("Não há notas para excluir.")
                else:
                    try:
                        indice = int(input('Digite o número da nota que deseja excluir: ')) - 1
                        if 0 <= indice < len(self.__anotacoes):
                            nota_removida = self.__anotacoes.pop(indice)
                            print(f"Nota '{nota_removida}' excluída com sucesso.")
                        else:
                            print("Número inválido.")
                    except ValueError:
                        print("Por favor, digite um número válido.")

            elif opcao == '4':
                senha_atual = input('Digite sua senha atual: ')
                if senha_atual == self.__senha:
                    senha_nova = input('Digite a nova senha: ')
                    self.__senha = senha_nova
                else:
                    print('Senha incorreta você não pode mudar a senha!')

            elif opcao == '5':
                with open('anotacoes.txt', 'w') as arquivo:
                    for i, nota in enumerate(self.__anotacoes, start=1):
                        arquivo.write(f"{i}. {nota}\n")
                print("Notas exportadas com sucesso para 'anotacoes.txt'.")

            elif opcao == '6':
                break

secreto = AnotacoesSecretas()
secreto.ativo()
