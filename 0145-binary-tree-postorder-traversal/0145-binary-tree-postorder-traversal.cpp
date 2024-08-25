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
    vector<int> res; //so helper function can access vector 
    vector<int> postorderTraversal(TreeNode* root) {
        postOrderHelper(root); 
        return res; 
    }

private: 
    void postOrderHelper(TreeNode* root) {
        if (!root) { //base case 
            return;
        }
        postOrderHelper(root->left); //post order traversal 
        postOrderHelper(root->right); 
        res.push_back(root->val);
    }
};