def main(S):
    res = [
        sum(s < S[i] for s in S[i+1:])
        for i in range(len(S))
        ]
    
    print(res)

if __name__ == "__main__":
    S= [ 3, 4, 9, 6, 1]
    main(S)