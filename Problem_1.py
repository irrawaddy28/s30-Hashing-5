'''
269 Alien Dictionary
https://leetcode.com/problems/alien-dictionary/description/

There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.


Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Solution:
1. Topological Sort + Hashing
First, we create a graph (adjacency list) by comparing a pair of adjacent words in the input word list. We traverse the two words character by character until the first char mismatch. When that happens, we note down character precedence in the adjacency list.
eg. words = ["wrt","wrf","er","ett","rftt"]
pair 1: word1 = wrt, word2 = wrf
adj_list = {t: [f]}

pair 2: word1 = wrf, word2 = er
adj_list = {t: [f], w: [e]}
.
.
.

Why should we stop at first char mismatch? Why not consider 2nd or 3rd char mismatches?
Consider the two lexicographically ordered strings
first = 'acdeb'
second = 'adbec'

The 1st mismatch (c != d) is at index 1. This implies that c comes before d in the English language alphabet ordering.

The 2nd mismatch (d != b) is at index 2. Does this imply that d comes before b in the English language alphabet ordering? No.

Coming back to the problem, from the graph, we count the incoming edges (indegrees) and start BFS with nodes having zero indegree. As we process, we append characters to the result and reduce indegrees of neighbors.
https://youtu.be/gYpcp_e1rXM?t=1796

Let N = no. of words in the input list 'words' and K = avg length of word in the input list
TC: O(NK), SC: O(1)

'''
from typing import List
from collections import defaultdict, deque

def alienOrder(words: List[str]) -> str:
    def build_graph(words):
        nonlocal h
        N = len(words)
        for i in range(N-1):
            first, m = words[i], len(words[i])
            second, n = words[i+1], len(words[i+1])
            if first.startswith(second) and m > n:
                h = {}
                return

            i1, i2 = 0, 0
            while i1 < m and i2 < n:
                c1 = first[i1]
                c2 = second[i2]
                if c1 == c2:
                    i1 += 1
                    i2 += 1
                    continue
                h[c1].add(c2)
                indegrees[ord(c2) - ord('a')] += 1
                i1 += 1
                i2 += 1
                break

    indegrees = [0]*26
    h = defaultdict(set)
    build_graph(words)
    if len(h) == 0:
        return ""
    q = deque()
    for k in h.keys():
        index = ord(k) - ord('a')
        if indegrees[index] == 0:
            q.append(k)

    order = ""
    while q:
        curr = q.popleft()
        order += curr
        all_chars = h[curr]
        if not all_chars:
            continue
        for c in all_chars:
            index = ord(c) - ord('a')
            indegrees[index] -= 1
            if indegrees[index] == 0:
                q.append(c)

    if len(order) != len(h):
        return ""
    return order


def run_alienOrder():
    tests = [(["wrt","wrf","er","ett","rftt"], "wertf"),
             (["wrt","wrf","er","ett","rfttz"], "wertf"),
             (["z","x"], "zx"),
             (["z","x","z"], "")]
    for test in tests:
        words, ans = test[0], test[1]
        print(f"\nwords = {words}")
        alphabet = alienOrder(words)
        print(f"alphabet = {alphabet}")
        success = (ans == alphabet)
        print(f"Pass: {success}")
        if not success:
            print("Failed")
            return

run_alienOrder()
