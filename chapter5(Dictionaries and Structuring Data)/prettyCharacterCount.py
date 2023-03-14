import pprint

count = {}
message = 'A wise old fool thought he had all it took to become very arrogant and saucy well, he forgot we had a God and Jehovah is His name, can you guess that old fool?'

for i in message :
    count.setdefault(i,0)
    count[i] += 1
pprint.pprint(count)

