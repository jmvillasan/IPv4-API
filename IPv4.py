from requests import get


#Getting the public IPv4 Address
print (get('https://api.ipify.org').text)