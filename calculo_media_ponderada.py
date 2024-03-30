#nomeação das variáveis e seus respectivos "placeholders"
#notaP1 = z; notaP2 = w; notaP3 = x; notaP4 = y
notaP1=notaP2=notaP3=notaP4=0.0
z=w=x=y = 0.0

#função que permite um input que não seja um número ser considerado como um, ao invés de dar erro.
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

#aplicação da função is_numeric(value) em cada nota
z_input = notaP1=(input('Coloque a sua nota peso 1 aqui: '))
if is_numeric(z_input):
    notaP1=float(z_input)
else:
    notaP1= float(z)
w_input = notaP2=input('Coloque a sua nota peso 2 aqui: ')
if is_numeric(w_input):
    notaP2=float(w_input)
else: 
    notaP2 = float(w)
x_input = notaP3=input('Coloque a sua nota peso 3 aqui: ')
if is_numeric(x_input):
    notaP3=float(x_input)
else: 
    notaP3 = float(x)
y_input = notaP4=input('Coloque a sua nota peso 4 aqui: ')
if is_numeric(y_input):
    notaP4 = float(y_input)
else: 
    notaP4 = float(y)

#É nomeado as variáveis ligadas às notas
media = (notaP1*1 + notaP2 *2 + notaP3 * 3 + notaP4 * 4) / 10
nota_minima_rec = 12 - media
resolver_para_nP1= (60-(notaP2*2 + notaP3*3 +notaP4*4))/1
resolver_para_nP2 = (60-(notaP1*1 + notaP3*3 +notaP4*4))/2
resolver_para_nP3 =(60-(notaP2*2 + notaP1*1 +notaP4*4))/3
resolver_para_nP4 = (60-(notaP2*2 + notaP3*3 +notaP1*1))/4


#Lógica do cálculo da média
if (notaP1 == x and 2<media<6): 
    print(f'Você precisa de {resolver_para_nP1:.1f} pontos peso 1 para ter uma nota azul.')
elif (notaP2 == x and 2<media<=6):
    print(f'Você precisa de {resolver_para_nP2:.1f} pontos peso 2 para ter uma nota azul.')
elif (notaP3 == x and 2<media<=6):
    print(f'Você precisa de {resolver_para_nP3:.1f} pontos peso 3. para ter uma nota azul')
elif (notaP4 == x and 3<=media<=6):
    print(f'Você precisa de {resolver_para_nP4:.1f} pontos peso 4 para ter uma nota azul.')
elif(2<=media < 6):
    print(f'Você ficou de recuperação! Você precisará tirar no mínimo {nota_minima_rec:.1f} para passar, sua média foi {media:.1f}!')
elif (nota_minima_rec>10 or media<2):
    print(f'Você reprovou! Boa sorte na próxima! Você precisaria tirar {nota_minima_rec:.1f} para passar...')
else:
    print(f'Você passou! Sua média final foi {media:.1f}...')
