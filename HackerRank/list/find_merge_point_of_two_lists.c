/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
int findMergeNode(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2)
{
    SinglyLinkedListNode *p1 = head1, *p2 = head2;

    while (true) {
        if (p1 == p2) {
            return p1->data;
        }
        p1 = p1->next;
        p2 = p2->next;
        if (!p1)
            p1 = head2;
        if (!p2)
            p2 = head1;
    }
}
