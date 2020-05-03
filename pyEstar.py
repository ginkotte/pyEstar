userArr = []
pwdArr = []

user = str(input("Seja bem vindo ao PyEstar.\nPara começar, cadastre seu login:\n"))
userArr.append(user)

pwd = str(input("Agora, cadastre sua senha:\n"))
pwdArr.append(pwd)

print("Usuário cadastrado com sucesso!")

userLogin = []
pwdLogin = []

while userLogin != userArr or pwdLogin != pwdArr:
    userLogin = [input("Digite seu login:\n")]
    pwdLogin = [input("Digite sua senha:\n")]

logado = False

if userLogin == userArr and pwdLogin == pwdArr:
    logado = True
    print("Seja bem-vindo, você está logado!")

carroArr1 = []
qtdCarro = 0

if logado == True:
    carroArr1.append(str(input("Vamos cadastrar seu veículo.\nPara começar, digite a marca do veículo:\n")))
    carroArr1.append(str(input("Agora, digite o modelo do veículo:\n")))
    carroArr1.append(str(input("Agora, digite a cor do veículo:\n")))
    carroArr1.append(input("E para finalizar, digite a placa do veículo:\n"))
    qtdCarro += 1
    print(carroArr1)

verifBool = True
carteiraCred = 0
useCarro1 = []
useCarro2 = []

while verifBool == True:
    menuOpt = int(input("Menu. \n 1- Comprar PyEstar \n 2- Comprar Créditos \n 3- Consultar Créditos \n 4- Última Utilização \n 5- Cadastrar Veículo \n"
                        "\nDigite o número correspondente a opção que deseja acessar:\n"))

    if menuOpt == 1:

        if carteiraCred >= 50:
            if qtdCarro == 2:
                carOpt = int(input("Selecione qual veículo você deseja utilizar:\n"
                                   "1- " + carroArr1[1]+ "\n"
                                   "2- " + carroArr2[1]+ "\n"))
            else:
                carOpt = 1

            if carOpt == 1:
                useCarro1.append(carroArr1[1])
                dataOpt = input("Insira a data para utilização do serviço: \n")
                horaOpt = input("Insira o horário para utilização do serviço (Lembrando que o serviço dura 1 hora e começa a contar a partir do horário escolhido: \n")
                useCarro1.append(dataOpt)
                useCarro1.append(horaOpt)
                print("Compra realizada com sucesso para" + str(useCarro1))
            elif carOpt == 2:
                useCarro2.append(carroArr2[1])
                dataOpt = input("Insira a data para utilização do serviço: \n")
                horaOpt = input("Insira o horário para utilização do serviço (Lembrando que o serviço dura 1 hora e começa a contar a partir do horário escolhido: \n")
                useCarro2.append(dataOpt)
                useCarro2.append(horaOpt)
                print("Compra realizada com sucesso para" + str(useCarro2))

            carteiraCred -= 50
            print("Após essa compra você possui " + str(carteiraCred) + " créditos.")

        else:
            print("Você não possui créditos suficientes, são necessários 50 créditos para comprar um PyEstar.")

    elif menuOpt == 2:
        qtdCredit = int(input("Digite a quantidade de créditos que você deseja comprar:\n"))
        confBuy = int(input("Você está prestes a comprar " + str(qtdCredit) + " Créditos. \n"
                                                                          "Digite 1 para confirmar ou 0 para cancelar.\n"))
        if confBuy == 1:
            print("Obrigado por comprar " + str(qtdCredit) + " créditos")
            carteiraCred = carteiraCred + qtdCredit

    elif menuOpt == 3:
        print("Você possui " +str(carteiraCred)+ " créditos.")

    elif menuOpt == 4:
        if not useCarro1 and not useCarro2:
            print("Você ainda não utilizou os serviços do PyEstar")
        elif not useCarro2:
            print("Os últimos usos com o veículo " + str(carroArr1[1]) + " foram os seguintes: \n" + str(useCarro1))
        elif not useCarro1:
            print("Os últimos usos com o veículo " + str(carroArr2[1]) + " foram os seguintes: \n" + str(useCarro2))
        else:
            print("Os últimos usos com o veículo " + str(carroArr1[1]) + " foram os seguintes: \n" + str(useCarro1))
            print("Os últimos usos com o veículo " + str(carroArr2[1]) + " foram os seguintes: \n" + str(useCarro2))

    elif menuOpt == 5:
        print("O total de carros que podem ser registrados por conta é 2!")
        confReg = int(input("Você deseja cadastrar mais um veículo?\nDigite 1 para cadastrar, digite 2 para voltar ao menu\n"))

        if confReg == 1:
            carroArr2 = []
            if logado == True:
                carroArr2.append(str(input("Vamos cadastrar seu veículo.\nPara começar, digite a marca do veículo:\n")))
                carroArr2.append(str(input("Agora, digite o modelo do veículo:\n")))
                carroArr2.append(str(input("Agora, digite a cor do veículo:\n")))
                carroArr2.append(input("E para finalizar, digite a placa do veículo:\n"))
                qtdCarro += 1
                print(carroArr2)
