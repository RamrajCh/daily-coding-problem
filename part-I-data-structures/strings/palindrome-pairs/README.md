# Get Palindrome Pairs
## Problem Statement
Given a list of words, write a function to find all pairs of words which are palindromes of each other. The result should be a list of pairs of indices, where each pair represents the indices of the two words in the original list that are palindromes of each other.

## Examples

Input: `["code", "edoc", "da", "d"]`

Output: `[(0, 1), (2, 3)]`

Explanation: The first pair `(0, 1)` represents the words "code" and "edoc" which are palindromes of each other. The second pair `(2, 3)` represents the words "da" and "d" which are also palindromes of each other.

Input: `["hello", "olleh", "world", "dlrow"]`

Output: `[(0, 1), (2, 3)]`

Explanation: The first pair `(0, 1)` represents the words "hello" and "olleh" which are palindromes of each other. The second pair `(2, 3)` represents the words "world" and "dlrow" which are also palindromes of each other.