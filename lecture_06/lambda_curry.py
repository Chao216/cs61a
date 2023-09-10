sweet = lambda x: lambda y: lambda z: x + y + z

ans = sweet(2)(5)(7)

print(ans)

chocolate = lambda a: lambda b: lambda c: lambda d: lambda e: print(a," ",b," ",c," ",d," ",e," ")
chocolate("我们")("中国")("真的是")("太厉害")("了")

def f1(a):
    def f2(b):
        def f3(c):
            def f4(d):
                def f5(e):
                    print(a," ",b," ",c," ",d," ",e," ")
                return f5
            return f4
        return f3
    return f2

f1("哥们儿")("不费力")("就")("住进了")("高楼")