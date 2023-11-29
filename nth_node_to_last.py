"""
 * Dada una lista enlazada simple y un valor N, devuelve el nodo N empezando por el final
 *
 * Ejemplo:
 *  Input: 1->2->4->6, 2
 *  Output: 4
"""

from singleLinkedList import Node

class nhNode:
    def find_nth_node_from_end(self, head, n):
        slow_ptr = head
        fast_ptr = head
        
        for _ in range(n):
            if not fast_ptr:
                return None
            fast_ptr = fast_ptr.next_node
        
        while fast_ptr:
            slow_ptr = slow_ptr.next_node
            fast_ptr = fast_ptr.next_node
        
        return slow_ptr
