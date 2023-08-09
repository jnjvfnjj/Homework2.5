class SlotMachine:
    def name(name):
        
        print(f"здарствуйте,{name}")

    def __init__(self):
        self.user_balance = 100
        self.game_balance = 0
        
    def info(self):
        name = "meergul"
        return f"имя = {name},  ваш баланс:{self.user_balance}, ваш игровой баланс:{self.game_balance}" 
    
    def top_up_balance(self):
        money = int(input("на какую сумму вы хотите пополнить баланс: "))
        if money >= 100:
            print("Вы можете пополнить до 100$")
        else:
            def balance_up():
                self.game_balance + money
                print(f"ваш игровой баланс: {balance_up}")

    def game(self):
            count = 0 
            import random
            random_number = random.randint(1, 10)
            while count < 5:
                    user_number = int(input("выберите от 1 до 10: "))
                    if user_number == random_number:
                            print("вы выиграли")
                            self.game_balance += 50
                            print("ваш баланс пополнен на 50$")
                            break
                    else:
                            print("повторите попытку")
                            count += 1
                    print("вы проиграли")
                    self.game_balance -= 10
            

    def conslusion_money(self):
         conclude_money = int(input("какую сумму вы хотите вывести?: "))
         if conclude_money <= 50:
              print("Вывести можно от 50$")
         else:
              final_maney = self.user_balance + conclude_money
              print(f"ваш баланс: {final_maney}")

    def main(self):
        print(slotMachine.info())
        print (slotMachine.top_up_balance())      
        print(slotMachine.game())
        print(slotMachine.conslusion_money())


slotMachine = SlotMachine()
slotMachine.name()


slotMachine.main()
       

                