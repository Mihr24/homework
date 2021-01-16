def Soundex(A: str):
    soundex_code = A[0].upper()
    i = 1
    F = [1] * 6
    while i < len(A) and len(soundex_code) < 4:
        if A[i] in "bfpv" and F[0]:
            soundex_code += "1"
            F = [1] * 6
            F[0] = 0
        elif A[i] in "cgjkqsxz" and F[1]:
            soundex_code += "2"
            F = [1] * 6
            F[1] = 0
        elif A[i] in "dt" and F[2]:
            soundex_code += "3"
            F = [1] * 6
            F[2] = 0
        elif A[i] in "l" and F[3]:
            soundex_code += "4"
            F = [1] * 6
            F[3] = 0
        elif A[i] in "mn" and F[4]:
            soundex_code += "5"
            F = [1] * 6
            F[4] = 0
        elif A[i] == "r" and F[5]:
            soundex_code += "6"
            F = [1] * 6
            F[5] = 0
        else:
            F = [1] * 6
        i += 1
    while not (len(soundex_code) == 4):
        soundex_code += "0"
    return soundex_code


def levenstein(A: str, B: str, ):
    F = [[(i + j) if i * j == 0 else 0 for j in range(len(B) + 1)]
         for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
    return F[len(A)][len(B)]
