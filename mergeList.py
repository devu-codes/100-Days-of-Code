# merge two sorted linked list

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
# 1->3->5->7
# 2->4->6->8

def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head2 
    
    merger, temp = Node(-1), Node(-1)

    if head1.val <= head2.val:
        merger = head1
        head1 = head1.next
    else:
        merger = head2
        head2 = head2.next
    temp = merger
    while head1 and head2:
        if head1.val <= head2.val:
            temp.next = head1
            temp = temp.next 
            head1 = head1.next 
        else:
            temp.next = head2 
            temp = temp.next
            head2 = head2.next

    temp.next = head1 if head1 else head2

    return merger