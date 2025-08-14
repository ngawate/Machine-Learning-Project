def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")

# Example usage
if __name__ == "__main__":
    path = input("Enter the file path: ")
    data = read_file(path)
    if data is not None:
        print("File content:\n", data)