from Model import Model

class Control:
    def __init__(self):
        self.modelo = Model()
        self.opcao = -1

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("\n\n********* Seja bem vindo!! *********\nEscolha uma das opções abaixo:\n\n" +
                "0. Sair\n" +
                "1. Ver Catálogo\n" +
                "2. Gerenciar Catálogo")
        self.setOpcao(int(input()))

    def menuCatalogo(self):
        print("\n\n********* Seja bem-vindo ao catálogo!! *********:")
        print(self.modelo.selecionar())
        print("\n\nLinks para receitas em vídeo para OUVINTES:\n" +
              '1-(RECEITAS DE PAI: https://www.youtube.com/c/ReceitasdePai\n' +
              '2-(PALMIRINHA ONOFRE: https://www.youtube.com/user/vovopalmirinhaonofre/videos\n' +
              '3-(RECEITAS DA JOSI: https://www.youtube.com/c/ReceitasdaJosivideos\n'
              )
        print("\n\nLinks para receitas em vídeo para SURDOS:\n" +
              '1-(COZINHANDO EM LIBRAS: https://www.youtube.com/watch?v=VnDw12HK7jY\n'                  +
              '2-(RECEITAS DA BRU EM LIBRAS: https://www.youtube.com/c/ReceitasdaBruEMLIBRAS\n'         +
              '3-(CONFEITALIBRAS: https://www.youtube.com/c/ConfeitaLibras\n'
              )

    def menuAdmin(self):
        print("\n\n********* Seja bem-vindo!! *********\nEscolha uma das opções abaixo:\n\n" +
                "0. Voltar\n" +
                "1. Inserir Receita\n" +
                "2. Consultar Todas as Receitas\n" +
                "3. Atualizar o Nome da Receita\n" +
                "4. Atualizar Ingredientes da Receita\n" +
                "5. Atualizar Modo de Preparo da Receita\n" +
                "6. Atualizar o Link da Receita\n" +
                "7. Deletar Receita")
        self.setOpcao(int(input()))

    def cadastrar(self):
        print("Informe o nome da receita:")
        nome = input()
        print("Informe os ingredientes para a receita:")
        ingrediente = str(input())
        print("Informe o modo de preparo para a receita:")
        preparo = str(input())
        print("Informe o link para a receita em libras:")
        link = str(input())
        print(self.modelo.inserir(nome, ingrediente, preparo, link))

    def atualizarNome(self):
        print("Informe o código que será atualizado:")
        cod = int(input())
        print("Informe o novo nome da receita:")
        name = input()
        self.modelo.atualizar("nome", name, cod)

    def atualizarIngrediente(self):
        print("Informe o código que será atualizado:")
        cod = int(input())
        print("Informe o novo ingrediente:")
        ing = input()
        self.modelo.atualizar("igrediente", ing, cod)

    def atualizarPreparo(self):
        print("Informe o código que será atualizado:")
        cod = int(input())
        print("Informe o novo modo de preparo:")
        prep = input()
        self.modelo.atualizar("preparo", prep, cod)

    def atualizarLink(self):
        print("Informe o código que será atualizado:")
        cod = int(input())
        print("Informe o novo link:")
        libras = input()
        self.modelo.atualizar("link",libras, cod)

    def excluir(self):
        print("Informe o código do dado que deseja deletar:")
        cod = int(input())
        print(self.modelo.excluir(cod))

    def operacao(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.operacaoCatalogo()
            elif self.getOpcao() == 2:
                self.operacaoAdmin()

    def operacaoAdmin(self):
        while self.getOpcao() != 0:
            self.menuAdmin()
            if self.getOpcao() == 0:
                self.menu()
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            elif self.getOpcao() == 3:
                self.atualizarNome()
            elif self.getOpcao() == 4:
                self.atualizarIngrediente()
            elif self.getOpcao() == 5:
                self.atualizarPreparo()
            elif self.getOpcao() == 6:
                self.atualizarLink()
            elif self.getOpcao() == 7:
                self.excluir()

    def operacaoCatalogo(self):
        while self.getOpcao() != 0:
            self.menuCatalogo()
            print("\n\nPressione 0 para Voltar")
            self.setOpcao(int(input()))
            if self.getOpcao() == 0:
                self.menu()
            else:
                print("Opção inválida!")

    def arroz(self):
       print( '*-* ARROZ *-*\n\n'                                                                                                           +
              'A.Aqueça uma panela com azeite, acrescente a cebola, o alho e deixe refogar mexendo até que esteja dourado\n'                +
               'B.Acrescente arroz, o sal e frite bem.\n'                                                                                   +
               'C.Coloque água fervente até que cubra o arroz, abaixe o fogo e deixe cozinhar\n'                                            +
               'D.Caso a água seque e o arroz ainda não esteja cozido, adicione mais água\n'                                                +
               'E.Deixe cozinhar atpé secat. cheque novamente se já está cozido.Desligue o fogo, solte o arroz com um garfo e sirva\n'      +
               'LINK LIBRAS: https://www.youtube.com/watch?v=l19rhrVX_3c\n')

    def feijao(self):
        print('*-* FEIJÃO *-*\n\n'                                                          +
              'A.Coloque o feijão lavado numa panela comum e leve ao fogo alto\n'           +
              'B.Quando ferver, desligue e tampe\n'                                         +
              'C.Deixe assim por uma hora, para hidratar os grãos\n'                        +
              'D.Depois é só escorrer e está pronto para cozinhar\n'                        +
              'LINK LIBRAS: https://www.youtube.com/watch?v=oqv2v29lJ3Y\n')

    def macarrao(self):
        print('*-* MACARRÃO *-*\n\n'                                                                                                                        +
              'A.Em uma panela, coloque aproximadamente 2 litros e meio de água para cozinhar o macarrão e acrescente sal a gosto.Deixe ferver.\n'          +
              'B.Adicione meio pacote do macarrão de sua preferencia e cozinhe até ficar al dente.Escorra e reserve.\n'                                     +
              'C.Em seguida, adicione 4 colheres de sopa de óleo e meia cebola\n'                                                                           +
              'D.Acrescente meia xicara do molho de sua preferencia e deixe ferver\n'                                                                       +
              'E.Depois, transfira o macarrão para a panela e misture.Sirva em seguida\n'                                                                   +
              'LINK LIBRAS: https://www.youtube.com/watch?v=5WVrja9j3Co\n')

    def arrozDoce(self):
        print('*-* ARROZ DOCE *-*\n\n'                                                                              +
              'A.Em uma panela grande, misture o arroz com 1 litro de água fria e leve ao fogo até ferver\n'        +
              'B.Abaixe o fogo e deixe cozinhar até que fique macio\n'                                              +
              'C.Junte o leite Moça, mexa bem e cozinhe por cerfca de 10 minutos, ou até engrossar\n'               +
              'D.Sirva polvilhado com a canela em pó\n'                                                             +
              'LINK LIBRAS: https://www.youtube.com/watch?v=jjBgYYXVtTw\n')

    def canjica(self):
        print('*-* CANJICA *-*\n\n'                                                                                                                         +
              'A.Em uma panela de pressão, leve a canjica demolhada ao fogo em com 2 e meio litros de água fria, reduzindo o fogo após a fervura\n'         +
              'B.Deixe cozinhar por cerca de 1 hora\n'                                                                                                      +
              'C.Depois de cozida, retire do fogo, deixe sair toda a pressão e abra a panela\n'                                                             +
              'D.Junte o Leite MOÇA, o Leite NINHO e deixe ferver por mais 5 minutos, mexendo de vez em quando até ficar cremosa\n'                         +
              'E.Despeje em uma tigela funda e sirva polvilhada com canela\n'                                                                               +
              'LINK LIBRAS: https://www.youtube.com/watch?v=mwpfTeoQLgE\n')

    def chaDeAmendoim(self):
        print('*-* CHÁ DE AMENDOIM *-*\n\n'
              'A.Bata o amendoim com a água no liquidificador, na função pulsar, até que os amendoins estejam bem triturados\n'     +
              'B.Em uma panela, coloque o leite, o leite condensado e a mistura do liquidificador\n'                                +
              'C.Leve-a ao fogo médio e cozinhe até engrossar\n'                                                                    +
              'D.Caso queira deixar seu chá mais doce, acrescente leite condensado\n'                                               +
              'LINK LIBRAS: https://www.youtube.com/watch?v=VnDw12HK7jY\n')

    def ouvinte(self):
        print('1-(RECEITAS DE PAI: https://www.youtube.com/c/ReceitasdePai\n'                       +
              '2-(PALMIRINHA ONOFRE: https://www.youtube.com/user/vovopalmirinhaonofre/videos\n'    +
              '3-(RECEITAS DA JOSI: https://www.youtube.com/c/ReceitasdaJosivideos\n')

    def surdo(self):
        print('1-(COZINHANDO EM LIBRAS: https://www.youtube.com/watch?v=VnDw12HK7jY\n'                  +
              '2-(RECEITAS DA BRU EM LIBRAS: https://www.youtube.com/c/ReceitasdaBruEMLIBRAS\n'         +
              '3-(CONFEITALIBRAS: https://www.youtube.com/c/ConfeitaLibras\n')