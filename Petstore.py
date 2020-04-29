"""
This is a project called 'Petstore' with in code documentation.
    @author  = Shadrach Simon Sundar , Rayma Elsa Babu
This program allows the user to add animal breeds to various categories,
it is not possible to add integer values in the entry box and its not possible to add the same name twice.

"""


"""
The below lines of code will import the class tkinter and all its functions
including ttk and message box. ttk is used to create combo box and messagebox is used to 
create warning message boxes
"""
from tkinter import *  # From the class tkinter all the functions are imported.
from tkinter import ttk  # From the class tkinter the function ttk is imported to create combobox.
from tkinter import messagebox  # From the class tkinter the function message box is imported to create Error messages.

"""
The next line create a class called Petstore which takes two arguments, 
which are : the object itself and the main window root is passed as master.
Inside the class Petstore, the First function created is a special function called
__init__ function which is used to initialize which gets called by itself and 
executes the next set of codes automatically. 
A background picture is assigned to a label to be displayed. A display frame to 
show the current feedback of the pets selected is made. Every line of code has 
been documented and easily accessible for future development purposes.
a function called 'labels()' is created to make the necessary labels to be displayed
on the interface. An edit frame is created to hold the edit field at the desired postion on 
user interface. Three edit fields are created for three different animal breeds input.
Three combo boxes which holds assigned animal breeds are created using the function ttk.combobox()
and the default value to be displayed is mentioned using the current() function. When the combo box
is pressed, it displays a predefined animal breed list which holds predefined values to be displayed on the 
display frame. A function named buttons() is created to contain all the buttons required for the program.
The button click1 click2 and click3 are assigned to get details for Dogs, Cats and Birds respectively,
the buttons click4, click5, click6 are assigned to add breeds to the combo boxes of Dogs, Cats and Birds respectively.
the functions for click1, click2 and click3 works in the similar way, the current displayes value of the combo box is fetched and
compared. If the Option is "Select" and if the user pressed get details then, in the display box a statement will appear
stating that, please select one of the breeds and then press get details. If the option is empty, a warning message 
will appear to guide the user saying the field cannot be empty and to select the option on the list. And if the user
types a value which is not on the list, it will display that the selected breed is not on the list. This is done by comparing the 
current element on the combo box with the variable which holds the values of the combo box by using if and elif methods.
If the current element is a newly added element, then it will display, thank you for adding a new breed to the petstore family.
To add new values to the combo boxes, three edit fields are created. One for each animal category. When the user leaves a blank 
field and tries to add that element to the combo box, a warning message will appear which is done again by if method. if the value 
is not blank then the else block will be executed. Inside the else block at first, there is another if block which checks if the 
value entered contains only alphabet or not, if true then the another if block checks if the value is already present in the old list.
If true, then it gives a warning message saying that the value already exists. If not in the list then the value is added to the combo box.
If the value entered is not an alphabet and if it has a digit or if its alphanumeric, it is check with the help of an elif block.
if none of it is true, then another else block is executed confirming that the value entered has special characters in it and
a warning message is displayed using the messagebox function.
Pre-defined statements are set to be displayed for old values of the elements in the combo box outside the class suite.
Finally a window is created to be passed into the class Petstore through and object 'x'. The size of the window is
defined using the function geometry "1500X900 ". Finally the window 'root' is made to run on loop till the window is closed. 
 
"""
class Petstore:  # class Petstore is created.

    def __init__(self,
                 master):  # The method __init__() gets called automatically when the class Petstore is called through an object.
        self.bk_image = PhotoImage(
            file='pet1.png')  # Uses the function PhotoImage() to store the image file in the variable bk_image
        self.bk_label = Label(master,
                              image=self.bk_image)  # The function label() creates a label in the master window and passes the image to the label.
        self.bk_label.place(relwidth=1,
                            relheight=1)  # The function place() places the label in the master window and the parameters relwidth and relheight makes the label fit to the window size.
        self.labels()  # calls the function labels() and creates all the labels in the main window.

        dis_frame = Frame(master, bg='#80c1ff',
                          bd=10)  # creates a frame inside the window with specified background color and specified border thickness
        dis_frame.place(x=50, y=500, relwidth=0.30,
                        relheight=0.10)  # places the label at specified x and y co-ordinates relative to the size of the window.
        self.dis_label = Label(dis_frame, text="Please select one pet and press the button details", fg='black',
                               font=20)  # creates a label in dis_frame with specified text font and color.
        self.dis_label.place(relwidth=1,
                             relheight=1)  # places the label in the frame relative to the size of the frame.
        ed_frame1 = Frame(master, bg='#80c1ff', bd=10)  # creates a frame for the edit box.
        ed_frame1.place(x=1100, y=500, relwidth=0.10,
                        relheight=0.06)  # Places the frame at specified x-y co-ordinates and relative to the specified width and height of the window.
        self.ed_entry1 = Entry(ed_frame1)  # Creates an Entry widget inside the frame.
        self.ed_entry1.place(relwidth=1, relheight=1)  # places the entry widget inside the frame.
        ed_frame2 = Frame(master, bg='#80c1ff', bd=10)  # creates a frame for the next entry widget.
        ed_frame2.place(x=1100, y=568, relwidth=0.10,
                        relheight=0.06)  # Places the frame at specified x-y co-ordinates and relative to the specified width and height of the window.
        self.ed_entry2 = Entry(ed_frame2)  # Creates an Entry widget inside the frame.
        self.ed_entry2.place(relwidth=1, relheight=1)  # places the entry widget inside the frame.
        ed_frame3 = Frame(master, bg='#80c1ff', bd=10)  # creates a frame for the next entry widget.
        ed_frame3.place(x=1100, y=636, relwidth=0.10,
                        relheight=0.06)  # Places the frame at specified x-y co-ordinates and relative to the specified width and height of the window.
        self.ed_entry3 = Entry(ed_frame3)  # Creates an Entry widget inside the frame.
        self.ed_entry3.place(relwidth=1, relheight=1)  # places the entry widget inside the frame.
        self.combo1 = ttk.Combobox(master)  # Creates a combo box in the main window)
        self.combo1['values'] = ("Select", "Labrador", "Pug", "Beagle")  # Creates a list of values in the combo box.
        self.combo1.current(
            0)  # Displays the default value in the combo box by specifying the index number of the value.
        self.combo1.place(x=50, y=300)  # Places the combo box in the x-y co-ordinate of the main window.
        self.combo2 = ttk.Combobox(master)  # Creates a combo box in the main window)
        self.combo2['values'] = (
            "Select", "Persian", "Siberian", "Himalayan")  # Creates a list of values in the combo box.
        self.combo2.current(
            0)  # Displays the default value in the combo box by specifying the index number of the value.
        self.combo2.place(x=450, y=300)  # Places the combo box in the x-y co-ordinate of the main window.
        self.combo3 = ttk.Combobox(master)  # Creates a combo box in the main window )
        self.combo3['values'] = ("Select", "Cockatoo", "Macaw", "Dove")  # Creates a list of values in the combo box.
        self.combo3.current(
            0)  # Displays the default value in the combo box by specifying the index number of the value.
        self.combo3.place(x=850, y=300)  # Places the combo box in the x-y co-ordinate of the main window.
        self.buttons()  # calls the function buttons() which creates all the buttons inside the button function.

    def labels(self):  # Creates the function labels().
        Label(self.bk_label, text="Enter the name of the Dog breed you want to sell :", font=("Arial Bold", 18),bg='#A6891B').place(x=650, y=514)  # creates a label with specified text and places it in the mentioned x and y co-ordinate
        Label(self.bk_label, text="Enter the name of the Cat breed you want to sell :", font=("Arial Bold", 18),bg='#6B4AB8').place(x=650, y=582)  # creates a label with specified text and places it in the mentioned x and y co-ordinate
        Label(self.bk_label, text="Enter the name of the Bird breed you want to sell :", font=("Arial Bold", 18),bg='#4AB853').place(x=650, y=650)  # creates a label with specified text and places it in the mentioned x and y co-ordinate
        Label(self.bk_label, text="'Welcome to the pet store'", font=("Arial Bold", 50),bg='#DAD785').place(x=400, y=100)  # creates a label with specified text and places it in the mentioned x and y co-ordinate
        Label(self.bk_label, text="Dogs", font=("Arial Bold", 25), bg='#A6891B').place(x=115, y=250)  # creates a label with specified text and places it in the mentioned x and y co-ordinate
        Label(self.bk_label, text="Cats", font=("Arial Bold", 25), bg='#6B4AB8').place(x=515, y=250)  # creates a label with specified text and places it in the mentioned x and y co-ordinate
        Label(self.bk_label, text="Birds", font=("Arial Bold", 25), bg='#4AB853').place(x=915, y=250)  # creates a label with specified text and places it in the mentioned x and y co-ordinate

    def buttons(self):  # creates the function buttons().
        Button(self.bk_label, text="Get Details", activeforeground='#73C6B6', fg='red',command=self.click1).place(x=50, y=400)  # creates a button with the specified text and assigns it to the function click1 when pressed.
        Button(self.bk_label, text="Get Details", activeforeground='#73C6B6', fg='red', command=self.click2).place(x=450, y=400)  # creates a button with the specified text and assigns it to the function click2 when pressed.
        Button(self.bk_label, text="Get Details", activeforeground='#73C6B6', fg='red', command=self.click3).place(x=850, y=400)  # creates a button with the specified text and assigns it to the function click3 when pressed.
        Button(self.bk_label, text="Add details", activeforeground='#73C6B6', fg='red', command=self.click4).place(x=1250, y=512)  # creates a button with the specified text and assigns it to the function click4 when pressed.
        Button(self.bk_label, text="Add details", activeforeground='#73C6B6', fg='red', command=self.click5).place(x=1250, y=580)  # creates a button with the specified text and assigns it to the function click5 when pressed.
        Button(self.bk_label, text="Add details", activeforeground='#73C6B6', fg='red', command=self.click6).place(x=1250, y=648)  # creates a button with the specified text and assigns it to the function click6 when pressed.

    def click1(self):  # Creates a method click1 to be called when the button below the dog section is pressed.
        global a, b, c  # the variables 'a' 'b' 'c' defined outside the method can be used inside the suite using the Global keyword.
        old_list = self.combo1.cget(
            'values')  # the existing values of the combo box1 is assigned to a variable old_list.
        current_ele = self.combo1.get()  # The displayed value on combobox1 is fetched and assigned to a variable current_ele

        if current_ele == '':  # If the current value in the combobox is empty the following code will be executed.
            messagebox.showerror('Oops',
                                 'The Option cannot be empty,Please select one of the Dog breed and press Details')  # Displays the error window with the specified message.
        elif current_ele == "Select":  # If the current value in the combobox is 'select' the following code will be executed.
            messagebox.showerror('Oops',
                                 'Please Select one of the option on the list and then press get details')  # Displays the error window with the specified message.
            self.dis_label.config(
                text="Please select one of the breeds and press get details")  # Displays the specified text in the display label.
        elif current_ele == "Labrador":  # If the current value in the combobox is 'Labrador' the following code will be executed.
            self.dis_label.config(
                text=a)  # Displays the text stored in the variable 'a' in the display label by using the config function.
        elif current_ele == "Pug":  # If the current value in the combobox is 'Pug' the following code will be executed.
            self.dis_label.config(
                text=b)  # Displays the text stored in the variable 'b' in the display label by using the config function.
        elif current_ele == "Beagle":  # If the current value in the combobox is 'Beagle' the following code will be executed.
            self.dis_label.config(
                text=c)  # Displays the text stored in the variable 'c' in the display label by using the config function.
        elif current_ele not in old_list:  # If the current value in the combobox does not belong to old_list the following code will be executed.
            messagebox.showerror('Oops',
                                 'The selected Dog Breed is not on the list')  # Displays the error window with the specified message.
            self.dis_label.config(text="Not in the list")  # Displays the specified text in the display label.
        else:  # If the current value is a newly added value, the following block will be executed.
            self.dis_label.config(
                text="Thank you for adding the Dog '" + current_ele + "' to the pet store family")  # Displays the specified text along with the name of that element in the display label.

    def click2(self):  # Creates a method click2 to be called when the button below the Cat section is pressed.
        global d, e, f  # the variables 'd' 'e' 'f'  defined outside the method can be used inside the suite using the Global keyword.
        old_list = self.combo2.cget(
            'values')  # the existing values of the combo box2 is assigned to a variable old_list.
        current_ele = self.combo2.get()  # The displayed value on combobox2 is fetched and assigned to a variable current_ele

        if current_ele == '':  # If the current value in the combobox is empty the following code will be executed.
            messagebox.showerror('Oops',
                                 'The Option cannot be empty,Please select one of the Cat breed and press get Details')  # Displays the error window with the specified message.
        elif current_ele == "Select":  # If the current value in the combobox is 'select' the following code will be executed.
            messagebox.showerror('Oops',
                                 'Please Select one of the option on the list and then press get details')  # Displays the error window with the specified message.
            self.dis_label.config(
                text="Please select one of the breeds and press details")  # Displays the specified text in the display label.
        elif current_ele == "Persian":  # If the current value in the combobox is 'Persian' the following code will be executed.
            self.dis_label.config(
                text=d)  # Displays the text stored in the variable 'd' in the display label by using the config function.
        elif current_ele == "Siberian":  # If the current value in the combobox is 'Siberian' the following code will be executed.
            self.dis_label.config(
                text=e)  # Displays the text stored in the variable 'e' in the display label by using the config function.
        elif current_ele == "Himalayan":  # If the current value in the combobox is 'Himalayan' the following code will be executed.
            self.dis_label.config(
                text=f)  # Displays the text stored in the variable 'f' in the display label by using the config function.
        elif current_ele not in old_list:  # If the current value in the combobox does not belong to old_list the following code will be executed.
            messagebox.showerror('Oops',
                                 'The selected Cat Breed is not on the list')  # Displays the error window with the specified message.
            self.dis_label.config(text="Not in the list")  # Displays the specified text in the display label.
        else:  # If the current value is a newly added value, the following block will be executed.
            self.dis_label.config(
                text="Thank you for adding the Cat '" + current_ele + "' to the pet store family")  # Displays the specified text along with the name of that element in the display label.

    def click3(self):  # Creates a method click1 to be called when the button below the Bird section is pressed.
        global g, h, i  # the variables 'g' 'h' 'i'  defined outside the method can be used inside the suite using the Global keyword.
        old_list = self.combo3.cget(
            'values')  # the existing values of the combo box3 is assigned to a variable old_list.
        current_ele = self.combo3.get()  # The displayed value on combobox3 is fetched and assigned to a variable current_ele

        if current_ele == '':  # If the current value in the combobox is empty the following code will be executed.
            messagebox.showerror('Oops',
                                 'The Option cannot be empty,Please select one of the Bird breed and press get Details')  # Displays the error window with the specified message.
        elif current_ele == "Select":  # If the current value in the combobox is 'select' the following code will be executed.
            messagebox.showerror('Oops',
                                 'Please Select one of the option on the list and then press get details')  # Displays the error window with the specified message.
            self.dis_label.config(
                text="Please select one of the breeds and press details")  # Displays the specified text in the display label.
        elif current_ele == "Cockatoo":  # If the current value in the combobox is 'Cockatoo' the following code will be executed.
            self.dis_label.config(
                text=g)  # Displays the text stored in the variable 'g' in the display label by using the config function.
        elif current_ele == "Macaw":  # If the current value in the combobox is 'Macaw' the following code will be executed.
            self.dis_label.config(
                text=h)  # Displays the text stored in the variable 'h' in the display label by using the config function.
        elif current_ele == "Dove":  # If the current value in the combobox is 'Dove' the following code will be executed.
            self.dis_label.config(
                text=i)  # Displays the text stored in the variable 'i' in the display label by using the config function.
        elif current_ele not in old_list:  # If the current value in the combobox does not belong to old_list the following code will be executed.
            messagebox.showerror('Oops',
                                 'The selected Bird Breed is not on the list')  # Displays the error window with the specified message.
            self.dis_label.config(text="Not in the list")  # Displays the specified text in the display label.
        else:
            self.dis_label.config(
                text="Thank you for adding the Bird '" + current_ele + "' to the pet store family")  # If the current value is a newly added value, the following block will be executed.

    def click4(self):  # Creates a method click4 to be called when the button next to add new dog statement is pressed.
        newtext = self.ed_entry1.get()  # Assigns the input data from entry box1 to a variable 'newtext'.
        vals = self.combo1.cget('values')  # Assigns the original values to the variable 'vals'

        if newtext == '':  # If the input data is empty the following code will be executed.
            messagebox.showerror('Oops',
                                 'The Edit field cannot be empty , Type the name of the Dog breed you want to sell')  # Displays the error window with the specified message.
        else:  # If the input data is not empty then the following set of code will be executed.
            if newtext.isalpha():  # If the input data is a string with only alphabets, then the following code will execute.
                if newtext not in vals:  # Only If the input data is not available in the original combo box list, then the following code will execute.
                    self.combo1.config(values=vals + (newtext,))  # The new input will be added to the old list.
                    messagebox.showinfo('Congratulations',
                                        'The new pet has been added')  # Displays the information box with the specified text.
                    self.dis_label.config(
                        text="You have added '" + newtext + "' to the dog section")  # Displays the specified text along with the newly added value in the display label.
                else:  # If the input data is already available in the original combo box list, then the following code will execute.
                    messagebox.showinfo('Oops',
                                        'Sorry the Breed already exists, try adding a breed which is not on the list')  # Displays the info box with the specified text

            elif newtext.isdigit() or newtext.isalnum():  # If the input data is a string with numbers and alpha-numeric values, then the following code will execute.
                messagebox.showinfo('Oops',
                                    'Sorry its is not possible to add numeric or alpha-numeric Values, please enter a '
                                    'valid name')  # Displays the info box with specified text.
                self.dis_label.config(
                    text="Please enter a name with alphabets only")  # Displays the specified text on the display label
            else:  # If the input data has special characters in it, then the following code will be executed.
                messagebox.showinfo('Oops',
                                    'Sorry its is not possible to add special characters, please enter a valid name')  # Displays the specified text in a info box.
                self.dis_label.config(
                    text="Please enter a name with alphabets only")  # Displays the specified text in the display label.

    def click5(self):  # Creates a method click5 to be called when the button next to add new Cat statement is pressed.
        newtext = self.ed_entry2.get()  # Assigns the input data from entry box1 to a variable 'newtext'
        vals = self.combo2.cget('values')  # Assigns the original values to the variable 'vals'

        if newtext == '':  # If the input data is empty the following code will be executed.
            messagebox.showerror('Oops',
                                 'The Edit field cannot be empty , Type the name of the Cat breed you want to sell')  # Displays the error window with the specified message.
        else:  # If the input data is not empty then the following set of code will be executed.
            if newtext.isalpha():  # If the input data is a string with only alphabets, then the following code will execute.
                if newtext not in vals:  # Only If the input data is not available in the original combo box list, then the following code will execute.
                    self.combo2.config(values=vals + (newtext,))  # The new input will be added to the old list.
                    messagebox.showinfo('Congratulations',
                                        'The new pet has been added')  # Displays the information box with the specified text.
                    self.dis_label.config(
                        text="You have added '" + newtext + "' to the cat section")  # Displays the specified text along with the newly added value in the display label.
                else:  # If the input data is already available in the original combo box list, then the following code will execute.
                    messagebox.showinfo('Oops',
                                        'Sorry the Breed already exists, try adding a breed which is not on the list')  # Displays the info box with the specified text

            elif newtext.isdigit() or newtext.isalnum():  # If the input data is a string with numbers and alpha-numeric values, then the following code will execute.
                messagebox.showinfo('Oops',
                                    'Sorry its is not possible to add numeric or alpha-numeric Values, please enter a '
                                    'valid name')  # Displays the info box with specified text.
                self.dis_label.config(
                    text="Please enter a name with alphabets only")  # Displays the specified text on the display label
            else:  # If the input data has special characters in it, then the following code will be executed.
                messagebox.showinfo('Oops',
                                    'Sorry its is not possible to add special characters, please enter a valid name')  # Displays the specified text in a info box.
                self.dis_label.config(
                    text="Please enter a name with alphabets only")  # Displays the specified text in the display label.

    def click6(self):  # Creates a method click4 to be called when the button next to add new Bird statement is pressed.
        newtext = self.ed_entry3.get()  # Assigns the input data from entry box1 to a variable 'newtext'
        vals = self.combo3.cget('values')  # Assigns the original values to the variable 'vals'

        if newtext == '':  # If the input data is empty the following code will be executed.
            messagebox.showerror('Oops',
                                 'The Edit field cannot be empty , Type the name of the Bird breed you want to sell')  # Displays the error window with the specified message.
        else:  # If the input data is not empty then the following set of code will be executed.
            if newtext.isalpha():  # If the input data is a string with only alphabets, then the following code will execute.
                if newtext not in vals:  # Only If the input data is not available in the original combo box list, then the following code will execute.
                    self.combo3.config(values=vals + (newtext,))  # The new input will be added to the old list.
                    messagebox.showinfo('Congratulations',
                                        'The new pet has been added')  # Displays the information box with the specified text.
                    self.dis_label.config(
                        text="You have added '" + newtext + "' to the bird section")  # Displays the specified text along with the newly added value in the display label.
                else:  # If the input data is already available in the original combo box list, then the following code will execute.
                    messagebox.showinfo('Oops',
                                        'Sorry the Breed already exists, try adding a breed which is not on the list')  # Displays the info box with the specified text

            elif newtext.isdigit() or newtext.isalnum():  # If the input data is a string with numbers and alpha-numeric values, then the following code will execute.
                messagebox.showinfo('Oops',
                                    'Sorry its is not possible to add numeric or alpha-numeric Values, please enter a '
                                    'valid name')  # Displays the info box with specified text.
                self.dis_label.config(
                    text="Please enter a name with alphabets only")  # Displays the specified text on the display label
            else:  # If the input data has special characters in it, then the following code will be executed.
                messagebox.showinfo('Oops',
                                    'Sorry its is not possible to add special characters, please enter a valid name')  # Displays the specified text in a info box.
                self.dis_label.config(
                    text="Please enter a name with alphabets only")  # Displays the specified text in the display label.


# Assigns String to a variable 'a'
a = "Name: Labrador;" \
    " Age: 2 months old;" \
    " Colour: black;" \
    " weight: 2 kg."
# Assigns String to a variable 'b'
b = "Name: Pug;" \
    " Age: 1 month old;" \
    " Colour: beige;" \
    " weight: 1 kg."
# Assigns String to a variable 'c'
c = "Name: Beagle;" \
    " Age: 3 months old;" \
    " Colour: brown;" \
    " weight: 1 kg."
# Assigns String to a variable 'd'
d = "Name: Persian;" \
    " Age: 2 months old;" \
    " Colour: cream;" \
    " weight: 1 kg."
# Assigns String to a variable 'e'
e = "Name: Siberian;" \
    " Age: 4 months old;" \
    " Colour: grey;" \
    " weight: 600 g."
# Assigns String to a variable 'f'
f = "Name: Himalayan;" \
    " Age: 1 month old;" \
    " Colour: white;" \
    " weight: 200 g."
# Assigns String to a variable 'g'
g = "Name: Cockatoo;" \
    " Age: 6 month old;" \
    " Colour: blue;" \
    " weight: 300 g."
# Assigns String to a variable 'h'
h = "Name: Macaw" \
    " Age: 3 months old;" \
    " Colour: blue;" \
    " weight: 120 g."
# Assigns String to a variable 'i'
i = "Name: Dove;" \
    " Age: 3 months old;" \
    " Colour: white;" \
    " weight: 125 g"
root = Tk()  # Passes the window Tk() to an object 'root'
root.geometry("1500x900")  # Gives the dimension of the window.
root.title("Elsa's Pet Store")  # Gives window title.
x = Petstore(root)  # Passes the class Petstore with parameter 'root' to an object 'x'
root.mainloop()  # Runs the main window on loop till the window is closed.
