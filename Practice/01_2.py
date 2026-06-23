#use booleans to store as variables so it's easier to read
print("[INITALIZING VALUES TO DEFAULT]")
counter = 0
is_valid_number = True

print(f"counter := {counter}")

print(f"\tis_valid_number := {is_valid_number}\n")


print("[TAKING USER INPUT]")
while(counter < 3):
    print(f"\t[CURRENT LOOP ITTERATION : ({counter})]")
    user_input = input("\t\tEnter a number ")
    is_valid_number = is_valid_number and user_input == "1"
    print(f"\t\tis_valid_number := {is_valid_number}")
    counter+=1

print("\n[FINAL EVALUATION]")
if is_valid_number: 
    print("At least one number inputed was invalid")
else:
    print("All numbers are good!")
