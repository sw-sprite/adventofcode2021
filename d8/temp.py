import sys

displays = [
    tuple(part.split() for part in display.split(" | "))
        for display in sys.stdin.readlines()
        if display.strip()
]

print("Part 1:",
    sum(
        sum(len(digit) in {2, 3, 4, 7} for digit in display[1])
            for display in displays
    )
)

#
total = 0
for digits, challenge in displays:
    d1 = set(list([ digit for digit in digits if len(digit) == 2 ][0]))
    d7 = set(list([ digit for digit in digits if len(digit) == 3 ][0]))
    d4 = set(list([ digit for digit in digits if len(digit) == 4 ][0]))
    d8 = set(list([ digit for digit in digits if len(digit) == 7 ][0]))
    d9 = set(list([ digit for digit in digits if len(digit) == 6 and len( set(list(digit)) - set.union(d4, d7) ) == 1 ][0]))
    d0 = set(list([ digit for digit in digits if len(digit) == 6 and set(list(digit)) != d9 and all(s in digit for s in d7) ][0]))
    d6 = set(list([ digit for digit in digits if len(digit) == 6 and set(list(digit)) != d9 and set(list(digit)) != d0 ][0]))
    d3 = set(list([ digit for digit in digits if len(digit) == 5 and all(s in digit for s in d7) ][0]))
    e = min(d8 - d9)
    d2 = set(list([ digit for digit in digits if len(digit) == 5 and e in digit ][0]))
    d5 = set(list([ digit for digit in digits if len(digit) == 5 and set(list(digit)) != d3 and set(list(digit)) != d2 ][0]))

    ds = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

    n = ""
    for digit in challenge:
        n = n + str(ds.index(set(list(digit))))

    total = total + int(n)

print("Part 2:", total)