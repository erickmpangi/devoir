import sys

# Lecture de l'entrée standard
input = sys.stdin.read
data = input().splitlines()

TC = int(data[0])

for k in range(1, TC + 1):
    arr = list(map(int, data[k].split()))
    n = len(arr)
    
    # Implémentation du tri fusion avec comptage dans le corps principal
    temp = [0] * n
    count = 0
    size = 1

    while size < n:
        left = 0
        while left < n:
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                i = left
                j = mid + 1
                k_temp = left
                while i <= mid and j <= right:
                    if arr[i] <= arr[j]:
                        temp[k_temp] = arr[i]
                        i += 1
                    else:
                        temp[k_temp] = arr[j]
                        count += (mid - i + 1)  # Toutes les inversions ici
                        j += 1
                    k_temp += 1

                while i <= mid:
                    temp[k_temp] = arr[i]
                    i += 1
                    k_temp += 1
                while j <= right:
                    temp[k_temp] = arr[j]
                    j += 1
                    k_temp += 1

                for i in range(left, right + 1):
                    arr[i] = temp[i]

            left += 2 * size
        size *= 2

    print(count)
