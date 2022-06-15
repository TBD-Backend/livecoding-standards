# Identifying code smells
# https://refactoring.guru/refactoring

# what is the purpose of these variables?
# ❌
a = 234
b = 34324
z = 42254
# I know what this is for!
# ✅
card_padding = 234


def draw_boxes(x, y):
    # do something
    return


# where do these numbers come from?
# magic numbers are bad! ❌
draw_boxes(x=3, y=3)
