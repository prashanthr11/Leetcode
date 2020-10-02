/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(head) {
            auto odd = new ListNode();
            auto even = new ListNode();
            auto x = odd;
            auto y = even;
            int cnt = 1;

            auto tmp = head;
            while (tmp) {
                if (cnt % 2) {
                    auto x2 = new ListNode(tmp -> val);
                    odd -> next = x2;
                    odd = odd -> next;
                }
                else {
                    auto x2 = new ListNode(tmp -> val);
                    even -> next = x2;
                    even = even -> next;
                }
                ++cnt;
                tmp = tmp -> next;
            }
            x = x -> next;
            head = x;
            while (x -> next)
                x = x -> next;

            x -> next = y -> next;
        }
        return head;
    }
};
