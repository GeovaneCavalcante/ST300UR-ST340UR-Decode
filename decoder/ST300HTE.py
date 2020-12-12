

def decode(msg):
    list_protocol = msg.split(';')
    data_decode = {
        "HDR": list_protocol[0],
        "DEV_ID": list_protocol[1],
        "MODEL": list_protocol[2],
        "SW_VER": list_protocol[3],
        "DATE":  list_protocol[4],
        "TIME":  list_protocol[5],
        "DIST":  list_protocol[6],
        "PWR_VOLT":  list_protocol[7],
        "H_METER":  list_protocol[8],
        "BCK_VOLT":  list_protocol[9],
        "MSG_TYPE":  list_protocol[10],
        "TRAVEL_DIST":  list_protocol[11],
        "TRAVEL_TIME":  list_protocol[12],
        "TIME_STOP":  list_protocol[13],
        "TIME_MOVING":  list_protocol[14],
        "LAT_TRAVEL_ST":  list_protocol[15],
        "LON_TRAVEL_ST":  list_protocol[16],
        "LAT_TRAVEL_FI":  list_protocol[17],
        "LON_TRAVEL_FI":  list_protocol[18],
        "AVERAGE_SPD":  list_protocol[19],
        "MAX_SPD":  list_protocol[20],
        "TIME_OVER_SPD":  list_protocol[21],
        "TIME_ECO_UP":  list_protocol[22],
        "TIME_ECO_DOWN":  list_protocol[23],
        "TIME_ECO_INSIDE":  list_protocol[24],
        "TIME_OVER_RPM":  list_protocol[25],
        "TIME_DC":  list_protocol[26],
        "DRIVER_ID":  list_protocol[27],

    }
    return data_decode
