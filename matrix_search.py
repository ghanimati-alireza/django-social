
def search_2d_matrix(matrix: list, target: int) -> bool:
    if not matrix:
        return False

    left, right = 0, len(matrix) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1] and target in matrix[mid]:
            return True
        elif target < matrix[mid][0]:
            right = mid - 1
        else:
            left = mid + 1

    return False

matrix = input()
target = input()
print(search_2d_matrix(matrix, target))