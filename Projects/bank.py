import random

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def new_bank_account(self, customer_name, phone_number):
        phone_number = str(phone_number)  # Ensure phone number is a string
        account_id = random.randint(1, 1000)  # Generate a random account ID

        print(f'A new bank account creation is requested with the name {customer_name}. Please recheck your phone number {phone_number}. Your account ID is {account_id}. Do not share this ID with anyone.')
        confirmation = input('Confirm? (y/n): ')

        if 'y' in confirmation.lower():
            print('Thank you for your confirmation. Our team will contact you in a few days.')
            account_info = f'Name: {customer_name}, Phone Number: {phone_number}, ID: {account_id}\n'

            # Store the account information in a file
            with open('accounts.txt', 'a') as file:
                file.write(account_info)
                print('Stored your information.')

        elif 'n' in confirmation.lower():
            print('Ok, let\'s update the information.')
            update_field = input('Which information do you want to change (name/number): ')

            if 'na' in update_field.lower():
                new_name = input('Enter the new name: ')
                print(f'Now the name is {new_name}') 

                # Update the account information with the new name
                with open('accounts.txt', 'a') as file:
                    file.write(f'Name: {new_name}, Phone Number: {phone_number}, ID: {account_id}\n')
                    print('Stored your updated information.')

            elif 'nu' in update_field.lower():
                new_phone_number = input('Enter the new phone number: ')
                print(f'Now the new phone number is {new_phone_number}')

                # Update the account information with the new phone number
                with open('accounts.txt', 'a') as file:
                    file.write(f'Name: {customer_name}, Phone Number: {new_phone_number}, ID: {account_id}\n')
                    print('Stored your updated information.')

    def deposit(self, customer_name, account_id):
        # Verify if the account ID exists and matches the customer's name
        with open('accounts.txt', 'r') as file:
            content = file.read()
            
            if str(account_id) not in content:
                print('The ID you entered is not correct.')
                return
            
            if f'{account_id} {customer_name}\n' not in content:
                print('Your name and ID do not match.')
                return

        print('After confirmation, please tell me how much amount you want to deposit.')
        deposit_amount = int(input())
        confirmation = input('Are you sure? (y/n): ')

        if 'y' in confirmation.lower():
            print('Transaction is being processed.')

            # Read the current balances
            with open('balance.txt', 'r') as file:
                lines = file.readlines()
        
            # Update the balance or create a new record if not found
            with open('balance.txt', 'w') as file:
                account_found = False
                for line in lines:
                    if str(account_id) in line:
                        parts = line.split(',')
                        previous_balance = int(parts[2].split()[-1])
                        new_balance = previous_balance + deposit_amount
                        file.write(f'Name: {customer_name}, ID: {account_id}, Balance: {new_balance}\n')
                        account_found = True
                    else:
                        file.write(line)
            
                if not account_found:
                    file.write(f'Name: {customer_name}, ID: {account_id}, Balance: {deposit_amount}\n')
        else:
            print('The transaction has been cancelled.')

    def withdrawal(self, customer_name, account_id):
        # Read the current balances
        with open('balance.txt', 'r') as file:
            lines = file.readlines()

        # Update the balance or notify if the account is not found
        with open('balance.txt', 'w') as file:
            account_found = False
            for line in lines:
                if str(account_id) in line:
                    parts = line.split(',')
                    previous_balance = int(parts[2].split()[-1])
                    withdrawal_amount = int(input('Enter the amount to withdraw: '))
                    new_balance = previous_balance - withdrawal_amount
                    if new_balance < 0:
                        print('Withdrawal amount exceeds balance. Transaction cancelled.')
                        return
                    file.write(f'Name: {customer_name}, ID: {account_id}, Balance: {new_balance}\n')
                    account_found = True
                else:
                    file.write(line)

            if not account_found:
                print('Account not found.')

    def information(self, customer_name, account_id):
        # Retrieve the account balance information
        with open('balance.txt', 'r') as file:
            lines = file.readlines()

        account_found = False
        for line in lines:
            if str(account_id) in line:
                parts = line.split(',')
                balance_info = parts[2].split()[-1]
                print(f'Account found - Name: {customer_name}, ID: {account_id}, Balance: {balance_info}')
                account_found = True

        if not account_found:
            print('Account not found.')

