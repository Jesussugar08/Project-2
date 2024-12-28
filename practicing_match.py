print("================================")
print("Enter 'end' to finish ")
print("================================")
while True:

    user_input = input("how old are you?: ").strip()

    if user_input.lower() == "end":
        print("has been finished")
        break

    try:
        age = int(user_input)
    except ValueError:
        print("Please enter a valid age or type 'end' to finish")
        continue

    match age:

        case age if age < 0:
            print("invalid age")

        case age if age <= 2:
            print("You are a baby ")

        case age if age <= 12:
            print("You are child")

        case age if age <= 18:
            print("You are a teenager ")

        case age if age <= 64:
            print("You are an adult")

        case _:
            print("You are a senior citizen")
