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
    int sumOfLeftLeaves(TreeNode* root) {
        int ans = 0;
        if(root) {
            stack<TreeNode*> st;
            st.push(root);
            
            while(!st.empty()) {
                auto tp = st.top();
                st.pop();
                if(tp -> left) {
                    st.push(tp -> left);
                    if(tp -> left -> left == NULL && tp -> left -> right == NULL)
                        ans = ans + tp -> left -> val;
                }
                
                if(tp -> right)
                    st.push(tp -> right);
            }
        }
        return ans;
    }
};
