from colorama import init, Fore, Style
from tqdm import tqdm
import time

# Initialize colorama
init(autoreset=True)

def show_progress():
    """Simulates a loading bar for conversions."""
    print(Fore.CYAN + "Processing your conversion... 🚀")
    for _ in tqdm(range(100), desc="Converting", ascii=True, colour="green"):
        time.sleep(0.01)

def unit_converter():
    print(Style.BRIGHT + Fore.YELLOW + "Welcome to the Unit Converter!")
    print(Fore.CYAN + "Choose the type of conversion you'd like to perform:")

    # Conversion options
    options = {
        1: "Kilometers to Miles",
        2: "Miles to Kilometers",
        3: "Celsius to Fahrenheit",
        4: "Fahrenheit to Celsius"
    }

    # Display options
    for key, value in options.items():
        print(f"{key}. {value}")

    try:
        choice = int(input(Fore.YELLOW + "\nEnter the number of your choice: "))

        if choice in options:
            value = float(input(Fore.GREEN + f"Enter the value to convert ({options[choice]}): "))
            
            # Show progress bar
            show_progress()

            if choice == 1:  # Kilometers to Miles
                result = value * 0.621371
                unit_from, unit_to = "Kilometers", "Miles"
            elif choice == 2:  # Miles to Kilometers
                result = value / 0.621371
                unit_from, unit_to = "Miles", "Kilometers"
            elif choice == 3:  # Celsius to Fahrenheit
                result = (value * 9/5) + 32
                unit_from, unit_to = "Celsius", "Fahrenheit"
            elif choice == 4:  # Fahrenheit to Celsius
                result = (value - 32) * 5/9
                unit_from, unit_to = "Fahrenheit", "Celsius"
            
            print(Fore.GREEN + f"\n✅ Conversion Completed!")
            print(Fore.YELLOW + f"{value} {unit_from} = {result:.2f} {unit_to}")
        else:
            print(Fore.RED + "Invalid choice! Please select a valid option.")

    except ValueError:
        print(Fore.RED + "Invalid input! Please enter a numeric value.")

def main():
    while True:
        unit_converter()
        retry = input(Fore.CYAN + "\nDo you want to perform another conversion? (yes/no): ").strip().lower()
        if retry != "yes":
            print(Fore.YELLOW + "Thank you for using the Unit Converter. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()