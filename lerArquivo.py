from random import choice

#Função para sorteio de palavra em um arquivo
def listarPalavras(arquivo):
    arquivo = open(arquivo, 'r')
    concatenarLinhas = " "
    #Juntando as linhas para as palavras serem separadas por ;
    for linha in arquivo:
        linha = linha.strip()
        linha += ";"#Adicionando ao final de cada linha lida
        concatenarLinhas += linha
    #Não esquecer de fechar o arquivo aberto
    arquivo.close()
    #Troca todos os espaços restantes
    concatenarLinhas = concatenarLinhas.replace(' ', ';')
    #Colocar as palavras em uma lista
    listaPalavras = concatenarLinhas.split(';')
    #Filtrar palavras vazias
    listaPalavras = [palavra for palavra in listaPalavras if (palavra != '')]
    return (listaPalavras)

def sortearPalavra(arquivo):
    listaPalavras = listarPalavras(arquivo)
    palavraSortada = choice(listaPalavras).upper()#Para sortear a palavra e torna-la maiuscula
    return(palavraSortada)