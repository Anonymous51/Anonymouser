import requests
import requests

elkuser = "u153763a5eee69fe1daaaffd70cd18d3c"
elkpass = "C46604A38BB88F846E71338FD6E81CC2"

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
print r.json()
