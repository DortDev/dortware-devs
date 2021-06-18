import requests
r = requests.get('https://www.fbi.gov/wanted')

theUserNameInputGiven = input('WHAT IS YOUR USERNAME FOR AUTH: ')
# No hwid checks needed i trust th epeople
thePasswordGivenInputGivenForAuth = input('PLEASE ENTER PASSWORD FOR AUTH: ')

suces = "false"

for line in r.text:
 if line == theUserNameInputGiven + " | " + thePasswordGivenInputGIvenForAuth:
  print('authencintated!')
  suces = "true"

if suces == "true":
 print("sucesful authenciated oyu" + theUserNameInputGiven)
if suces = "false":
 print("sorry" + theUserNameINputGiven + "THE UATH FAILED!")
 
 # client load herr
 
 
 def getClientMainScreenWelcomeText(THEUSERNAMEUSEDFORTHECLIENTMAINSCREENWELCOMETEXT):
  return "Welcome to dortwar" + THEUSERNAMEUSEDFORTHECLIENTMAINSCREENWELCOMETEXT
 
class client():
 def write(MESSAGEtoWRITEonHOMESCREEN):
  print(MESSAGEtoWRITEonHOMESCREEN)
 
client.write(getClientMainScreenWelcomeText(theUserNameInputGiven))
