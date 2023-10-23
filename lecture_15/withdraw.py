def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return "insufficient balance"
        b[0] = b[0] - amount
        return b[0]
    return withdraw

withdrawhund = make_withdraw_list(100)

for _ in range(5):
    print(withdrawhund(30))