def main(S):
    res = [0 for _ in range(len(S))]
    
    for i in range(len(S)):
        for j in range(i, len(S)):
            if S[j] < S[i]: res[i] += 1
    
    print(res)

if __name__ == "__main__":
    S= [ 3, 4, 9, 6, 1]
    main(S)