def read_input(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            content = [line.rstrip() for line in f.readlines()]
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None
