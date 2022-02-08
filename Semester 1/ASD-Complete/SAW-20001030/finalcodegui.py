###################################################################################################
# SAW ACCOMODATION SYSTEM
# UWE Advanced Software Development Coursework.
# Ashley Pearson - 20001030
# William Robertson - 20005074
# Sonia Tadlaoui - 21039395
#

# All code written and implemented by above members, with the exception of the below package imports
###################################################################################################


# Necessary imports for correct functioning.


# Date time used for date calculations
import datetime
from datetime import date

# Sqlite3 used for database connections
import sqlite3
from sqlite3.dbapi2 import Connection

# Tkinter used as the main GUI throughout.
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import GROOVE, RAISED, RIGHT

# platform used to provide tailored experiance based on platform
import platform

# Dateutil used to calculate date differences based on calender entries.
from dateutil.relativedelta import relativedelta

# Tkcalender used to provide date entry boxes.
from tkcalendar.dateentry import DateEntry

# Random used to create student ids.
import random

# Garbage collector used to loop through all class instances.
import gc

# Unless clearly stated otherwise, '.get____()' methods are used to return an existing value within an object, and '.set_____()' methods are used to add/change the atttribute.

# Declare colors for regular use throughout program
color1 = "#632150"
color2 = "#b4a7d6"

# Define user class which will be inherited by hall manager and warden.


class User:
    # Hold all halls created.
    Halls = []
    # All values must be determined at initiation.

    def __init__(self, userName, password, ID, name):
        # Username and password used for login
        self.userName = userName
        self.password = password
        # Clearance level determines privalleges, admin=0, hall manager= 1 Warden = 2
        self.clearanceLevel = self.clearanceLevel
        # ID of staff member.
        self.ID = ID
        # Name of staff member.
        self.name = name

    # Getters to return above values to avoid direct access, self ensures that particular instances are editted, not the class.
    # These getters can be accessed by all child classes.
    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    def getClearanceLevel(self):
        return self.clearanceLevel

    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def getHalls(self):
        return self.Halls


# Hall manager inherits from above user.
class HallManager(User):
    # All hall managers have an auto assigned clearance of 1.
    clearanceLevel = 1
    # Super is called for the init method to avoid code redundancy.

    def __init__(self, userName, password, ID, name):
        super().__init__(User, self, ID, name)
        self.userName = userName
        self.password = password


# TheWarden also inherits from User.
class TheWarden(User):
    # Clearance level of 2.
    clearanceLevel = 2
    # Super is used again to use the User init method.

    def __init__(self, userName, password, ID, name):
        super().__init__(User, self, ID, name)
        self.userName = userName
        self.password = password
        self.name = name
        # Accomodation office class has a "number of wardens" counter, which is incremented upon creation of new wardens.
        UWEBristolAccomodationOffice.wardens += 1


# Uwe accomodation office is the admin class and has a "superset view" able to perform the functions of both hall manager and warden.
class UWEBristolAccomodationOffice(HallManager):
    # Clearance level 0= full access.
    clearanceLevel = 0
    # Counter of wardens, incremented by the warden init method automatically.
    wardens = 0

    # Default values as there is only one instance of this class.
    def __init__(self):
        super().__init__("ADMIN", "ADMINPASSWORD", 101, "Uwe Accomodation Office")

    # Method to add a hall and all required values.
    def addHall(hall, name, number, teleNumber, address):
        hall = Hall(name, number, teleNumber, address)

    # Method to add a warden and all required values.
    def addWarden(warden, userName, password, ID, name):
        warden = TheWarden(userName, password, ID, name)

    # Method to add a manager and all required values.
    def addManager(manager, userName, password, ID, name):
        manager = HallManager(userName, password, ID, name)


# Hall class
class Hall:
    # Init method with all required values.
    def __init__(self, name, number, teleNumber, address):
        self.name = name
        self.number = number
        self.teleNumber = teleNumber
        self.address = address
        # Create a list within each hall instance to contain all rooms in that hall.
        self.rooms = []
        # Append this hall to the list of Halls at admin level upon creation
        User.Halls.append(self)

    def getNumberOfRooms(self):
        return len(self.rooms)

    def getName(self):
        return self.name

    def getNumber(self):
        return self.number

    def getTeleNumber(self):
        return self.teleNumber

    def getAddress(self):
        return self.address

    def getRooms(self):
        return self.rooms

    # Add a room to the hall, also appends the room to the 'rooms' list.
    def addRoom(self, roomNumber, rentalRate):
        roomNumber = Room(roomNumber, rentalRate)
        self.rooms.append(roomNumber)

    # Function for testing purposes, creates a user defined number of rooms with a value randomly selected from a list of sensible rental rates.
    # This function could be called upon the creation of a new halls to easily create x number of rooms with a defined rental rate.
    def pop_rooms(self, num):
        roomsval = [400, 450, 500, 550, 600]
        for x in range(1, num + 1):
            name = Room(x, random.choice(roomsval))
            self.rooms.append(name)

    # Function to print all keys attribute of all rooms in a given hall.
    def list(self):
        rooms = []
        for x in self.rooms:
            print(
                x.leaseID,
                x.roomNumber,
                x.rentalRate,
                x.cleaningStatus,
                x.occupancyStatus,
            )
            rooms.append(x)
        # Returns a list of all details.
        return rooms


# Room class
class Room:
    # Cleaning status defaults to clean.
    cleaningStatus = "Clean"
    # Occupancy defaults to false ie. available.
    occupancyStatus = False
    # No lease is assigned upon creation
    roomLease = None
    leaseID = None
    # Init method

    def __init__(self, roomNumber, rentalRate):
        self.roomNumber = roomNumber
        self.rentalRate = rentalRate

    def setCleaningStatus(self, x):
        self.cleaningStatus = x

    def getCleaningStatus(self):
        return self.cleaningStatus

    def getRoomNumber(self):
        return self.roomNumber

    def getOccupancyStatus(self):
        return self.occupancyStatus

    # Method to assign a lease to a class.
    def addLease(self, startDate, endDate, studentName, studentID, leaseDuration):
        # Create a student record based on the student details provided during init.
        StudentRecord(studentName, studentID)
        # create a lease object using the details provided.
        roomLease = Lease(startDate, endDate, studentName,
                          studentID, leaseDuration)
        # LeaseID associated with a room is tied to the roomLease created above and its leasenum, acting as a key.
        self.leaseID = roomLease.leaseNum
        self.roomLease = roomLease
        # If a lease ID is present in a room(ie as created 2 lines above) rooms occupancy status is set to true(room is occupied.)
        if self.leaseID != None:
            self.occupancyStatus = True
        self.leaseDuration = leaseDuration

    def getLeaseID(self):
        return self.leaseID

    def getLease(self):
        return self.roomLease

    def getRentalRate(self):
        return self.rentalRate

    # function to delete a lease.
    def deleteLease(self):
        # set rooms leaseID
        self.leaseID = None
        self.roomLease = None
        # As leaseID is deleted, occupancy status is set to false(rooms is available)
        if self.leaseID == None:
            self.occupancyStatus = False
        # Use garbage collector to loop through all instances of Lease.
        for obj in gc.get_objects():
            if isinstance(obj, Lease):
                # When a matching Lease object is found (using the above defined 'key', delete the lease.)
                if Lease.leaseNum == self.leaseID:
                    del obj

    # function to return if a room has a lease or not, returns boolean value.
    def hasLease(self):
        if self.roomLease == None:
            return False
        else:
            return True


# Student record class.
class StudentRecord:
    def __init__(self, studentName, studentID):
        self.studentName = studentName
        self.studentID = studentID

    def getStudentName(self):
        return self.studentName

    def getStudentID(self):
        return self.studentID

    def setStudentName(self, x):
        self.studentName = x


# Lease class.
class Lease:
    # Lease number defaults to 0 at runtime.
    leaseNum = 0
    # Init method for Lease class.

    def __init__(self, startDate, endDate, studentName, studentID, leaseDuration):
        # Create a student record upon lease creation.
        self.studentDetails = StudentRecord(studentName, studentID)
        # Increment lease counter automatically, ensuring no 2 leases can have the same ID number.
        Lease.leaseNum += 1
        self.startDate = startDate
        self.endDate = endDate
        self.leaseDuration = leaseDuration

    def getStartDate(self):
        return self.startDate

    def getStudentRecord(self):
        return self.studentDetails

    def getLeaseID(self):
        return self.leaseNum

    def getEndDate(self):
        return self.endDate

    def setStartDate(self, x):
        self.startDate = x

    def setEndDate(self, x):
        self.endDate = x

    def getLeaseDuration(self):
        return self.leaseDuration

    def setLeaseDuration(self, x):
        self.leaseDuration = x


# The below instances are created for testing purposes and demonstrate the use of classes throughout, these instances are to be replaced with legitimate classes on deployment.

# Create a "HallManager" instance, as per the init method.
Manager = HallManager("TheManager", "ManagerPassword", 201, "ManagerName")

# Create 3 halls as per the Hall init method.
Wallscourt = Hall("Wallscourt", 1, "0117 123 456", "Wallscourt Test Address")
Brecon = Hall("Brecon", 2, "0117 123 123", "Brecon Test address")
Cotswold = Hall("Cotswold", 3, "0117 123 567", "Cotswold Test address")

# Create 3 Warden objects as per the init method in TheWarden
Ash = TheWarden("WardenAsh", "AshPassword", 1, "Ash")
Will = TheWarden("WardenWill", "WillPassword", 2, "Will")
Sonia = TheWarden("WardenSonia", "SoniaPassword", 3, "Sonia")

# Create Admin user, with attributes defined in the init method.
UWE = UWEBristolAccomodationOffice()

# Create empty array to hold all wardens usernames, passwords and clearancelevels
j = []
# Loop through all TheWarden objects and add to array.
for obj in gc.get_objects():
    if isinstance(obj, TheWarden):
        j.append([obj.getUserName(), obj.getPassword(), obj.getClearanceLevel()])

# Loop through all HallManagers and add username, password and clearance level.
for obj in gc.get_objects():
    if isinstance(obj, HallManager):
        j.append([obj.getUserName(), obj.getPassword(), obj.getClearanceLevel()])

# Create array to hold warden ID, Username and names.
k = []
for obj in gc.get_objects():
    if isinstance(obj, TheWarden):
        k.append([obj.getID(), obj.getUserName(), obj.getName()])

# Populate the above halls with the respective number of rooms.
Wallscourt.pop_rooms(10)
Cotswold.pop_rooms(12)
Brecon.pop_rooms(14)

# Establish DB  connection
db = sqlite3.connect("SAW.db")
Connection = db.cursor()

# Connection.execute('''DROP TABLE User''')

# If table doesnt exist, create to store username, password and clearance level.
Connection.execute(
    """CREATE TABLE if not exists User (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                Clearance_level INTEGER NOT NULL)
                """
)
# If table doesnt exist, create to store Warden ID, Username and name level.
Connection.execute(
    """CREATE TABLE if not exists Warden (
                W_ID INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                name TEXT NOT NULL,
                FOREIGN KEY (username) REFERENCES User (username))
                """
)
# Insert all values from the J array into user table.
Connection.executemany("""INSERT INTO User VALUES(?,?,?)""", j)
Connection.execute(("""SELECT * FROM User"""))
Variable = Connection.fetchall()
# Insert all values from K array into Warden Table.
Connection.executemany("""INSERT INTO Warden VALUES(?,?,?)""", k)
Connection.execute(("""SELECT * FROM Warden"""))
Variable = Connection.fetchall()

# Main GUI page, two arguements are passed in, row(Warden/HallManager/AccomodationOffice objects) and the clearance level.


def Admin_Page(row, userlevel):
    print(userlevel)
    global textbox
    # Logout function, destorys the main page and opens the login page.

    def logout():
        Admin_Page.destroy()
        login_page()

    # Create main window of GUI.
    Admin_Page = tk.Tk()
    # Define dimensions of window.
    Admin_Page_width = 620
    Admin_Page_height = 700
    # Get Screen dimensions of device.
    screen_width = Admin_Page.winfo_screenwidth()
    screen_height = Admin_Page.winfo_screenheight()
    # Get the center of the screen.
    centerx = int(screen_width / 2 - Admin_Page_width / 2)
    centery = int(screen_height / 2 - Admin_Page_height / 2)
    # Set the window to a fixed size, with no resize ability for viewing consistency.
    Admin_Page.minsize(width=Admin_Page_width, height=Admin_Page_height)
    Admin_Page.maxsize(width=Admin_Page_width, height=Admin_Page_height)
    # titles the window based on username
    Admin_Page.title(row[0] + "'s Home Page")
    # Set window to open in the centre of the screen.
    Admin_Page.geometry(
        f"{Admin_Page_width}x{Admin_Page_height}+{centerx}+{centery}")
    # set background colour of window.
    Admin_Page.configure(background=color1)

    # Set style of custom widgets in ttk
    style = ttk.Style(Admin_Page)
    # Check if platform is mac, if so set most user friendly theme.
    if platform.system() == "Darwin":
        # Edit date widgets on mac to make it viewable due to known compatibility issues on the platform.
        style.theme_use("alt")
        style.configure("DateEntry", foreground="black")
        print("Yup mac")
    # If OS is detected as windows, use appropriate windows based theme.
    else:
        style.theme_use("winnative")
        print("Not a mac ")

    # Define Top frame of GUI, pass in username.
    def TopFrames(row):
        # Anchor top frame to Admin Page.
        TopFrame = Frame(Admin_Page, background=color1)
        # Pack is used regularly as the geometry manager to place widgets within the GUI.
        TopFrame.pack()
        # Create label with custom settings at the top of the window.
        title = tk.Label(
            TopFrame,
            text="SAW Accomodation",
            foreground="white",
            background=color1,
            width=30,
            height=1,
            font=("calibri 11 bold"),
        )
        # Pady provide yaxis padding for spacing, padx is also used throughout, Side sets location with frames.
        title.pack(pady=2, side=LEFT)

        # Create a personalise title, welcoming the specific user by name for ID purposes and tailored experiance.
        title2 = tk.Label(
            TopFrame,
            text="Welcome  | " + row[0] + " |",
            foreground="white",
            background=color1,
            width=30,
            height=1,
            font=("calibri 11 bold"),
        )
        title2.pack(pady=2, side=LEFT)
        # Create logout button
        logoutbutton = tk.Button(
            TopFrame,
            text="Logout",
            # Command executes the function 'logout' defined above on click.
            command=logout,
            background="white",
            highlightbackground=color1,
            foreground="black",
        )
        logoutbutton.pack(side=RIGHT)
        # Quit button close app on click.
        QuitButton = tk.Button(
            TopFrame,
            text="Quit",
            command=Admin_Page.destroy,
            background="white",
            highlightbackground=color1,
            foreground="black",
        )
        QuitButton.pack(pady=2, side=RIGHT)

    # Middle farmes, userlevel passed in
    def MiddleFrames(userlevel):
        # Style choices below are for aesthetic reasons and create the GUI appearance.
        Mainframe = Frame(
            Admin_Page,
            background="white",
            highlightthickness=2,
            highlightbackground="black",
            pady=10,
            padx=5,
        )
        Mainframe.pack(pady=3)
        # Hall frame

        def HallFrames():
            global textbox
            # Define Hall frame attributes
            HallFrame = Frame(
                Mainframe,
                background=color2,
                width=550,
                height=100,
                highlightthickness=2,
                highlightbackground="black",
            )
            HallFrame.pack(pady=10)
            # Create left hall frame anchored to HallFrame
            LeftHallFrame = Frame(HallFrame, background=color2)
            LeftHallFrame.pack(pady=15, side=LEFT)
            # Select Hall title
            HallTitle = tk.Label(
                LeftHallFrame,
                text="Select Hall",
                font="calibri 13 underline bold",
                foreground="black",
                background=color2,
                width=32,
                height=1,
            )
            HallTitle.pack()
            # Create a copy of halls array
            HallsList1 = User.Halls
            # Create an empty array and add names of halls to list
            HallsList = []
            for x in HallsList1:
                HallsList.append(x.name)
            # Create a StringVar for self updating data.
            Hall_Chosen = tk.StringVar()
            # Default Hall_chosen to item no 1.
            Hall_Chosen.set(HallsList[1])

            # Declare chosenHall as global for access throughout program
            global chosenHall
            # Eval chosenHall to take the actual data for execution
            chosenHall = eval(Hall_Chosen.get())
            # Create Right Hall frame and attach to the right side of Hall Frame.
            RightHallFrame = Frame(HallFrame, background=color2)
            RightHallFrame.pack(pady=15, side=RIGHT)
            # Create dropdown box that contains halls list, on command PickedHall(below) is executed.
            Combo = tk.OptionMenu(
                LeftHallFrame, Hall_Chosen, *HallsList, command=PickedHall
            )
            # Alter style for visibilty on mac
            Combo.configure(foreground="black")
            Combo.pack(padx=5, pady=5)
            # Create a textbox as stringvar that contains the selected halls name, address and telephone number, dynamically updates.
            textbox = tk.StringVar(
                RightHallFrame,
                "Hall Name:  "
                + str(chosenHall.getName())
                + "\nHall Address:  "
                + str(chosenHall.getAddress())
                + "\nPhone Number:  "
                + str(chosenHall.getTeleNumber()),
            )
            # Style the above textbox and pack on screen.
            T = Label(
                RightHallFrame,
                font="calibri 10 bold",
                foreground="black",
                background=color2,
                width=32,
                height=4,
                relief=FLAT,
                textvariable=textbox,
            )
            T.pack(padx=25)
            # Return Hall_chosen for use.
            return Hall_Chosen

        # Define picked hall function
        def PickedHall(b):
            # Use global textbox and chosenhall
            global textbox, chosenHall
            chosenHall = eval(Hall_Chosen.get())

            Hall = chosenHall
            # Create empty array to hold Hall rooms data.
            data = []
            # initialise a counter for looping through array.
            count = 0
            # Clear treeview list.
            for item in RoomList.get_children():
                RoomList.delete(item)
            # Loop through all rooms in a hall.
            for x in Hall.getRooms():
                # If room is unoccupied:
                if x.hasLease() == False:
                    # Add data for list view
                    data.append(
                        [
                            # Get rooms number
                            x.getRoomNumber(),
                            # Get Hall Number
                            Hall.getNumber(),
                            # Print Available
                            "Available",
                            # Print student name - N/A
                            "N/A ",
                            # Print Rooms rental rate as string
                            "£" + str(x.getRentalRate()),
                            # get occupancy status
                            x.getOccupancyStatus(),
                            # get cleaningstatus.
                            x.getCleaningStatus(),
                        ]
                    )
                # If room does have a lease:
                else:
                    data.append(
                        [
                            # Get room number
                            x.getRoomNumber(),
                            # Get Hall Number
                            Hall.getNumber(),
                            # Get lease id
                            x.getLeaseID(),
                            # Get student name associated with room.
                            x.getLease().getStudentRecord().getStudentName(),
                            # get rental rate as string
                            "£" + str(x.getRentalRate()),
                            # Get occupancy status
                            x.getOccupancyStatus(),
                            # get cleaning status
                            x.getCleaningStatus(),
                        ]
                    )
            # Loop through data array and insert into roomlist.
            for record in data:
                RoomList.insert(
                    parent="",
                    index="end",
                    iid=count,
                    text="",
                    values=(
                        record[0],
                        record[1],
                        record[2],
                        record[3],
                        record[4],
                        record[5],
                        record[6],
                    ),
                )
                # Increment counter
                count = count + 1
            # update text for use in textbox
            text = (
                "Hall Name:  "
                + str(Hall.getName())
                + "\nHall Address:  "
                + str(Hall.getAddress())
                + "\nHall Telephone Number:  "
                + str(Hall.getTeleNumber())
            )
            global textbox
            # set textbox to contain above text
            textbox.set(text)
            # Set norooms variable to contain the number of rooms in selected hall.
            norooms.set(
                "Total number of rooms in "
                + Hall.getName()
                + ": "
                # Use length of hall array to get number of rooms
                + str(len(Hall.rooms))
            )
            # Set a lease counter to 0
            leases = 0
            # Loop through chosen hall, if a room has a lease, increment counter.
            for x in chosenHall.getRooms():
                if x.hasLease() == True:
                    leases += 1
            # Create lease variable which calculates free rooms based on norooms-leases.
            lease = len(Hall.rooms) - leases

            # Set nolease text to contain the number of rooms available to let.
            noleases.set(
                "Total number of free rooms in "
                + chosenHall.getName()
                + ": "
                + str(lease)
            )

        # Create roomframes function.
        def RoomFrames():
            # Create roomframe, frame.
            RoomFrame = Frame(
                Mainframe,
                background=color2,
                width=550,
                height=175,
                highlightthickness=2,
                highlightbackground="black",
            )
            RoomFrame.pack(pady=10, padx=5)
            # Create toproom frame anchored to roomframe
            TopRoomFrame = Frame(
                RoomFrame, background=color2, width=550, height=175)
            TopRoomFrame.pack()
            # Create left room frame, anchored to top room frame
            LeftRoomFrame = Frame(
                TopRoomFrame, background=color2, width=550, height=175
            )
            LeftRoomFrame.pack(pady=20, padx=30, side=LEFT)
            # Create rightroomframe anchored to toproomframe
            RightRoomFrame = Frame(
                TopRoomFrame, background=color2, width=550, height=175
            )
            RightRoomFrame.pack(pady=10, padx=30, side=RIGHT)
            # Create table room frame
            TableRoomFrame = Frame(
                RoomFrame, background=color2, width=550, height=175)
            TableRoomFrame.pack(pady=1, padx=20)
            # Create 'Select room' title
            RoomTitle = tk.Label(
                LeftRoomFrame,
                text="Select Room",
                font="calibri 13 underline bold",
                foreground="black",
                background=color2,
                width=20,
                height=1,
            )
            RoomTitle.pack()
            # Declare Globals for further use.
            global norooms, noleases, chosenHall
            # create number of rooms variable.
            norooms = StringVar(
                RightRoomFrame,
                "Total number of rooms in: " +
                str(chosenHall.getNumberOfRooms()),
            )
            leases = 0
            # Create number of rooms available variable as default.
            for x in chosenHall.getRooms():
                if x.hasLease() == True:
                    leases += 1
            lease = chosenHall.getNumberOfRooms() - leases
            # Create number of free rooms variable default value.
            noleases = StringVar(
                RightRoomFrame,
                "Total number of free rooms in "
                + chosenHall.getName()
                + ": "
                + str(lease),
            )
            # Create number of rooms label to contain no of rooms.
            HallNomRooms = tk.Label(
                RightRoomFrame,
                textvariable=norooms,
                font="calibri 10 bold",
                foreground="black",
                background=color2,
                width=35,
                height=1,
            )
            HallNomRooms.pack()

            # Create number of free rooms label to contain no of free rooms.
            HallNomLeases = tk.Label(
                RightRoomFrame,
                textvariable=noleases,
                font="calibri 10 bold",
                foreground="black",
                background=color2,
                width=35,
                height=1,
            )
            HallNomLeases.pack()

            # ================================================================================================
            # Below this is the main Treeview, displaying all fetched room data.
            # ================================================================================================

            # Set scrollbar within treeview to allow for scrolling through larger lists.
            room_scroll = Scrollbar(TableRoomFrame)
            style = ttk.Style()
            Hall = chosenHall
            # Set style of treeview, primarily for easier viewing on mac.
            style.configure("Treeview", background="white",
                            fieldbackground="white")
            # Set colour of highlighted row for aesthetics and viewability
            style.map("Treeview", background=[("selected", color1)])

            # Create Treeview
            RoomList = ttk.Treeview(
                TableRoomFrame,
                # Allow scrolling
                yscrollcommand=room_scroll.set,
                xscrollcommand=room_scroll.set,
            )
            # Create empty data array
            data = []
            # Initialise a counter for looping through array.
            count = 0
            # Clear treeview list.
            for item in RoomList.get_children():
                RoomList.delete(item)
            # Loop through all rooms in a hall.
            for x in Hall.getRooms():
                # If room is unoccupied:
                if x.hasLease() == False:
                    # Add data for list view
                    data.append(
                        [
                            # Get rooms number
                            x.getRoomNumber(),
                            # Get Hall Number
                            Hall.getNumber(),
                            # Print Available
                            "Available",
                            # Print student name - N/A
                            "N/A ",
                            # Print Rooms rental rate as string
                            "£" + str(x.getRentalRate()),
                            # get occupancy status
                            x.getOccupancyStatus(),
                            # get cleaningstatus.
                            x.getCleaningStatus(),
                        ]
                    )
                # If room does have a lease:
                else:
                    data.append(
                        [
                            # Get room number
                            x.getRoomNumber(),
                            # Get Hall Number
                            Hall.getNumber(),
                            # Get lease id
                            x.getLeaseID(),
                            # Get student name associated with room.
                            x.getLease().getStudentRecord().getStudentName(),
                            # get rental rate as string
                            "£" + str(x.getRentalRate()),
                            # Get occupancy status
                            x.getOccupancyStatus(),
                            # get cleaning status
                            x.getCleaningStatus(),
                        ]
                    )
            # Loop through data array and insert into roomlist at given index value.
            for record in data:
                RoomList.insert(
                    parent="",
                    index="end",
                    iid=count,
                    text="",
                    values=(
                        record[0],
                        record[1],
                        record[2],
                        record[3],
                        record[4],
                        record[5],
                        record[6],
                    ),
                )
                # Increment counter
                count = count + 1
            # Pad treeview for visibility
            RoomList.pack(pady=10)
            # Create treeview columns
            RoomList["columns"] = (
                "RoomNum",
                "HallNum",
                "LeaseNumber",
                "StuName",
                "RentalRate",
                "Occupied",
                "CleanStatus",
            )
            # Customise columns of treeview for appropriate default viewing.
            RoomList.column("#0", width=0, stretch=NO)
            RoomList.column("RoomNum", anchor=CENTER, width=70)
            RoomList.column("HallNum", anchor=CENTER, width=70)
            RoomList.column("LeaseNumber", anchor=CENTER, width=70)
            RoomList.column("StuName", anchor=CENTER, width=90)
            RoomList.column("RentalRate", anchor=CENTER, width=70)
            RoomList.column("Occupied", anchor=CENTER, width=70)
            RoomList.column("CleanStatus", anchor=CENTER, width=90)

            # Create headings for treeview.
            RoomList.heading("#0", text="", anchor=CENTER)
            RoomList.heading("RoomNum", text="Room Num", anchor=CENTER)
            RoomList.heading("HallNum", text="Hall Num", anchor=CENTER)
            RoomList.heading("LeaseNumber", text="Lease Num", anchor=CENTER)
            RoomList.heading("StuName", text="Student Name", anchor=CENTER)
            RoomList.heading("RentalRate", text="Rental Rate", anchor=CENTER)
            RoomList.heading("Occupied", text="Occupied", anchor=CENTER)
            RoomList.heading(
                "CleanStatus", text="Cleaning Status", anchor=CENTER)

            # Return treeview for further use
            return RoomList

            # End of treeview.
            # ================================================================================================

        # Define Leaseframes function, passing in the roomlist treeview and the userlevel for privillege assignement.
        def LeaseFrames(RoomList, userlevel):
            # Create change status function for editting a rooms cleaning status.
            def ChangeStatus(b):
                Hall = chosenHall
                # Selected gets the room currently selected in treeview.
                selected = RoomList.focus()
                # x is the index of the room selected.
                x = int(selected)
                # If rooms does not have lease:
                # access rooms using the getrooms function and the x variable as an index.
                if Hall.rooms[x].hasLease() == False:
                    # Edit selected room with the following values.
                    RoomList.item(
                        selected,
                        text="",
                        values=(
                            # Get selected room number
                            Hall.getRooms()[x].getRoomNumber(),
                            # Get selected rooms hall number
                            Hall.getNumber(),
                            # Text placeholders as the room is unoccupied:
                            "Available",
                            "N/A ",
                            # Get room Rental Rate as string
                            "£" + str(Hall.getRooms()[x].getRentalRate()),
                            # Get rooms occupancy status
                            Hall.getRooms()[x].getOccupancyStatus(),
                            # Get the selected cleaning status value from the dropdown box.
                            StatusV.get(),
                        ),
                    )
                # If room Does have a lease:
                else:
                    # if the selected cleaning status value does NOT equal offline, insert the following values:
                    if StatusV.get() != "Off-Line":
                        RoomList.item(
                            selected,
                            text="",
                            values=(
                                # Get selected room number
                                Hall.getRooms()[x].getRoomNumber(),
                                # Get selected rooms hall number
                                Hall.getNumber(),
                                # Text placeholders as the room is unoccupied:
                                Hall.getRooms()[x].getLeaseID(),
                                Hall.getRooms()[x]
                                .getLease()
                                .getStudentRecord()
                                .getStudentName(),
                                # Get room Rental Rate as string
                                "£" + str(Hall.getRooms()[x].getRentalRate()),
                                # Get rooms occupancy status
                                Hall.getRooms()[x].getOccupancyStatus(),
                                # Get the selected cleaning status value from the dropdown box.
                                StatusV.get(),
                            ),
                        )
                    # If room does have a lease and the user attempts to set status to offline, error check and print error, no changes are made.
                    else:
                        messagebox.showerror(
                            title="Resident in Room, Error",
                            message="There is currently a student living in this Room!\nYou cannot set this Room to Off-Line!",
                        )
                # Set the cleaning status selected.
                Hall.rooms[x].setCleaningStatus(StatusV.get())

            # Define the Lease Manage function
            def LeaseManage():
                # Create update table function for updating tree view contents.
                def UpdateTable():
                    # Set Hall to chosenHall
                    Hall = chosenHall
                    # Clear treeview.
                    for item in RoomList.get_children():
                        RoomList.delete(item)
                    # Create Empty array to store data.
                    data = []
                    # Initialise counter to 0.
                    count = 0
                    # Loop through all rooms in the chosen hall
                    for x in range(len(Hall.rooms)):
                        # if no lease found:
                        if Hall.getRooms()[x].hasLease() == False:
                            # Add following data to array:
                            data.append(
                                [
                                    # Get room number
                                    Hall.getRooms()[x].getRoomNumber(),
                                    # Get Hall Number
                                    Hall.getNumber(),
                                    # Place holder as no lease found:
                                    "Available",
                                    "N/A ",
                                    # Get Rental Rate
                                    "£" + str(Hall.getRooms()
                                              [x].getRentalRate()),
                                    # Get occupancy status
                                    Hall.getRooms()[x].getOccupancyStatus(),
                                    # Get Cleaning Status
                                    Hall.getRooms()[x].getCleaningStatus(),
                                ]
                            )
                        # if lease found:
                        else:
                            data.append(
                                [
                                    # Get room number
                                    Hall.getRooms()[x].getRoomNumber(),
                                    # Get hall number
                                    Hall.getNumber(),
                                    # Get leaseID
                                    Hall.getRooms()[x].getLeaseID(),
                                    # Get Student Name
                                    Hall.getRooms()[x]
                                    .getLease()
                                    .getStudentRecord()
                                    .getStudentName(),
                                    # Get rental rate
                                    "£" + str(Hall.getRooms()
                                              [x].getRentalRate()),
                                    # Get occupancy status
                                    Hall.getRooms()[x].getOccupancyStatus(),
                                    # Get cleaning status
                                    Hall.getRooms()[x].getCleaningStatus(),
                                ]
                            )
                    # Loop through data array and insert into roomlist at given indexes
                    for record in data:
                        RoomList.insert(
                            parent="",
                            index="end",
                            iid=count,
                            text="",
                            values=(
                                record[0],
                                record[1],
                                record[2],
                                record[3],
                                record[4],
                                record[5],
                                record[6],
                            ),
                        )
                        # Incremement counter
                        count = count + 1
                    # The below code creates buttons and assigns a state based on clearancelevel (passed in as userlevel)
                    # If a hall has a lease:
                    if Hall.getRooms()[x].hasLease() == True:
                        # If clearancelevl is 0(admin):
                        if userlevel == 0:
                            # Add lease button is disabled, as a lease is already assigned.
                            ADD_button["state"] = DISABLED
                            # Delete, update and review lease buttons are all functioning.
                            DELETE_button["state"] = NORMAL
                            UPDATE_button["state"] = NORMAL
                            REVIEW_button["state"] = NORMAL

                        # If clearancelevel is 1(Hall Manager):
                        if userlevel == 1:
                            # Add lease button is disabled, as a lease is already assigned.
                            ADD_button["state"] = DISABLED
                            # Delete, update and review lease buttons are all functioning.
                            DELETE_button["state"] = NORMAL
                            UPDATE_button["state"] = NORMAL
                            REVIEW_button["state"] = NORMAL

                        # If clearance level is 2(Warden):
                        if userlevel == 2:
                            # Due to editing privalleges within spec, the warden may not edit a lease, but for visibilty is able to view the current lease.
                            REVIEW_button["state"] = NORMAL

                    # If a lease is not found:
                    else:
                        # If clearancelevl is 0(admin):
                        if userlevel == 0:
                            # Add button is enabled for the creation of a new lease.
                            ADD_button["state"] = NORMAL
                            # Delete, update and review lease buttons are disabled, as there is no lease to perform their assigned functions on.
                            DELETE_button["state"] = DISABLED
                            UPDATE_button["state"] = DISABLED
                            REVIEW_button["state"] = DISABLED
                        # If clearancelevel is 1(Hall Manager):
                        if userlevel == 1:
                            # Add button is enabled for the creation of a new lease.
                            ADD_button["state"] = NORMAL
                            # Delete, update and review lease buttons are disabled, as there is no lease to perform their assigned functions on.
                            DELETE_button["state"] = DISABLED
                            UPDATE_button["state"] = DISABLED
                            REVIEW_button["state"] = DISABLED
                        # If clearancelevel is 2(Warden):
                        if userlevel == 2:
                            # Review button is disabled, as there is no lease to review.
                            REVIEW_button["state"] = DISABLED
                        # All relevant input boxes (Student name, start date, end date) are greyed out as the warden cannot handle Leases.
                        Student_entry["state"] = "disabled"
                        StartDate_entry["state"] = "disabled"
                        EndDate_entry["state"] = "disabled"
                        # Disable clean status dropdown to avoid a cleaning status being set when no room is selected.
                        CL_entry["state"] = "disabled"

                # Define function for Add lease button
                def Add():
                    # Get global enddate.
                    global enddate
                    Hall = chosenHall
                    # Selected is the selected item from the room list.
                    selected = RoomList.focus()
                    # x is the index of the selected room.
                    x = int(selected)
                    # if room does not have a lease:
                    if Hall.getRooms()[x].hasLease() == False:
                        # If cleaning status is NOT offline:
                        if StatusV.get() != "Off-Line":
                            # If student name is valid:
                            if (
                                # Check text has been entered
                                Student_entry.get() != "N/A "
                                # check length of name is 2+ characters
                                and (len(Student_entry.get()) > 2)
                                # Check if name contains digits
                                and (Student_entry.get().isdigit() == False)
                            ):
                                # Lease duration is calculated using relativedelta, and is the difference between the start and end dates.
                                leaseDuration = relativedelta(
                                    StartDate_entry.get_date(), EndDate_entry.get_date()
                                )
                                # Lease duration is then parsed for the months and days only to meet the spec
                                leaseDuration = "%s months, %s days." % (
                                    # relative delta returns a negative figure, *-1 to return the opposite number.
                                    -1 * leaseDuration.months,
                                    -1 * leaseDuration.days,
                                )
                                # Add lease to selected room
                                Hall.getRooms()[x].addLease(
                                    # Add start date
                                    StartDate_entry.get_date(),
                                    # Add end date
                                    EndDate_entry.get_date(),
                                    # Add student name
                                    Student_entry.get(),
                                    (
                                        # create a randomised unique student number, with hall number and room number added to decrease chance for duplicat numbers.
                                        random.randrange(1000, 9999)
                                        + int(Hall.getNumber())
                                        + int(Hall.getRooms()
                                              [x].getRoomNumber())
                                    ),
                                    # Add lease duration
                                    leaseDuration,
                                )
                                # Update table
                                UpdateTable()

                                # Set leases to 0
                                leases = 0
                                # Loop through rooms, calculating free rooms.
                                for x in chosenHall.rooms:
                                    if x.hasLease() == True:
                                        leases += 1
                                lease = len(Hall.rooms) - leases
                                # set noleases textbox to number of free rooms
                                noleases.set(
                                    "Total number of free rooms in "
                                    + chosenHall.getName()
                                    + ": "
                                    + str(lease)
                                )
                            # If student name validations were not met display error:
                            else:
                                messagebox.showerror(
                                    title="Input Error",
                                    message="You did not input a Valid Student Name!",
                                )
                        # If Room is offline display error:
                        else:
                            messagebox.showerror(
                                title="Off-Line Room Error",
                                message="This Room is Off-Line!\nPlease Pick a Different Room!",
                            )
                    # If room is already occupied, display error:
                    else:
                        messagebox.showerror(
                            title="Already Existing Lease",
                            message="This Room Already has a Lease!",
                        )
                        pass
                    # Disable entry fields until room is selected.
                    Student_entry["state"] = "disabled"
                    StartDate_entry["state"] = "disabled"
                    EndDate_entry["state"] = "disabled"
                    CL_entry["state"] = "disabled"
                    # Disable all buttons for all level users:
                    if userlevel == 0:
                        ADD_button["state"] = DISABLED
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    if userlevel == 1:
                        ADD_button["state"] = DISABLED
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    if userlevel == 2:
                        REVIEW_button["state"] = DISABLED

                # Define delete function:
                def Delete():
                    Hall = eval(Hall_Chosen.get())
                    # Selected is the selected item in treeview
                    selected = RoomList.focus()
                    # x is the index of the selected item.
                    x = int(selected)

                    # If room has lease:
                    if Hall.getRooms()[x].hasLease() == True:
                        # Call delete lease function
                        Hall.getRooms()[x].deleteLease()
                        # Update table
                        UpdateTable()

                        # re-calculate free rooms and set text box.
                        leases = 0
                        for x in eval(Hall_Chosen.get()).rooms:
                            if x.hasLease() == True:
                                leases += 1
                        lease = len(Hall.rooms) - leases

                        noleases.set(
                            "Total number of free rooms in "
                            + eval(Hall_Chosen.get()).getName()
                            + ": "
                            + str(lease)
                        )
                    # Contingency error message for if a room with no lease is somehow selected for lease deletion.
                    else:
                        print("error")

                    # Disable all entry fields until room selected.
                    Student_entry["state"] = "disabled"
                    StartDate_entry["state"] = "disabled"
                    EndDate_entry["state"] = "disabled"
                    CL_entry["state"] = "disabled"

                    # Disable all buttons for all users until selection.
                    if userlevel == 0:
                        ADD_button["state"] = DISABLED
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    if userlevel == 1:
                        ADD_button["state"] = DISABLED
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    if userlevel == 2:
                        REVIEW_button["state"] = DISABLED

                # Define update function
                def Update():
                    Hall = eval(Hall_Chosen.get())
                    # Get selected room from treeview.
                    selected = RoomList.focus()
                    x = int(selected)

                    # If room has lease:
                    if Hall.getRooms()[x].hasLease() == True:
                        # If cleaning status is not offline:
                        if StatusV.get() != "Off-Line":
                            if (
                                # validate student name:
                                Student_entry.get() != "N/A "
                                and (len(Student_entry.get()) > 2)
                                and (Student_entry.get().isdigit() == False)
                            ):
                                # Get the lease object to be updated
                                halltoupdate = Hall.getRooms()[x].getLease()
                                # Get the student record to be updated.
                                recordtoupdate = halltoupdate.getStudentRecord()

                                # Calculate new lease duration
                                leaseDuration = (
                                    EndDate_entry.get_date()
                                    - StartDate_entry.get_date()
                                )
                                leaseDuration = relativedelta(
                                    StartDate_entry.get_date(), EndDate_entry.get_date()
                                )
                                leaseDuration = "%s months, %s days." % (
                                    -1 * leaseDuration.months,
                                    -1 * leaseDuration.days,
                                )

                                # Set new start date to the inputted date
                                halltoupdate.setStartDate(
                                    StartDate_entry.get_date())
                                # Set new end date to the inputted date
                                halltoupdate.setEndDate(
                                    EndDate_entry.get_date())
                                # Set the student name of the student record and lease to the inputted name(ID remains the same to allow for spelling error correction without creating new student)
                                recordtoupdate.setStudentName(
                                    Student_entry.get())
                                # set new lease duration.
                                halltoupdate.setLeaseDuration(leaseDuration)
                                # Update table
                                UpdateTable()
                            # if student name fails validation print error:
                            else:
                                messagebox.showerror(
                                    title="Input Error",
                                    message="You did not input a Valid Student Name!",
                                )
                        # If room offline print error(Lease should not be possible on offline room.)
                        else:
                            messagebox.showerror(
                                title="Off-Line Room Error",
                                message="This Room is Off-Line!\nPlease Pick a Different Room!",
                            )
                    # If no lease found and button somehow pressed, print contingency error:
                    else:
                        messagebox.showerror(
                            title="No Existing Lease",
                            message="This Room Does Not Have A Lease!",
                        )
                        pass
                    # Disable all input until room selected:
                    Student_entry["state"] = "disabled"
                    StartDate_entry["state"] = "disabled"
                    EndDate_entry["state"] = "disabled"
                    CL_entry["state"] = "disabled"

                    # Disable all buttons to all users until room selected:
                    if userlevel == 0:
                        ADD_button["state"] = DISABLED
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    if userlevel == 1:
                        ADD_button["state"] = DISABLED
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    if userlevel == 2:
                        REVIEW_button["state"] = DISABLED

                # Create add button, which performs add function on click
                ADD_button = Button(
                    button_frame,
                    text="Add Lease",
                    highlightbackground=color2,
                    command=Add,
                    fg="black",
                )
                ADD_button.grid(row=0, column=0, padx=10, pady=10)

                # Create delete button, which performs delete function on click
                DELETE_button = Button(
                    button_frame,
                    text="Delete Lease",
                    command=Delete,
                    background="white",
                    highlightbackground=color2,
                    foreground="black",
                )
                DELETE_button.grid(row=0, column=1, padx=10, pady=10)
                # Create update button, which performs update function on click
                UPDATE_button = Button(
                    button_frame,
                    text="Update Lease",
                    command=Update,
                    background="white",
                    highlightbackground=color2,
                    foreground="black",
                )
                UPDATE_button.grid(row=0, column=2, padx=10, pady=10)
                # Disable buttons by default.
                ADD_button["state"] = DISABLED
                DELETE_button["state"] = DISABLED
                UPDATE_button["state"] = DISABLED
                # Return buttons for use.
                return (ADD_button, DELETE_button, UPDATE_button)

            # Define reviewing function
            def Reviewing():
                # define review function
                def Review():
                    Hall = chosenHall

                    # get selected room
                    selected = RoomList.focus()
                    x = int(selected)
                    # If rooms has lease:
                    if Hall.getRooms()[x].hasLease() == True:
                        # Create popup window of fixed size with matching theme, nonresizable to display lease details in a readable format
                        root = Tk()
                        root.title("Lease Details:")
                        root.geometry("240x260")
                        root.resizable(FALSE, FALSE)
                        windowFrame = Frame(root, bg=color1)
                        windowFrame.pack(fill="both", expand=True)

                        # create text variable to hold dynamic text created below
                        T = Text(
                            windowFrame,
                            font="calibri 10 bold",
                            foreground="black",
                            background="white",
                            width=32,
                            height=10,
                            relief=FLAT,
                            pady=25,
                        )
                        # Use getters to retrieve appropriate lease details and place in string format
                        text = (
                            "Lease Number:       "
                            + str(Hall.getRooms()[x].getLease().getLeaseID())
                            + "\nRoom Number:       "
                            + str(Hall.getRooms()[x].getRoomNumber())
                            + "\nRental Rate:             "
                            + str("£" + str(Hall.getRooms()
                                  [x].getRentalRate()))
                            + "\n\nStart Date:               "
                            + str(StartDate_entry.get())
                            + "\nEnd Date:                 "
                            + str(EndDate_entry.get())
                            + "\nLease Duration:      "
                            + str(Hall.getRooms()
                                  [x].getLease().getLeaseDuration())
                            + "\n\nStudent Name:      "
                            + str(
                                Student_entry.get()
                                + "\nStudent ID:              "
                                + str(
                                    Hall.getRooms()[x]
                                    .getLease()
                                    .getStudentRecord()
                                    .getStudentID()
                                )
                            )
                        )
                        # Insert text retrieved by getters into text box and pack into window.
                        T.insert(tk.END, text)
                        T.pack(padx=15, pady=15)
                        # Disable textbox until called
                        T["state"] = "disabled"

                        # create button to close window
                        button = Button(
                            windowFrame,
                            text=" Close ",
                            command=lambda: root.destroy(),
                            bg=color2,
                            fg="black",
                            highlightbackground=color1,
                            relief=SOLID,
                        )
                        # Pack button at bottom of window.
                        button.pack(side="bottom", fill="none", expand=True)

                        root.mainloop()
                        #
                    # If button somehow pressed and no lease found display contingency error:
                    else:
                        messagebox.showerror(
                            title="No Lease", message="Sorry! No lease available"
                        )

                # Create review button that calls review function on press
                REVIEW_button = Button(
                    button_frame,
                    text="Review Lease",
                    command=Review,
                    background="white",
                    highlightbackground=color2,
                    foreground="black",
                )
                REVIEW_button.grid(row=0, column=3, padx=10, pady=10)

                # Disable button by default
                REVIEW_button["state"] = DISABLED

                # Disable entry fields by default
                Student_entry["state"] = "disabled"
                StartDate_entry["state"] = "disabled"
                EndDate_entry["state"] = "disabled"
                CL_entry["state"] = "disabled"

                # return created button
                return REVIEW_button

            # Create leaseframe
            LeaseFrame = Frame(
                Mainframe,
                background=color2,
                width=550,
                height=150,
                highlightthickness=2,
                highlightbackground="black",
                pady=15,
                padx=20,
            )
            LeaseFrame.pack()

            # create dataframe
            data_frame = Frame(LeaseFrame, background=color2, pady=5)
            data_frame.pack()

            # create button frame
            button_frame = Frame(
                LeaseFrame, background=color2, width=550, pady=2)
            button_frame.pack(expand="YES", fill="x")

            # create Label "Student Name"
            Student_label = Label(
                data_frame, text="Student Name:", background=color2, foreground="black"
            )
            Student_label.grid(row=0, column=0, padx=10, pady=10)

            # Additional formatting required for visibility on mac systems:
            if platform.system() == "Darwin":
                # Create student name entry box
                Student_entry = Entry(
                    data_frame,
                    width=14,
                    background="white",
                    highlightbackground=color2,
                    foreground="black",
                )
                Student_entry.grid(row=0, column=1, padx=1, pady=1)
            # Same box on windows, less granular control over widths required.
            else:
                Student_entry = Entry(
                    data_frame,
                    width=20,
                    background="white",
                    highlightbackground=color2,
                    foreground="black",
                )
                Student_entry.grid(row=0, column=1, padx=20, pady=1)
            # Get current day
            today = date.today()
            # return date in d/m/y format (as string)
            today = today.strftime("%d/%m/%Y")
            # convert back to datetime object.
            today = datetime.datetime.strptime(today, "%d/%m/%Y").date()

            # Create start date label
            StartDate_label = Label(
                data_frame,
                text="Lease Start Date:",
                background=color2,
                foreground="black",
            )
            # create copy of todays date object
            stdate = today

            # define get date function with optional arguements for callback functions
            def get_date(*args):
                # use global enddate
                global enddate
                # get inputted start date
                startdate = StartDate_entry.get_date()
                # set end date to start date +1 month (using relative delta for accurate calender dates)
                enddate = StartDate_entry.get_date() + relativedelta(months=+1)
                EndDate_entry.grid(row=1, column=3, padx=1, pady=1)
                # get global stdate
                global stdate
                # Enable enddate button
                EndDate_entry["state"] = "normal"
                EndDate_entry.grid(row=1, column=3, padx=10, pady=1)
                # set enddate
                enddate = startdate + relativedelta(months=+1)
                # Set default enddate to enddate (start +1 month)
                EndDate_entry.set_date(enddate)
                # set minumum date of the end date to enddate to prevent contracts <1month
                EndDate_entry.config(mindate=enddate)

            # create start date label
            StartDate_label.grid(row=1, column=0, padx=10, pady=10)
            # If mac, extra formatting required:
            if platform.system() == "Darwin":
                # Create start date entry with minimum date of today, to avoid past bookings.
                StartDate_entry = DateEntry(
                    data_frame,
                    selectmode="day",
                    year=2022,
                    month=1,
                    day=1,
                    width=13,
                    date_pattern="dd/MM/yyyy",
                    mindate=today,
                )
                StartDate_entry.grid(row=1, column=1, padx=1, pady=1)
                # On selection of a newdate call getdate function without the need for buttons
                StartDate_entry.bind("<<DateEntrySelected>>", get_date)

            # If not mac, less formatting:
            else:
                StartDate_entry = DateEntry(
                    data_frame,
                    selectmode="day",
                    year=2022,
                    month=1,
                    day=1,
                    width=17,
                    date_pattern="dd/MM/yyyy",
                    mindate=today,
                )
                StartDate_entry.grid(row=1, column=1, padx=1, pady=1)
                StartDate_entry.bind("<<DateEntrySelected>>", get_date)

            # create enddate label
            EndDate_label = Label(
                data_frame,
                text="Lease End Date:",
                background=color2,
                foreground="black",
            )
            EndDate_label.grid(row=1, column=2, padx=10, pady=10)
            # get start date
            stdate = StartDate_entry.get_date()
            # Get earliest possible end date
            earliestEndDate = stdate
            earliestEndDate = earliestEndDate + relativedelta(months=+1)

            # if mac, extra formatting for enddate entry width:
            if platform.system() == "Darwin":
                EndDate_entry = DateEntry(
                    data_frame, selectmode="day", width=13, date_pattern="dd/MM/yyyy",
                )
                EndDate_entry.grid(row=1, column=3, padx=1, pady=1)

            # if not, use greater width:
            else:
                EndDate_entry = DateEntry(
                    data_frame,
                    selectmode="day",
                    year=2022,
                    width=17,
                    date_pattern="dd/MM/yyyy",
                )
                EndDate_entry.grid(row=1, column=3, padx=10, pady=1)
            # Create cleaning status label
            CL_label = Label(
                data_frame, text="Clean status:", background=color2, foreground="black"
            )
            CL_label.grid(row=0, column=2, padx=10, pady=10)

            # 3 possible cleaning statuses
            Status = ["Clean", "Dirty", "Off-Line"]
            # Create stringvar to dynamically update
            StatusV = tk.StringVar()
            # Set initially to na
            StatusV.set("N/A")
            # Create dropdown with above cleaning status values, on click call changestatus function
            CL_entry = tk.OptionMenu(
                data_frame, StatusV, *Status, command=ChangeStatus)
            CL_entry.configure(foreground="black", width=10)
            CL_entry.grid(row=0, column=3, padx=10, pady=10)

            # Entry boxes disabled by default
            Student_entry["state"] = "disabled"
            StartDate_entry["state"] = "disabled"
            EndDate_entry["state"] = "disabled"
            CL_entry["state"] = "disabled"

            # If user level is 0 (admin):
            if userlevel == 0:
                # Enable Add, delete and update buttons calling the LeaseManage function
                ADD_button, DELETE_button, UPDATE_button = LeaseManage()
                # Review button calls the reviewing function.
                REVIEW_button = Reviewing()
            # If user level is 1(Hall Manager):
            elif userlevel == 1:
                # Enable Add, delete and update buttons calling the LeaseManage function
                ADD_button, DELETE_button, UPDATE_button = LeaseManage()
                # Review button calls the reviewing function.
                REVIEW_button = Reviewing()
            # If user level is 2 (Warden):
            elif userlevel == 2:
                # Review button calls the reviewing function.
                REVIEW_button = Reviewing()

            # Define the select item function to be called when a treeview item is selected.
            def selectItem(event):
                Hall = chosenHall
                # Enable data entry buttons by default on selection of a room.
                Student_entry["state"] = "normal"
                StartDate_entry["state"] = "normal"
                EndDate_entry["state"] = "normal"
                CL_entry["state"] = "normal"

                # Get the selected item from the list.
                selected = RoomList.focus()
                x = int(selected)

                # Delete the student entry box.
                Student_entry.delete(0, END)

                # If room has lease:
                if Hall.getRooms()[x].hasLease() == True:
                    # If userlevel is 0(admin):
                    if userlevel == 0:
                        # Add button is disabled as a lease is present.
                        ADD_button["state"] = DISABLED
                        # Delete, update and review are enabled.
                        DELETE_button["state"] = NORMAL
                        UPDATE_button["state"] = NORMAL
                        REVIEW_button["state"] = NORMAL

                    # if userlevel is 1(Hall manager):
                    if userlevel == 1:
                        # Add button is disabled as a lease is present.
                        ADD_button["state"] = DISABLED
                        # Delete, update and review are enabled.
                        DELETE_button["state"] = NORMAL
                        UPDATE_button["state"] = NORMAL
                        REVIEW_button["state"] = NORMAL

                    # If userlevel is 2 (Warden):
                    if userlevel == 2:
                        # Add, delete and update are disabled for warden, review is visible.
                        REVIEW_button["state"] = NORMAL
                # If room does not have lease:
                else:
                    # If userlevel is 0(admin):
                    if userlevel == 0:
                        # Add button is enabled.
                        ADD_button["state"] = NORMAL
                        # Delete, update and review are disabled as no lease is present
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    # If userlevel is 1(HallManager):
                    if userlevel == 1:
                        # Add button is enabled.
                        ADD_button["state"] = NORMAL
                        # Delete, update and review are disabled.
                        DELETE_button["state"] = DISABLED
                        UPDATE_button["state"] = DISABLED
                        REVIEW_button["state"] = DISABLED
                    # If userlevel is 2(warden):
                    if userlevel == 2:
                        # Only review button is present and is disabled as no lease is present
                        REVIEW_button["state"] = DISABLED
                # get selected room from treeview
                selected = RoomList.focus()
                # Save the selected data into a values variable
                values = RoomList.item(selected, "values")
                # if room has lease:
                if Hall.getRooms()[x].hasLease() == True:
                    # Place current student name into student entry box
                    Student_entry.insert(0, values[3])
                    # Set end date to today+1 month
                    enddate = today + relativedelta(months=+1)
                    # Clear start date
                    StartDate_entry.delete(0, "end")
                    # Set start date minimum date to today.
                    StartDate_entry.config(mindate=today)
                    # Set start date to current leases start date.
                    StartDate_entry.set_date(
                        Hall.getRooms()[x].getLease().getStartDate()
                    )
                    # Clear current end date
                    EndDate_entry.delete(0, "end")
                    # Set minimum lease end date to the calculated enddate variable.
                    EndDate_entry.config(mindate=enddate)
                    # Set end date default entry to current lease end date.
                    EndDate_entry.set_date(
                        Hall.getRooms()[x].getLease().getEndDate())

                # If room has no lease:
                else:
                    # Calculate enddate
                    enddate = today + relativedelta(months=+1)
                    # Set minimum start date to today
                    StartDate_entry.config(mindate=today)
                    # set minimum end date to enddate variable
                    EndDate_entry.config(mindate=enddate)
                    # Set default start date to today
                    StartDate_entry.set_date(today)
                    # Set default end date to enddate.
                    EndDate_entry.set_date(enddate)
                # Set cleaning status entry box to rooms current cleaning status.
                StatusV.set(values[6])

                # if userlevel is 1(Hall manager):
                if userlevel == 1:
                    # Cleaning status editting is not open to hall manager.
                    CL_entry["state"] = "disabled"
                # If userlevel is 2 (Warden):
                if userlevel == 2:
                    # Start date, end date and student name entries are disabled to the warden.
                    Student_entry["state"] = "disabled"
                    StartDate_entry["state"] = "disabled"
                    EndDate_entry["state"] = "disabled"

            # Selecting an item in the roomview calls the selectitem function
            RoomList.bind("<<TreeviewSelect>>", selectItem)
            # =========================================================================================

        # Call the hallframes function
        Hall_Chosen = HallFrames()
        # Call the room frames function
        RoomList = RoomFrames()
        # Pass roomlist and userlevel into the leaseframe
        LeaseFrames(RoomList, userlevel)

    # Pass row(user) into top frames
    TopFrames(row)
    # Pass userlevel into middle frames.
    MiddleFrames(userlevel)
    # Close loop of admin page (bulk of gui)
    Admin_Page.mainloop()


# Define login page
def login_page():
    # Create window using the same geometry tools as the main admin page.
    window = tk.Tk()
    window_width = 800
    window_height = 520
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    centerx = int(screen_width / 2 - window_width / 2)
    centery = int(screen_height / 2 - window_height / 2)
    window.minsize(width=window_width, height=window_height)
    window.maxsize(width=window_width, height=window_height)

    # Path of background image.

    # Anchor image to the window and fill the window.

    # Title the window.
    window.title("Saw Accomdation Management")
    # Place window on screen
    window.geometry(f"{window_width}x{window_height}+{centerx}+{centery}")

    # Define upperframe function
    def UpperFrame():
        # Create upperframe
        upperFrame = Frame(
            window,
            background=color1,
            width=800,
            height=20,
            highlightthickness=1,
            highlightbackground="black",
        )
        upperFrame.pack(pady=0)

    # Define middle frame
    def MiddleFrame():
        # define login function
        def login():
            # Creat username and password variables that fetch data from entry boxes.
            username = name_entry.get()
            password = passwordEntry.get()

            # Get users from database with matching username and password.
            Connection.execute(
                """SELECT * FROM User WHERE username = ? AND password = ?""",
                (username, password),
            )
            # row == succesfful retrieval of a user, to be passed into gui.
            row = Connection.fetchone()

            # If no row (user) is found return login details error.
            if row == None:
                messagebox.showerror(
                    "Failed Login!", "Username Or Password Not Recognised!"
                )

            else:
                # If matching username is found
                if username == row[0]:
                    # and matching password is found
                    if password == row[1]:
                        # Close Login page and pass in user and clearance level to gui function(launching the app)
                        window.destroy()
                        Admin_Page(row, row[2])

        # Create login frame
        LoginFrame = Frame(
            window,
            background=color2,
            width=3,
            height=2,
            highlightthickness=4,
            highlightbackground=color1,
        )
        LoginFrame.pack(pady=135)

        # Create please login label.
        title = tk.Label(
            LoginFrame,
            text="Welcome, please login below.",
            foreground="black",
            background=color2,
            width=40,
            height=2,
            font=("calibri"),
            relief=RAISED,
        )
        title.pack()

        # Create name label
        tk.Label(LoginFrame, text="Name:", background=color2,
                 foreground="black").pack()

        # Create name entry box
        name_entry = tk.Entry(
            LoginFrame,
            background="light grey",
            relief=RAISED,
            foreground="black",
            highlightbackground=color2,
        )
        name_entry.pack()

        # Create password label
        tk.Label(
            LoginFrame, text="Password:", background=color2, foreground="black"
        ).pack()

        # Create password entry box.
        passwordEntry = tk.Entry(
            LoginFrame,
            background="light grey",
            relief=RAISED,
            # Show "*" regardless of data entered for privacy.
            show="*",
            foreground="black",
            highlightbackground=color2,
        )
        passwordEntry.pack()

        # Create global incrementer
        global showpasscount
        showpasscount = 1

        # Define showpass function to show password true text.
        def showPass():
            # Use showpasscount global counter.
            global showpasscount
            # Create an odd or even loop to either show or hide password
            if showpasscount % 2 == 1:
                passwordEntry.config(show="")
            else:
                passwordEntry.config(show="*")
            # Increment counter on each call so the next call will perform the opposite action.
            showpasscount += 1

        # Shoe password button that calls the showpass function
        ShowPassword = tk.Button(
            LoginFrame,
            text="Reveal password",
            foreground="black",
            highlightbackground=color2,
            command=showPass,
            relief=GROOVE,
        )
        ShowPassword.pack()

        # Create the login button that calls the login command on click.
        loginbutton = tk.Button(
            LoginFrame,
            text="Login",
            foreground="black",
            highlightbackground=color2,
            command=login,
            relief=GROOVE,
        )
        loginbutton.pack(pady=5)

    # Define bottom frame
    def BottomFrame():

        # create bottom frame
        bottomFrame = Frame(
            window,
            background=color1,
            width=800,
            height=20,
            highlightthickness=1,
            highlightbackground="black",
        )
        bottomFrame.pack()

        # Define left frame
        def LeftFrame():
            # Create left frame
            leftFrame = Frame(
                bottomFrame, background="lightgrey", width=29, height=20)
            leftFrame.pack(side=LEFT)

            # Create footer label with system info
            InfoLabel = tk.Label(
                leftFrame,
                width="60",
                height="5",
                text="      UWE Accomodation Office",
                background=color1,
                foreground="white",
                anchor="w",
            )
            InfoLabel.pack()

        # define rightframe function
        def Rightrame():
            # create rightframe frame
            rightFrame = Frame(
                bottomFrame, background=color1, width=20, height=20)
            rightFrame.pack(side=RIGHT)

            # Create footer with False mobile number.
            InfoLabel2 = tk.Label(
                rightFrame,
                width="60",
                height="5",
                text="Telelphone number: 0117 000101       ",
                background=color1,
                foreground="white",
                anchor="e",
            )
            InfoLabel2.pack()

        # Call left and right frames
        LeftFrame()
        Rightrame()

    # Call upper, middle and bottom frames.
    UpperFrame()
    MiddleFrame()
    BottomFrame()
    # Close login page loop.
    window.mainloop()


# FOR TESTING PURPOSES ONLY:
# uncomment the below lines to access the admin login, Hall manager login and Warden login directly.
# - These testing classes may no function correctly if user init's are editted at the top of this program.
# Admin_Page(j[0], j[0][2])
# Admin_Page(j[3], j[3][2])
# Admin_Page(j[4], j[4][2])


# Call login page function
login_page()


# ============================================================================================================================
