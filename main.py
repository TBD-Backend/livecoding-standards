sample = 321

# yoda conditions
if 321 == sample:
    print("hello")

# how we expect it
if sample == 321:
    print("hello")

example = lambda x: x + 4

coords = [ 2, 45, 45, 19 ]


print(*map(lambda x: x + 4, coords))
