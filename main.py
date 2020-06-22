from lerArquivo import *
from utilitariosJogo import *
from datetime import datetime

import json

#-------------------------------- Variáveis de controle do jogo ------------------------------
tentativasLetra = 5
letrasErradas = 0
suporPalavras = 3
ganhouJogo = False
letrasUtilizadas = []


#------------------------------------- Funções de controle -----------------------------------

#Verifica se a letra já foi testada pelo usuário
def letraRepetida(letra, listaLetras): 
    if(letra not in listaLetras):
        return False
    else:
        return True
 
 #   
def printarStatus(dica, tentativasLetra, suporPalavras):
    print('Palavra: ' + dica + '\n')
    print('Tentativas de letra restantes: ' + str(tentativasLetra))
    print('Tentativas de palavra restantes: ' + str(suporPalavras))
    print('Letras tentadas: ' + ','.join(letrasUtilizadas))
    print('Letras erradas: ' + str(letrasErradas)  + '\n')



#--------------------------------------- INICIO DO JOGO --------------------------------------

print('### JOGO DA FORCA ###')

nomeUsuario = input('Digite seu nome: ')
emailUsuario = input('Digite seu email: ')

print("\nA palavra foi escolhida, dica inicial: \n")
palavraOculta = sortearPalavra('baseDados.txt')
dica = dicaPalavra(palavraOculta)



while((tentativasLetra > 0) and (suporPalavras > 0) and not(ganhouJogo)):
    
    print('Digite a ação que deseja tomar:')
    print('1 - Advinhar letra\n2 - Advinhar a palavra')
    
    option = input('Digite a opção: ')

    if(option == '1'):
        print('\n####################')
        letra = input('Insira uma letra: ')  
        
        #Realizando a verficação antes de prosseguir
        while(not(letraCorreta(letra))):
            letra = input("\nPor favor, digite uma letra no formato correto: ")

        while(letraRepetida(letra, letrasUtilizadas)):
            letra = input('Você já tentou esta letra, por favor tente outra: ')
            
        letrasUtilizadas.append(letra)

        estadoAnteriorDica = dica
        dica = letraPalavra(letra, palavraOculta, dica)

        #Verifica se errou a letra
        if(estadoAnteriorDica == dica):
            letrasErradas += 1
            tentativasLetra -= 1
            printarStatus(dica, tentativasLetra, suporPalavras)
        
        elif(dica == True): #Verifica se o jogo foi ganho
            print('Parabéns! Você descobriu a palavra oculta!')
            print('Palavra: ' + palavraOculta + '\n')
            ganhouJogo = True
        
        else:
            printarStatus(dica, tentativasLetra, suporPalavras)
        
    elif (option == '2'):
        print('\n####################')
        palpite = input('Insira seu palpite: ')

        if(palpitePalavra(palpite, palavraOculta)): #Verifica se o jogo foi ganho
            print('Palavra: ' + palavraOculta + '\n')
            ganhouJogo = True
        else:
            suporPalavras -= 1
            printarStatus(dica, tentativasLetra, suporPalavras)
    else:
        print('Por favor, insira uma opção válida!\n')

#Tratamento final ao status do jogo
if(not ganhouJogo):
    print('Você perdeu o jogo! :(')
    status = 'Perdeu o jogo! :('
else:
    status = 'Venceu o jogo!'

data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


resultadoJogo = {
    'Nome Jogador': nomeUsuario,
    'E-mail Jogador': emailUsuario,
    'Palavra Oculta': palavraOculta,
    'Status': status,
    'Data e Hora': data
}

with open('historico.json', 'a') as arquivoJson:
    json.dump(resultadoJogo, arquivoJson, indent=4)