def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print("*********")
        print(n)
        print("$$$$$$$$$$$$$$")
        print("金刚葫芦娃")

cascade(123456789)