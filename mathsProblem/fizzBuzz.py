def fizzBuzz(A):
        res = []
        for i in range(1, A+1):
            print("#"*20)
            val = "Fizz"*(i%3==0) + "Buzz"*(i%5==0)
            print(val)
            res += [val] if val else [i]
            print(res)
        return res

print(fizzBuzz(6))