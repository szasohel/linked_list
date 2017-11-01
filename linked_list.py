class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def get_length(list):
    # determine length of the list
    length_list = 0
    current_node = list
    current_node2 = list.next
    while current_node != None and current_node != current_node2:
        current_node = current_node.next
        if current_node2 != None:
            current_node2 = current_node2.next
        if current_node2 != None:
            current_node2 = current_node2.next
        length_list += 1

    # Check if the list is circular 
    if current_node == None:
        return length_list
    else:
        return "circular"

def question5(list, m):

    # check if m is integer
    if type(m) != int:
        return "Please enter an integer!"
    
    length_list = get_length(list)

    if length_list == "circular":
        return "Linked list is circular!"
        
    if length_list < m:
        return "Number entered is greater than the length of list!"
    
    # find mth element by traversing
    current_node = list
    for i in range(length_list - m):
        current_node = current_node.next
        
    return current_node.data

def test5():
    n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    
    print (question5(n1,3))


test5()
