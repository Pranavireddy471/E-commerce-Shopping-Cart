import tkinter as tk
from tkinter import messagebox

# Sample products (you can add more)
products = [
    {"name": "Laptop", "price": 70000},
    {"name": "Smartphone", "price": 30000},
    {"name": "Headphones", "price": 2000},
    {"name": "Smartwatch", "price": 4000},
    {"name": "USB Drive", "price": 600},
]

cart = []

# Add product to cart
def add_to_cart(product):
    cart.append(product)
    messagebox.showinfo("Added", f"{product['name']} added to cart!")

# Show cart window
def show_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("🛒 Shopping Cart")
    cart_window.geometry("400x400")
    cart_window.configure(bg="#f5f5f5")

    tk.Label(cart_window, text="Items in Cart", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)

    total = 0
    for item in cart:
        tk.Label(cart_window, text=f"{item['name']} - ₹{item['price']}", font=("Arial", 12), bg="#f5f5f5").pack()
        total += item["price"]

    tk.Label(cart_window, text=f"\nTotal: ₹{total}", font=("Arial", 14, "bold"), fg="green", bg="#f5f5f5").pack(pady=10)

    tk.Button(cart_window, text="Checkout", bg="#4caf50", fg="white", font=("Arial", 12), command=lambda: checkout(cart_window)).pack(pady=10)

# Checkout simulation
def checkout(window):
    if not cart:
        messagebox.showwarning("Empty", "Your cart is empty!")
        return
    messagebox.showinfo("Success", "Payment Processed Successfully!\nThank you for shopping 🛍️")
    cart.clear()
    window.destroy()

# Main GUI
root = tk.Tk()
root.title("🛍️ Python E-Commerce App")
root.geometry("500x500")
root.configure(bg="#e3f2fd")

title = tk.Label(root, text="Welcome to My Shop", font=("Arial", 20, "bold"), bg="#e3f2fd", fg="#0d47a1")
title.pack(pady=20)

product_frame = tk.Frame(root, bg="#e3f2fd")
product_frame.pack()

# Display products
for product in products:
    frame = tk.Frame(product_frame, bg="white", bd=2, relief="groove", padx=10, pady=10)
    frame.pack(pady=10, fill="x", padx=20)

    name = tk.Label(frame, text=product["name"], font=("Arial", 14, "bold"), bg="white")
    name.pack(anchor="w")

    price = tk.Label(frame, text=f"Price: ₹{product['price']}", font=("Arial", 12), bg="white")
    price.pack(anchor="w")

    add_btn = tk.Button(frame, text="Add to Cart", bg="#0d47a1", fg="white",
                        command=lambda p=product: add_to_cart(p))
    add_btn.pack(anchor="e", pady=5)

# View Cart Button
cart_btn = tk.Button(root, text="View Cart 🛒", font=("Arial", 14), bg="#ff9800", fg="white", command=show_cart)
cart_btn.pack(pady=20)

root.mainloop()
