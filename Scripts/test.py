import time, sys
import http.client, urllib.request, urllib.parse, urllib.error
import random

API_KEY_WRITE = 'TZOLPCLYLWWZTWCH'  # Specify your Write API Key !!!


def send_values( color, number, Type ):
    global API_KEY_WRITE
    params = urllib.parse.urlencode(
             {'field1': color, 'field2': number,'field3': Type,
              'key': API_KEY_WRITE} )
    headers = { "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "text/plain" }
    conn = http.client.HTTPConnection("api.thingspeak.com:80")

    try:
        conn.request( "POST", "/update", params, headers ) # send HTTP request
        resp = conn.getresponse() # get HTTP response
        print('status:', resp.status, resp.reason) # read HTTP status
        entry_id = resp.read()  # read response string
        conn.close()            # close HTTP connection
        if entry_id.isdigit() and int(entry_id) > 0:
            print('Entry ID:', entry_id)
            return True
        else:
            return False
    except:
         print("Connection failed")
         return False

if __name__ == "__main__":
    try:
        while True:
           # generate random values for temperature and relative humidity
           color  = int(random.random()*10 + 250)/10.0
           number = int(random.random()*25 + 500)/10.0
           Type   = int(random.random()*15 + 100)/10.0

           if send_values( color, number, Type ): # submit values
               print('Data submission: OK')
           else:
               print('Data submission: Failed!')

           time.sleep(15) # sleep for 20 seconds

    except KeyboardInterrupt:
        print('Stopped..')
    finally:
        pass