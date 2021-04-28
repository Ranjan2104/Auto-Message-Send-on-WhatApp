import pywhatkit as kt
import getpass as gp

#display welcome msg
print("Auto Message Send on Whatsapp!")

#the target phone number
p_num = gp.getpass(prompt='Phoneumber: ', stream=None) 

#the message to be send User
msg = "This Msg From Python!"

#Method Calling
kt.sendwhatmsg(p_num, msg, 11, 25)
