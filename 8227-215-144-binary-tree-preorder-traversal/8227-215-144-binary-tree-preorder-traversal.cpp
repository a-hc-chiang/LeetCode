/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) {
            vector<int> vec; 
            return vec; 
        }
        helper(root); 
        return output; 
    }
private: 
    vector<int> output; 
    void helper(TreeNode* root) {
        if (!root) {
            return; 
        }
        output.push_back(root->val); 
        helper(root->left); 
        helper(root->right); 
    }
};