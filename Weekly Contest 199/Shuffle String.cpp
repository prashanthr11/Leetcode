class Solution {
public:
    string restoreString(string s, vector<int>& a) {
        vector<char> ans((int)s.size()) ;
        for(auto i = 0; i < (int)a.size(); ++i) 
            ans[a[i]]= s[i];
        
        string x = "";
        for(auto i:ans)
            x += i;
        return x;
    }
};