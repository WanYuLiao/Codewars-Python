"""
Credit Card Mask
7kyu

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. 
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
"""
# Version 1
def maskify(cc):
    
    length = len(cc)
    if length <= 4: 
        return cc
    else:
        mask = ['#'] * (length-4)
        mask += cc[length-4:]
        mask_str = ''.join(mask)
        return mask_str

# Version 2
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

# Test Run
print (maskify('SF$SDfgsd2eA'))
print (maskify('123'))
