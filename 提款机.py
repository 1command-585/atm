import sys

class ATM:
    """模拟简单的提款机"""

    def __init__(self, initial_balance=1000, pin="1234"):
        self.balance = initial_balance
        self.pin = pin
        self.authenticated = False

    def authenticate(self):
        """验证用户 PIN 码"""
        attempts = 3
        while attempts > 0:
            entered_pin = input("请输入您的 PIN 码: ")
            if entered_pin == self.pin:
                self.authenticated = True
                print("验证成功！\n")
                return True
            else:
                attempts -= 1
                print(f"PIN 码错误，还剩 {attempts} 次机会。")
        print("验证失败，程序退出。")
        sys.exit()

    def check_balance(self):
        """查询余额"""
        print(f"当前余额为: {self.balance:.2f} 元")

    def deposit(self):
        """存款"""
        try:
            amount = float(input("请输入存款金额: "))
            if amount <= 0:
                print("金额必须大于零。")
            else:
                self.balance += amount
                print(f"成功存入 {amount:.2f} 元，当前余额为 {self.balance:.2f} 元")
        except ValueError:
            print("输入无效，请输入数字。")

    def withdraw(self):
        """取款"""
        try:
            amount = float(input("请输入取款金额: "))
            if amount <= 0:
                print("金额必须大于零。")
            elif amount > self.balance:
                print("余额不足，无法取款。")
            else:
                self.balance -= amount
                print(f"成功取出 {amount:.2f} 元，当前余额为 {self.balance:.2f} 元")
        except ValueError:
            print("输入无效，请输入数字。")

    def run(self):
        """启动 ATM 程序"""
        print("=" * 40)
        print("欢迎使用 Python ATM 提款机")
        print("=" * 40)

        # 验证 PIN 码（可选，可注释掉以跳过验证）
        self.authenticate()

        while True:
            print("\n请选择操作：")
            print("1. 查询余额")
            print("2. 存款")
            print("3. 取款")
            print("4. 退出")

            choice = input("请输入数字 (1-4): ").strip()

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("感谢使用，再见！")
                break
            else:
                print("无效选项，请重新输入。")

if __name__ == "__main__":
    atm = ATM(initial_balance=int(0), pin="56942034")  # 可修改初始余额和 PIN 码
    atm.run()