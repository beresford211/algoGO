
def zigZagLevelOrder(node):
   stack = [node]
   left_to_right = True

   while (len(stack) > 0):
       current_arr = []

       if left_to_right:
           for i in range(len(stack)):
               current_val = stack[i]
               current_arr.append(stack[i].val)
               if current_val.left:
                   current_arr.append(current_val.left)
               elif current_val.right:
                   current_arr.append(current_val.right)

       elif left_to_right == False:
           for i in range(len(stack)):
               current_val = stack[len(stack) - (i + 1)]
               current_arr.append(current_val.val)
               if current_val.left:
                   current_arr.append(current_val.left)
               elif current_val.right:
                   current_arr.append(current_val.right)
       left_to_right = not left_to_right
