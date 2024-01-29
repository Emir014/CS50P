filename = input("File name: ").strip().lower()
dot_index = filename.rfind(".")
# If there are no "." characters:
if dot_index == -1:
    filename = ""
extension = filename[dot_index + 1:]
if extension == "jpg":
    extension = "jpeg"

match extension:
    case "gif" | "jpeg" | "png":
        prefix = "image/"
    case "pdf" | "zip":
        prefix = "application/"
    case "txt":
        prefix = "text/plain"
        extension = ""
    case _:
        prefix = "application/"
        extension = "octet-stream"

print(prefix + extension)
