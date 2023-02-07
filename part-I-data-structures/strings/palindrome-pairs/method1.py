def is_palindrome(word):
    return word == word[::-1]

def main(S):
    pairs = []
    for i in range(len(S)-1):
        for j in range(1, len(S)):
            if i == j: continue
            word = S[i] + S[j]
            if is_palindrome(word):
                pairs.append((i,j))
    print(pairs)

if __name__ == "__main__":
    S = ["code", "edoc", "da", "d"]
    main(S)