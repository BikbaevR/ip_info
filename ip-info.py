from twoip import TwoIP
import http.client

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ip = ((conn.getresponse().read()).decode())
twoip = TwoIP(key = None)

ip_info = twoip.geo(ip=str(ip))


for name, address in ip_info.items():
    
    if(name == 'country_code'):
        continue
    elif(name == 'country_rus'):
        continue
    elif(name == 'country_ua'):
        continue
    elif(name == 'region_rus'):
        continue
    elif(name == 'region_ua'):
        continue
    elif(name == 'city_rus'):
        continue
    elif(name == 'city_ua'):
        continue
    elif(name == 'zip_code'):
        continue
    print(' {0} : {1}'.format(name, address))


    