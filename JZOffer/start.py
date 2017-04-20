
irr = 'DGBAECF'
lrr = 'ABCDEFG'

pos = [0] * len(irr)

for i in range(len(irr)):
    ch = irr[i]
    p = lrr.index(ch)
    pos[i] = p

print(pos[1:3])