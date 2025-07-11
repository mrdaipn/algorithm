from typing import Counter


def sherlock_string(s: str) -> str:
    char_counts = Counter(s)
    frequencies_count = Counter(char_counts.values())

    if len(frequencies_count) == 1:
        return "YES"

    if len(frequencies_count) > 2:
        return "NO"

    (freq1, count1), (freq2, count2) = frequencies_count.items()

    if (count1 == 1 and (freq1 - 1 == freq2 or freq1 == 1)) or (
        count2 == 1 and (freq2 - 1 == freq1 or freq2 == 1)
    ):
        return "YES"

    return "NO"
