# iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# o contato deve ter (Nome, telefone, Email e opção de adicionar aos favoritos)
#vizualizar lista de contatos
# , editar um contato
# , marcar/desmarcar contato como favorito
# , ver lista de favoritos e 
# apagar um contato
def converte(expressao):
    if expressao == "y":
        return  True
    elif expressao == "n":
        return  False
    
def visualizar(lista):
    print("-----------------------------------------------------------------")
    for contato  in lista:
        contato_nome = contato["nome"]
        contato_numero = contato["telefone"]
        contato_email = contato["email"]
        favorito = "★" if contato["favoritado"] else " "
        print(f"{favorito}) {contato_nome} tel: {contato_numero}, email: {contato_email}")
    print("-----------------------------------------------------------------")
def criar_contato(lista, nome_contato, telefone_contato, email_contato, favorito):

    lista.append({"nome": nome_contato,
                  "telefone": telefone_contato,
                  "email": email_contato,
                  "favoritado": favorito})
    
    return

def editar_contato(lista,nome, novo_nome, novo_telefone, novo_email, favorito):
     for contato in lista:
         if contato["nome"] == nome:
             contato["nome"] = novo_nome
             contato["telefone"] = novo_telefone
             contato["email"] = novo_email
             contato["favoritado"] = favorito

def ver_favoritos(lista):
    for contato in lista:
        if contato["favoritado"]:
            lista_de_favoritos.append(contato)
    visualizar(lista_de_favoritos)

def des_favoritar(lista, nome_contato):
    for contato in lista:
        if contato["nome"] == nome_contato:
            if contato["favoritado"]:
                contato["favoritado"] = False
            else:
                contato["favoritado"] = True

def deletar_contato(lista, nome_contato):
    for contato in lista:
        if contato["nome"] == nome_contato:
            lista.remove(contato)

lista_de_favoritos = []
lista_de_contatos = []


while True:
    print("\n[1] adicionar contato a lista")
    print("[2] vizualizar lista de contatos")
    print("[3] editar contatos")
    print("[4] vizualizar lista de favoritos")
    print("[5] (des)favoritar contato")
    print("[6] apagar um contato")
    print("[sair] fechar agenda de contatos\n")
    escolha = input("digite a ação que deseja fazer: ")

    if escolha == "1":
        nome_do_contato = input("Digite o nome do contato: ")
        telefone = input("Digite o numero do contato: ")
        email_do_contato = input("Digite o Email do contato: ")
        pergunta_favorito = input("Adicionar o contato para a lista de favoritos? [y/n]: ")
        if pergunta_favorito == "y":
            favorito = True
        elif pergunta_favorito == "n":
            favorito = False
        try:
            criar_contato(lista_de_contatos,nome_do_contato,telefone,email_do_contato,favorito)
        except Exception as er:
            print(f"Erro: {er}")
        else:
            print("\ncontato criado com sucesso!")
    
    if escolha == "2":
        visualizar(lista_de_contatos)
    
    if escolha == "3":
        visualizar(lista_de_contatos)
        nome = input("\nDigite o nome do contato que deseja editar: ")
        novo_nome = input("Digite o novo nome que deseja colocar: ")
        novo_telefone = input("Digite o novo telefone: ")
        novo_email = input("Digite o novo email: ")
        novo_favorito = input("Deseja salvar o contato como favorito? [y/n]")
        favoritado = converte(novo_favorito)
        editar_contato(lista_de_contatos, nome, novo_nome, novo_telefone, novo_email, favoritado)
    if escolha == "4":
        ver_favoritos(lista_de_contatos)
    
    if escolha == "5":
        nome_contato = input("digite o nome do contato que deseja (des)favoritar: ")
        des_favoritar(lista_de_contatos, nome_contato)
        print("contato (des)favoritado com sucesso!")
    
    if escolha == "6":
        nome_contato = input("digite o nome do contato que deseja deletar: ")
        deletar_contato(lista_de_contatos, nome_contato)
        print("contato deletado com sucesso!")
        
    if escolha == "sair":
        break

