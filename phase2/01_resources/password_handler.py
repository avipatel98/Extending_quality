import hmac
import hashlib

# WARNING - this is code only for a course exercise and should not be used for
# passwords in the real world!

key = "super secret key which nobody knows"
sequence = "1234567890abcdefghijklmnopqrstuvwxyz"
password = b'$\xed\xb8v\x10\x1f\xe2\xa6\xc2\x0f\xaf[\x98|\xc7\x84l\xe1H\x02"\xed\xbf\xde\xd7>/;.\x9bI\xdf'

def hide_password(pw):
    return hmac.new(bytes(key, 'utf-8'), bytes(pw, 'utf-8'), hashlib.sha256).digest()

def check_password(sig, pw):
    return hmac.compare_digest(hide_password(pw), sig)

def try_all_the_codes():
    for c1 in sequence:
        for c2 in sequence:
            for c3 in sequence:
                for c4 in sequence:
                    if check_password(password,f"{c1}{c2}{c3}{c4}") == False:
                        continue
                    else:
                        return f"{c1}{c2}{c3}{c4}"

print(try_all_the_codes())