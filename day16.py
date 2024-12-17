def remove_snow(s: str) -> str:
    i = 1

    while i < len(s):
        prev_char = s[i - 1]

        if prev_char == s[i]:
            s = s[:i - 1] + s[i + 1:]
            i = 0

        i += 1

    return s 


if __name__ == "__main__":
    print(remove_snow("abbaca"))