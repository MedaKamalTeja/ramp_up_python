import random

def generate_random_employee_id():
    return random.randint(1, 9999)

def generate_random_location():
    locations = ["Kormangala", "HSR Layout", "Ballary", "Mumbai", "Chennai", "Nellore", "Gurgaon", "Hyderabad"]
    return random.choice(locations)

def generate_random_salary():
    return round(random.uniform(20000, 150000))

def generate_employee_details(num_employees):
    for _ in range(num_employees):
        emp_id = generate_random_employee_id()
        location = generate_random_location()
        salary = generate_random_salary()
        
        yield {"Employee ID": emp_id, "Location": location, "Salary": salary}

def main():
            num_employees = int(input("Enter the number of employees to generate:"))
            employee_generator = generate_employee_details(num_employees)


            if num_employees==0:
                    print("Please enter a valid number of employees.")
            
            print("\nEmployee Details:")
            for employee_details in employee_generator:
                print("-" * 20)
                for key, value in employee_details.items():
                    print(f"{key}: {value}")
                #print()

        
if __name__ == "__main__":
     main()
