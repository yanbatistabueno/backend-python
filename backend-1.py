import requests
# #Exercício 1
# response = [
#     {
#         "nome": "Loja Exemplo 1",
#         "endereço": {
#             "rua": "Rua Exemplo 1",
#             "cidade": "Exemplo City 1"
#         },
#         "produtos": [
#             {"id": 1, "nome": "Produto A", "preço": 29.99},
#             {"id": 2, "nome": "Produto B", "preço": 34.99}
#         ]
#     },
#     {
#         "nome": "Loja Exemplo 2",
#         "endereço": {
#             "rua": "Rua Exemplo 2",
#             "cidade": "Exemplo City 2"
#         },
#         "produtos": [
#             {"id": 1, "nome": "Produto C", "preço": 45.50},
#             {"id": 2, "nome": "Produto D", "preço": 15.00}
#         ]
#     },
#     {
#         "nome": "Loja Exemplo 3",
#         "endereço": {
#             "rua": "Rua Exemplo 3",
#             "cidade": "Exemplo City 3"
#         },
#         "produtos": [
#             {"id": 1, "nome": "Produto E", "preço": 22.00},
#             {"id": 2, "nome": "Produto F", "preço": 39.99}
#         ]
#     },
#     {
#         "nome": "Loja Exemplo 4",
#         "endereço": {
#             "rua": "Rua Exemplo 4",
#             "cidade": "Exemplo City 4"
#         },
#         "produtos": [
#             {"id": 1, "nome": "Produto G", "preço": 55.00},
#             {"id": 2, "nome": "Produto H", "preço": 5.99}
#         ]
#     },
#     {
#         "nome": "Loja Exemplo 5",
#         "endereço": {
#             "rua": "Rua Exemplo 5",
#             "cidade": "Exemplo City 5"
#         },
#         "produtos": [
#             {"id": 1, "nome": "Produto I", "preço": 33.00},
#             {"id": 2, "nome": "Produto J", "preço": 27.50}
#         ]
#     }
# ]


# produtos_retirados = []
# for lojas in response: #Pegar o valor de cada loja
#     for i in lojas["produtos"]: #Pegar todos os valores de todos os produtos de cada loja
#         if(i["preço"] > 30): #Ver se o preço retirado é maior que 30
#             produtos_retirados.append(i) #Armazenar os produtos que passaram pela condição
# print("Resposta do exercício 1:", produtos_retirados)


# #Exercício 2
# responsejson = {
#     "nome": "Loja Exemplo",
#     "endereço": {
#         "rua": "Rua Exemplo",
#         "cidade": "Exemplo City"
#     },
#     "produtos": [
#         {"id": 1, "nome": "Produto A", "preço": 29.99},
#         {"id": 2, "nome": "Produto B", "preço": 19.99}
#     ]
# }

# preco_produto_b_direto = 0

# preco_produto_b_direto = responsejson["produtos"][1]["preço"] #Acessar diretamente pelo JSON


# #Ou passar por cada valor e pegar o valor do produto específico

# preco_produto_b = 0

# for produtos in responsejson["produtos"]: #Pegar o valor de todos os produos
#     if(produtos["nome"] == "Produto B"): #Comparar o valor "nome" e ver se é igual a Produto B
#         preco_produto_b = produtos["preço"] #Se for passar o valor do "preço" para a variavel

# print("Resposta do exercício 2:", preco_produto_b)

# #Exercício 3
# lista_sort= [5,8,3,0,8,1,9,10,20,30]

# lista_sort.sort() #Usando a própria função do python

# #Ou usando o método de flutuação

# lista = [5,8,3,0,8,1,9,10,20,30]

# for i in range(len(lista)): #Ver cada item da lista
#     for v in range(i + 1, len(lista)): #Ver cada item proximo da lista
#         if lista[i] > lista[v]: #Se o item atual for maior que o proximo item da lista, inverter os dois
#            lista[i], lista[v] = lista[v], lista[i]

# print("Resposta do exercício 3:", lista)

# #Exercício 4

# listaString = ["   joao   ","   maria   ","  joana  "]
# listaStringArrumada = []

# #Usando a função replace do python

# for string in listaString: #Passar por cada string da lista
#     v = string.replace(" ", "") #Substituir cada espaço vazio por nada
#     listaStringArrumada.append(v) #Colocar os itens arrumados na nova lista

# #Ou usando um algoritimo que pega todo caractere que não seja um " " de uma string e guardando os caracteres selecionados em uma nova string

# newString = ""
# listaStringArrumadaAlgoritmo = []
# for string in listaString: #Passando por cada string da lista
#     for i in string: #Passando por cada caractere da string selecionada
#         if(i != " "): #Se o caractere não for um " " ele vai adicionar ele na nova string
#             newString += i
#     listaStringArrumadaAlgoritmo.append(newString) #Colocar a nova string formada na lista
#     newString = "" #Zerar o valor da nova string para ela receber um outro valor

# print("Resposta do exercício 4:", listaStringArrumadaAlgoritmo)

# #Exercício 5

# listaRemover = [1, 2, 3, 4, 5, 6]
# valorRemovido = listaRemover[1] #Guardar o valor do segundo item da lista
# listaRemover.pop(1) #Remover o segundo item da lista
# print("Resposta do exercício 5:", valorRemovido, listaRemover)

# #Exercício 6

# listaRemoverJoao = ["joao", "ana", "joana", "joao", "ricardo", "joao"]
# count = 0
# for string in listaRemoverJoao:
#     count += 1
#     if(string == "joao"):
#         listaRemoverJoao.pop(count - 1)
# print("Resposta do exercício 6:", listaRemoverJoao)

# #Exercício 7

# itens = ["item1", "item2", "item3", "item4", "item5", "item6", "item7"]
# count = 0

# while count <=5: #Delimitar o valor do while loop até 5
#     print(itens[count]) #Mostrar o valor dentro da lista com o index igual ao da variável que está incrementando
#     count +=1 #Incrementar o valor da variável

# #Exercício 8

# def getResponse(api):
#     completed = 0 #Criar uma váriavel para armazenar a quantidade de tarefas completadas
#     pending = 0 #Criar uma váriavel para armazenar a quantidade de tarefas pendentes
#     response = requests.get(api) #Enviar uma solitação get para a api e receber os dados
#     responseJson = response.json() #Transformar os dados recebidos em Json
#     for users in responseJson: #Verificar cada dado dentro da resposta
#         if(users["completed"] == False): #Verificar se o valor "completed" é True e se for adicionar +1 para a varíavel pending
#             pending += 1
#         elif(users["completed"] == True): #Verificar se o valor "completed" é True e se for adicionar +1 para a varíavel completed
#             completed += 1
#     print("Existem: ", pending, "tarefas pendentes.")
#     print("Existem: ", completed, "tarefas completadas")

# getResponse("https://jsonplaceholder.typicode.com/todos")

# #Exercício 9

# response = requests.get("https://jsonplaceholder.typicode.com/users")
# responseJson = response.json()

# for i in responseJson:
#     nome = i["name"]
#     username = i["username"]
#     email = i["email"]
#     rua = i["address"]["street"]
#     numero = i["address"]["suite"]
#     print("Nome: ", nome, "Username:", username, "Email:", email, "Rua:", rua, "Numero:", numero)

# #Exercício 10

# class Fifo():
#     def __init__(self):
#         self.lista = []
    
#     def adicionar(self, item):
#         self.lista.append(item)
    
#     def vazio(self):
#         return len(self.lista)

#     def remover(self):
#         if self.vazio != 0:
#             return self.lista.pop(len(self.lista) - 1)
    
#     def mostrarLista(self):
#         return self.lista
    
# lista = Fifo()
# lista.adicionar(10)
# print(lista.mostrarLista())
# lista.adicionar(20)
# print(lista.mostrarLista())
# alemento = lista.remover()
# print(lista.mostrarLista())

#Exercício 11

# class Lifo():
#     def __init__(self):
#         self.lista = []
    
#     def adicionar(self, item):
#         self.lista.append(item)
    
#     def vazio(self):
#         return len(self.lista)

#     def remover(self):
#         if self.vazio != 0:
#             return self.lista.pop(0)
    
#     def mostrarLista(self):
#         return self.lista
   
# lista = Lifo()
# lista.adicionar(10)
# print(lista.mostrarLista())
# lista.adicionar(20)
# print(lista.mostrarLista())
# alemento = lista.remover()
# print(lista.mostrarLista())

