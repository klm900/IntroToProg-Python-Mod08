# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KLMartinez,12.13.21,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name

        product_price: (float) with the products's standard price
    methods:
        __str__(self): modified string method to display object
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class;
        KLMartinez,12.13.21,Modified code to complete assignment 8
    """
    # --- Fields ---
    #product_name = ''  # Not used - properties are used instead
    #product_price = ''

    # --- Constructor ---
    def __init__(self, product_name = 'null', product_price = 0):  # Initialize product object with name and price fields
        # --- Attributes ---
        self.__product_name = product_name  # Implicit fields name and price
        self.__product_price = product_price

    # --- Properties ---
    @property  # Getter for name
    def product_name(self):
        return str(self.__product_name).title()  # Display product names in title case
    @product_name.setter  # Setter for name
    def product_name(self, new_value):
        self.__product_name = str(new_value)  # Be sure the new value is a string

    @property  # Getter for price
    def product_price(self):
        return float(self.__product_price)  # Display product price as a floating point value
    @product_price.setter  # Setter for price
    def product_price(self, new_value):
        try:  # Check that the price can be converted to a floating point value
            self.__product_price = float(new_value)  # Store the price as a floating point value
        except ValueError:
            print('Product price can only contain numbers. Please try again')  # ValueError exception
    # --- Methods ---
    def __str__(self):  # Modify string method to display the object attributes, comma separated
        return self.product_name + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KLMartinez,12.13.21,Modified code to complete assignment 8
    """
    @staticmethod
    def read_data_from_file(file_name, list_of_objects):
        """ Reads data from a file into a list of product objects

        :param file_name: (string) with name of file:
        :param list_of_objects: (list) list of product objects to create using the data:
        :return: (list) of objects, populated from file
        """
        file = open(file_name, 'r')
        for line in file:
            name_read, price_read = line.split(",")
            objProduct = Product(name_read.strip(), price_read.strip())
            list_of_objects.append(objProduct)
        file.close()
        return list_of_objects

    @staticmethod
    def write_data_to_file(file_name, list_of_objects):
        """ Writes data from list of objects to the file

        :param file_name: (string) with name of file
        :param list_of_objects: (list) object data that will be saved to the file
        :return: nothing
        """
        file = open(file_name, "w")
        for row in list_of_objects:  # For each object, write the values (comma separated)
            file.write(str(row) + '\n')
        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs input and output tasks:

    methods:
        output_welcome():

        output_menu():

        output_current_products(list_of_objects):

        output_exit_confirmation():

        input_menu_choice(): -> (choice; string)

        input_new_product(): -> (name_add, price_add; tuple with new product info)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        KLMartinez,12.13.21,Modified code to complete assignment 8
    """

    @staticmethod
    def output_welcome():
        """  Display the description of the program to the user

        :return: nothing
        """
        print('\nWelcome to the Product program! \n'
              'This program keeps an inventory of products and their standard prices.')
        # print()  # Extra line

    @staticmethod
    def output_menu():
        """  Display the program menu to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) View current product list
        2) Add a new product
        3) Save list and exit program
        ''')

    @staticmethod
    def output_current_products(list_of_objects):
        """ Shows the current products in the list of product objects

        :param list_of_objects: (list) of objects you want to display
        :return: nothing
        """
        print('Current product names and standard prices:')
        for objProduct in list_of_objects:  # Use string method from Product class to print objects
            print(objProduct)

    @staticmethod
    def output_exit_confirmation():
        """ Shows the user that the list was saved, and says goodbye

        :return: nothing
        """
        print('Product list saved. Goodbye!')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from the user

        :return: string
        """
        choice = str(input('Which option would you like to perform (1, 2, or 3)?: ')).strip()
        print()  # Extra line for looks
        return choice

    @staticmethod
    def input_new_product():
        """ Gets a new product name and price from the user

        :return: (tuple) with name and price entered by the user
        """
        print('Enter the product name and standard price.')
        name_add = input('Product name: ')  # User enters a name
        price_add = input('Standard price (enter only numbers): ')  # User enters a price (float enforced in data class)
        #print()  # Extra line
        return name_add, price_add

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

IO.output_welcome()  # Display program description

# Load each line from the text file to an object, add to list of product objects
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

# Display menu of options
while (True):
    IO.output_menu()  # Display menu of options
    userChoice = IO.input_menu_choice()  # Get user menu choice

    if userChoice == '1':  # User selection 1: View current product list
        IO.output_current_products(lstOfProductObjects)
        continue  # to show the menu

    elif userChoice == '2':  # User selection 2: Add a new product
        name_add, price_add = IO.input_new_product()  # Capture user-entered name and price
        objProductAdd = Product()  # Initialize new product object with the default values
        objProductAdd.product_name = name_add  # Try setting the name to the user-entered value
        try:
            objProductAdd.product_price = price_add  # Try setting the name to the user-entered value
        except ValueError as e:  # Raise exception if the price is non-numeric
            print(e)
        if objProductAdd.product_price != 0:  # Check if product_price is not 0
            lstOfProductObjects.append(objProductAdd)  # Append new object to list of product objects
        else:
            continue  # If 0, move on without appending the partially updated object to the list

    elif userChoice == '3':  # User selection 3: Save list and exit program
        FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)  # Write list of product objects to txt file
        IO.output_exit_confirmation()  # Print save & exit confirmation
        break  # Exit program

# Main Body of Script  ---------------------------------------------------- #