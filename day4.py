# 5 stars
def createXmasTree(height, ornament):
  num_ornamenta = 1
  tree = ""

  for i in range(height - 1, -1, -1):
    tree = "_" * i + ornament * num_ornaments + "_" * i + "\n"
    nun_ornaments += 2

  base = "_" * (height - 1) + "#" + "_" * (height - 1)
  tree += base + "\n" + base
  return tree
