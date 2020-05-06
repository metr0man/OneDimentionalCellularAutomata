import random

def genGrid(rule, seed, slide, colors, above, width, height, firstRow):
    # create grid var
    grid = []

    # generate first row
    row = []
    if firstRow == "random":
        random.seed(seed + str(slide))
        for i in range(width):
            row.append(random.randrange(colors))

    elif firstRow == "one":
        for i in range(width):
            row.append(0)
        row[int(width / 2)] = 1
    grid.append(row)

    # create rule lookup
    ruleStr = base10toN(rule, colors)
    for i in range(colors ** above - len(ruleStr)):
        ruleStr = "0" + ruleStr

    # generate the remaining rows
    for i in range(1, height):
        row = []
        for j in range(width):
            aboveStr = ""  # base c string of length a
            for k in range(j - int(above / 2), j + int(above / 2) + 1):
                if k < 0:
                    aboveStr += str(grid[i - 1][k % width])
                elif k >= width:
                    aboveStr += str(grid[i - 1][k % width])
                else:
                    aboveStr += str(grid[i - 1][k])

            # convert aboveStr to a base10 int
            aboveInt = 0  # in range [0, c^a)
            for k in range(above):
                aboveInt += (colors ** k) * int(aboveStr[above - 1 - k])
            aboveInt = colors ** above - aboveInt - 1

            row.append(int(ruleStr[aboveInt]))

        grid.append(row)

    return grid


def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string
