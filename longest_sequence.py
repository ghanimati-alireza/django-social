
def longest_sequence(list: list) -> int:
    longest_sequence_length = 0
    sequence_length = 0
    for num in list:
        if num - 1 not in list and num + 1 in list:
            sequence_length += 1
        elif num - 1 in list and num + 1 in list:
            sequence_length += 1
        elif num - 1 in list and num + 1 not in list:
            sequence_length += 1
            longest_sequence_length = max(sequence_length, longest_sequence_length)
            sequence_length = 0
        elif num - 1 not in list and num + 1 not in list:
            continue
    return longest_sequence_length








original_list = input().split()
int_list = [int(i) for i in original_list]
int_list.sort()
print(longest_sequence(int_list))