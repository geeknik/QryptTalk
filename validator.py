import re

def validate_ip(ip):
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False
    return all(map(lambda x: 0 <= int(x) <= 255, ip.split(".")))

def validate_port(port):
    return 0 <= port <= 65535
