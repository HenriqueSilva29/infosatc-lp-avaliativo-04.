palavra= str(input('Qualquer palavra que vier na sua  mente: '))
novaPalavra= str(input('Outra palavra que vier na sua  mente: '))
print(' A palavra: {}'.format(palavra))
print(' E a palavra: {}'.format(novaPalavra))
string = palavra[::-1]
outraString = novaPalavra
if (string == outraString):
     print("As palavras sao inversamente iguais")
elif(string != outraString):
    print("as palavras não sao inversamentes iguais")
       
