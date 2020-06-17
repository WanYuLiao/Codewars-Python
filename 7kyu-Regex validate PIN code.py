"""
Regex validate PIN code Ver.1
7kyu

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False

"""
# Version 1
def validate_pin(pin):
    #return true or false
    pin = str(pin)
    if sum(c in '1234567890' for c in pin) == 4 or sum(c in '1234567890' for c in pin) == 6:
        if sum(c in '1234567890' for c in pin) == len(pin):
            return True
        return False
    else:
        return False

# Version 2
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# Test Run
print (validate_pin('123445'))
print (validate_pin('1.23445'))
print (validate_pin('13445'))


