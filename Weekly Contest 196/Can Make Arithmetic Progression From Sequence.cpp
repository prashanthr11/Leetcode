class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& a) {
        sort(begin(a), end(a));
        int d = abs(a[1] - a[0]);
        for(int i = 1; i < a.size(); ++i) {
            if(abs(a[i - 1] - a[i]) != d)
                return false;
        }
        return true;
    }
};
