from kademlia.network import Server
from secure_deletion import secure_delete

class SecureForgetfulStorage(Server.storage_class):
    def __setitem__(self, key, value):
        if key in self:
            secure_delete(self[key])
        super().__setitem__(key, value)

    def __delitem__(self, key):
        secure_delete(self[key])
        super().__delitem__(key)

def start_dht_node(port):
    dht_node = Server(storage=SecureForgetfulStorage())
    dht_node.listen(port)
    return dht_node
