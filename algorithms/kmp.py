from . import StringSearchAlgorithm


class KnuthMorrisPratt(StringSearchAlgorithm):

    def search(self, text: str, pattern: str) -> int:
        if not pattern or not text:
            return -1

        m = len(pattern)
        n = len(text)

        if m > n:
            return -1

        lps = [0] * m
        prev = 0

        for i in range(1, m):
            while prev > 0 and pattern[i] != pattern[prev]:
                prev = lps[prev - 1]

            if pattern[i] == pattern[prev]:
                prev += 1

            lps[i] = prev

        j = 0
        for i in range(n):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]

            if text[i] == pattern[j]:
                j += 1

            if j == m:
                return i - m + 1

        return -1
