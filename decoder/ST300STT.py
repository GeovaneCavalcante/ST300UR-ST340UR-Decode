

def decode(msg):
    list_protocol = msg.split(';')
    data_decode = {
        "HDR": list_protocol[0],
        "DEV_ID": list_protocol[1],
        "MODEL": list_protocol[2],
        "SW_VER": list_protocol[3],
        "DATE":  list_protocol[4],
        "TIME":  list_protocol[5],
        "CELL":  list_protocol[6],
        "LAT":  list_protocol[7],
        "LON":  list_protocol[8],
        "SPD":  list_protocol[9],
        "CRS":  list_protocol[10],
        "SATT":  list_protocol[11],
        "FIX":  list_protocol[12],
        "DIST":  list_protocol[13],
        "PWR_VOLT":  list_protocol[14],
        "I/O":  list_protocol[15],
        "MODE":  list_protocol[16],
        "MSG_NUM":  list_protocol[17],
        "H_METER":  list_protocol[18],
        "BCK_VOLT":  list_protocol[19],
        "MSG_TYPE":  list_protocol[20],
        "DID":  list_protocol[21],
        "DID_REG":  list_protocol[22],
        "CELL_ID":  list_protocol[23],
        "MCC":  list_protocol[24],
        "MNC":  list_protocol[25],
        "RX_LVL":  list_protocol[26],
        "LAC":  list_protocol[27],
        "TM_ADV":  list_protocol[28],
    }

    return data_decode
