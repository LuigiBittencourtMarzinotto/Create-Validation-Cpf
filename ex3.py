import random
import re

def validarCpf(veio,valor_craido):
    if veio=="switch":
        cpf = input("Digite seu cpf para ser validado: ")
        cpf= re.sub(r'[^0-9]',"",cpf)
        print(cpf[0:3],".",cpf[3:6],".",cpf[6:9],"-",cpf[9:], sep="")
    elif veio=="criado":
        cpf=valor_craido
    cpfTraco=[]
    valorInicia=10
    for valore in cpf:
        cpfTraco.append(int(valore))
    cpfTraco[9]=0
    cpfTraco[10]=0
    cpfNew=[]
    total=0
    for valor in cpfTraco:
        cpfNew.append(int(valor)*valorInicia)
        valorInicia=valorInicia-1
    for valorNew in cpfNew:
        total+=valorNew
    total*=10
    result=total%11
    if result>9:
        result=0
    cpfTraco[9]=result
    total=0
    cpfNew=[]
    valorInicia=11
    for valor in cpfTraco:
        cpfNew.append(int(valor)*valorInicia)
        valorInicia=valorInicia-1
    for valorNew in cpfNew:
        total+=valorNew
    total*=10
    resultSegundo=total%11
    if resultSegundo>9:
        resultSegundo=0
    cpfTraco[10]=resultSegundo
    cpfFinal =""
    for number in cpfTraco:
        cpfFinal+=str(number)
    if veio =="switch":
        if cpfFinal==cpf :
            print("Seu cpf vou verificado e foi aprovado")
        else:
            print("Seu cpf foi reprovado")
    else:
        print(cpfFinal[0:3],".",cpfFinal[3:6],".",cpfFinal[6:9],"-",cpfFinal[9:], sep="")

def criarCPF():
    cpf_criado=[]
    for i in range(9):
        cpf_criado.append(random.randint(1,9))
    cpf_criado.append(0)
    cpf_criado.append(0)
    validarCpf("criado",cpf_criado)

def switch(case):
    if case == "v":
        return validarCpf("switch",0)
    elif case == "c":
        return criarCPF()
    else:
        return print("valor inserido inválido")

while True:
    opcao_client= input("Selecione uma opção valida: [v]alidar CPF [c]riar CPF [s]air: ")
    if opcao_client=="s":
        break
    switch(case=f"{opcao_client}")#aqui puxamos uma função que criamos usando o nome switch e passamos parametros nela como em outras linguagens