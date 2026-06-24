policies = []
customers = []


def add_policy():
    print("\n--- Add Policy ---")
    name = input("Enter policy name: ")
    duration = int(input("Enter duration (in years): "))
    premium = float(input("Enter monthly premium (INR): "))
    cover = float(input("Enter coverage amount (INR): "))

    policy = {
        "id": len(policies) + 1,
        "name": name,
        "duration": duration,
        "premium": premium,
        "cover": cover
    }
    policies.append(policy)
    print(f"Policy '{name}' added successfully!")


def view_policies():
    print("\n--- All Policies ---")
    if len(policies) == 0:
        print("No policies found.")
        return

    for p in policies:
        print(f"\nID       : {p['id']}")
        print(f"Name     : {p['name']}")
        print(f"Duration : {p['duration']} years")
        print(f"Premium  : INR {p['premium']:.2f}/month")
        print(f"Coverage : INR {p['cover']:.2f}")
        print("-" * 30)


def enroll_customer():
    print("\n--- Enroll Customer ---")
    if len(policies) == 0:
        print("No policies available.")
        return

    view_policies()
    name = input("Enter customer name: ")
    age = int(input("Enter age: "))
    phone = input("Enter phone number: ")
    policy_id = int(input("Enter Policy ID to enroll: ")) - 1

    if policy_id < 0 or policy_id >= len(policies):
        print("Invalid Policy ID.")
        return

    selected = policies[policy_id]

    customer = {
        "id": len(customers) + 1,
        "name": name,
        "age": age,
        "phone": phone,
        "policy": selected["name"],
        "premium": selected["premium"],
        "payment": "Pending"
    }
    customers.append(customer)

    print(f"\nCustomer '{name}' enrolled in '{selected['name']}'!")
    print(f"Monthly Premium : INR {selected['premium']:.2f}")
    print(f"Coverage        : INR {selected['cover']:.2f}")


def view_customers():
    print("\n--- All Customers ---")
    if len(customers) == 0:
        print("No customers found.")
        return

    for c in customers:
        print(f"\nID       : {c['id']}")
        print(f"Name     : {c['name']}")
        print(f"Age      : {c['age']}")
        print(f"Phone    : {c['phone']}")
        print(f"Policy   : {c['policy']}")
        print(f"Premium  : INR {c['premium']:.2f}/month")
        print(f"Payment  : {c['payment']}")
        print("-" * 30)


def update_payment():
    print("\n--- Update Payment ---")
    if len(customers) == 0:
        print("No customers found.")
        return

    cid = int(input("Enter Customer ID: "))
    for c in customers:
        if c["id"] == cid:
            print(f"Current status: {c['payment']}")
            print("1. Paid\n2. Pending")
            ch = input("Choose: ")
            if ch == "1":
                c["payment"] = "Paid"
            else:
                c["payment"] = "Pending"
            print("Payment updated!")
            return

    print("Customer not found.")


def save_to_file():
    file = open("insurance_data.txt", "w")

    file.write("=== POLICIES ===\n")
    for p in policies:
        file.write(f"{p['id']},{p['name']},{p['duration']},{p['premium']},{p['cover']}\n")

    file.write("\n=== CUSTOMERS ===\n")
    for c in customers:
        file.write(f"{c['id']},{c['name']},{c['age']},{c['phone']},{c['policy']},{c['premium']},{c['payment']}\n")

    file.close()
    print("Data saved.")


def load_from_file():
    try:
        file = open("insurance_data.txt", "r")
        lines = file.readlines()
        file.close()

        section = None
        policies.clear()
        customers.clear()

        for line in lines:
            line = line.strip()
            if line == "=== POLICIES ===":
                section = "policies"
            elif line == "=== CUSTOMERS ===":
                section = "customers"
            elif line == "":
                continue
            elif section == "policies":
                p = line.split(",")
                policies.append({"id": int(p[0]), "name": p[1], "duration": int(p[2]),
                                  "premium": float(p[3]), "cover": float(p[4])})
            elif section == "customers":
                p = line.split(",")
                customers.append({"id": int(p[0]), "name": p[1], "age": int(p[2]),
                                   "phone": p[3], "policy": p[4], "premium": float(p[5]),
                                   "payment": p[6]})

        print("Data loaded.")

    except FileNotFoundError:
        print("No saved data. Starting fresh.")


def agent_menu():
    while True:
        print("\n==========================")
        print("        AGENT MENU        ")
        print("==========================")
        print("1. Add Policy")
        print("2. View Policies")
        print("3. View Customers")
        print("4. Update Payment")
        print("5. Save Data")
        print("6. Back")
        print("==========================")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_policy()
        elif choice == "2":
            view_policies()
        elif choice == "3":
            view_customers()
        elif choice == "4":
            update_payment()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def customer_menu():
    while True:
        print("\n==========================")
        print("      CUSTOMER MENU       ")
        print("==========================")
        print("1. View Policies")
        print("2. Enroll in Policy")
        print("3. Back")
        print("==========================")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            view_policies()
        elif choice == "2":
            enroll_customer()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


def main():
    load_from_file()

    while True:
        print("\n==========================")
        print("  LIFE INSURANCE SYSTEM   ")
        print("==========================")
        print("1. Agent")
        print("2. Customer")
        print("3. Exit")
        print("==========================")

        choice = input("Enter choice (1-3): ")

        if choice == "1":
            agent_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
