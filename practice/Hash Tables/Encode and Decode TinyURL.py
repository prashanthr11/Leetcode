class Codec:
    
    def __init__(self):
        self.dt = defaultdict(list)

    def encode(self, a: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        tmp = hash(a)
        self.dt[tmp] = a
        return str('http://tinyurl.com/' + str(tmp))
        

    def decode(self, a: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        a = a.split('/')
        return self.dt[int(a[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
