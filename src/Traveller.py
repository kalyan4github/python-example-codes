import mariadb

class Traveller:
    firstName = ''
    lastName =''
    city =''
    mobile =''
    email = ''

    def inputFromUser(self):
        Traveller.firstName = input("Enter First Name")
        Traveller.lastName = input("Enter Last Name")
        Traveller.city = input("Enter City")
        Traveller.mobile = input("Enter Mobile")
        Traveller.email = input("Enter Email")

    def displayTravellerData(self):
        print("First Name- ", Traveller.firstName)
        print("Last Name- ", Traveller.lastName)
        print("City- ", Traveller.city)
        print("Mobile No- ", Traveller.mobile)
        print("Email- ", Traveller.email)


    def getdbconnection(self):
        try:
            con = mariadb.connect(user="root",
                                  password="",
                                  host="localhost",
                                  port=3306,
                                  database="travellerdb")
            cursor = con.cursor()
            cursor.execute("INSERT INTO traveller (FIRST_NAME, LAST_NAME, CITY, MOBILE_NUMBER, EMAIL) VALUES (?, ?, ?, ?, ?)",
                           (Traveller.firstName,  Traveller.lastName, Traveller.city, Traveller.mobile, Traveller.email))
            con.commit()
            con.close()
        except mariadb.Error as e:
            print(f"Error connecting to DB..{e}")


t = Traveller()
t.inputFromUser()
t.displayTravellerData()
t.getdbconnection()
