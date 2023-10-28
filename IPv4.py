import socket
from requests import get


def ipv4_to_ipv6(ipv4_address):
    try:
        ipv4_packed = socket.inet_pton(socket.AF_INET, ipv4_address)
        ipv4_hex = ipv4_packed.hex()
        ipv6_address = f'::ffff:{ipv4_hex[:4]}:{ipv4_hex[4:]}'
        return ipv6_address
    except socket.error:
        return None

ipv4_address = (get('https://api.ipify.org').text)
ipv6_address = ipv4_to_ipv6(ipv4_address) 

if ipv6_address:
    print(f"IPv4 is: {ipv4_address}")
    print(f"IPv6 equivalency is: {ipv6_address}")
else:
    print("Invalid IPv4 address provided.")