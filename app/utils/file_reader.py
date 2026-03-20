def stream_file(file):
    for line in file.file:
        yield line.decode("utf-8", errors="ignore")
