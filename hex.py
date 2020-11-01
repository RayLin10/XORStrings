import sys
mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()
inp = open(inpfile).read()
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

keyLength = len(key)
output = ""

for index, letter in enumerate(inp):
    value = ord(letter) ^ ord(key[index % keyLength])
    output += chr(value)

print(output)