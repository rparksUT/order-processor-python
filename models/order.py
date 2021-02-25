class Order:
    """Class that represents the Order object."""
    def __init__(self, orderNum, description, customer, lineItems = None):
        self.orderNum = orderNum
        self.description = description
        self.customer = customer
        self.lineItems = lineItems or []
        self.subtotal = 0

    def calc_subtotal(self):
        subtotal = 0
        for item in self.lineItems:
            subtotal += item.unitCost * item.quantity
        self.subtotal = subtotal

    def get_invoice(self):
        """Generate the invoice details to return."""
        invoice = ''
        self.calc_subtotal()
        total = round(self.subtotal + (self.subtotal * 0.075), 2)
        invoice += f'\nCustomer Information:\n'
        invoice += f'Customer: \t {self.customer.firstName} {self.customer.lastName}\n'
        invoice += f'Email: \t {self.customer.email}\n'
        invoice += f'\nOrder Information:\n'
        invoice += f'Order #: \t {self.orderNum}\n'
        invoice += f'Description:\t {self.description}\n'

        invoice += f'\nLine Items:\n'
        counter = 0
        for item in self.lineItems:
            counter += 1
            invoice += f'Line Item #{counter}:\t'
            invoice += f'Part#: {item.partNum}, CostPerUnit($): ${item.unitCost}, Quantity: {item.quantity}\n'
        invoice += f'\nSubtotal = ${self.subtotal}\n'
        invoice += f'--------------------------------------------\n'
        invoice += f'Total(7.5% tax included) = ${total}\n'
        return invoice

class Customer:
    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

class OrderLineItem:
    def __init__(self, partNum, unitCost, quantity):
        self.partNum = partNum
        self.unitCost = unitCost
        self.quantity = quantity