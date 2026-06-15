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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        //reaches the end
        if (list1 == nullptr){
            return list2;
        }
        if (list2 == nullptr){
            return list1;
        }

        //2 iterators one at the start of list1 one at the start of list2
        
        ListNode* curr1 = list1;
        ListNode* curr2 = list2;

        //curr2 is larger or equal
        if (curr2->val >= curr1->val){
            curr1->next = mergeTwoLists(curr1->next, curr2);
            return curr1;
            
        } else{ //curr1 is larger
            curr2->next = mergeTwoLists(curr2->next, curr1);
            return curr2;
        }

    }
};
