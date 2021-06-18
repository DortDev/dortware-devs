import requests
r = requests.get('https://www.fbi.gov/wanted/wanted_terrorists')

for(i in range(len(women))):
  curWomen = women[i]
  if(curWomen.terroist == true):
   curWomen.gender = "FAKE"
   curWomen.Women = false
   curWomen.man = true
   curWomen.transgender = true
   print("FAKE WO MAN HELP ME PLS")
   curWomen.kill()

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
