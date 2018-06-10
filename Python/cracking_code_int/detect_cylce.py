"""
https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    '''
    Solution using a dict
    '''
    cur_node = head
    memo = {}
    while cur_node.next:
        if cur_node.data in memo:
            return True
        else:
            memo[cur_node.data] = cur_node.data
            cur_node = cur_node.next
    return False

def has_cylce_no_memo(head):
    '''
    Solution with no memory
    '''
    fast_node = head
    slow_node = head
    while fast_node.next:
        if fast_node.data == slow_node.data:
            return True
        else:
            fast_node = fast_node.next.next
            slow_node = slow_node.next
    return False