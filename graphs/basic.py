def min_subset_product(arr):
    if not arr:
        return 0
    n = len(arr)
    if n == 1:
        return arr[0]
    max_neg = float('-inf')
    min_pos = float('inf')
    count_neg = count_zero = 0
    product = 1
    for num in arr:
        if num == 0:
            count_zero += 1
            continue
        if num < 0:
            count_neg += 1
            max_neg = max(max_neg, num)
        else:
            min_pos = min(min_pos, num)
        product *= num

    if count_zero == n:
        return 0

    if count_neg == 0 and count_zero > 0:
        return 0

    if count_neg % 2 == 1:
        return product

    if count_neg > 0:
        return product // max_neg

    return min_pos

A = [ -1, -1, -2, 4, 3 ]
print("Produit minimum possible :", min_subset_product(A))
