class FileReader:

    @staticmethod
    def read(filepath: str) -> str:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Помилка при читанні файлу {filepath}: {e}")
            return ""
