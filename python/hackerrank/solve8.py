def breakingRecords(scores):
  min_count = 0
  max_count = 0
  minimum = scores[0]
  maximum = scores[0]
  
  for score in scores:
    if score < minimum:
      minimum = score
      min_count += 1 
    elif score > maximum:
      maximum = score
      max_count += 1
      
  return max_count, min_count

print(breakingRecords([12,24,10,24]))