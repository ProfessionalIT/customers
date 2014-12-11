Sua hospedagem suporta Python e PostgreSQL  ?

Fiz o script abaixo para testar se o driver de conexão com o PostgreSQL psycopg2 está instalado corretamente e tudo está funcionando direito, conforme o esperado.
Espero que possa ser útil para mais alguém.

Salve o código abaixo com o nome, por exemplo pg_test.py e troque as variáveis conforme os dados de sua conexão e tabela.

import sys
import psycopg2
import traceback

def faca_algo_com_a_excessao():
    exc_type, exc_value = sys.exc_info()[:2]
    print 'Deu a %s excessao com a mensagem "%s" na %s' % \
        (exc_type.__name__, exc_value, threading.current_thread().name)

try:
    conn=psycopg2.connect("dbname='seu_banco_de_dados' user='usuario_do_banco' host='seu_servidor' password='senha_do_usuario'")
except:
    faca_algo_com_a_excessao()
    traceback.print_exc()

cur = conn.cursor()

try:
    cur.execute("""SELECT * FROM sua_tabela""")
except:
    faca_algo_com_a_excessao()
    traceback.print_exc()

registros = cur.fetchall()
print "\nRows: \n"
for registro in registros:
    print "  ", registro[1]
