class Solution {
public:
    int maxProduct(vector<int>& a) {
        sort(begin(a), end(a));
        int n = a.size() - 1;
        return ((a[n] - 1 )* (a[n - 1] - 1));
        
    }
};
