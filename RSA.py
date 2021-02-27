from random import randrange #Biblioteca para números aleatórios
def Primo(ini,tam):
	numero = randrange(ini,tam)
	divisores = 0
	for divisor in range(1, numero):
		if numero % divisor ==0:
			divisores = divisores + 1
		if divisores > 1:
			break
	if divisores > 1:
		return Primo(0,1000)
	else:
		return numero
def InversoMultiplicativo(a,P):
	for i in range(0,P):
		if(i*a)%P==1:
			return i 
def encrip(frase):
	ASCII = [0]*len(frase)
	for i in range(0,len(frase)):
		ASCII[i] = ord(frase[i])
	codificar = [0]*len(frase)
	for i in range(0,len(frase)):
		codificar[i]=(ASCII[i]**e)%n
	return codificar
def imprimir(frase):
	for i in range(0,len(frase)):
		print(chr(frase[i]),end="")
	print("\n")
def descrip(frase):
	codificar = [0]*len(frase)
	for i in range(0,len(frase)):
		codificar[i] = frase[i]
	for i in range(0,len(frase)):
		codificar[i]=(codificar[i]**d)%n
	return codificar
p=Primo(0,1000) #chama função que criar um número Primo
q=Primo(0,1000)
n=p*q 
t=(p-1)*(q-1) #totiente em n
e = Primo(1,t) #Segunda chave publica 1>e>t
d = InversoMultiplicativo(e,t)
print("Primeira Chave Pública: ",n)
print("Segunda Chave Pública: ",e)
print("Primeira Chave Privada",p," e ",q)
print("Segunda Chave Privada: ",d)
frase = input("Entre com o texto para codificar: ")
print(frase)
print(encrip(frase))
imprimir(descrip(encrip(frase)))
