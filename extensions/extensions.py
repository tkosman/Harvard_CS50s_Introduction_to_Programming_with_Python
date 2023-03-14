ext = input("File name: ").strip().lower()
match ext[ext.rfind("."):]:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case __:
        print("application/octet-stream")
