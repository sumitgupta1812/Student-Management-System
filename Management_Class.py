import Management_Database
class Management():

    def add_data(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone

    def display_data(self):
        print("Name of the employee is:",self.name)
        print("Address of the employee is:",self.address)
        print("Phone of the employee is:",self.phone)


    def save_details(self):
        Management_Database.save_records(self.name,self.address,self.phone)




    def display_details(self):
        return Management_Database.display_records()














