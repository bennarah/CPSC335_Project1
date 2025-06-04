def sort_discs(discs):
    swap_count = 0
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(discs) - 1):
            if discs[i] == 'D' and discs[i + 1] == 'L':
                discs[i], discs[i + 1] = discs[i + 1], discs[i]
                swapped = True
                swap_count += 1

        for i in range(len(discs) - 1, 0, -1):
            if discs[i - 1] == 'D' and discs[i] == 'L':
                discs[i - 1], discs[i] = discs[i], discs[i - 1]
                swapped = True
                swap_count += 1

    return discs, swap_count

final_discs, swaps = sort_discs(['L', 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L',
 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L', 'D', 'L', 'D'])
print("Final order:", final_discs)
print("Total swaps:", swaps)
