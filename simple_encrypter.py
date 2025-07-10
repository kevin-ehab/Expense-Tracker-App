import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
            '-', '_', '=', '+', '[', ']', '{', '}', r'\\', '|',
            ';', ':', "'", '"', ',', '<', '.', '>', '/', '?',
            '`', '~', ' ']

def method_1(password):
    keys = ["#6700122", "#4902192", "#9012841", "#7012279", "#1293804"]
    code = ""
    for letter in password:
        index = alphabet.index(letter)
        index *= 2
        index += 3
        code += str(index) + ","
    code = code[:-1]
    key = random.choice(keys)
    return {
        "code": code,
        "key": key
    }

def method_2(password):
    keys = ["#3091723", "#7209468", "#8912102", "#3082112", "#6478021"]
    code = ""
    for letter in password:
        index = alphabet.index(letter)
        index *= 4
        if index != 0:
            index -= 1
        code += str(index) + ","
    code = code[:-1]
    key = random.choice(keys)
    return {
        "code": code,
        "key": key
    }
def method_3(password):
    keys = ["#3040982", "#7203432", "#8912102", "#3082132", "#6478011"]
    code = ""
    for letter in password:
        index = alphabet.index(letter)
        index += 3
        code += str(index) + ","
    code = code[:-1]
    key = random.choice(keys)    
    return {
        "code": code,
        "key": key
    }
def method_4(password):
    keys = ["#6700211", "#4392190", "#9012941", "#7032289", "#1013804"]
    code = ""    
    for letter in password:
        index = alphabet.index(letter)
        if index % 2 != 0:
            index = index * 3
        else:
            index = index + 2
        code += str(index) + ","
    
    code = code.rstrip(",")
    key = random.choice(keys)

    return {
        "code": code,
        "key": key
    }
def method_5(password):
    keys = ["#5823941", "#7941203", "#1637289", "#9083120", "#4712384"]
    code = ""
    for letter in password:
        index = alphabet.index(letter)
        if index % 2 != 0:
            index += 2
        index *= 3
        code += str(index) + ","
    code = code[:-1]

    key = random.choice(keys)
    return {
        "code": code,
        "key": key
    }

def encrypt(password):
    methods = [method_1, method_2, method_3, method_4, method_5]
    method = random.choice(methods)
    return method(password)

def decrypt(code__key):
    code = code__key["code"]
    key = code__key["key"]
    decrypted = ""
    if key in ["#5823941", "#7941203", "#1637289", "#9083120", "#4712384"]:
        for i in code.split(","):
            index = int(int(i)/3)
            if index % 2 != 0:
                index -= 2
            letter = alphabet[index]
            decrypted += letter
    elif key in ["#6700211", "#4392190", "#9012941", "#7032289", "#1013804"]:
        for i in code.split(","):
            index = int(i)
            if index % 2 != 0:
                index = index // 3
            else:
                index = index - 2
            letter = alphabet[index]
            decrypted += letter
    elif key in ["#3040982", "#7203432", "#8912102", "#3082132", "#6478011"]:
        for i in code.split(","):
            if not i.strip():
                continue
            index = int(i) - 3
            if 0 <= index < len(alphabet):
                letter = alphabet[index]
                decrypted += letter
    elif key in ["#3091723", "#7209468", "#8912102", "#3082112", "#6478021"]:
        for i in code.split(","):
            index = int(i)
            if index != 0:
                index += 1
            index = int(index / 4)
            letter = alphabet[index]
            decrypted += letter
    elif key in ["#6700122", "#4902192", "#9012841", "#7012279", "#1293804"]:
        for i in code.split(","):
            index = int(i)-3
            index = int(index / 2)
            letter = alphabet[index]
            decrypted += letter
    else:
        return "invalid"
    return decrypted