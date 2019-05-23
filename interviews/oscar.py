# Enter your code here. Read input from STDIN. Print output to STDOUT

# input:
# -inf        4                         9                 inf
# <-----------|-------------------------|---------------->
#       true             false                true
# -inf                    6                               inf
# <-----------------------|------------------------------>
#             true                     false

# [(-inf, 4), (4, 9), (9, inf)] - A
# [(-inf, 6), (6, inf)] - B

# [(4, 9), (9, inf)] - A
# [(4, 6), (6, inf)] - B
# output -> (-inf, 4) = True

# [(6, 9), (9, inf)] - A
# [(6, inf)] - B
# output -> (-inf, 4) = True

# [(-inf, inf)] - A
# [(-inf, 3), (3, inf)] - B


# [(-inf, 3, T), (3, 3, F), (3, inf, T)] - A
# [(-inf, 6, T), (6, inf, F)] - B

# [(3, 3, F), (3, inf, T)] - A
# [(3, 6, T), (6, inf, F)] - B
# OUT => (-inf, 3, T)

# [(3, inf, T)] - A
# [(3, 6, T), (6, inf, F)] - B
# OUT => (3, 3, F)


# [(inf, inf)] - A
# [] - B


# output:
# -inf        4           6             9                 inf
# <-----------|-----------|-------------|---------------->
#      true       false        false         false

from math import inf


class Period(object):
    def __init__(self, start, end, status):
        """
        :param start int:
        :param end int:
        :param status bool:
        """
        self.start = start
        self.end = end
        self.status = status


def mergePeriods(periodA, periodB):
    merged = []
    while len(periodA) > 0 and len(periodB) > 0:
        a = periodA[0]
        b = periodB[0]
        segment = None
        if a.start == a.end:
            periodA = periodA[1:]
        elif b.start == b.end:
            periodB = periodB[1:]
        elif a.end < b.end:
            b.start = a.end
            segment = a
            segment.status = (a.status and b.status)
            periodA = periodA[1:]
        else:
            a.start = b.end
            segment = b
            segment.status = (a.status and b.status)
            periodB = periodB[1:]

        merged.append(segment)
    return merged


def testNormalInput():
    periodA = [
        Period(-inf, 4, True),
        Period(4, 9, False),
        Period(9, inf, True)
    ]
    periodB = [
        Period(-inf, 6, True),
        Period(6, inf, False)
    ]
    expected = [
        Period(-inf, 4, True),
        Period(4, 6, False),
        Period(6, 9, False),
        Period(9, inf, False)
    ]

    result = mergePeriods(periodA, periodB)

    for res in result:
        print(res.start, res.end, res.status)


def testPointAsInput():
    print("====")
    periodA = [
        Period(-inf, 3, True),
        Period(3, 3, False),
        Period(3, inf, True)
    ]
    periodB = [
        Period(-inf, 6, True),
        Period(6, inf, False)
    ]

    result = mergePeriods(periodA, periodB)

    for res in result:
        print(res.start, res.end, res.status)


testNormalInput()
testPointAsInput()
