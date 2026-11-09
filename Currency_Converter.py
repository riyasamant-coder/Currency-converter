
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


exchange_rates = {
    "INR": Decimal("1"),
    "USD": Decimal("83"),
    "EUR": Decimal("90"),
    "GBP": Decimal("105")
}



def convert_to_inr(amount, currency):
    return amount * exchange_rates[currency]



def convert_currency(amount, from_currency, to_currency):

    
    amount_in_inr = convert_to_inr(amount, from_currency)

    
    converted_amount = amount_in_inr / exchange_rates[to_currency]

    
    converted_amount = converted_amount.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    return converted_amount



def main():

    print("================================")
    print("       CURRENCY CONVERTER")
    print("================================")

    print("Supported currencies: INR, USD, EUR, GBP")

    try:
        
        amount_input = input("Enter amount: ")
        amount = Decimal(amount_input)

        
        if not amount.is_finite():
            print("Invalid amount. Enter a valid number.")
            return

        if amount < 0:
            print("Amount cannot be negative.")
            return

        
        from_currency = input("From currency: ").strip().upper()
        to_currency = input("To currency: ").strip().upper()

        
        if from_currency not in exchange_rates:
            print(
                f"Unsupported currency '{from_currency}'. "
                "Available: INR, USD, EUR, GBP"
            )
            return

        
        if to_currency not in exchange_rates:
            print(
                f"Unsupported currency '{to_currency}'. "
                "Available: INR, USD, EUR, GBP"
            )
            return

        
        result = convert_currency(
            amount, from_currency, to_currency
        )

        
        print("\nConversion Result:")
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

    except InvalidOperation:
        print("Invalid amount. Enter a number.")

    except Exception as error:
        print("An unexpected error occurred:", error)



if __name__ == "__main__":
    main()
