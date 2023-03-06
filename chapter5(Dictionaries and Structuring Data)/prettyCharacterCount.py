import pprint

messsage = 'It is going to be great today Jesus christ is already here, well I am going to use this method to build one of the greatest companies this world can ever dream of, it will only be to the srvice of God purposes on earth with $5 trillion of Dollars in Value'

count = {}
for character in messsage:
    count.setdefault(character, 0)
    count[character] += 1
pprint.pprint(count)