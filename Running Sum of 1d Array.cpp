class Solution {
public:
    vector<int> runningSum(vector<int>& a) {
        vector<int> x(a.size());
        x[0] = a[0];
        for(auto i = 1; i < a.size(); ++i) {
            x[i] = x [i - 1] + a[i];
        }
        return x;
        
    }
};
