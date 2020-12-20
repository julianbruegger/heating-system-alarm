import Adafruit_DHT
import time
import mysql.connector
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail(): # Define Mail function
    #Creating Mail-Content
    mail_content = ('''Hallo,

Dies ist eine automatisierte Mail.

Die Temparatur in der Heizung ist unter 63 Grad gefallen. Diese liegt bei '''
    + str(temp) +''' grad.

Bitte Kontrolliere dies, vielen Dank.



Weitere Informationen finden sie unter:

heizung.widacher.tk''')

    #The mail addresses and password
    sender_address = 'Sender@mail.com' #Add your sender-mail
    sender_pass = 'yourpassword' #Add your sender-mail Password
    receiver_address = 'reciver@mail.com' #Mail-addres of reciver
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = '[WARNUNG] - Temparatur ist niedrig!'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

null_variable = None
# Define db
mydb = mysql.connector.connect(
    host="###", #Ip Addres of database (ex. 10.20.30.40) 
    user="heiz", # Username for mySql Database
    password="***", # PWD for Mysql Database
    database="temp_data") #Database
mycursor = mydb.cursor()

#Sensor Details, chose right for your purpouse
#sensor = Adafruit_DHT.DHT11 
#sensor = Adafruit_DHT.DHT21 
sensor = Adafruit_DHT.DHT22 

#Chose GPIO Pin where DATA of DHT is connected to
pin = 21


# Get temperature
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity > 100:
    sys.exit()
# Due some Errors wit values over 100, I created a filter. 

if humidity is null_variable:
    print('Value is null')
    time.sleep(60)
else:
     #Insert values into db
     sql = "INSERT INTO heizung (time, humidity, temperature) VALUES (now(), %s,%s)"
     temp = ((temperature) + 10) # Add an offset to the temperature
     val = (humidity, temp)
     mycursor.execute(sql, val)
     mydb.commit()

if temp < 63 :
    #Check if Temperature is lower than 63 degrees celcius
    time.sleep(300) # Wait 5 mins
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) # get data again
    temp = ((temperature) + 10) # Add an offset to the temperature
    if temp < 63 :
        #If new mesurement ist still lower than 63 degrees, send alert-Mail
        mail()