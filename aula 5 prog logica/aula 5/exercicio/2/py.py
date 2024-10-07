while True:
    print("menu")
    print("1. contar de 1 a 5")
    print("2. sdair")
    opcao = input("escolha uma opcap: ")

    if opcao == "1":
        for i in range(1,6):
            print(i)
    elif opcao == "2":
        print("saindo do programa.")
        break
    else:
        print("opcao invalkida")        