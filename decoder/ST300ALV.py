

def decode(msg):
    list_protocol = msg.split(';')
    data_decode = {
        "HDR": list_protocol[0],
        "DEV_ID": list_protocol[1],
    }

    return data_decode
