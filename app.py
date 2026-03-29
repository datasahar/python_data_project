phone_numbers = {'Amal':'1111111111',
'Mohammed':'2222222222',
'Khadijah':'3333333333',
'Abdullah':'4444444444',
'Rawan':'5555555555',
'Faisal':'6666666666',
'Layla':'7777777777'}

# دالة التحقق من صحة الرقم
def is_valid_number(number):
    count = 0
    for char in number:
        count += 1
    if count != 10:
        return False
    for char in number:
        if char < "0" or char > "9":
            return False
    return True


# دالة البحث عن الأسم باستخدام الرقم
def find_name_by_number():
    phone_number = input("Enter the phone number: ")
    if is_valid_number(phone_number):
        for name, number in phone_numbers.items():
            if phone_number == number:
                print(name)
                return
        print("Sorry, the number is not found")
    else:
        print("This is invalid number")


# دالة البحث عن الرقم باستخدام الأسم
def find_number_by_name():
    name = input("Enter the name: ")
    for owner, number in phone_numbers.items():
        if owner == name:
            print(number)
            return
    print("Sorry, the name is not found")


# دالة إضافة جهة اتصال جديدة
def add_new_contact():
    new_name = input("Add new name: ")
    new_number = input("Add new number: ")
    if is_valid_number(new_number):
        phone_numbers[new_name] = new_number
        print("Contact added successfully!")
    else:
        print("This is invalid number")


# استدعاء الدالات
find_name_by_number()
find_number_by_name()
add_new_contact()




