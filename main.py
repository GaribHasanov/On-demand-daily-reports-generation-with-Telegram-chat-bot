import pyodbc
import psycopg2
import config
from telebot import TeleBot as tb
from telebot import types
import threading


server = "serverip"
database = "dbname"
username = "dbuser"
password = "dbpassword"



bot = tb(config.token)

#Retrieving loans information by typing "/loan" in Telegram chat bot channel
@bot.message_handler(commands=['loan'])  
def vb_reply(message):
    stand_qry(query1,message.from_user.id)
  
  
#Retrieving repayments information by typing "/repayment" in Telegram chat bot channel
@bot.message_handler(commands=['repayment'])  
def vb_reply(message):
    stand_qry(query2,message.from_user.id)


#Retrieving failed or successful jobs by typing "/jobs" in Telegram chat bot channel
@bot.message_handler(commands=['jobs'])  
def vb_reply(message):
    stand_qry(query3,message.from_user.id)


id_list = config.telegram_user_id_list

#add your own SQL query
query1 =  ("""select branch_name, sum(amount) as amount from loans where date = DATE(now()) group by branch_name""")
query2 =  ("""select branch_name, sum(amount) as amount from repayments where date = DATE(now()) group by branch_name""")
query3 =  ("""select status, description from jobs where date = DATE(now()) """)




def stand_qry(param1,user_id):
    if user_id in id_list:
        conn = psycopg2.connect(dbname=database, user=username, password=password, host=server)
        cursor = conn.cursor()
        streng = []
        cursor.execute(param1)
        sql_qry_output = cursor.fetchall()

        for row in sql_qry_output:
        	streng.append(row)
        
        message_for_user = ' \n'.join(map(str, streng))
		
        message_for_user = message_for_user.replace('(', '')
		
        message_for_user = message_for_user.replace(',)', '')
		
        message_for_user = message_for_user.replace('\'', '')
        
        bot.send_message(user_id, message_for_user)
        cursor.close()
        conn.close()
    else:
        bot.send_message(user_id,"You do not have permissions")

def runBot():
	bot.infinity_polling(True)


if __name__=='__main__':
    t1 = threading.Thread(target=runBot)
    t1.start()