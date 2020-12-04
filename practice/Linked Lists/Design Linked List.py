class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None
        self.ln = 0
        

    def get(self, idx: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.ln > idx:
            cnt = 0
            tmp = self.root
            while tmp:
                if cnt == idx:
                    return tmp.val
                cnt += 1
                tmp = tmp.next
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.root = ListNode(val, self.root)
        self.ln += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp = self.root
        if tmp:
            while tmp.next:
                tmp = tmp.next

            tmp.next = ListNode(val)
        else:
            self.root = ListNode(val)
        self.ln += 1

    def addAtIndex(self, idx: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if idx <= self.ln:
            if idx == 0:
                return self.addAtHead(val)
            if idx == self.ln:
                return self.addAtTail(val)
        
            cnt = 1
            tmp = self.root
            while cnt < idx:
                tmp = tmp.next
                cnt += 1
            tmp.next = ListNode(val, tmp.next)
            self.ln += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < self.ln:
            self.ln -= 1
            if index == 0:
                self.root = self.root.next
            else:
                cnt, tmp = 0, self.root
                while cnt < index - 1:
                    tmp = tmp.next
                    cnt += 1
                if tmp.next:
                    tmp.next = tmp.next.next
                else:
                    tmp.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
