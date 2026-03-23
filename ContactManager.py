#creating an empty dict, that stores data in key value pair and converts the key into hash - so for key we must use immutable obect

contacts = {}

#here email ="", means email field is optional, if not entered use empty sttring, while name and phoone are required

def add_contact(name, phone, email=""):
     
     if name in contacts:
          
          #old way to print, use f for new
          print(name + " already in contacts.")
          return
     
     #use name as key, and add the phone and email to that key
     contacts[name] = {"phone" : phone, "email" : email}

     # herer f is similar to concatenation operator
     print(f" '{name}' added.")

     #search contact
def search_contact(name):
          if name in contacts:
               
               #here info is another dict that stores, only phone and email, its like a innrer dict
               info = contacts[name]

               print(f"\n Name : {name}")
               print(f"\n Phone : {info['phone']}")

               #here for email we are using .get bcoz, email is key, if email is not there the prog will crash, so we are using get, to use get if email key is there then print if not then NA
               print(f"Email: {info.get('email') or 'N/A'}")
          else:
               print(f"Name '{name}' not found.")

def delete_contact(name):
     if contacts.pop(name, None) is not None:
          print(f"'{name}' deleted.")
     else:
          print(f"'{name}' not found.")     

def list_contacts():
     if not contacts:
          print("no contacts saved.")
          return          
     print(f"\n{'Name':<20} {'Phone':<15} Email")
     print("-" * 50)
     for name, info in contacts.items():
        print(f"{name:<20} {info['phone']:<15} {info.get('email') or 'N/A'}")

while True:
     print("\n1.Add  2.Search 3.Delete 4.List 5.Quit")   
     choice = input("Choice : ").strip()

     if choice == "1":
            add_contact(input("Name: ").strip(), input("Phone: ").strip(), input("Email (optional): ").strip())     
     elif choice == "2": search_contact(input("Name : ").strip())       
     elif choice == "3": delete_contact(input("Name: ").strip())
     elif choice == "4": list_contacts()
     elif choice == "5": break
     else: print("Enter 1-5.")