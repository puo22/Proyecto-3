# runtime/files.py

def write_file(path, content):
    with open(path, "w") as f:
        f.write(str(content))
    print(f"[FILE] Archivo escrito: {path}")
    return True

def read_file(path):
    with open(path, "r") as f:
        data = f.read()
    print(f"[FILE] Archivo leído: {path}")
    return data
