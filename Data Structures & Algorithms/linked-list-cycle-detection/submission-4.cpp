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
        if (head == nullptr){
            return false;
        }
        int iterations =0;
        while (head != nullptr && iterations < 1000){
            head = head->next;
            iterations++;
        }
        return !(iterations < 1000);
    }
};
