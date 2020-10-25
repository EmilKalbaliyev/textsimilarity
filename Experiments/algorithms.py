from difflib import SequenceMatcher
from pyjarowinkler import distance
import Levenshtein as lev


def dl(seq1, seq2):
    oneago = None
    thisrow = list(range(1, len(seq2) + 1)) + [0]
    for x in range(len(seq1)):
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in range(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1]
                and seq1[x-1] == seq2[y] and seq1[x] != seq2[y]):
                thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
    return thisrow[len(seq2) - 1]
    
def lcs(a, b):

    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1]
            result = a[x-1] + result
            x -= 1
            y -= 1

    return result


def LCStr(X, Y):

    m = len(X)
    n = len(Y)
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if(i==m and j==n and LCSuff[i][j]==2):
                LCSuff[i - 1][j - 1] = 0
                LCSuff[i][j] = 0
            elif (i!=m and j!=n and LCSuff[i][j]==2 and LCSuff[i+1][j+1]!=3):
                LCSuff[i-1][j-1] = 0
                LCSuff[i][j] = 0
            elif(i==m and j==n and LCSuff[i][j]==1):
                LCSuff[i][j] = 0
            elif (i!=m and j!=n and LCSuff[i][j]==1 and LCSuff[i+1][j+1]!=2):
                LCSuff[i][j] = 0

    sum=[m]
    for i in range(m ):
        sum.append(0)
    res=0
    for i in range(m):
        for j in range(n + 1):
            sum[i]=sum[i]+ LCSuff[i][j]
        if(sum[i]>0):
            res=res+1
    return res / m * 100



def Ratcliff_Obershelp(a, b):
    return SequenceMatcher(None, a, b).ratio() *100

def Damerau_Levenshtein(X,Y):

    damerau = dl(X,Y)
    lens=len(X) + len(Y)
    return ((lens - damerau) / (lens)) *100

def Levenshtein(X,Y):
    return lev.ratio(X, Y)*100

def Jaro_Winkler(X,Y):
    return distance.get_jaro_distance(X, Y, winkler=True, scaling=0.1)*100

def Jaro(X,Y):
    return distance.get_jaro_distance(X, Y, winkler=False, scaling=0.1)*100

def LCSeq(X,Y):
    return 2. * len(lcs(X, Y)) / (len(X) + len(Y)) * 100

