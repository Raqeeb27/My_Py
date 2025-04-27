import magic

def get_file_type(file_path):
    mime = magic.Magic(mime=True)
    return mime.from_file(file_path)

file_path = "example.txt"
file_type = get_file_type(file_path)
print("File type:", file_type)
