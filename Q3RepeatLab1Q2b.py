
currency = input("Enter your currency code: ")

match currency:
    case "AUD":
        print("Australian Dollar")
    case "MYR":
        print("Malaysian Ringgit")
    case"IDR":
        print("Indonesian Rupiah")
    case "SGD":
        print("Singapore Dollar")
    case _:
        print("Unknown currency")

print("After switch")