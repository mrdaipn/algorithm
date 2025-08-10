from typing import List


class AlternativeString:

    def alternate(self, s: str) -> int:
        """
        Return the length of longest possible alternative string
        obtained by removing some of occurences of character in `s`
        """
        distinct_characters = self.distinct_chars(s)
        return self.max_length(distinct_characters, s)

    def distinct_chars(self, s: str) -> int:
        return set(s)

    def max_length(self, distinct_chars: List, s: str) -> int:
        max_length = 0
        for c1 in distinct_chars:
            for c2 in distinct_chars:
                if c1 != c2:
                    remain_str = self.remain_str(s, c1, c2)
                    if self.is_alternative_string(remain_str):
                        max_length = max(max_length, len(remain_str))

        return max_length

    def remain_str(self, s, c1, c2):
        if not s:
            return ""

        s1 = [c for c in s if c in [c1, c2]]
        return "".join(s1)

    def is_alternative_string(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                return False

        return True
