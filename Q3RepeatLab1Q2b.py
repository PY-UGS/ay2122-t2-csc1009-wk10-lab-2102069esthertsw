# get user input on currency code
currency = input("Enter your currency code: ")

# python switch case equivalent
match currency:
    case "AUD":
        print("Australian Dollar")
    case "MYR":
        print("Malaysian Ringgit")
    case"IDR":
        print("Indonesian Rupiah")
    case "SGD":
        print("Singapore Dollar")
    case _: #default case
        print("Unknown currency")

print("After switch")
