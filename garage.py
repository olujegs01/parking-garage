class ParkingGarage:
    def __init__(self, total_spaces):
        self.tickets = [i for i in range(1, total_spaces + 1)] 
        self.parking_spaces = [i for i in range(1, total_spaces + 1)] 
        self.current_ticket = {}  

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)  
            space = self.parking_spaces.pop(0)  
            self.current_ticket[ticket] = {"paid": False, "space": space}  
            print(f"Ticket {ticket} has been issued. Parking space {space} is allocated.")
        else:
            print("Sorry, the parking garage is full.")

    def payForParking(self, ticket):
        if ticket in self.current_ticket and not self.current_ticket[ticket]["paid"]:
            amount = input("Please enter the amount to pay: ")
            if amount:
                print("Your ticket has been paid. You have 15 minutes to leave.")
                self.current_ticket[ticket]["paid"] = True
            else:
                print("Payment cannot be empty.")
        else:
            print("Invalid ticket number or ticket already paid.")

    def leaveGarage(self, ticket):
        if ticket in self.current_ticket:
            if self.current_ticket[ticket]["paid"]:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.current_ticket[ticket]["space"])  
                self.tickets.append(ticket)  
                del self.current_ticket[ticket]  
            else:
                print("Please pay for parking before leaving.")
        else:
            print("Invalid ticket number.")

