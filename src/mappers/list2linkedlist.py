from src.structures.listnode import ListNode


def to_linkedlist(lst):
    root = ListNode(None)
    pt = root

    for item in lst:
        pt.next = ListNode(item)
        pt = pt.next

    return root.next
