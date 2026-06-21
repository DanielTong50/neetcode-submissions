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
    bool hasCycle(ListNode* head) {
        if (head == nullptr || head->next == nullptr){
            return false;
        }
        ListNode* curr1 = head;
        ListNode* curr2 = head->next;

        while (curr2 != nullptr && curr2->next != nullptr){
            if (curr1 == curr2){ //if they ever reach
                return true;
            } else{
                curr1 = curr1->next;
                curr2 = curr2->next->next;
            }
        }

        return false;

    }
};
