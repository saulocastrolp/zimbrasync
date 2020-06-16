# -*- coding: UTF-8 -*-
import subprocess
import shlex
import argparse

parser = argparse.ArgumentParser(description = 'Script para sincronização de contas de email zimbra em massa.')
parser.add_argument('--arq', action = 'store', dest = 'arq', required = False,
                           help = 'O arquivo com as contas de email a serem sincronizadas.')
parser.add_argument('--conta', action = 'store', dest = 'conta',
                           default = False, required = False,
                           help = 'A conta para sincronização.')
parser.add_argument('--host1', action = 'store', dest = 'host1',
                           default = False, required = False,
                           help = 'O host de origem.')
parser.add_argument('--userauth1', action = 'store', dest = 'userauth1',
                           default = False, required = False,
                           help = 'O usuário de autenticação do servidor de origem.')
parser.add_argument('--passwd1', action = 'store', dest = 'passwd1',
                           default = False, required = False,
                           help = 'A senha de autenticação do servidor de origem.')
parser.add_argument('--host2', action = 'store', dest = 'host2',
                           default = False, required = False,
                           help = 'O host de destino.')
parser.add_argument('--userauth2', action = 'store', dest = 'userauth2',
                           default = False, required = False,
                           help = 'O usuário de autenticação do servidor de destino.')
parser.add_argument('--passwd2', action = 'store', dest = 'passwd2',
                           default = False, required = False,
                           help = 'A senha de autenticação do servidor de destino.')
arguments = parser.parse_args()

log = open('log_sync.txt', 'w')


host1 = input("Informe o servidor origem: ") if not arguments.host1 else arguments.host1
authuser1 = input("Informe o usuario de autenticação do servidor de origem: ") if not arguments.userauth1 else arguments.userauth1
password1 = input("Informe a senha de autenticação do servidor de origem: ") if not arguments.passwd1 else arguments.passwd1
host2 = input("Informe o servidor destino: ") if not arguments.host2 else arguments.host2
authuser2 = input("Informe o usuario de autenticação do servidor de destino: ") if not arguments.userauth2 else arguments.userauth2
password2 = input("Informe a senha de autenticação do servidor de destino: ") if not arguments.passwd2 else arguments.passwd2

if arguments.arq :
    arq = open(arguments.arq, 'r')
    for line in arq:
        conta = line.strip()
#        print(comand)
#        break
        args = shlex.split("imapsync --host1 {} --host2 {} --user1 {} --user2 {} --authuser1 {} --password1 '{}' --authuser2 {} --password2 '{}' --authmech2 PLAIN --authmech1 PLAIN --ssl1 --ssl2 --noerrorsdump".format(host1, host2, conta, conta, authuser1, password1, authuser2, password2))
        try:
            output = subprocess.check_output(args).decode("utf-8")
            print(output)
            log.write("concluido a sincronização usando o comando: {}".format(conta))
            print("concluido a sincronização usando o comando: {}".format(conta))
        except subprocess.CalledProcessError as error:
            print("Erro ao executar o comando: {}".format(conta))
            log.write("Erro ao executar o comando: {}".format(conta))
#        break
    arq.close()
elif arguments.conta:
    conta = arguments.conta
    args = shlex.split("imapsync --host1 {} --host2 {} --user1 {} --user2 {} --authuser1 {} --password1 '{}' --authuser2 {} --password2 '{}' --authmech2 PLAIN --authmech1 PLAIN --ssl1 --ssl2 --noerrorsdump".format(host1, host2, conta, conta, authuser1, password1, authuser2, password2))
    #print("imapsync --host1 {} --host2 {} --user1 {} --user2 {} --authuser1 {} --password1 '{}' --authuser2 {} --password2 '{}' --authmech2 PLAIN --authmech1 PLAIN --ssl1 --ssl2".format(host1, host2, conta, conta, authuser1, password1, authuser2, password2))
    try:
        output = subprocess.check_output(args).decode("utf-8")
        print(output)
        log.write("concluido a sincronização usando o comando: {}".format(conta))
        print("concluido a sincronização usando o comando: {}".format(conta))
    except subprocess.CalledProcessError as error:
        print("Erro ao executar o comando: {} o erro foi: {}".format(conta, error))
        log.write("Erro ao executar o comando: {}".format(conta))
else:
    print("Você deve informar um dominio ou um comando para sincronização!")
log.close()