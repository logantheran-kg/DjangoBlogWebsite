s = 'BANANA'
# vowel = [A,E,I,O,U]
count = 0
j = int(0)


def minion_game(s):

    for idx, item in enumerate(s):
        j = idx

        while j <= len(s):
            print('{}'.format(s[idx:j]))
            j += 1

minion_game(s)