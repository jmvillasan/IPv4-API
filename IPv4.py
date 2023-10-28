import socket
from requests import get


# user defined function para sa pag convert from IPv4 to IPv6
def ipv4_to_ipv6(ipv4_address):
    # try-catch block para sa error handling
    try:
        # ivalidate kung tama yung IPv4
        ipv4_packed = socket.inet_pton(socket.AF_INET, ipv4_address)
        # convert IPv4 to hexadecimals
        ipv4_hex = ipv4_packed.hex()
        # sepparate yung 2nd last hexa pair at last hexa pair using colon
        ipv6_address = f'::ffff:{ipv4_hex[:4]}:{ipv4_hex[4:]}'
        # return yung converted address
        return ipv6_address
    except socket.error:
        return None

# input yung icoconvert na IPv4 address
ipv4_address = (get('https://api.ipify.org').text)
# convert gamit yung ipv4_to_ipv6() function
ipv6_address = ipv4_to_ipv6(ipv4_address) 

if ipv6_address:
    # if successful, ioutput yung IPv6 address
    print(f"IPv4 is: {ipv4_address}")
    print(f"IPv6 equivalency is: {ipv6_address}")
else:
    #if failed, ewan ko nlng ahahaha!
    print("Invalid IPv4 address provided.")