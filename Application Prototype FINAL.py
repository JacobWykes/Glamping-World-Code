import tkinter as tk

class item:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        itemList.append(self)
        itemNames.append(name)

def getPrice():
    for s in itemList:
        if s.name == selectedItem.get():
            price.set(s.price*var5.get())
    for s in itemList:
        if s.name == selectedItem.get():
            price2.set(s.price*var5.get()+(s.price*var5.get())*0.13)

#Creates the height and width for the window
HEIGHT = 600 
WIDTH = 725
root = tk.Tk()

canvas = tk.Canvas(root,height=HEIGHT, width = WIDTH, bg= 'black')
canvas.pack()
root.title("Glamping World Phone Ordering Processing")
#This is used for the backgroud
lower_frame = tk.Frame(root, bg="black")
lower_frame.place(relx=0,rely=0,relwidth = 1, relheight=1)        
#All of the content goes on top of the frame
frame = tk.Frame(root, bg="#e6e6e6")
frame.place(relx=0.01,rely=0.01,relwidth = 0.98, relheight=0.98)


#This is used to make the items in the item class
itemList = []
itemNames = []

item("", 0)
item("Tent", 100)
item("Sleeping Bag", 30)
item("Sleeping Pad", 25)
item("First Aid Kit", 40)
item("Backpack", 50)
item("Tarp", 15)


price = tk.IntVar()
price2 = tk.IntVar()
selectedItem = tk.StringVar()
selectedItem.set(itemNames[0])

label =tk.Label(frame, text= "Product Name", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.35,relwidth=.2, relheight=.05)
var2 = tk.StringVar()
options_menu2 = tk.OptionMenu(frame,selectedItem, *itemNames)
options_menu2.place(relx=.25, rely=.35,relwidth=.15, relheight=.05)



label = tk.Label(frame, text= "Product Cost", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.69, rely=.4,relwidth=.16, relheight=.05)
priceLable = tk.Label(frame, textvariable = price, font='Helvetica 12', bg="white")
priceLable.place(relx=.865, rely=.4,relwidth=.08, relheight=.05)
label = tk.Label(frame, text= "$", font='Helvetica 12', bg="white")
label.place(relx=.85, rely=.4,relwidth=.02, relheight=.05)

label = tk.Label(frame, text= "Total Cost", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.69, rely=.455,relwidth=.16, relheight=.045)
priceLable = tk.Label(frame, textvariable = price2, font='Helvetica 12', bg="white")
priceLable.place(relx=.865, rely=.455,relwidth=.08, relheight=.045)
label = tk.Label(frame, text= "$", font='Helvetica 12', bg="white")
label.place(relx=.85, rely=.455,relwidth=.02, relheight=.045)

label = tk.Label(frame, text= "(Sales Tax: 13%)", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.52, rely=.45,relwidth=.18, relheight=.05)

#This is used to Calculate the costs
button2 = tk.Button(frame, text="Add item to cart",font='Helvetica 12', bg='light gray', fg='black', command = getPrice)
button2.place(relx=.05, rely=.45,relwidth=.2, relheight=.05)

label =tk.Label(frame, text= "Glamping World Phone Ordering",font='Helvetica 18 bold', bg='light grey')
label.place(relx=0, rely=0,relwidth=1, relheight=.1)
#Just a line break so it looks good
label =tk.Label(frame,font='Helvetica 12', bg='black')
label.place(relx=0, rely=.1,relwidth=1, relheight=.0075)

#This is used to create the picture
photo = tk.PhotoImage(file="C:\Python\GWlogo.gif") # specify the path to your file
label = tk.Label(frame, image=photo, bg='light grey',justify='right')  #put the image in a label to disdaply it in the window
label.place(relx=.8, rely=.0,relwidth=.2, relheight=.1)  # show the label on the screen

#Customer information section break
label =tk.Label(frame, text= "Customer's Information", anchor= 'w', font='Helvetica 12 bold', bg="#e6e6e6")
label.place(relx=0, rely=.1075,relwidth=.27, relheight=.05)

#Most of the following is creating lables and fields for data entry
label =tk.Label(frame, text= "First Name", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.15,relwidth=.2, relheight=.05)
first_name_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
first_name_entry.place(relx=.25, rely=.15,relwidth=.25, relheight=.05)

label =tk.Label(frame, text= "Surname", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.5, rely=.15,relwidth=.2, relheight=.05)
last_name_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
last_name_entry.place(relx=.7, rely=.15,relwidth=.25, relheight=.05)

label =tk.Label(frame, text= "Customer ID", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.2,relwidth=.2, relheight=.05)
customerID_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
customerID_entry.place(relx=.25, rely=.2,relwidth=.25, relheight=.05)

label =tk.Label(frame, text= "Birthday(Optional)", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.5, rely=.2,relwidth=.2, relheight=.05)
birthday_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
birthday_entry.place(relx=.7, rely=.2,relwidth=.25, relheight=.05)

label =tk.Label(frame, text= "Dial Code", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.25,relwidth=.2, relheight=.05)
var = tk.StringVar()
options_menu = tk.OptionMenu(frame,var,"+1","+506","+44","+52","+91","+86")
options_menu.place(relx=.25, rely=.25,relwidth=.1, relheight=.05)

label =tk.Label(frame, text= "Phone Number", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.36, rely=.25,relwidth=.15, relheight=.05)
phone_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
phone_entry.place(relx=.52, rely=.25,relwidth=.15, relheight=.05)

label =tk.Label(frame, text= "Email", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.665, rely=.25,relwidth=.07, relheight=.05)
email_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
email_entry.place(relx=.74, rely=.25,relwidth=.255, relheight=.05)

#Creates the next section for Product details
label =tk.Label(frame, text= "Product Details", anchor= 'w', font='Helvetica 12 bold', bg="#e6e6e6")
label.place(relx=0, rely=.3,relwidth=.18, relheight=.05)

#Most of the following is creating lables and fields for data entry
label =tk.Label(frame, text= "Product Number", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.4, rely=.35,relwidth=.2, relheight=.05)
var3 = tk.StringVar()
options_menu3 = tk.OptionMenu(frame,var3,"1001","1002","1003","1007","1010","1013")
options_menu3.place(relx=.6, rely=.35,relwidth=.1, relheight=.05)
label =tk.Label(frame, text= "Item Size", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.73, rely=.35,relwidth=.1, relheight=.05)
var4 = tk.StringVar()
options_menu4 = tk.OptionMenu(frame,var4,"XS","S","M","L","XL","XXL")
options_menu4.place(relx=.85, rely=.35,relwidth=.1, relheight=.05)

#Most of the following is creating lables and fields for data entry
label =tk.Label(frame, text= "Item Quantity", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.4,relwidth=.2, relheight=.05)
var5 = tk.IntVar()
options_menu5 = tk.OptionMenu(frame,var5,"1","2","3","4","5","6","7","8","9")
options_menu5.place(relx=.25, rely=.4,relwidth=.08, relheight=.05)
label =tk.Label(frame, text= "Currency", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.35, rely=.4,relwidth=.12, relheight=.05)
var6 = tk.StringVar()
options_menu6 = tk.OptionMenu(frame,var6,"United States Dollar","Costa Rican colón")
options_menu6.place(relx=.48, rely=.4,relwidth=.2, relheight=.05)

var880 = tk.StringVar()
var880.set('0.00')
R1 = tk.Radiobutton(frame, text = "Regular Customer", variable = var880, value = '0.00', bg="#e6e6e6", font='Helvetica 10 bold')
R2 = tk.Radiobutton(frame, text = "Preferred Customer(5% Discount)", variable = var880, value = '0.05', bg="#e6e6e6", font='Helvetica 10 bold')
R1.place(relx=.27, rely=.3,relwidth=.2, relheight=.042)
R2.place(relx=.5, rely=.3,relwidth=.35, relheight=.042)

var800 = tk.StringVar()
var800.set('1')
R1 = tk.Radiobutton(frame, text = "New Customer", variable = var800, value = '1', bg="#e6e6e6", font='Helvetica 10 bold')
R2 = tk.Radiobutton(frame, text = "Returning Customer", variable = var800, value = '2', bg="#e6e6e6", font='Helvetica 10 bold')
R1.place(relx=.3, rely=.1075,relwidth=.18, relheight=.042)
R2.place(relx=.5, rely=.1075,relwidth=.22, relheight=.042)

#This is used to create the Help button uptop
menu = tk.Menu(frame)
root.config(menu=menu)
subMenu = tk.Menu(menu)
menu.add_cascade(label = "Help", menu=subMenu)
subMenu.add_command(label="Entering Information")
subMenu.add_command(label="Get Online Help")
subMenu.add_command(label="Tutorial")

#This is the next section Shipping Details
label =tk.Label(frame, text= "Shipping Details", anchor= 'w', font='Helvetica 12 bold', bg="#e6e6e6")
label.place(relx=0, rely=.5,relwidth=.18, relheight=.05)

#This Creates the RadioButton for in store pickup and ship to address
var802 = tk.StringVar()
var802.set('0.05')
R3 = tk.Radiobutton(frame, text = "In-Store Pickup", variable = var802, value = '0.05', bg="#e6e6e6", font='Helvetica 10 bold')
R4 = tk.Radiobutton(frame, text = "Ship to Address", variable = var802, value = '0.1', bg="#e6e6e6", font='Helvetica 10 bold')
R3.place(relx=.3, rely=.5,relwidth=.2, relheight=.045)
R4.place(relx=.5, rely=.5,relwidth=.2, relheight=.045)

#Most of the following is creating lables and fields for data entry
label =tk.Label(frame, text= "Address", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.55,relwidth=.15, relheight=.05)
address_entry1 = tk.Entry(frame,font='Helvetica 12', bg='white')
address_entry1.place(relx=.2, rely=.55,relwidth=.3, relheight=.05)

label =tk.Label(frame, text= "City", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.45, rely=.55,relwidth=.10, relheight=.05)
city_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
city_entry.place(relx=.535, rely=.55,relwidth=.15, relheight=.05)

label =tk.Label(frame, text= "State/Provinces", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.68, rely=.55,relwidth=.18, relheight=.05)
var7 = tk.StringVar()
options_menu7 = tk.OptionMenu(frame,var7,"San Jose","Heredia","Alajuela", "Cartago", "Puntarenas", "Guanacaste","Limon")
options_menu7.place(relx=.86, rely=.55,relwidth=.135, relheight=.05)

label =tk.Label(frame, text= "Country", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.6,relwidth=.15, relheight=.05)
var8 = tk.StringVar()
options_menu8 = tk.OptionMenu(frame,var8,"Costa Rica","United States")
options_menu8.place(relx=.2, rely=.6,relwidth=.15, relheight=.05)


var801 = tk.StringVar()
var801.set('0.05')
R5 = tk.Radiobutton(frame, text = "5% (standard 5-7 business days)", variable = var801, value = '0.05', bg="#e6e6e6", font='Helvetica 10 bold')
R6 = tk.Radiobutton(frame, text = "10% (standard 3-5 business days)", variable = var801, value = '0.1', bg="#e6e6e6", font='Helvetica 10 bold')
R5.place(relx=.3, rely=.65,relwidth=.32, relheight=.045)
R6.place(relx=.65, rely=.65,relwidth=.34, relheight=.045)

label =tk.Label(frame, text= "Postal Code", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.45, rely=.6,relwidth=.13, relheight=.05)
postal_code_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
postal_code_entry.place(relx=.6, rely=.6,relwidth=.15, relheight=.05)

label =tk.Label(frame,justify='left', text= "Payment Details", anchor= 'w', font='Helvetica 12 bold', bg="#e6e6e6")
label.place(relx=0, rely=.7,relwidth=.18, relheight=.05)

label =tk.Label(frame, text= "Name on Card", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.74,relwidth=.18, relheight=.05)
name_on_card_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
name_on_card_entry.place(relx=.25, rely=.74,relwidth=.3, relheight=.05)
label =tk.Label(frame, text= "CVV", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.64, rely=.74,relwidth=.1, relheight=.05)

CVV_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
CVV_entry.place(relx=.75, rely=.74,relwidth=.1, relheight=.05)
label =tk.Label(frame, text= "Card Number", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.79,relwidth=.18, relheight=.05)

card_number_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
card_number_entry.place(relx=.25, rely=.79,relwidth=.3, relheight=.05)
label =tk.Label(frame, text= "Expiration", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.58, rely=.79,relwidth=.15, relheight=.05)

var10 = tk.StringVar()
options_menu10 = tk.OptionMenu(frame,var10,"01","02","03","04","05","06","07","08","09","10","11","12")
options_menu10.place(relx=.72, rely=.79,relwidth=.08, relheight=.05)
var11 = tk.StringVar()
options_menu11 = tk.OptionMenu(frame,var11,"19","20","21","22","23","24","25","26")
options_menu11.place(relx=.8, rely=.79,relwidth=.08, relheight=.05)
button = tk.Button(frame, text="Submit Order",font='Helvetica 14 bold', bg='light gray', fg='black', command = root.destroy)
button.place(relx=.79, rely=.94,relwidth=.2, relheight=.05)

label =tk.Label(frame, text= "Billing Address", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.88,relwidth=.175, relheight=.05)
address_entry2 = tk.Entry(frame,font='Helvetica 12', bg='white')
address_entry2.place(relx=.23, rely=.88,relwidth=.3, relheight=.05)

label =tk.Label(frame, text= "City", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.45, rely=.88,relwidth=.10, relheight=.05)
city_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
city_entry.place(relx=.535, rely=.88,relwidth=.15, relheight=.05)

label =tk.Label(frame, text= "State/Provinces", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.68, rely=.88,relwidth=.18, relheight=.05)
var7 = tk.StringVar()
options_menu7 = tk.OptionMenu(frame,var7,"San Jose","Heredia","Alajuela", "Cartago", "Puntarenas", "Guanacaste","Limon")
options_menu7.place(relx=.86, rely=.88,relwidth=.135, relheight=.05)

label =tk.Label(frame, text= "Country", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.05, rely=.93,relwidth=.15, relheight=.05)
var8 = tk.StringVar()
options_menu8 = tk.OptionMenu(frame,var8,"Costa Rica","United States")
options_menu8.place(relx=.2, rely=.93,relwidth=.15, relheight=.05)

label =tk.Label(frame, text= "Postal Code", font='Helvetica 12', bg="#e6e6e6")
label.place(relx=.45, rely=.93,relwidth=.13, relheight=.05)
postal_code_entry = tk.Entry(frame,font='Helvetica 12', bg='white')
postal_code_entry.place(relx=.6, rely=.93,relwidth=.15, relheight=.05)
CheckVar8 = tk.IntVar()
C8 = tk.Checkbutton(frame, text = "Same as Shipping Address", variable = CheckVar8, onvalue = 1, offvalue = 0, height=5, width = 20,bg="#e6e6e6", font='Helvetica 10 bold')
C8.place(relx=.1, rely=.8389,relwidth=.34, relheight=.0375)

#loops to create window
root.mainloop()    

