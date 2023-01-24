def main(S):
    # initialize
    left, right = 0, 0
    max_seen, min_seen = -float("inf"), float("inf")
    
    # first find left bound
    for j in range(len(S)-1, -1, -1):
        min_seen = min(min_seen, S[j])
        if S[j] > min_seen:
            left = j
    
    # then find right bound
    for i in range(len(S)):
        max_seen = max(max_seen, S[i])
        if S[i] < max_seen:
            right = i
            
    print ((left, right))

if __name__ == "__main__":
    S = [1,3,4,2,5]
    main(S)  