class ATM:
    def __init__(self):
        self.note_values = [2000,500,200,50]
    
    def withdraw(self, amount):
        if amount <= 0 or amount % 50 != 0:
            print("Invalid withdrawal amount. Please enter a valid amount.")
            return
        
        notes_count = {}
        remaining_amount = amount
        
        for note_value in self.note_values:
            if remaining_amount >= note_value:
                count = remaining_amount // note_value
                notes_count[note_value] = count
                remaining_amount %= note_value
        
        if remaining_amount == 0:
            print("Withdrawal successful. Notes returned:")
            for note_value, count in notes_count.items():
                print(f"{note_value} notes: {count}")
        else:
            print("Unable to dispense the exact amount with available notes.")
    
    def run(self):
        while True:
            try:
                withdrawal_amount = int(input("Enter the amount to withdraw: "))
                self.withdraw(withdrawal_amount)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
            
            choice = input("Do you want to continue (Y/N)? ").strip().lower()
            if choice != 'y':
                print("Transaction cancelled.")
                break

if __name__ == "__main__":
    atm = ATM()
    atm.run()
