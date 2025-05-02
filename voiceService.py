def package_options(data):
    """Display available packages in a formatted way"""
    for item in data["packages"]:
        print(f"{item['id']}. {item['description']} for {item['price']} (valid {item['validity']})")

def process_package_selection(data):
    """Handle package selection and purchase process"""
    while True:
        try:
            print(f"\n{data['category'] if 'category' in data else data['name']}:")
            package_options(data)
            max_id = max(pkg['id'] for pkg in data['packages'])
            user_choice = int(input(f"Select an option (1-{max_id}) or 0 to exit: "))
            
            if user_choice == 0:
                print(f"Exiting package selection...")
                return False
            
            selected = next((item for item in data['packages'] if item["id"] == user_choice), None)
            if selected is None:
                print("Invalid selection, please try again")
                continue
            
            print(f"\nSelected: {selected['description']} for {selected['price']}")
            
            while True:
                print("\nConfirm Purchase:")
                print("1. Confirm purchase")
                print("2. Choose another package")
                print("3. Exit to main menu")
                
                try:
                    confirm = int(input("Enter your choice: "))
                    
                    if confirm == 1:
                        print(f"Successfully purchased {selected['description']} package!")
                        print("Thank you for your purchase!")
                        return True
                    elif confirm == 2:
                        break  # Back to package selection
                    elif confirm == 3:
                        return False  # Exit to main menu
                    else:
                        print("Invalid choice, please try again")
                except ValueError:
                    print("Please enter a valid number!")
        except ValueError:
            print("Please enter a valid number!")

def data_package_menu(data):
    """Handle data package category selection"""
    while True:
        print("\nData Package Categories:")
        for i, category in enumerate(data["categories"], 1):
            print(f"{i}. {category['name']}")
        print("0. Back to main menu")
        
        try:
            selected = int(input("\nSelect a category: "))
            if selected == 0:
                break
            elif 1 <= selected <= len(data["categories"]):
                process_package_selection(data["categories"][selected-1])
            else:
                print("Invalid selection, please try again")
        except ValueError:
            print("Please enter a valid number!")

def main_menu():
    """Main menu for all package types"""
    while True:
        print("\nEthio Telecom Package Selection")
        print("1. Data Packages")
        print("2. SMS Packages")
        print("3. Voice Packages")
        print("0. Exit")
        
        try:
            choice = int(input("Select service type: "))
            if choice == 0:
                print("Thank you for using Ethio Telecom services!")
                break
            elif choice == 1:
                data_package_menu(data_packages)
            elif choice == 2:
                data_package_menu(sms_packages)  # Now uses same structure as data
            elif choice == 3:
                data_package_menu(voice_packages)  # Now uses same structure as data
            else:
                print("Invalid selection, please try again")
        except ValueError:
            print("Please enter a valid number!")
# Package data structures
data_packages = {
    "categories": [
        {
            "name": "Daily Data Packages",
            "packages": [
                {"id": 1, "description": "25MB", "price": "5 Birr", "validity": "1 day"},
                {"id": 2, "description": "75MB", "price": "10 Birr", "validity": "1 day"},
                {"id": 3, "description": "150MB", "price": "20 Birr", "validity": "1 day"},
                {"id": 4, "description": "500MB", "price": "50 Birr", "validity": "1 day"}
            ]
        },
        {
            "name": "Weekly Data Packages",
            "packages": [
                {"id": 5, "description": "1GB", "price": "100 Birr", "validity": "7 days"},
                {"id": 6, "description": "2GB", "price": "150 Birr", "validity": "7 days"}
            ]
        },
        {
            "name": "Monthly Data Packages",
            "packages": [
                {"id": 7, "description": "4GB", "price": "200 Birr", "validity": "30 days"},
                {"id": 8, "description": "10GB", "price": "400 Birr", "validity": "30 days"},
                {"id": 9, "description": "20GB", "price": "700 Birr", "validity": "30 days"},
                {"id": 10, "description": "50GB", "price": "1200 Birr", "validity": "30 days"}
            ]
        }
    ]
}

sms_packages = {
    "categories": [
        {
            "name": "Daily SMS Packages",
            "packages": [
                {"id": 1, "description": "10 SMS", "price": "2 Birr", "validity": "1 day"},
                {"id": 2, "description": "20 SMS", "price": "4 Birr", "validity": "1 day"}
            ]
        },
        {
            "name": "Weekly SMS Packages",
            "packages": [
                {"id": 3, "description": "50 SMS", "price": "8 Birr", "validity": "7 days"},
                {"id": 4, "description": "100 SMS", "price": "15 Birr", "validity": "7 days"}
            ]
        },
        {
            "name": "Monthly SMS Packages",
            "packages": [
                {"id": 5, "description": "200 SMS", "price": "30 Birr", "validity": "30 days"},
                {"id": 6, "description": "500 SMS", "price": "60 Birr", "validity": "30 days"}
            ]
        }
    ]
}

voice_packages = {
    "categories": [
        {
            "name": "Daily Voice Packages",
            "packages": [
                {"id": 1, "description": "10 minutes", "price": "5 Birr", "validity": "1 day"},
                {"id": 2, "description": "20 minutes", "price": "8 Birr", "validity": "1 day"}
            ]
        },
        {
            "name": "Weekly Voice Packages",
            "packages": [
                {"id": 3, "description": "60 minutes", "price": "20 Birr", "validity": "7 days"},
                {"id": 4, "description": "120 minutes", "price": "35 Birr", "validity": "7 days"}
            ]
        },
        {
            "name": "Monthly Voice Packages",
            "packages": [
                {"id": 5, "description": "300 minutes", "price": "80 Birr", "validity": "30 days"},
                {"id": 6, "description": "600 minutes", "price": "150 Birr", "validity": "30 days"}
            ]
        }
    ]
}
# Start the application
if __name__ == "__main__":
    main_menu()