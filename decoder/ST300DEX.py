

def decode(msg):
    list_protocol = msg.split(';')
    data_decode = {
        "HDR": list_protocol[0],
        "DEV_ID": list_protocol[1],
        "VER": list_protocol[2],
        "LEN": list_protocol[3],
        "DATA":  list_protocol[4],
        "CHK_SUM":  list_protocol[5],
    }

    return data_decode
