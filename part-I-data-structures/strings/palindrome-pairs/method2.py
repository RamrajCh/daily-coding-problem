def is_palindrome(word):
    return word == word[::-1]

def main(S):
    d = {word : i for i, word in enumerate(S)}
    result = []
    
    for i in range(len(S)):
        for j in range(len(S)):
            prefix = S[i][:j]
            suffix = S[i][j:]
            res_prefix = prefix[::-1]
            res_suffix = suffix[::-1]
            
            if (is_palindrome(suffix) and res_prefix in d):
                if i != d[res_prefix]:
                    result.append((i, d[res_prefix]))
                    
            if (is_palindrome(prefix) and res_suffix in d):
                if i != d[res_suffix]:
                    result.append((d[res_suffix], i))
    
    print(result)

if __name__ == "__main__":
    S = ["code", "edoc", "da", "d"]
    main(S)