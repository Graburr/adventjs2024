import re

def decode_filename(filename: str) -> str:
  return re.search(r"_([a-zA-Z_-]+\.\w+)", filename)[1]
