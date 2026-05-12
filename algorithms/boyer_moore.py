from . import StringSearchAlgorithm


class BoyerMoore(StringSearchAlgorithm):

    def search(self, text: str, pattern: str) -> int:
        if not pattern or not text:
            return -1

        m = len(pattern)
        n = len(text)

        if m > n:
            return -1

        bad_char = {}
        for i in range(m):
            bad_char[pattern[i]] = i

        shift = 0

        while shift <= n - m:
            j = m - 1

            while j >= 0 and pattern[j] == text[shift + j]:
                j -= 1

            if j < 0:
                return shift

            bad_index = bad_char.get(text[shift + j], -1)
            shift += max(1, j - bad_index)

        return -1
