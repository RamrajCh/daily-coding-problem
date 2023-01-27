def main(S):
    max_so_far = S[0]
    max_ending_here = S[0]
    
    for i in range(1, len(S)):
        max_ending_here = max(S[i], S[i] + max_ending_here)
        max_so_far = max(max_ending_here, max_so_far)
        
    print(max_so_far)

if __name__ == "__main__":
    S = [-2,1,-3,4,-1,2,1,-5,4]
    main(S)