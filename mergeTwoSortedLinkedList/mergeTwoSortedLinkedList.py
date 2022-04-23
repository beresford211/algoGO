class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self, head_node = None):
    self.head = head_node

  def add(self, val):
    new_head = Node(val)
    new_head.next = self.head
    self.head = new_head
    
  def traverse(self):
    head = self.head
    print("Starting traversal from head")
    while head:
      print("visiting node: {0}".format(head.val))
      head = head.next
    print("Traversal complete")
    
  def size(self):
    node_count = 0
    current_node = self.head
    while current_node:
      node_count += 1
      current_node = current_node.next
    return node_count
  
  def __repr__(self):
    text = ''
    head = self.head
    while head:
      text += str(head.val) + ' -> '
      head = head.next
    return text

linked_list_a = LinkedList()
linked_list_b = LinkedList()
linked_list_a.add('z')
linked_list_a.add('x')
linked_list_a.add('c')
linked_list_a.add('a')
linked_list_b.add('u')
linked_list_b.add('g')
linked_list_b.add('b')


def merge(linked_list_a, linked_list_b):
    head = None
    leader = None
    if linked_list_a is None:
        return linked_list_a
    if linked_list_b is None:
        return linked_list_b

    ll1 = linked_list_a.head
    ll2 = linked_list_b.head

    while ll1 or ll2:
        if leader is None:
            templl1 = ll2.next
            templl2 = ll1.next

            if ll1.val < ll2.val:
                head = ll1
                leader = ll1
                ll2.next = None 

                leader.next = ll2
            else:
                head = ll2
                leader = ll2
                ll1.next = None
                leader.next = ll1       

            leader = leader.next
            ll1 = templl1
            ll2 = templl2
 

        if ll1 is not None and ll2 is None:
            templl1 = ll1.next        
            # set leader next to be the next node
            leader.next = ll1
            # set the next node to be the leader
            print("leader ll1 next", leader.next.val)
            leader = leader.next 
            ll1 = templl1
            continue

        elif ll2 is not None and ll1 is None:
            templl2 = ll2.next
            leader.next = ll2
            print("leader ll2.next", leader.next.val)
            leader = leader.next
            ll2 = templl2
            continue

        if ll1.val < ll2.val:
            templl1 = ll1.next        
            # set leader next to be the next node
            leader.next = ll1
            # set the next node to be the leader
            print("leader ll1 next", leader.next.val)
            leader = leader.next 
            ll1 = templl1
        else:
            templl2 = ll2.next
            leader.next = ll2
            print("leader ll2.next", leader.next.val)
            leader = leader.next
            ll2 = templl2



'''
    Things i learned from this 
        - Don't forget about the end of the list at one point one of the linked lists will be null and you want to operate until both of them are null. 
        Otherwise you won't be able to continously iterate
        - (you have to do a lot of magic if you want to do it in constant space (actually i don't think you really need to do this at all)
'''



merged_linked_list = merge(linked_list_a, linked_list_b)

print("Merged list should contain all nodes in sorted order: a -> b -> c -> g ->u -> x -> z")
print("Your function returned: {0}".format(merged_linked_list)) 
