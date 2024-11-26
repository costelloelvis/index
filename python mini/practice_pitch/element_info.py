import periodictable

def get_element_info(symbol):
    try:
        element = periodictable.elements.symbol(symbol)
        print(f"Element: {element.name}")
        print(f"Symbol: {element.symbol}")
        print(f"Atomic Number: {element.number}")
        print(f"Atomic Mass: {element.mass}")
        print(f"Density: {element.density}")
    except ValueError:
        print("Invalid element symbol.")

def main():
    element_symbol = input("Enter the symbol of the element: ")
    get_element_info(element_symbol)

if __name__ == "__main__":
    main()
