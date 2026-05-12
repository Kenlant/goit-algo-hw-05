from . import StringSearchAlgorithm


class RabinKarp(StringSearchAlgorithm):

    def __init__(self, prime: int = 101):
        self.prime = prime

    def search(self, text: str, pattern: str) -> int:
        if not pattern or not text:
            return -1

        m = len(pattern)
        n = len(text)

        if m > n:
            return -1

        base = 256
        pattern_hash = 0
        text_hash = 0
        h = 1

        for _ in range(m - 1):
            h = (h * base) % self.prime

        for i in range(m):
            pattern_hash = (base * pattern_hash + ord(pattern[i])) % self.prime
            text_hash = (base * text_hash + ord(text[i])) % self.prime

        for i in range(n - m + 1):
            if pattern_hash == text_hash:
                if text[i:i + m] == pattern:
                    return i

            if i < n - m:
                text_hash = (
                    base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % self.prime
                if text_hash < 0:
                    text_hash += self.prime

        return -1
