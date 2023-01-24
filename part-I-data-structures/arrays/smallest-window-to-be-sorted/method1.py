def main(S):
    # firste sort the S
    sort_S = sorted(S)
    l, r = None, None
    
    for i in range(len(S)):
        if S[i] != sort_S[i]:
            if not l:
                l = i
            else:
                r = i
    
    print((l,r))

if __name__ == "__main__":
    S = [1,6,5,2,9]
    main(S)    