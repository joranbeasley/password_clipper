import hashlib,time
import pyperclip
VERSION = "0.0.1"
def create_password():
    return hashlib.md5(bytes(str(time.time()),"latin1") + b"Fake Password").hexdigest()[:22]+":"\
           +hashlib.md5(b"PW"+bytes(str(time.time()),'latin1')).hexdigest()[:18]

def create_and_copy_password():
    pw = create_password()
    pyperclip.copy(pw)
    print(pw)

if __name__ == "__main__":
    create_and_copy_password()