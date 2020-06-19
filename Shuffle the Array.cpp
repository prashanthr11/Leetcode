class Solution {
public:
    vector<int> shuffle(vector<int>& a, int n) {
        vector<int> res;
        for(auto i = 0; i < n; ++i) {
            res.push_back(a[i]);
            res.push_back(a[i + n]);
        }
        return res;
    }
};
