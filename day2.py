# 5 stars
def createFrame(names):
    max_word_length = max(len(name) for name in names)
    top_bottom_frame = '*' * (max_word_length + 4)
    result = f"{top_bottom_frame}\n"

    for name in names:
        result += f"* {name}" + (" " * (max_word_length - len(name))) + " *\n"

    result += top_bottom_frame
    return result