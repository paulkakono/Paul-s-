

def main():
    items = []

    while True:
        print("\n--- MENU ---")
        print("1. Add")
        print("2. View")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")

        match choice:
            case "1":
                item = input("Enter item to add: ")
                items.append(item)
                print(f"'{item}' added successfully.")
            case "2":
                if not items:
                    print("List is empty.")
                else:
                    print("\nItems:")
                    for index, item in enumerate(items, 1):
                        print(f"{index}. {item}")
            case "3":
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()