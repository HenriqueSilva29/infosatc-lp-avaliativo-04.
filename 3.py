
senha=[]
apto=[]
nome=[]
cpf=[]
usuario=0


def informaçoes ():
    nome.anexar ( input ( "Insira o seu nome" ))
    cpf.anexar ( input ( "Insira o seu cpf" ))
    senha.anexar ( input ( "Insira o sua senha" ))
    apto.anexar ( input ( "Insira o seu apto" ))

def user ( x , y , nome , cpf , senha , apto ):
    print( "" )
    print( "O nome do usuario" , x , "é" , nome [ y ])
    print( "O cpf do usuario" , x , "é" , cpf [ y ])
    print( "A senha do usuario" , x , "é" , senha [ y ])
    print( "O usuario" , x , "esta apto?" , apto [ y ])

pessoa = ( int ( input ( "Quantas pessoas irão fazer o teste de doação de sangue?" )))
for  x  in range ( pessoa ):


 for x in range(5):
    texto=""
    escolha=""
    opcao=0
    print("")
    idade=(int(input("Sua idade: ")))
    peso=(float(input(" Seu peso: ")))
    tempo=(float(input("Quantas horas de sono na ultima noite: ")))
    if idade>16 and idade<69:
        opcao+=1
    else:
        texto="idade "+texto
    if peso>50:
        opcao+=1
    else:
        texto="peso "+texto
    if tempo>6:
        opcao+=1
    else:
        texto="sono "+texto
    if opcao==3:
        print("Pode doar sangue")
        escolha=(input("Quer fazer o cadastro?(s/n): "))
        if(escolha=="s"):
           informaçoes()
        else:
            pass
    else:
        print("Infelizmente não pode doar sangue devido a falta de:",texto)
for x in range(usuario):
   user()