def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False

    difference_count = 0

    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            difference_count += 1

        if difference_count > 1:
            return False

    return difference_count == 1


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))