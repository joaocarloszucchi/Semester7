count = 0
counttotal = 0
for a in range(1,7):
    d1 = a
    for b in range(1,7):
        d2 = b
        for c in range(1,7):
            d3 = c
            for d in range(1,7):
                d4 = d
                for e in range(1,7):
                    d5 = e
                    for f in range(1,7):
                        d6 = f
                        sum = d1 + d2 + d3 + d4 + d5 + d6
                        if sum == 18:
                            count += 1
                        counttotal += 1

print(count, counttotal)
print(count/counttotal)
