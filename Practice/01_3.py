#use booleans to store as variables so it's easier to read
print("[INITALIZING VALUES TO DEFAULT]")
is_valid_number = True
print(f"\tis_valid_number := {is_valid_number}\n")


# 1 == True, 0 == False
a = 2
print("a is: ", a)
a = bool(a)
print("a is: ", a)

b = -1
print("b is: ", b)
b = bool(b)
print("b is: ", b)
exit()

print(f"[ENTER THE FIRST NUMBER]")
user_input = input("\t\tEnter a number ")
is_valid_number = is_valid_number and user_input == "1"
print(f"is_valid_number := {is_valid_number}")

print(f"[ENTER THE SECOND NUMBER]")
user_input = input("\t\tEnter a number ")
is_valid_number = is_valid_number and user_input == "1"
print(f"is_valid_number := {is_valid_number}")

print(f"[ENTER THE THIRD NUMBER]")
user_input = input("\t\tEnter a number ")
is_valid_number = is_valid_number and user_input == "1"
print(f"is_valid_number := {is_valid_number}")

print("\n[FINAL EVALUATION]")
if is_valid_number == True: 
    print("All numbers are good!")
else:
    print("At least one number inputed was invalid")
