def adicionar_contatos(contatos, nome, telefone, email, ):
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"Seu Contato {nome} foi adicionado com sucesso!")
  return

def ver_lista_contatos(contatos):
  for i, contato in enumerate(contatos, start=1):
    favorito = '☆' if contato['favorito'] else '' 
    print(f"{i}. {favorito} Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
  return


def editar_contato(contatos, indice_contato, nome, numero, email):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]['nome'] = nome
    contatos[indice_contato_ajustado]['telefone'] = numero
    contatos[indice_contato_ajustado]['email'] = email
    print('Contato Atualizado!')
  else:
    print('Indice do Contato nao existe')
  return

def adicionar_remover_favorito(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):

    if contatos[indice_contato_ajustado]['favorito']:
      contatos[indice_contato_ajustado]['favorito'] = False
      print('Contato {} foi Removido com sucesso dos favoritos')
    else:
      contatos[indice_contato_ajustado]['favorito'] = True
      print(f'Contato {contatos[indice_contato_ajustado]['nome']} foi Adicionado com sucesso dos favoritos')

  else:
    print('Indice do Contato nao existe')
  return

def ver_lista_favoritos(contatos):
  for i, contato in enumerate(contatos, start=1):
    if contato['favorito']:
      favorito = '☆' if contato['favorito'] else '' 
      print(f"{i}. {favorito} Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos.remove(contatos[indice_contato_ajustado])
    print('Contato removido com sucesso!')
  else:
    print('Indice do Contato nao existe')
  return

contatos = []

while True:
  print("-" * 20)
  print('Lista de Contato')
  print("-" * 20)
  print("1. Adicionar Contato")
  print("2. Ver Lista de Contato")
  print("3. Editar Contato")
  print("4. Adicionar ou remover Contato Favorito")
  print("5. Ver Lista de Favoritos")
  print("6. Deletar Contato")
  print("7. Sair")
  print("-" * 20)
  escolha = input('Digite um opcao: ')


  if escolha == '1':
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    adicionar_contatos(contatos, nome, telefone, email)


  elif escolha == '2':
    ver_lista_contatos(contatos)

  elif escolha == '3':
    ver_lista_contatos(contatos)
    indice_contato = input('Digite o indice do contato que voce quer atualizar: ')
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    editar_contato(contatos, indice_contato, nome, telefone, email)

  elif escolha == '4':
    ver_lista_contatos(contatos)
    indice_contato = input('Digite o indice do contato que voce quer atualizar: ')
    adicionar_remover_favorito(contatos, indice_contato)

  elif escolha == '5':
    ver_lista_favoritos(contatos)

  elif escolha == '6':
    ver_lista_contatos(contatos)
    indice_contato = input('Digite o indice do contato que voce quer deletar: ')
    deletar_contato(contatos, indice_contato)

  elif escolha == '7':
    break

print('Saindo do Projeto')
