#uniform_shop1_ASSESMENT.py
#create an app for uniform orders
#Ishanika. S, April 8th 2021

name = ""
age = ""

user_items = []


password_list = []

#MAKE 2D LIST
user_list = [["bdsc", "Pass1234"]]


total_cost = 0 
price = []

def calculatetotal():
    global total_cost
    total = price * 1
    print("Your total comes to ${}".format(total))
    print("Please Take This To The Front Desk At The BDSC Uniform Shop")
                                           


def menu(name):
    mode = int(input("""Choose mode by entering a number: \n1.View Junior Unform Prices \n2.View Senior Uniform Prices\n3.Purchase Items \n4.Exit"""))
    return mode

def junior_uniform_prices():
    f = open("abc.txt.txt", "r")
    print(f.read())    
  
#CHANGE TO TEXT FILE
                  
def senior_uniform_prices():
    s_uniform = int(input("""Senior uniform shop prices (YR 12-13): \n1S. BOYS Short Sleeve Shirt = $47.00 \n2S. BOYS Tie (Terms 2 and 3 compulsory) = 25.00 \n3S. BOYS Dress Socks = 9.00 \n4S. GIRLS Short Sleeve Blouse = $46.00 \n5S. GIRLS Skirt = $100 \n6S. GIRLS Socks = $9.00 \n7S. OPTIONAL OPTIONS: \n8S. UNISEX School Jacket = $111.00 \n9S. UNISEX Scarf 32.00 \n10S. UNISEX Cap = $10.00 \n11S. UNISEX Whanau Tee = $40.00 \n12S. UNISEX PE Shorts = $34.00 \n13S. BOYS Blazer = $245.00 \n14S. BOYS Long Sleeve Shirt (Terms 2 and 3 only) \nAvailable for purchase in Terms 2 and 3 only = $50.00 \n15S. BOYS Shorts(Terms 1 and 4 only) = $55.00 \n16S. BOYS Socks (for the Shorts) = $9.00 \n17S. GIRLS Blazer = $245.00 \n18S. GIRLS Long Sleeve Blouse (Terms 2 and 3 only) \nAvailable for purchase in Terms 2 and 3 only = $49.00 \n19S. GIRLS Tie = $25.00 \n20S. GIRLS Tights (Terms 2 and 3 only) = $9.00"""))
    print(s_uniform)
    s_sports = int(input("""1. Boys Rugby Shorts := $38.00" \n2. Girls Hockey Shorts = $32.00 \nG3. irls Spanks = $50.00 \n4. Unisex Tees = $35.00 \n5. Unisex Sweatshirts = $69.00 \n6. Unisex Socks = $16.00"""))
    print(s_sports)
    
def purchase_items():
    while True:
              
        item_input = input("Please Type number of the item you would like or type end:")
        if item_input == "end":
            break
        else:
            user_items.append(item_input)
            
    print("These are your items in your cart:", user_items) 
    print("Your Total is....")
    print("Your barcode is...Please take this to the BDSC Uniform Shop \nto complete your purchase. \nThank You")


# Introduce users to purpose of the app
print("Welcome to the 2021 BDSC Uniform Shop App.")



# Asks user for age, user must be above the age of 13 and under the age of 18
oldest_age = 18
youngest_age = 13
age = float(input("What is your age?: "))
if age < youngest_age:
    print("Apologies, you must be over the age of 13 to continue")
    exit()
elif age > oldest_age:
    print("Apologies, you must be under to age of 18 to continue")
    exit()
else :
    print("Thank you, Welcome")
    
# Main Routine
    while True:

#Asking for user input and .upper() function which converts user unput to uppercase
        user = input("Please enter: \nL to login or N to create an account: ").upper()
        if user == "L":
            u_username = input("Username: ")
            u_password = input("Password: ")
            if u_username and u_password in user_list:
                print("Welcome", name ,"Password Matched! You may now choose uniform shop app options. ")
            break
#Asking user to select to create an account, the password requirements must also be matched. 
        elif user == "N":
            u_username = input("Enter unsername: ")
            while True:
                u_password = input("Your password must be a minimum of 8 characters, include a capital letter and a number. \nEnter password:").strip()
                if (any(passcondition.isupper() for passcondition in u_password) and any(passcondition.isdigit()for passcondition in u_password) and len(u_password) >= 8):
                    user_list.append([u_username, u_password])
                    print("Your account has been created!")
                else:
                    print("Your password does not meet the password requirements. \nIt must have at least 8 characters, \include a capital letter as well as an integer")
                break
        else:
            print("That is an invalid option, please enter L to login ot N to create an account: ") 
            
while True:
    chosen_option = menu(name)
    if chosen_option == 1:
        junior_uniform_prices()     
    elif chosen_option == 2:
        senior_uniform_prices()
    elif chosen_option == 3:
        purchase_items()
        break
    elif chosen_option == 4:
        exit()
        break
    
    else:
        print("That is an invalid option, Please enter again")     
        


