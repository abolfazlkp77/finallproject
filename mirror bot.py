
import json                                 
from urllib.request import urlopen          
from urllib.parse import quote, unquote     
import time                                 


def aux_dec2utf8(resp):                     
    decoded = ''
    for line in resp:
        decoded += line.decode('utf-8')
    return decoded



TOKEN = '741998013:AAFwKeWC6Xx9lkk-oiiLM-8nCIwsMpiIAQg'       
URL   = 'https://api.telegram.org/bot{}/'.format(TOKEN)       

cmd   = 'getme'                                               


resp  = urlopen(URL + cmd)                                     
line  = aux_dec2utf8(resp)                                     
gtm   = json.loads(line)                                       


status = True                                                  
while status:                                                  

    cmd = 'getUpdates'                                         

    resp = urlopen(URL + cmd)                                  
    line = aux_dec2utf8(resp)                                  
    upds = json.loads(line)                                    

    NoM  = len(upds['result'])                                 

    if NoM != 0:                                               

        msg  = upds['result'][0]['message']                    
        chid = str(msg['chat']['id'])                          

        if 'text' in msg:
            txt  = quote(msg['text'].encode('utf-8'))              

            cmd  = 'sendMessage'                                   

            resp = urlopen(URL + cmd +
                 '?chat_id={}&text={}'.format(chid, txt))          
            line = aux_dec2utf8(resp)                              
            chck = json.loads(line)                                


            if chck['ok']:                                         

                uid = upds['result'][0]['update_id']               
                cmd = 'getUpdates'                                 
                urlopen(URL + cmd + '?offset={}'.format(uid + 1))  
        else:
            uid = upds['result'][0]['update_id']                   
            cmd = 'getUpdates'                                     
            urlopen(URL + cmd + '?offset={}'.format(uid + 1))      
    print('Waiting!')
    time.sleep(5)
