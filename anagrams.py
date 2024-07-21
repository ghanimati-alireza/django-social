
def group_anagrams(anagrams: list) -> list:
    anagrams_dict = {}

    for string in anagrams:
        letters = tuple(sorted(list(string)))
        if letters in anagrams_dict:
            anagrams_dict[letters].append(string)
            print(anagrams_dict)
        else:
            anagrams_dict[letters] = []
            anagrams_dict[letters].append(string)
            print(anagrams_dict)

    return list(anagrams_dict.values())


anagrams = input().split()
print(anagrams)
print(group_anagrams(anagrams))