from collections import Counter

def is_anagram(string1, string2):
    return Counter(string1) == Counter(string2)

def main(string, word):
    res = []
    
    for i in range(len(string) - len(word) + 1):
        win = string[i:i+len(word)]
        if is_anagram(win, word):
            res.append(i)
            
    print(res)

if __name__ == "__main__":
    w = "ab"
    s = "abxaba"
    
    main(s,w)