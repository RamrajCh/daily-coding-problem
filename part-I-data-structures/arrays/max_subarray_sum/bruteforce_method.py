def main(S):
    current_max = 0
    for i in range(len(S)-1):
        for j in range(i, len(S)):
            current_max = max(current_max, sum(S[i:j]))
    
    print(current_max)

if __name__ == "__main__":
    S = [-2,1,-3,4,-1,2,1,-5,4]
    main(S)