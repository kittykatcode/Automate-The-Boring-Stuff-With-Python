import pprint

message = ' its a lovely day today, what else can we do , So terribly worried about everythin whats going n have no fucking clue'

count= {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] +1

pprint.pprint(count)
