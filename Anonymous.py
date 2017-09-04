import requests
import requests

elkuser = "u7a17a264bdfcaabdda55f1d71386b133"
elkpass = "411D02E289CA62A2B488FFF19CF8717C"

wrong_art = """



          \                                                               
         _ \    __ \    _ \   __ \   |   |  __ `__ \    _ \   |   |   __| 
        ___ \   |   |  (   |  |   |  |   |  |   |   |  (   |  |   | \__ \ 
      _/    _\ _|  _| \___/  _|  _| \__, | _|  _|  _| \___/  \__,_| ____/ 
                               ____/                                 
  Expect us !
  SMS SPOOFER BY @Anas (Anonymous51)



"""
print wrong_art


print "To:",
recipient = raw_input()
print "From:",
sender = raw_input()
print "Message:",
messagetext = raw_input()

url = "https://api.46elks.com/a1/SMS"
r = requests.post(url, data={'to': recipient,'from': sender,'message': messagetext}, auth=(elkuser, elkpass))
print A.Mn()
