from models.order import Order, Customer, OrderLineItem

class Program:
    """Class where the application starts up"""
    def main(self):
        """Application starts here."""
        print('Welcome to Vader\'s dark side Imperium, what items would you like?')
        customer = self.get_customer_details()
        order = self.get_order_details(customer)
        lineItems = self.get_order_items()
        order.lineItems = lineItems
        # Display the invoice details
        print('\nInvoice Details\n')
        invoice = order.get_invoice()
        print(invoice)

    def get_customer_details(self):
        print('Please provide the following customer information: ')
        firstName = input('Enter first name: ')
        lastName = input('Enter last name: ')
        email = input('Enter customer email address ')
        return Customer(firstName, lastName, email)

    def get_order_details(self, customer):
        print('Order Information:')
        orderNumber = input('Enter the order #: ')
        description = input('Enter the order description: ')
        return Order(orderNumber, description, customer)

    def get_order_items(self):
        lineItems = []
        numOfLineItems = int(input('How many line items will need to be included on this order? '))
        counter = 1
        while counter <= numOfLineItems:
            print(f'Please enter the line item information for line item #{counter}')
            partNumber = input('Enter the part #: ')
            cost = float(input('Enter the cost per unit: '))
            quantity = float(input('Enter the number of items to include: '))
            lineItems.append(OrderLineItem(partNumber, cost, quantity))
            counter += 1
        return lineItems

if __name__ == '__main__':
    program = Program()
    program.main()