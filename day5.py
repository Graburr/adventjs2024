# 5 stars
def organizeShoes(shoes):
    shoes_shorted = {}

    for shoe in shoes:
        if not shoes_shorted[shoe["size"]]:
            shoes_shorted[shoe["size"]] = [["I", 0], ["R", 0]]
        
        if shoe["type"] == "I":
            shoes_shorted[shoe["size"]][0][1] += 1
        else:
            shoes_shorted[shoe["size"]][1][1] += 1
    
    result = []

    for size, pairs in shoes_shorted.items(): 
        num_pairs = min(pairs[0][1], pairs[1][1])
        result.extend(size * num_pairs)
                
    return result

