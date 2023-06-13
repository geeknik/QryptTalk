import socks

def create_tor_socket():
    tor_socket = socks.socksocket()
    tor_socket.set_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    return tor_socket
