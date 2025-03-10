class User:
    def __init__(self, citizen_id: str, name: str):
        self.__id = citizen_id
        self.__name = name
        self.__account:list[Account] = []
        self.__atm_card:list[ATMCard] = []
    
    def get_name(self):
        return self.__name
    
    def get_account(self):
        return self.__account

    def add_account(self, account):
        self.__account.append(account)

    def get_atm_card(self):
        return self.__atm_card
    
    def add_atm_card(self, atm_card):
        self.__atm_card.append(atm_card)

class Account:
    def __init__(self, account_number: str, owner: User, init_balance=0):
        self.__number = account_number
        self.__owner = owner
        self.__amount = init_balance
        self.__atm_card = None
        self.__transaction = []

    def get_number(self):
        return self.__number
    
    def get_atm_card(self):
        return self.__atm_card

    def set_atm_card(self, atm_card):
        self.__atm_card = atm_card

    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount):
        self.__amount = amount
    
    def get_all_transaction(self):
        return self.__transaction
    
    def add_transaction(self, transaction):
        self.__transaction.append(transaction)
    
    def deposit(self, amount, atm_id):
        self.__amount += amount
        transaction = Transaction("D", amount, self.__amount, atm_id)

        self.add_transaction(transaction)
    
    def withdraw(self, amount, atm_id):
        if self.__amount < amount:
            return "Error"
         
        self.__amount -= amount
        transaction = Transaction("W", amount, self.__amount, atm_id)

        self.add_transaction(transaction)

    def transfer(self, amount, transfer_acc, atm_id):
        if self.__amount < amount:
            return "Can't transfer amount less your account"
                
        self.__amount -= amount
        transfer_acc.balance += amount

        transaction = Transaction("TW", amount, self.__amount, atm_id)
        self.add_transaction(transaction)

        transfer_transaction = Transaction("TD", amount, transfer_acc.balance, atm_id)
        transfer_acc.add_transaction(transfer_transaction)

        return "Success"

    balance = property(get_amount, set_amount)

class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__number = card_number
        self.__account = account
        self.__pin = pin
    
    def get_number(self):
        return self.__number
    
    def get_account(self):
        return self.__account
    
    def get_pin(self):
        return self.__pin

class ATMMachine:
    max_withdraw = 40000

    def __init__(self, machine_id: str, initial_balance: float = 1000000):
        self.__id = machine_id
        self.__balance = initial_balance

    def get_id(self):
        return self.__id

    def get_amount(self):
        return self.__balance
    
    def set_amount(self, amount):
        self.__balance = amount
    
    def insert_card(self, bank, atm_card, pin) -> Account | None:
        if pin != "1234":
            return "Invalid PIN"

        for user in bank.get_user():
            for account in user.get_account():
                if account.get_atm_card() == atm_card:
                    return account

        return None

    def deposit(self, account:Account, amount):
        if amount <= 0:
            return "Error"
        
        self.__balance += amount

        account.deposit(amount, self.__id)

        return "Success"

    def withdraw(self, account:Account, amount):
        if amount <= 0:
            return "Error"
        
        if self.__balance < amount:
            return "ATM has insufficient funds"
        
        if amount > ATMMachine.max_withdraw:
            return "Exceeds daily withdrawal limit of 40,000 baht"
        
        res = account.withdraw(amount, self.__id)

        if res != None:
            return "Error"
        
        self.__balance -= amount

        return "Success"

    def transfer(self, account:Account, trans_acc:Account, amount):
        if amount <= 0:
            return "Error"
        
        res = account.transfer(amount, trans_acc, self.__id)
        
        return res
    
    balance = property(get_amount, set_amount)

class Bank:
    def __init__(self, name: str):
        self.__name = name
        self.__users = []
        self.__atm_machine = []

    def get_user(self):
        return self.__users
    
    def set_users(self, users):
        self.__users = users
    
    def get_atm_machine(self, id) -> None | ATMMachine:
        for machine in self.__atm_machine:
            if machine.get_id() == id:
                return machine
            
        return None
    
    def set_atm_machine(self, atm_machine):
        self.__atm_machine = atm_machine

class Transaction:
    def __init__(self, type, amount, after_amount,machine:ATMMachine):
        self.__type = type
        self.__amount = amount
        self.__after_amount = after_amount
        self.__atm = machine
    
    def get_type(self):
        return self.__type

    def get_amount(self):
        return self.__amount

    def get_after_amount(self):
        return self.__after_amount
    
    def get_atm_id(self):
        return self.__atm
    
##################################################################################

#     {     รหัสประชาชน    :[ชื่อ,            หมายเลขบัญชี, หมายเลข ATM, จำนวนเงิน]}
user = {'1-1101-12345-12-0':['Harry Potter', '1234567890', '12345', 20000],
       '1-1101-12345-13-0':['Hermione Jean Granger', '0987654321', '12346', 1000]}

atm = {'1001':1000000,'1002':200000}

all_users:list[User] = []
all_account:list[Account] = []
all_atm_card:list[ATMCard] = []
all_atm_machine:list[ATMMachine] = []

def initialize():
    for id in user:
        inst_user = User(id, user[id][0])
        inst_account = Account(user[id][1], inst_user, user[id][3])
        inst_atm_card = ATMCard(user[id][2], inst_account, "1234")

        inst_user.add_account(inst_account)
        inst_user.add_atm_card(inst_atm_card)

        inst_account.set_atm_card(inst_atm_card)

        all_users.append(inst_user)
        all_account.append(inst_account)
        all_atm_card.append(inst_atm_card)
        
    for id in atm:
        all_atm_machine.append(ATMMachine(id, atm[id]))

initialize()

lnwza_bank = Bank(name="LnwZaBank")

lnwza_bank.set_users(all_users)
lnwza_bank.set_atm_machine(all_atm_machine)

def todo():
    # TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
    # TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
    # TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
    # TODO :   return เป็น instance ของธนาคาร
    # TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
    # print("TODO 1", lnwza_bank.get_name())
    print("TODO 1", lnwza_bank)
    # print("TODO 1 ATM Machine:", [i.get_id() for i in all_atm_machine])
    print("TODO 1 ATM Machine:", all_atm_machine)
    print()

    # TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
    # TODO     2) atm_card เป็นหมายเลขของ atm_card
    # TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
    # TODO     ควรเป็น method ของเครื่อง ATM
    atm_card = all_atm_card[0]
    atm_machine = lnwza_bank.get_atm_machine('1001')
    account = atm_machine.insert_card(lnwza_bank, atm_card, atm_card.get_pin())
    print("TODO 2", account)
    print()

    # TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0
    deposit = atm_machine.deposit(account, 500)
    print("TODO 3", deposit)
    print()

    # TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account 3) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
    withdraw = atm_machine.withdraw(account, 500)
    print("TODO 4", withdraw)
    print()

    # TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
    # TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
    # TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
    # TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
    # TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

    transfer = atm_machine.transfer(account, all_account[1], 1000)
    print("TODO 5", transfer)
    print()

############################# TEST CASE ############################################
def test_case():
    atm1 = lnwza_bank.get_atm_machine('1001')
    atm2 = lnwza_bank.get_atm_machine('1002')

    harry = all_users[0]
    hermione = all_users[1]

    harry_atm_card = harry.get_atm_card()[0]
    hermione_atm_card = hermione.get_atm_card()[0]

    # Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
    # และเรียกใช้ function หรือ method จากเครื่อง ATM
    # ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
    # Ans : 12345, 1234567890, Success

    # x = ATMCard("123", Account("asda", User("asd","asdas")),"1234")
    print("Test case #1")
    harry_account = atm1.insert_card(lnwza_bank, harry_atm_card, harry_atm_card.get_pin())
    print("Ans :", harry_atm_card.get_number(), harry_account.get_number())
    print()

    # Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
    # ให้เรียกใช้ method ที่ทำการฝากเงิน
    # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
    # Hermione account before test : 1000
    # Hermione account after test : 2000
    hermione_account = atm2.insert_card(lnwza_bank, hermione_atm_card, hermione_atm_card.get_pin())
    if hermione_account == None:
        print("Error")

    print("Test case #2")
    print("Hermione account before test :", hermione_account.balance)
    atm2.deposit(hermione_account, 1000)
    print("Hermione account after test :", hermione_account.balance)
    print()

    # Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
    # ผลที่คาดหวัง : แสดง Error
    print("Test case #3")
    tc3 = atm2.deposit(hermione_account, -1)
    print("แสดง", tc3)
    print()

    # Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
    # ให้เรียกใช้ method ที่ทำการถอนเงิน
    # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
    # Hermione account before test : 2000
    # Hermione account after test : 1500
    print("Test case #4")
    print("Hermione account before test :", hermione_account.balance)
    atm2.withdraw(hermione_account, 500)
    print("Hermione account after test :", hermione_account.balance)
    print()

    # Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
    # ผลที่คาดหวัง : แสดง Error
    print("Test case #5")
    tc5 = atm2.withdraw(hermione_account, 2000)
    print("ผลที่คาดหวัง : แสดง", tc5)
    print()

    # Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
    # ให้เรียกใช้ method ที่ทำการโอนเงิน
    # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
    # Harry account before test : 20000
    # Hermione account before test : 1500
    print("Test case #6")
    print("Harry account before test :", harry_account.balance)
    print("Hermione account before test :", hermione_account.balance)
    print()
    atm2.transfer(harry_account, hermione_account, 10000)
    # Harry account after test : 10000
    # Hermione account after test : 11500
    print("Harry account after test :", harry_account.balance)
    print("Hermione account after test :", hermione_account.balance)
    print()

    # Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
    # ผลที่คาดหวัง
    # Hermione transaction : D-ATM:1002-1000-2000
    # Hermione transaction : W-ATM:1002-500-1500
    # Hermione transaction : TD-ATM:1002-10000-11500
    print("Test case #7")

    tc7 = hermione_account.get_all_transaction()
    for transaction in tc7:
        t_type = transaction.get_type()
        t_amount = transaction.get_amount()
        t_after_amount = transaction.get_after_amount()
        t_atm = transaction.get_atm_id()
        print(f"Hermione transaction : {t_type}-ATM:{t_atm}-{t_amount}-{t_after_amount}", )
    print()

    # Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
    print("Test case #8")
    # ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
    # atm_machine = bank.get_atm('1001')
    # test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
    # ผลที่คาดหวัง
    # Invalid PIN
    atm_machine = lnwza_bank.get_atm_machine('1001')
    test_result = atm_machine.insert_card(lnwza_bank, harry_atm_card, "9999")
    print(test_result)
    print()

    # Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อครั้ง (40,000 บาท)
    # atm_machine = bank.get_atm('1001')
    # account = atm_machine.insert_card('12345', '1234')  # PIN ถูกต้อง
    # harry_balance_before = account.get_balance()
    # print(f"Harry account before test: {harry_balance_before}")
    # print("Attempting to withdraw 45,000 baht...")
    # result = atm_machine.withdraw(account, 45000)
    # print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
    # print(f"Actual result: {result}")
    # print(f"Harry account after test: {account.get_balance()}")
    # print("-------------------------")

    print("Test case #9")
    atm_machine = lnwza_bank.get_atm_machine('1001')
    account = atm_machine.insert_card(lnwza_bank, harry_atm_card, harry_atm_card.get_pin()) 
    print(f"Harry account before test: {account.balance}")
    print("Attempting to withdraw 45,000 baht...")
    result = atm_machine.withdraw(account, 45000)
    print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
    print(f"Actual result: {result}")
    print(f"Harry account after test: {account.balance}")
    print("-------------------------")
    print()

    # Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ

    # atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
    # account = atm_machine.insert_card('12345', '1234')
    # print("Test case #10 : Test withdrawal when ATM has insufficient funds")
    # print(f"ATM machine balance before: {atm_machine.get_balance()}")
    # print("Attempting to withdraw 250,000 baht...")
    # result = atm_machine.withdraw(account, 250000)
    # print(f"Expected result: ATM has insufficient funds")
    # print(f"Actual result: {result}")
    # print(f"ATM machine balance after: {atm_machine.get_balance()}")
    # print("-------------------------")

    atm_machine = lnwza_bank.get_atm_machine('1002')
    account = atm_machine.insert_card(lnwza_bank, harry_atm_card, harry_atm_card.get_pin())
    print("Test case #10 : Test withdrawal when ATM has insufficient funds")
    print(f"ATM machine balance before: {atm_machine.balance}")
    print("Attempting to withdraw 250,000 baht...")
    result = atm_machine.withdraw(account, 250000)
    print(f"Expected result: ATM has insufficient funds")
    print(f"Actual result: {result}")
    print(f"ATM machine balance after: {atm_machine.balance}")
    print("-------------------------")

test_case()