import base64


def get_chat_code():
    amount = 250
    li = "f62d0100"
    li_hexed = "02" + amount_to_hex(amount) + li
    return base64.b64encode(bytes.fromhex(li_hexed)).decode()


def amount_to_hex(amount):
    if amount < 16:
        return "0" + str(hex(amount).lstrip("0x").rstrip("L"))
    else:
        return hex(amount).lstrip("0x").rstrip("L")


if __name__ == '__main__':
    print("[&" + get_chat_code() + "]")
