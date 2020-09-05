class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        three = "Fizz"
        five = "Buzz"
        both = "FizzBuzz"
        ret = list()
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ret.append(both)
            elif i % 5 == 0:
                ret.append(five)
            elif i % 3 == 0:
                ret.append(three)
            else:
                ret.append(str(i))
        return ret
