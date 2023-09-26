balance = 0
transactions = []

def deposit(balance, amount):
    if amount % 50 == 0:
        balance += amount
        transactions.append(f"Пополнение: +{amount} у.е.")
        return balance
    else:
        print("Сумма пополнения должна быть кратной 50 у.е.")
        return balance

def withdraw(balance, amount):
    global transactions
    if amount % 50 == 0:
        if balance >= amount:
            withdrawal_fee = max(30, min(0.015 * amount, 600))
            balance -= (amount + withdrawal_fee)
            transactions.append(f"Снятие: -{amount} у.е. (Комиссия: -{withdrawal_fee} у.е.)")
            return balance
        else:
            print("Недостаточно средств на счете")
            return balance
    else:
        print("Сумма снятия должна быть кратной 50 у.е.")
        return balance

def calculate_tax(balance):
    return 0.1 * balance

def main():
    global balance
    while True:
        print(f"Текущий баланс: {round(balance, 2)} у.е.")
        print("Допустимые действия: пополнить - 1, снять - 2, выйти - 3")
        action = input("Выберите действие: ")
        if action == "1":
            amount = int(input("Введите сумму для пополнения: "))
            balance = deposit(balance, amount)
        elif action == "2":
            amount = int(input("Введите сумму для снятия: "))
            balance = withdraw(balance, amount)
        elif action == "3":
            break
        else:
            print("Неверное действие")

        if len(transactions) % 3 == 0:
            balance -= 0.03 * balance

        if balance > 5000000:
            tax = calculate_tax(balance)
            balance -= tax
            print(f"Удержан налог на богатство: {tax} у.е.")

    print("Список операций:")
    for transaction in transactions:
        print(transaction)

if __name__ == "__main__":
    main()