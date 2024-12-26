class User:
    def __init__(self, citizen_id: str, name: str):
        self.__id = citizen_id
        self.__name = name
        self.__account = []
        self.__atm_card = []
    
    def get_account(self):
        return self.__account

    def add_account(self, account):
        self.__account.append(account)

    def get_atm_card(self):
        return self.__atm_card
    
    def add_atm_card(self, atm_card):
        self.__atm_card.append(atm_card)

class Account:
    def __init__(self, account_number: str, owner: User, init_balance):
        self.__number = account_number
        self.__owner = owner
        self.__balance = init_balance
        self.__atm_card = None
        self.__transaction = []

    def get_number(self):
        return self.__number
    
    def set_number(self, account_number):
        self.__number = account_number
    
    def get_owner(self):
        return self.__owner
    
    def set_owner(self, owner):
        self.__owner = owner
    
    def get_atm_card(self):
        return self.__atm_card

    def set_atm_card(self, atm_card):
        self.__atm_card = atm_card

    def get_balance(self):
        return self.__balance
    
    def add_balance(self, amount):
        self.__balance += amount
    

    def add_transaction(self, transaction):
        self.__transaction.append(transaction)
    
    number = property(get_number, set_number)
    owner = property(get_owner, set_owner)

class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__number = card_number
        self.__account = account
        self.__pin = pin
        # print("Init ATMCard", card_number, account, pin)
        pass
    
    def get_number(self):
        return self.__number
    
    def get_account(self):
        return self.__account

class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__id = machine_id
        self.__amount = initial_amount

    def get_id(self):
        return self.__id

    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount):
        self.__amount = amount
    
    def add_amount(self, amount):
        self.__amount += amount
    
    def insert_card(self, bank, atm_card):
        for user in bank.get_user():
            for account in user.get_account():
                if account.get_atm_card() == atm_card:
                    return account
        return None
    
    amount = property(get_amount, set_amount)

class Bank:
    def __init__(self, name: str):
        self.__name = name
        self.__users = []
        self.__atm_machine = []

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_user(self):
        return self.__users
    
    def set_users(self, users):
        self.__users = users
    
    def add_user(self, user):
        self.__users.append(user)
    
    def get_atm_machine(self):
        return self.__atm_machine
    
    def set_atm_machine(self, atm_machine):
        self.__atm_machine = atm_machine
    
    def add_atm_machine(self, atm_machine):
        self.__atm_machine.append(atm_machine)
    
    def deposit(self, atm:ATMMachine, account:Account, amount):
        if amount <= 0 :
            return "Error"

        atm.add_amount(amount)
        
        account.add_transaction(Transaction("D", amount, atm))
        account.add_balance(amount)

        print(account.get_balance())

        return "Success"

    name = property(get_name, set_name)

class Transaction:
    def __init__(self, type: str, amount:int, machine:ATMMachine):
        self.__type:str = type
        self.__amount:int = amount

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
# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
lnwza_bank = Bank(name="LnwZaBank")
lnwza_bank.set_users(all_users)
lnwza_bank.set_atm_machine(all_atm_machine)

print("TODO 1", lnwza_bank.name)
print("TODO 1", [i.get_id() for i in all_atm_machine])
print()

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM
insert_card = all_atm_machine[0].insert_card(lnwza_bank, all_atm_card[0])
print("TODO 2", insert_card)
print()

# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0
deposit = lnwza_bank.deposit(all_atm_machine[0], insert_card, 500)
print("TODO 3", deposit)
print()

# TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Hermione account before test : 1500

# Harry account after test : 10000
# Hermione account after test : 11500


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
# atm_machine = bank.get_atm('1001')
# test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN

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