def disconnect_client():
    global connected, their_public_key, their_node_id
    connected = False
    if their_public_key:
        secure_delete(their_public_key)
    if their_node_id:
        secure_delete(their_node_id)
