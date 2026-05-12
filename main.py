import timeit
from typing import Tuple

from algorithms.boyer_moore import BoyerMoore
from algorithms.kmp import KnuthMorrisPratt
from algorithms.rabin_karp import RabinKarp
from file_reader import FileReader


def extract_test_patterns(text: str, num_chars: int = 15) -> Tuple[str, str]:
    start_idx = len(text) // 3
    real_pattern = text[start_idx:start_idx + num_chars]

    fake_pattern = "ZZZZZZZZZZZZZZZ" if len(
        "ZZZZZZZZZZZZZZZ") <= len(real_pattern) else "ZZZZ"

    return real_pattern, fake_pattern


def benchmark_algorithm(text: str, pattern: str, algorithm, iterations: int = 1000) -> float:
    def func():
        return algorithm.search(text, pattern)

    time_seconds = timeit.timeit(func, number=iterations)
    return time_seconds * 1000 / iterations


def execute_test(pattern: str, text: str, algorithms: dict, iterations: int = 1000) -> dict:
    test_data = {}
    for algo_name, algo in algorithms.items():
        time_ms = benchmark_algorithm(text, pattern, algo, iterations)
        result_index = algo.search(text, pattern)
        test_data[algo_name] = {
            'time': time_ms,
            'found': result_index != -1
        }
    return test_data


def analyze_file(filename: str, text: str, real_pattern: str, fake_pattern: str) -> dict:
    algorithms = {
        "Boyer-Moore": BoyerMoore(),
        "KMP": KnuthMorrisPratt(),
        "Rabin-Karp": RabinKarp()
    }
    iterations = 1000

    real_test = execute_test(real_pattern, text, algorithms, iterations)
    fake_test = execute_test(fake_pattern, text, algorithms, iterations)

    return {
        'filename': filename,
        'text_size': len(text),
        'real_pattern': real_pattern,
        'fake_pattern': fake_pattern,
        'real_test': real_test,
        'fake_test': fake_test,
    }


def main():
    text1 = FileReader.read("data/article1.txt")
    text2 = FileReader.read("data/article2.txt")

    if not text1 or not text2:
        print("Помилка: Не вдалося прочитати файли")
        return

    real1, fake1 = extract_test_patterns(text1)
    real2, fake2 = extract_test_patterns(text2)

    result1 = analyze_file("article1.txt", text1, real1, fake1)
    result2 = analyze_file("article2.txt", text2, real2, fake2)

    for result in (result1, result2):
        print(f"\n{result['filename']} ({result['text_size']} characters)")
        for test_name, test_data in [("Real substring", result['real_test']), ("Fake substring", result['fake_test'])]:
            print(f"  {test_name}:")
            for algo, data in test_data.items():
                print(f"    {algo}: {data['time']:.6f} ms")


if __name__ == "__main__":
    main()
