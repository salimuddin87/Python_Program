def calNthStep(R, G, Twin):
    probNth = 1.0
    T = R + G
    G1 = G
    R1 = R
    for i in range(Twin-1):
        probNth *= (float(G) / T)
        G -= 1
        T -= 1
    probNth *= (float(R) / T)
    return probNth 

def calProbToWin(R, G):
    prob = 0.0
    if G & 1:
        Twin = G
    else:
        Twin = G + 1
    
    n = ( G / 2 ) + 1
    for i in range(n):
        prob += calNthStep(R, G, Twin)
        Twin -= 2
    print prob

if __name__ == '__main__':
    calProbToWin(2,1)
