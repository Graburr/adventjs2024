# 5 stars
def in_box(box):
    for line in box[1:-1]:
        pos_gift = line.find('*')

        if pos_gift > 0 and pos_gift < len(line) - 1:
            return True

    return False