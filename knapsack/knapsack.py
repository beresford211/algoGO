from util import Loot

def knapsack(loot, weight_limit):
  grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]
  for row, item in enumerate(loot):
    row = row + 1
    for col in range(weight_limit + 1):
      weight_capacity = col
      previous = grid[row - 1][weight_capacity]
      if item.weight <= weight_capacity:
        item_weight = item.weight
        item_value = item.value
        previous_best_less_item_weight = grid[row -1][weight_capacity - item_weight]
        capacity_value_with_item = item_value + previous_best_less_item_weight
        capacity_value_without_item = grid[row-1][col]
        grid[row][col] = max(capacity_value_with_item, capacity_value_without_item)
      else:
        grid[row][col] = grid[row-1][col]
  
  return grid[-1][-1]

def knapsack(loot, weight_limit):
  # Here we want to create the col, we create the columns by taking the weight limit +!
  # here we want to create the rows by taking the len of the loot arr + 1
  grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]
  # here we have a row and item and we want to enumerate
  for row, item in enumerate(loot):
    # we always want to skip the first row as this should be zeros
    row = row + 1
    for col in range(weight_limit + 1):
      weight_capacity = col # weight_limit
      previous = grid[row -1][weight_capacity]
      if item.weight <= weight_capacity:
        item_weight = item.weight 
        item_value = item.value
        previous_best_less_item_weight = grid[row -1][weight_capacity - item_weight]
        capacity_value_with_item = item_value + previous_best_less_item_weight
        capacity_value_without_item = grid[row -1][col]
        grid[row][col] = max(capacity_value_with_item, capacity_value_without_item)
      else:
        grid[row][col] = grid[row-1][col]


def knapsack(loot, weight_limit):
    grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]

    for row, item in enumerate(loot):
        row = row + 1
        for col in range(weight_limit + 1):
            weight_capacity = col

    for row, item in enumerate(loot):
        # we need to add one so we don't zero index
        row = row + 1
        # we now want to iterate through the columns
        for col in range(weight_limit + 1):

            weight_capacity = col
            # we need to check what the previous highest value is
            # we can do this by going back onw row 
            # and we seeing what we could handle for the weight capacity there 
            previous = grid[row -1][weight_capacity]

            # if the weight of the item is less than the weight_capacity then we can potentially add it
            if item.weight <= weight_capacity:
                item_weight = item.weight
                item_value = item.value
                # what is the 
                previous_best_less_item_weight = grid[row -1][weight_capacity - item_weight]
                # if we add the value 
                capacity_value_with_item = item_value + previous_best_less_item_weight

   
available_loot = [Loot("Clock", 3, 8), Loot("Vase", 4, 12), Loot("Diamond", 1, 7)]
weight_capacity = 4
best_combo = knapsack(available_loot, weight_capacity)
print("The ideal loot given capacity {0} is\n{1}".format(weight_capacity, best_combo))r
