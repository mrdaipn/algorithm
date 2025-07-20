from collections import Counter


def sherlock_and_anagram(s):
    """Sherlock and anagram problem"""
    substr_count = Counter()
    n = len(s)

    # Generate all substrings
    for length in range(1, n):
        for start in range(n - length + 1):
            substr = s[start : start + length]
            # Sort the substring to normalize anagrams
            key = "".join(sorted(substr))
            substr_count[key] += 1

    # Count pairs
    count = 0
    for v in substr_count.values():
        if v > 1:
            count += v * (v - 1) // 2
    return count
