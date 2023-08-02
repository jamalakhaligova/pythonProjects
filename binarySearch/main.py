def binary_search(l, target):
    # example l = [1, 3, 5, 7, 8] target is 1
    mid = len(l) // 2
    start, end = 0, (len(l) - 1)
    try:
        if l[mid] == target:
            print(f"Found")
            return mid + 1
        elif l[mid] > target:
            binary_search(l[:mid], target)
        elif l[mid] < target:
            binary_search(l[mid:], target)
    except RecursionError:
        print("not found")


print(binary_search([1, 3, 5, 7, 8], 1))
