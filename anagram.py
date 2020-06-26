l1 = ["tar", "State", "rat", "art", "Taste", "dream"]


def check_anagram(l1):

    list2 = []
    for word in l1:
        list1 = []
        for i in range(len(l1)):
            if sorted(word.lower()) == sorted(l1[i].lower()):
                list1.append(l1[i])
        list2.append(list1)

    anagrams = []
    for i in list2:
        if i not in anagrams:
            anagrams.append(i)
    return anagrams


print(check_anagram(l1))