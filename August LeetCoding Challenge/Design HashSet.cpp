class MyHashSet {
public:
    /** Initialize your data structure here. */
    set<int> s;
    MyHashSet() {
        s.clear();
    }
    
    void add(int key) {
        s.insert(key);
    }
    
    void remove(int key) {
        s.erase(key);
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        for(auto i:s)
            if (i == key)
                return true;
        return false;
        
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
