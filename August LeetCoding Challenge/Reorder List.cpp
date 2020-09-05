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
    void reorderList(ListNode*& head) {
        if(head) {
            struct ListNode*p=(struct ListNode*)malloc(sizeof(struct ListNode));
            p=head;

            vector<struct ListNode*> v;
            int l,i;

            while(p!=NULL)
            {
                v.push_back(p);
                p=p->next;
            }

            l=v.size();
            p=head;

            for(i=0;i<l/2;i++)
            {
                if(i!=0)
                {
                    p->next=v[i];
                    p=p->next;
                }
                p->next=v[l-i-1];
                p=p->next;
            }

            if(l%2==1)
            {
                p->next=v[i];
                p=p->next;
            }
            p->next=NULL; 
        }
    }
};
