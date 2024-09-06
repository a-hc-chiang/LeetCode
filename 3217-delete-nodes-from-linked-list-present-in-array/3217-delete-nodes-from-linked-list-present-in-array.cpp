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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        vector<ListNode*> vec; 
        set<int> s(nums.begin(), nums.end());
        ListNode* temp = head;

        while (temp) { //iterate through list 
            if (!(s.contains(temp->val))) {
                ListNode* temp2 = temp; //placing nodes into an array
                vec.push_back(temp);
                temp = temp->next; 
                temp2 -> next = nullptr; 
            } else {
                ListNode* temp2 = temp;  //deleting the nodes present in nums
                temp = temp -> next; 
                delete temp2; 
            }
        }
        unsigned int i = 0; //first iterator tracker
        for (ListNode* l: vec) {
            if (i == 0) { //check if first iteration 
                head = l; 
                temp = head; 
                i++; 
            } else {
                temp -> next = l; 
                temp = temp -> next; 
            }
        }
        return head; 
    }
};