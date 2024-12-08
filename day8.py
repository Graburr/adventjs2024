# 5 stars
def draw_race(indices, length):
    result = []
    num_lanes = len(indices)

    for i, pos_reindeer in enumerate(indices):
        offset = " " * (num_lanes - i - 1)
        
        if pos_reindeer == 0:
            lane = "~" * length
        else:
            abs_pos = pos_reindeer if pos_reindeer > 0 else length + pos_reindeer
            lane = "~" * abs_pos + "r" + "~" * (length - abs_pos - 1)

        result.append(f"{offset}{lane} /{i + 1}")
    
    return '\n'.join(result)
