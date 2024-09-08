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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int listSize = 0; 
        ListNode* temp = head;

        while (temp) { //finding the size of the linked list 
            listSize++; 
            temp = temp->next; 
        } 

        vector<ListNode*> res;
        temp = head; //reseting 

        if (listSize < k) { //if you can't split in k parts
            for (unsigned int i = 0; i < k; i++) {
                if (listSize <= 0) {
                    res.push_back(nullptr);
                } else { //still need to split 
                    temp = head; 
                    if (head->next) {
                        head = head->next; 
                        temp->next = nullptr; 
                    }
                    res.push_back(temp);
                }
                --listSize; 
            }

        } else { //can split in k parts 
            int remainder = listSize%k; 
            ListNode* newHead = head; //new head to add
            for (unsigned int i = 0; i < k; i++) { //for each part
                res.push_back(newHead); //head added in 
                if (i == k - 1) break; //no need to traverse

                temp = newHead;
                for (int j = listSize/k - 1; j > 0; j--) { //traverse to split list
                    temp = temp->next; //moving temp
                }
                if (remainder > 0) temp = temp->next; //extra movement
                newHead = temp->next; 
                temp->next = nullptr; 
                --remainder;
            }
        }
        return res; 
    }
};