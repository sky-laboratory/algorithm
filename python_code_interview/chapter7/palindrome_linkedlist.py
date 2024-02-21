class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def parlindrome_linkedlist(head: ListNode) -> bool:
#     q: list = []
    
#     if not head:
#         return True
    
#     node = head
#     while node is not None:
#         q.append(node.val)
#         node = node.next
    
#     while len(q) > 1:
#         if q.pop() != q.pop(0):
#             return False
    
#     return True

# from collections import deque
# def parlindrome_linkedlist(head: ListNode) -> bool:
#     q = deque()
    
#     if not head:
#         return True
    
#     node = head
#     while node is not None:
#         q.append(node.val)
#         node = node.next
    
#     while len(q) > 1:
#         if q.popleft() != q.pop():
#             return False
    
#     return True

def parlindrome_linkedlist(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    
    # 런너를 이용해 역순 연결 리스트 구성함
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next 
    
    return not rev


# 연결 리스트 노드를 생성합니다.
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

# 노드를 연결합니다.
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# 함수를 실행하여 결과를 확인합니다.
print(parlindrome_linkedlist(node1))  # 출력: True