'''
    duplicates = ['a', 'a', 'g', 't', 't', 'x', 'x', 'x']
    remove_dups(duplicates)
    3, index of the last unique value: 'x'
    duplicates = ['a', 'g', 't', 'x' 'a', 'x', 't', 'x']
'''

def move_duplicates(dupe_list):
  unique_idx = 0
  for i in range(len(dupe_list) - 1):
    if dupe_list[i] != dupe_list[i + 1]:
       print("What is temp?", dupe_list[i], "i", i)
       print("What is unique?", dupe_list[unique_idx], "unique", unique_idx)
       print("What is arr?", dupe_list)

       dupe_list[i], dupe_list[unique_idx] = dupe_list[unique_idx], dupe_list[i]
       print("What is dupe_list[i] -- Post Change?", dupe_list[i], "i", i)
       print("What is dupe_list[unique] -- Post Change?", dupe_list[unique_idx], "unique", unique_idx)
       print("What is arr dupe_list -- Post Change?", dupe_list)
       print("---------------------------------------------------------", dupe_list)
       unique_idx += 1
  dupe_list[unique_idx], dupe_list[len(dupe_list) - 1] = dupe_list[len(dupe_list) - 1], dupe_list[unique_idx]
  print("-----$--------$---------$-----------$-------$------$----$", dupe_list)

  return unique_idx
'''

def move_duplicates(dupe_list):
    # how would you find if there are duplicates?
    unique = 0 
    for i in range(len(dupe_list)-1):
        if dupe_list[i] != dupe_list[i+1]:
           temp = dupe_list[i]
           print("What is temp?", dupe_list[i], "i", i)
           print("What is unique?", dupe_list[unique], "unique", unique)
           print("What is arr?", dupe_list)

           dupe_list[i] = dupe_list[unique]  
           dupe_list[unique] = temp
           print("What is dupe_list[i] -- Post Change?", dupe_list[i], "i", i)
           print("What is dupe_list[unique] -- Post Change?", dupe_list[unique], "unique", unique)
           print("What is arr dupe_list -- Post Change?", dupe_list)
           print("---------------------------------------------------------", dupe_list)
        
           unique += 1

    temp2 = dupe_list[len(dupe_list)-1]  
    dupe_list[len(dupe_list)-1] = dupe_list[unique]  
    dupe_list[unique] = temp2  
    return unique
        
'''

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']), 3, move_duplicates(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']) == 3))

print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']), 4, move_duplicates(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(move_duplicates([13, 13, 13, 13, 13, 42]), 1, move_duplicates([13, 13, 13, 13, 13, 42]) == 1))
