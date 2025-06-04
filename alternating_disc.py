def sort_discs(discs):
    swapped = True

    while swapped:
        swapped = False

        # Left to right pass
        for i in range(len(discs) - 1):
            if discs[i] == 'D' and discs[i + 1] == 'L':
                discs[i], discs[i + 1] = discs[i + 1], discs[i]
                swapped = True

        # Right to left pass
        for i in range(len(discs) - 1, 0, -1):
            if discs[i - 1] == 'D' and discs[i] == 'L':
                discs[i - 1], discs[i] = discs[i], discs[i - 1]
                swapped = True

    return discs

discs = ['L', 'D', 'L', 'D', 'D', 'L']
sorted_discs = sort_discs(discs)
print(sorted_discs)
