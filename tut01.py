x = {"A":550, "B":525, "C":595, "D":545, "E":565, "F":580, "G":625, "H":495, "I":660, "J":570, "K":540}

print(sorted( x.items(), key = lambda x : x[1] ))

print(x.values())