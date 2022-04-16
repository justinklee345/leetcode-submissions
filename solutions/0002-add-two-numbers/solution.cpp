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

#include <iostream>

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* to_return = new ListNode();
        bool l1_avail = true;
        bool l2_avail = true;
        bool surplus = false;
        ListNode* iter = to_return;
        while (l1_avail || l2_avail) {
            if (l1_avail && !l2_avail) {
                if (surplus) {
                    if (l1->val == 9) {
                        iter->val = 0;
                    } else {
                        iter->val = l1->val + 1;
                        surplus = false;
                    }
                } else {
                    iter->val = l1->val;
                }
            } else if (!l1_avail && l2_avail) {
                if (surplus) {
                    if (l2->val == 9) {
                        iter->val = 0;
                    } else {
                        iter->val = l2->val + 1;
                        surplus = false;
                    }
                } else {
                    iter->val = l2->val;
                }
            } else if (l1_avail && l2_avail) {
                if (l1->val + l2->val > 9) {
                    if (surplus) {
                        iter->val = l1->val + l2->val + 1 - 10;
                    } else {
                        iter->val = l1->val + l2->val - 10;
                        surplus = true;
                    }
                } else {
                    if (surplus) {
                        if (l1->val + l2->val == 9) {
                            iter->val = l1->val + l2->val + 1 - 10;
                            surplus = true;
                        } else {
                            iter->val = l1->val + l2->val + 1;  
                            surplus = false; 
                        }
                        
                    } else {
                        iter->val = l1->val + l2->val;
                    }
                    std::cout << "I'm being stupid: " << iter->val << std::endl;
                }
            }
            if (l1_avail && l1->next == nullptr) {
                l1_avail = false;
                l1 = nullptr;
            } else {
                if (l1_avail) {
                    l1 = l1->next;    
                }
            }
            if (l2_avail && l2->next == nullptr) {
                l2_avail = false;
                l2 = nullptr;
            } else {
                if (l2_avail) {
                    l2 = l2->next;
                }
            }
            if (!l1_avail && !l2_avail) {
                if (surplus) {
                    iter -> next = new ListNode(1);
                    break;
                } else {
                    break;
                }
            }
            iter->next = new ListNode();
            iter = iter->next;
        }
        return to_return;
    }
};
