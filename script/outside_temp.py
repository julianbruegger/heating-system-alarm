import Adafruit_DHT
import time
import mysql.connector
import smtplib

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
pin = 20


# Get temperature
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
#Check if Value is Null
if humidity is null_variable:
    print('Value is null')

else:
     #Insert values into db
     sql = "INSERT INTO outside (time, humidity, temperature) VALUES (now(), %s,%s)"
     val = (humidity, temperature)
     mycursor.execute(sql, val)
     mydb.commit()