/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
  public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {

    // Create a set of nodes from list A
    HashSet<ListNode> aNodes = new HashSet<ListNode>();

    ListNode pointer = headA;

    while (pointer != null) {
      aNodes.Add(pointer);
      pointer = pointer.next;
    }

    // Iterate through list B until we find a node that exists in the set
    pointer = headB;

    while (pointer != null && !aNodes.Contains(pointer)) {
      pointer = pointer.next;
    }

    return pointer;
  }
}
