'''
953 Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/description/

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.

Solution:
1. Hashing
First, we store each character's rank order in a hash map using the alien dictionary. Then we compare each pair of adjacent words in the inpur words array to check their order using the rank map. If any word comes later but should appear earlier, return false — else everything's good.
https://youtu.be/gYpcp_e1rXM?t=234
Time: O(NK), Space: O(1) (map size is fixed  at 26), K = avg len of word
'''
from typing import List
from collections import defaultdict

def isAlienSorted(words: List[str], order: str) -> bool:
    ''' Time: O(NK), Space: O(1) (map size is fixed  at 26), K = avg len of word '''
    def is_not_sorted(first, second):
        M, N = len(first), len(second)
        i, j = 0, 0
        while i < M and j < N:
            c1 = first[i]
            c2 = second[j]
            if c1 != c2:
                return h[c1] > h[c2]
            i += 1
            j += 1

        # At this point, all chars so far have matched. Hence, either the first
        # word is a prefix of the second word or vice-versa. If the first word
        # is a prefix, then we return False (meaning first word is smaller
        # and hence correctly appears before the second word).
        if M > N:
            return True # True = not sorted
        return False

    if not words:
        return True
    h = defaultdict(int)

    for i, c in enumerate(order):
        h[c] = i

    N = len(words)
    for i in range(N-1): # O(N)
        first = words[i]
        second = words[i+1]

        if is_not_sorted(first, second): # O(K)
            return False

    return True

def run_isAlienSorted():
    tests = [(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
             (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
             (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
    ]
    for test in tests:
        words, order, ans = test[0], test[1], test[2]
        print(f"\nwords = {words}")
        print(f"order = {order}")
        flag = isAlienSorted(words, order)
        success = (ans == flag)
        print(f"Pass: {success}")
        if not success:
            print("Failed")
            return

run_isAlienSorted()
