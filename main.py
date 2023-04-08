import base64


#defining various killing proof
fractal = "4f3f0100"
#w1
vale = "892f0100"
gorseval = "b72f0100"
sabetha = "a02f0100"
#w2
sloth = "8a2f0100"
matthias = "6f2f0100"
#w3
kc = "36340100"
xera = "5e340100"
#w4
carin = "ef3a0100"
Murssat = "8d390100"
samarog = "d7380100"
demios = "9e3a0100"
#w5
desmina = "e94f0100"
statue = "284f0100"
dhuum = "814e0100"
#w6
ca = "df590100"
twin = "1c5b0100"
qadim = "455a0100"
#w7
sabir = "86640100"
adina = "6e640100"
qadim2 = "27640100"

li = "f62d0100"
bone = "556e0100"

def get_chat_code(amount=250, kp=li):
    li_hexed = "02" + amount_to_hex(amount) + li
    return base64.b64encode(bytes.fromhex(li_hexed)).decode()


def amount_to_hex(amount):
    if amount < 16:
        return "0" + str(hex(amount).lstrip("0x").rstrip("L"))
    else:
        return hex(amount).lstrip("0x").rstrip("L")


if __name__ == '__main__':
    print("[&" + get_chat_code() + "]")
