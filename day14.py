# 5 stars
def min_moves_to_stables(reindeer, stables):
  stables.sort()
  reindeer.sort()
  return sum(abs(stables[i] - reindeer[i]) for i in range(len(reindeer)))
