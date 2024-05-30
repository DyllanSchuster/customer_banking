# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('What is your initial savings account balance? '))
    savings_interest = float(input('In dedcimal form, what is the APR for the savings account? '))
    savings_maturity = int(input('In months, how long would you like this account to mature for? '))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("Here are the details of your savings account: ")
    print(f"Your new Savings account balance is: ${updated_savings_balance:.2f}")
    print(f"You earned ${interest_earned:.2f} of interst over {savings_maturity} months.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('In decimal form, what is the APR for the CD account? '))
    cd_maturity = int(input('What is the length of months for your CD? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("Here are the details of the CD account: ")
    print(f"You earned ${interest_earned:.2f} of Interst over {cd_maturity} months.")
    print(f"Your new CD account balance is ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
