#!/usr/bin/python

# Hello world python program

import json, requests


#Teste 1 - Verificar o Status
response_teste_1 = requests.get("http://restchallenge-neoautomation.rhcloud.com/api/v1/users/")

status_code_esperado_teste_1 = 200
status_code_recebido_teste_1 = response_teste_1.status_code

if status_code_recebido_teste_1 == status_code_esperado_teste_1:
	print 'Resultado Teste 1 - Status: Sucesso'
else:
	print 'Resultado Teste 1 - Status: Falha (Resultado Esperado: 200. Resultado Retornado: ' + str(status_code_recebido_teste_1) + ')'



#Teste 1 - Verificar o tamanho da Lista
lista_user_teste_1 = json.loads(response_teste_1.content)

tamanho_lista_esperado_teste_1 = 2
tamanho_lista_retornato_teste_1 = len(lista_user_teste_1) 

if tamanho_lista_retornato_teste_1 == tamanho_lista_esperado_teste_1:
	print 'Resultado Teste 1 - Tamanho da Lista: Sucesso'
else:
	print 'Resultado Teste 1 - Tamanho da Lista: Falha (Resultado Esperado: 2. Resultado Retornado: ' + str(tamanho_lista_retornato_teste_1) + ')'



#Teste 2 - Verificar o Status
response_teste_2 = requests.get("http://restchallenge-neoautomation.rhcloud.com/api/v1/users/1")

status_code_esperado_teste_2 = 200
status_code_recebido_teste_2 = response_teste_2.status_code

if status_code_recebido_teste_2 == status_code_esperado_teste_2:
	print 'Resultado Teste 2 - Status: Sucesso'
else:
	print 'Resultado Teste 2 - Status: Falha (Resultado Esperado: 200. Resultado Retornado: ' + str(status_code_recebido_teste_2) + ')'



#Teste 2 - Verificar o Nome Maria para o atributo firstname
lista_user_teste_2 = json.loads(response_teste_2.content)

nome_firstname_esperado_teste_2 = 'Maria'
nome_firstname_recebido_teste_2 = lista_user_teste_2['firstname']

if nome_firstname_recebido_teste_2 == nome_firstname_esperado_teste_2:
	print 'Resultado Teste 2 - FirstName: Sucesso'
else:
	print 'Resultado Teste 2 - FirstName: Falha (Resultado Esperado: Maria. Resultado Retornado: ' + str(nome_firstname_recebido_teste_2) + ')'



#Teste 3 - Verificar o Status
login = data={"user":"admin","password":"123"}
response_teste_3 = requests.post("http://restchallenge-neoautomation.rhcloud.com/api/v1/login/", data=login)

status_code_esperado_teste_3 = 200
status_code_recebido_teste_3 = response_teste_3.status_code

if status_code_recebido_teste_3 == status_code_esperado_teste_3:
	print 'Resultado Teste 3 - Status: Sucesso'
else:
	print 'Resultado Teste 3 - Status: Falha (Resultado Esperado: 200. Resultado Retornado: ' + str(status_code_recebido_teste_3) + ')'



#Teste 3 - Verificar Resposta de Login Autorizado - Comportamento nao documentado. Retorno 400 Bad Request
resposta_login_autorizado_teste_3 = response_teste_3.content

msg_login_autorizado_esperada_teste_3 = 'you are logged in'

try:
	msg_login_autorizado_retornada_teste_3 = resposta_login_autorizado_teste_3['status']

	if msg_login_autorizado_retornada_teste_3 == msg_login_autorizado_esperada_teste_3:
		print 'Resultado Teste 3 - Login Autorizado: Sucesso'
	else:
		print 'Resultado Teste 3 - Login Autorizado: Falha (Resultado Esperado: you are logged in. Resultado Retornado: ' + str(msg_login_autorizado_retornada_teste_3) + ')'

except Exception, e:
	print 'Resultado Teste 3 - Login Autorizado: Falha (Sem Resposta Rest na tentativa de Login Autorizado)'



#Teste 4 - Verificar o Status
login = data={"user":"administrador","password":"123"}
response_teste_4 = requests.post("http://restchallenge-neoautomation.rhcloud.com/api/v1/login/", data=login)

status_code_esperado_teste_4 = 200
status_code_recebido_teste_4 = response_teste_4.status_code

if status_code_recebido_teste_4 == status_code_esperado_teste_4:
	print 'Resultado Teste 4 - Status: Sucesso'
else:
	print 'Resultado Teste 4 - Status: Falha (Resultado Esperado: 200. Resultado Retornado: ' + str(status_code_recebido_teste_4) + ')'



#Teste 4 - Verificar Resposta de Login Nao Autorizado - Comportamento nao documentado. Retorno 400 Bad Request
#resposta_login_nao_autorizado_teste_4 = json.loads(requests.get("http://restchallenge-neoautomation.rhcloud.com/api/v1/users/8").content)
resposta_login_nao_autorizado_teste_4 = response_teste_4.content

msg_login_nao_autorizado_esperada_teste_4 = 'unauthorized'

try:
	msg_login_nao_autorizado_retornada_teste_4 = resposta_login_nao_autorizado_teste_4['status']

	if msg_login_nao_autorizado_retornada_teste_4 == msg_login_nao_autorizado_esperada_teste_4:
		print 'Resultado Teste 4 - Login Nao Autorizado: Sucesso'
	else:
		print 'Resultado Teste 4 - Login Nao Autorizado: Falha (Resultado Esperado: unauthorized. Resultado Retornado: ' + str(msg_login_nao_autorizado_esperada_teste_4) + ')'

except Exception, e:	
	print 'Resultado Teste 4 - Login Nao Autorizado: Falha (Sem Resposta Rest na tentativa de Login Nao Autorizado)'	