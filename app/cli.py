import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import sessionmaker # type: ignore
from app.database import engine, Base, SessionLocal
from .models import Restaurant, MenuItem, Reservation
from .utils import clear_screen, get_input

Base.metadata.create_all(bind=engine)

#List of main menu
def main_menu():
    clear_screen()
    print("Restaurant Reservation System")
    print("1. Manage Restaurants")
    print("2. Manage Menu Items")
    print("3. Manage Reservations")
    print("4. Exit")
    choice = get_input("Choose an option: ", int)

#If statement 
    if choice == 1:
        restaurant_menu()
    elif choice == 2:
        menu_item_menu()
    elif choice == 3:
        reservation_menu()
    elif choice == 4:
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

#List of resturant  menu
def restaurant_menu():
    clear_screen()
    print("Restaurant Menu")
    print("1. Create Restaurant")
    print("2. Delete Restaurant")
    print("3. List Restaurants")
    print("4. View Restaurant Reservations")
    print("5. Back to Main Menu")

    choice = get_input("Choose an option: ", int)
    if choice == 1:
        create_restaurant()
    elif choice == 2:
        delete_restaurant()
    elif choice == 3:
        list_restaurants()
    elif choice == 4:
        view_restaurant_reservations()
    elif choice == 5:
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        restaurant_menu()

#list of menu item mune
def menu_item_menu():
    clear_screen()
    print("Menu Item Menu")
    print("1. Create Menu Item")
    print("2. Delete Menu Item")
    print("3. List Menu Items")
    print("4. Back to Main Menu")

    choice = get_input("Choose an option: ", int)
    if choice == 1:
        create_menu_item()
    elif choice == 2:
        delete_menu_item()
    elif choice == 3:
        list_menu_items()
    elif choice == 4:
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        menu_item_menu()

#List of reservation menu
def reservation_menu():
    clear_screen()
    print("Reservation Menu")
    print("1. Create Reservation")
    print("2. Delete Reservation")
    print("3. List Reservations")
    print("4. Back to Main Menu")

    choice = get_input("Choose an option: ", int)
    if choice == 1:
        create_reservation()
    elif choice == 2:
        delete_reservation()
    elif choice == 3:
        list_reservations()
    elif choice == 4:
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        reservation_menu()

#Creating Restaurant
def create_restaurant():
    clear_screen()
    name = get_input("Enter restaurant name: ")
    db = SessionLocal()
    restaurant = Restaurant(name=name)
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    print(f"Restaurant {name} created with ID {restaurant.id}")
    input("Press Enter to continue...")
    restaurant_menu()

#Deleting Restaurant
def delete_restaurant():
    clear_screen()
    list_restaurants()
    restaurant_id = get_input("Enter restaurant ID to delete: ", int)
    db = SessionLocal()
    restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
    if restaurant:
        db.delete(restaurant)
        db.commit()
        print(f"Restaurant ID {restaurant_id} deleted")
    else:
        print("Restaurant not found")
    input("Press Enter to continue...")
    restaurant_menu()

#List of restaurants
def list_restaurants():
    clear_screen()
    db = SessionLocal()
    restaurants = db.query(Restaurant).all()
    for restaurant in restaurants:
        print(restaurant)
    input("Press Enter to continue...")

#Viewing restaurant reservation list
def view_restaurant_reservations():
    clear_screen()
    list_restaurants()
    restaurant_id = get_input("Enter restaurant ID to view reservations: ", int)
    db = SessionLocal()
    reservations = db.query(Reservation).filter(Reservation.restaurant_id == restaurant_id).all()
    if reservations:
        for reservation in reservations:
            print(reservation)
    else:
        print("No reservations found for this restaurant.")
    input("Press Enter to continue...")


#Creating menu items
def create_menu_item():
    clear_screen()
    list_restaurants()
    restaurant_id = get_input("Enter restaurant ID to add menu item: ", int)
    name = get_input("Enter menu item name: ")
    price = get_input("Enter menu item price: ", int)
    db = SessionLocal()
    menu_item = MenuItem.create(name=name, price=price, restaurant_id=restaurant_id)
    print(f"Menu Item {name} created with ID {menu_item.id}")
    input("Press Enter to continue...")
    menu_item_menu()

#Deleting menu items
def delete_menu_item():
    clear_screen()
    list_menu_items()
    menu_item_id = get_input("Enter menu item ID to delete: ", int)
    db = SessionLocal()
    menu_item = db.query(MenuItem).filter(MenuItem.id == menu_item_id).first()
    if menu_item:
        db.delete(menu_item)
        db.commit()
        print(f"Menu Item ID {menu_item_id} deleted")
    else:
        print("Menu item not found")
    input("Press Enter to continue...")
    menu_item_menu()

#list of menu items
def list_menu_items():
    clear_screen()
    db = SessionLocal()
    menu_items = db.query(MenuItem).all()
    for menu_item in menu_items:
        print(menu_item)
    input("Press Enter to continue...")

#Creating Reservation
def create_reservation():
    clear_screen()
    list_restaurants()
    restaurant_id = get_input("Enter restaurant ID to make reservation: ", int)
    customer_name = get_input("Enter customer name: ")
    date_time = get_input("Enter reservation date and time (YYYY-MM-DD HH:MM): ")
    reservation = Reservation.create(customer_name=customer_name, date_time=date_time, restaurant_id=restaurant_id)
    print(f"Reservation created with ID {reservation.id}")
    input("Press Enter to continue...")
    reservation_menu()

#Deleting Reservation
def delete_reservation():
    clear_screen()
    list_reservations()
    reservation_id = get_input("Enter reservation ID to delete: ", int)
    db = SessionLocal()
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
    if reservation:
        db.delete(reservation)
        db.commit()
        print(f"Reservation ID {reservation_id} deleted")
    else:
        print("Reservation not found")
    input("Press Enter to continue...")
    reservation_menu()

#List of reservation
def list_reservations():
    clear_screen()
    db = SessionLocal()
    reservations = db.query(Reservation).all()
    for reservation in reservations:
        print(reservation)
    input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
