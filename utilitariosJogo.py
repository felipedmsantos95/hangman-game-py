from unicodedata import normalize

#Para ser utilizado na hora de comparar palpites, ignora acentos omitidos
def formatarPalavra(palavra):
    palavra = palavra.upper()
    return normalize('NFKD', palavra).encode('ASCII', 'ignore').decode('ASCII')

#Verifica tamanho da palavra e retorna a dica inicial da palavra no formato "_,_,_"
def dicaPalavra(palavra):
    dica = ""
    for letra in palavra:
        dica += "-"
    print(str(len(palavra)) + ' letras!')
    print(dica + '\n')
    return dica

#Metodo que verifica se letra foi inserida corretamente
def letraCorreta(letra):
    letra = letra.strip()
    #Verificar se a letra tem tamanho correto
    if(len(letra) != 1):
        return False
    else:
        return True


#Compara letra sugerida com a palavra oculta e printa as acertadas
def letraPalavra(letra, palavra, dica):
    
    
    letra = formatarPalavra(letra)
    palavraFormatada = formatarPalavra(palavra)
    #Retorna as posições que a letra ocorre na palavra
    ocorrenciasLetra = [i for i in range(len(palavraFormatada)) if palavraFormatada.startswith(letra, i)]

    dica = list(dica)
    for posicao in ocorrenciasLetra:
        dica[posicao] = letra.upper()
    dica = ''.join(dica)

    #Verifica se todas as letras já foram preenchidas
    if(dica.find('-') == -1):
        return True

    return dica

#Compara a tentativa de acertar a palavra com o palpite
def palpitePalavra(palpite, palavra):
    palpite = formatarPalavra(palpite).upper()
    palavraFormatada = formatarPalavra(palavra).upper()

    #Achou a palavra certa
    if(palavraFormatada == palpite):
        print('Parabéns! Você descobriu a palavra oculta!')
        return True
    else:
        print('Ainda não foi desta vez!')
        return False

def printarForca(tentativas):
    if(tentativas == 6):
        print('\n +----+')
        print(' |    |')
        print('      |')
        print('      |')
        print('      |')
        print('      |')
        print('========\n')
    elif(tentativas == 5):
        print('\n +----+')
        print(' |    |')
        print(' O    |')
        print('      |')
        print('      |')
        print('      |')
        print('========\n')
    elif(tentativas == 4):
        print('\n +----+')
        print(' |    |')
        print(' O    |')
        print(' |    |')
        print('      |')
        print('      |')
        print('========\n')
    elif(tentativas == 3):
        print('\n +----+')
        print(' |    |')
        print(' O    |')
        print('/|    |')
        print('      |')
        print('      |')
        print('========\n')
    elif(tentativas == 2):
        print('\n +----+')
        print(' |    |')
        print(' O    |')
        print('/|\   |')
        print('      |')
        print('      |')
        print('========\n')
    elif(tentativas == 1):
        print('\n +----+')
        print(' |    |')
        print(' O    |')
        print('/|\   |')
        print('/     |')
        print('      |')
        print('========\n')
    elif(tentativas == 0):
        print('\n +----+')
        print(' |    |')
        print(' O    |')
        print('/|\   |')
        print('/ \   |')
        print('   FIM|')
        print('========\n')