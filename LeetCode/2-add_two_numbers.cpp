/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode *head = nullptr, *tail = nullptr;
        int carry = 0;

        while (l1 && l2) {
            int tmp = carry + l1->val + l2->val;
            ListNode* node = new ListNode(tmp % 10);
            if (head == nullptr) {
                head = tail = node;
            } else {
                tail->next = node;
                tail = node;
            }
            carry = tmp / 10;
            l1 = l1->next;
            l2 = l2->next;
        }

        if (l2)
            l1 = l2;

        while (l1) {
            int tmp = carry + l1->val;
            ListNode* node = new ListNode(tmp % 10);
            if (head == nullptr) {
                head = tail = node;
            } else {
                tail->next = node;
                tail = node;
            }
            carry = tmp / 10;
            l1 = l1->next;
        }

        while (carry > 0) {
            int tmp = carry;
            ListNode* node = new ListNode(tmp % 10);
            if (head == nullptr) {
                head = tail = node;
            } else {
                tail->next = node;
                tail = node;
            }
            carry = tmp / 10;
        }

        return head;
    }
};
