import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file)

# Add a new contact
def add_contact():
    name = simpledialog.askstring("Name", "Enter contact name:")
    if not name:
        return
    phone = simpledialog.askstring("Phone", "Enter phone number:")
    email = simpledialog.askstring("Email", "Enter email address:")
    address = simpledialog.askstring("Address", "Enter address:")
    
    if not phone:
        messagebox.showwarning("Warning", "Phone number is required.")
        return
    
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    save_contacts(contacts)
    update_contact_list()

# View all contacts
def view_contacts():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# Search for a contact
def search_contact():
    search_query = simpledialog.askstring("Search", "Enter name or phone number to search:")
    if not search_query:
        return

    results = [name for name in contacts if search_query in name or search_query in contacts[name]['phone']]
    contact_list.delete(0, tk.END)
    for name in results:
        details = contacts[name]
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# Update a contact
def update_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showwarning("Warning", "No contact selected.")
        return
    
    name = selected_contact.split(' - ')[0]
    if name in contacts:
        phone = simpledialog.askstring("Phone", "Enter new phone number:", initialvalue=contacts[name]['phone'])
        email = simpledialog.askstring("Email", "Enter new email address:", initialvalue=contacts[name]['email'])
        address = simpledialog.askstring("Address", "Enter new address:", initialvalue=contacts[name]['address'])

        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        save_contacts(contacts)
        update_contact_list()

# Delete a contact
def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if not selected_contact:
        messagebox.showwarning("Warning", "No contact selected.")
        return

    name = selected_contact.split(' - ')[0]
    if name in contacts:
        if messagebox.askyesno("Delete", f"Are you sure you want to delete contact '{name}'?"):
            del contacts[name]
            save_contacts(contacts)
            update_contact_list()

# Update the contact list display
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name, details in contacts.items():
        contact_list.insert(tk.END, f"{name} - {details['phone']}")

# Create GUI
root = tk.Tk()
root.title("Contact Manager")

frame = tk.Frame(root)
frame.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact)
add_button.grid(row=0, column=0, padx=5)

view_button = tk.Button(button_frame, text="View Contacts", command=view_contacts)
view_button.grid(row=0, column=1, padx=5)

search_button = tk.Button(button_frame, text="Search Contact", command=search_contact)
search_button.grid(row=0, column=2, padx=5)

update_button = tk.Button(button_frame, text="Update Contact", command=update_contact)
update_button.grid(row=0, column=3, padx=5)

delete_button = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=0, column=4, padx=5)

contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)

# Load existing contacts
contacts = load_contacts()
update_contact_list()

root.mainloop()
