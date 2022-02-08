import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import BOTTOM, GROOVE, RAISED, RIGHT

defaultUser = "ash"  # If the user skips past the "Login Page" This will be the username
# If the user skips past the "Login Page" This will be the userlevel
defaultLevel = "1508"
defaultNoRooms = "0"
defaultNoAvilableLeases = "0"


def Manager_page(username):
    def logout():
        ManagerPage.destroy()
        login_page()

    ManagerPage = tk.Tk()
    ManagerPage_width = 600
    ManagerPage_height = 690
    screen_width = ManagerPage.winfo_screenwidth()
    screen_height = ManagerPage.winfo_screenheight()
    centerx = int(screen_width / 2 - ManagerPage_width / 2)
    centery = int(screen_height / 2 - ManagerPage_height / 2)
    ManagerPage.minsize(width=ManagerPage_width, height=ManagerPage_height)
    ManagerPage.maxsize(width=ManagerPage_width, height=ManagerPage_height)

    ManagerPage.title(username + "'s Home Page")
    ManagerPage.geometry(
        f'{ManagerPage_width}x{ManagerPage_height}+{centerx}+{centery}')
    ManagerPage.configure(background="coral")

    def TopFrames():
        TopFrame = Frame(ManagerPage, background="coral")
        TopFrame.pack()

        title = tk.Label(TopFrame, text="SAW Accomodation", foreground="black",
                         background="coral", width=30, height=1, font=("calibri 11 bold"))
        title.pack(pady=2, side=LEFT)

        title2 = tk.Label(TopFrame, text="Welcome  |" + username + defaultLevel + "|",
                          foreground="black", background="coral", width=30, height=1, font=("calibri 11 bold"))
        title2.pack(pady=2, side=LEFT)

        logoutbutton = tk.Button(TopFrame, text="Logout", command=logout)
        logoutbutton.pack(side=RIGHT)

        QuitButton = tk.Button(TopFrame, text="Quit",
                               command=ManagerPage.destroy)
        QuitButton.pack(pady=2, side=RIGHT)

    def MiddleFrames():
        Mainframe = Frame(ManagerPage, background="whitesmoke",
                          highlightthickness=2, highlightbackground="black")
        Mainframe.pack(pady=3)

        title = tk.Label(Mainframe, text="  ", foreground="black",
                         background="whitesmoke", width=570, font=("calibri 1"))
        title.pack()

        def HallFrames():
            HallFrame = Frame(Mainframe, background="darksalmon", width=550,
                              height=100, highlightthickness=2, highlightbackground="black")
            HallFrame.pack(pady=15)

            def LeftSide():

                LeftHallFrame = Frame(HallFrame, background="darksalmon")
                LeftHallFrame.pack(pady=15, side=LEFT)

                HallTitle = tk.Label(LeftHallFrame, text="Select Hall", font="calibri 13 underline bold",
                                     foreground="black", background="darksalmon", width=32, height=1)
                HallTitle.pack()
                HallsList = ["Pick a Hall", "Brecon Court", "Cotswold Court",
                             "Mendip Court", "Quantock Court", "WallsCourt"]
                value_inside = tk.StringVar()
                value_inside.set(HallsList[0])
                Combo = ttk.OptionMenu(LeftHallFrame, value_inside, *HallsList)
                Combo.pack(padx=5, pady=5)

            def RightSide():

                RightHallFrame = Frame(HallFrame, background="darksalmon")
                RightHallFrame.pack(pady=15, side=RIGHT)

                HallNomRooms = tk.Label(RightHallFrame, text="Total number of Rooms: " + defaultNoRooms,
                                        font="calibri 10 bold", foreground="black", background="darksalmon", width=35, height=1)
                HallNomRooms.pack()

                HallNomLeases = tk.Label(RightHallFrame, text="Number of available Leases: " + defaultNoAvilableLeases,
                                         font="calibri 10 bold", foreground="black", background="darksalmon", width=35, height=1)
                HallNomLeases.pack()

            LeftSide()
            RightSide()

        def RoomFrames():
            RoomFrame = Frame(Mainframe, background="coral", width=550,
                              height=175, highlightthickness=2, highlightbackground="black")
            RoomFrame.pack(pady=15)

            def TitleFrames():
                RoomTitle = tk.Label(RoomFrame, text="Select Room", font="calibri 13 underline bold",
                                     foreground="black", background="coral", width=60, height=1)
                RoomTitle.pack()

            def RoomTable():

                # ================================================================================================
                # Below this is the Table
                # ================================================================================================
                room_scroll = Scrollbar(RoomFrame)
                style = ttk.Style()
                style.theme_use('winnative')
                style.configure("Treeview", background="#ECC898",
                                fieldbackground="#ECC898")
                style.map('Treeview', background=[('selected', '#C19761')])
                RoomList = ttk.Treeview(
                    RoomFrame, yscrollcommand=room_scroll.set, xscrollcommand=room_scroll.set)
                RoomList.pack(pady=10)

                RoomList['columns'] = (
                    'NumRooms', 'RoomPrice', 'Available', 'Cleaned')

                RoomList.column("#0", width=0, stretch=NO)
                RoomList.column("NumRooms", anchor=CENTER, width=100)
                RoomList.column("RoomPrice", anchor=CENTER, width=80)
                RoomList.column("Available", anchor=CENTER, width=80)
                RoomList.column("Cleaned", anchor=CENTER, width=80)

                RoomList.heading("#0", text="", anchor=CENTER)
                RoomList.heading("NumRooms", text="Room Number", anchor=CENTER)
                RoomList.heading("RoomPrice", text="Room Price", anchor=CENTER)
                RoomList.heading(
                    "Available", text="Availability", anchor=CENTER)
                RoomList.heading("Cleaned", text="Clean Status", anchor=CENTER)
                # list of data
                data = [
                    ['1', '£2020', 'True', 'Clean'],
                    ['2', '£5000', 'False', 'Off-Line'],
                    ['3', '£1200', 'True', 'Dirty'],
                    ['4', '£2090', 'True', 'Clean'],
                    ['5', '£9875', 'False', 'Dirty']
                ]
                count = 0
                for record in data:
                    if count % 2 == 0:
                        RoomList.insert(parent='', index='end', iid=count, text='', values=(
                            record[0], record[1], record[2], record[3]), tags=('evenrow',))
                    else:
                        RoomList.insert(parent='', index='end', iid=count, text='', values=(
                            record[0], record[1], record[2], record[3]), tags=('oddrow',))
                # increment counter
                    count += 1

                RoomList.pack()
                selected = RoomList.focus()
                # Grab record values
                #Values = RoomList.item(selected, 'values')
                RoomList.pack()

                # End of table part
                # ================================================================================================
            TitleFrames()
            RoomTable()

        def LeaseFrames():
            LeaseFrame = Frame(Mainframe, background="darksalmon", width=700,
                               height=175, highlightthickness=2, highlightbackground="black")
            LeaseFrame.pack(pady=15)

            def dataFrames():
                data_frame = LabelFrame(
                    LeaseFrame, text="Record", background="darksalmon")
                data_frame.pack(fill="both", expand="NO", padx=20)

                NUM_label = Label(data_frame, text="Room Number")
                NUM_label.grid(row=0, column=0, padx=10, pady=10)
                NUM_entry = Entry(data_frame)
                NUM_entry.grid(row=0, column=1, padx=1, pady=1)
                #fn_entry.insert(0, record[0])
                PR_label = Label(data_frame, text="Room Price")
                PR_label.grid(row=0, column=2, padx=10, pady=10)
                PR_entry = Entry(data_frame)
                PR_entry.grid(row=0, column=3, padx=10, pady=10)
                #
                AV_label = Label(data_frame, text="Availability")
                AV_label.grid(row=1, column=0, padx=10, pady=10)
                AV_entry = Entry(data_frame)
                AV_entry.grid(row=1, column=1, padx=1, pady=1)
                #
                CL_label = Label(data_frame, text="Clean status")
                CL_label.grid(row=1, column=2, padx=10, pady=10)
                CL_entry = ttk.Combobox(data_frame)
                CL_entry.grid(row=1, column=3, padx=1, pady=1)
                # buttons

            def BottomFrames():
                button_frame = LabelFrame(
                    LeaseFrame, text="Edit", background="darksalmon")
                button_frame.pack(fill="both", expand="NO", padx=20)
                ADD_button = Button(button_frame, text="Add Lease")
                ADD_button.grid(row=0, column=0, padx=10, pady=10)
                DELETE_button = Button(button_frame, text="Delete Lease")
                DELETE_button.grid(row=0, column=1, padx=10, pady=10)
                Clean_button = Button(button_frame, text="Cleaning Status")
                Clean_button.grid(row=0, column=2, padx=10, pady=10)

            dataFrames()
            BottomFrames()

        HallFrames()
        RoomFrames()
        LeaseFrames()

    TopFrames()
    MiddleFrames()

    ManagerPage.mainloop()


def login_page():

    window = tk.Tk()
    window_width = 800
    window_height = 520
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    centerx = int(screen_width / 2 - window_width / 2)
    centery = int(screen_height / 2 - window_height / 2)
    window.minsize(width=window_width, height=window_height)
    window.maxsize(width=window_width, height=window_height)

    img = PhotoImage(file='/Users/willi/OneDrive/Pictures/home.PNG')
    BackgroundPicture = Label(window, image=img, width=window_width,
                              height=window_height, highlightthickness=1, highlightbackground="black")
    BackgroundPicture.place(x=0, y=0)

    window.title("Saw Accomdation Management")
    window.geometry(f'{window_width}x{window_height}+{centerx}+{centery}')

    def UpperFrame():
        upperFrame = Frame(window, background="coral", width=800,
                           height=20, highlightthickness=1, highlightbackground="black")
        upperFrame.pack(pady=0)

    def MiddleFrame():
        def login():
            file = open(
                "/Users/willi/OneDrive/Documents/POP/practicall/Year 2 ASD/Classes-CourseWork/Worksheet/testusernames.txt", "w")
            username = name_entry.get()
            password = passwordEntry.get()
            file.write(username + '\n')
            file.close()
            if username == "Will":
                if password == "123":
                    window.destroy()
                    Manager_page(username)
                else:
                    messagebox.showerror(
                        'Failed Login!', 'Incorrect Password!')
            else:
                messagebox.showerror(
                    'Failed Login!', 'Username Not Recognised!')

        LoginFrame = Frame(window, background="coral", width=3,
                           height=2, highlightthickness=2, highlightbackground="black")
        LoginFrame.pack(pady=150)

        title = tk.Label(LoginFrame, text="Welcome, please login below.", foreground="black",
                         background="coral", width=40, height=2, font=("calibri"), relief=RAISED)
        title.pack()

        tk.Label(LoginFrame, text="Name:", background="coral",
                 foreground="black").pack()

        name_entry = tk.Entry(
            LoginFrame, background="light grey", relief=RAISED)
        name_entry.pack()

        tk.Label(LoginFrame, text="Password:",
                 background="coral", foreground="black").pack()

        passwordEntry = tk.Entry(
            LoginFrame, background="light grey", relief=RAISED)
        passwordEntry.pack()

        loginbutton = tk.Button(LoginFrame, text="Login", foreground="black",
                                highlightbackground="light grey", command=login, relief=GROOVE)
        loginbutton.pack(pady=5)

    def BottomFrame():

        bottomFrame = Frame(window, background="coral", width=800,
                            height=20, highlightthickness=1, highlightbackground="black")
        bottomFrame.pack()

        def LeftFrame():
            leftFrame = Frame(bottomFrame, background="coral",
                              width=29, height=20)
            leftFrame.pack(side=LEFT)

            InfoLabel = tk.Label(leftFrame, width="60", height="5", text="      UWE Accomodation Office",
                                 background="coral", foreground="black", anchor='w')
            InfoLabel.pack()

        def Rightrame():
            rightFrame = Frame(
                bottomFrame, background="coral", width=20, height=20)
            rightFrame.pack(side=RIGHT)

            InfoLabel2 = tk.Label(rightFrame, width="60", height="5", text="Telelphone number: 07576 928525       ",
                                  background="coral", foreground="black", anchor='e')
            InfoLabel2.pack()
        LeftFrame()
        Rightrame()

    UpperFrame()
    MiddleFrame()
    BottomFrame()

    window.mainloop()
