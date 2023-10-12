## Restaurant Menu
# Define the Menu class
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name  # Name of the menu (e.g., "Brunch")
        self.items = items  # Dictionary of menu items and their prices
        self.start_time = start_time  # Start time in military time (e.g., 1100 for 11:00 AM)
        self.end_time = end_time  # End time in military time (e.g., 1600 for 4:00 PM)

    def __repr__(self):
        return f"{self.name} menu is available from {self.start_time} - {self.end_time}"

    def calculate_bill(self, purchased_items):
        """
        Calculate the total bill for a list of purchased items.
        
        Parameters:
        - purchased_items (list): A list of item names to be purchased.

        Returns:
        - total_price (float): The total price of the purchased items.
        """
        total_price = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                total_price += self.items[purchased_item]
        return total_price

# Define menu items and create Menu instances
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00} 
kids_menu = Menu('Kids', kids_items, 1100, 2100)

# Test the string representation and calculate_bill methods
print(brunch_menu)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

# Create a list of Menu instances
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

## Franchises
# Define the Franchise class
class Franchise:
    def __init__(self, address, menus):
        self.address = address  # Address of the franchise location
        self.menus = menus  # List of Menu instances available at the franchise

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        """
        Find the available menus at a given time.
        
        Parameters:
        - time (int): The time in military format (e.g., 1200 for 12:00 PM).

        Returns:
        - available_menus (list): A list of Menu instances available at the specified time.
        """
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

# Create two franchise instances
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)

# Test the available_menus method
print(flagship_store.available_menus(1200))

## Businesses
# Define the Business class
class Business:
    def __init__(self, name, franchises):
        self.name = name  # Name of the business
        self.franchises = franchises  # List of Franchise instances owned by the business

# Create a Business instance with two franchises
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Define the menu items for Take a' Arepa and create a Menu instance
arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)

# Create a franchise for Take a' Arepa
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# Create a Business instance for Take a' Arepa
arepa = Business("Take a' Arepa", [arepas_place])

# Print the menu of the Take a' Arepa franchise
print(arepa.franchises[0].menus[0])
