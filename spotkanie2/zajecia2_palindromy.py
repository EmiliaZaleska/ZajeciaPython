def wer1(slowo):
    for i in range(len(slowo)):
        if slowo[i] != slowo[-1 - i]:
            return False
    return True


def wer2(slowo):
    return slowo == slowo[::-1]


dane = ['kajak', 'kobyłamamałybok', 'palindrom', 'anna', [1, 2, 1], [1, 2, 3], ['ok', 'ok1', 'ok']]
wersje = [wer1, wer2]
for funkcja in wersje:
    for slowo in dane:
        print("{0}: {1}".format(slowo, funkcja(slowo)))