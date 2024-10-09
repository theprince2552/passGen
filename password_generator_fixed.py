import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Title Label
        self.title_label = tk.Label(root, text="Password Generator", font=('Arial', 24))
        self.title_label.pack(pady=10)

        # Length Entry
        self.length_label = tk.Label(root, text="Enter password length:", font=('Arial', 14))
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root, font=('Arial', 14))
        self.length_entry.pack(pady=5)

        # Complexity Level
        self.complexity_label = tk.Label(root, text="Select complexity level:", font=('Arial', 14))
        self.complexity_label.pack(pady=5)

        self.complexity_var = tk.StringVar(value="Medium")
        self.complexity_options = ["Easy", "Medium", "Hard"]
        for option in self.complexity_options:
            tk.Radiobutton(root, text=option, variable=self.complexity_var, value=option, font=('Arial', 12)).pack(anchor=tk.W)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=('Arial', 14))
        self.generate_button.pack(pady=20)

        # Password Display
        self.password_label = tk.Label(root, text="", font=('Arial', 18), fg="blue")
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive.")

            # Determine character sets based on complexity
            if self.complexity_var.get() == "Easy":
                characters = string.ascii_lowercase  # Only lowercase letters
            elif self.complexity_var.get() == "Medium":
                characters = string.ascii_letters + string.digits  # Letters and digits
            else:  # Hard
                characters = string.ascii_letters + string.digits + string.punctuation  # All characters

            # Generate the password
            password = ''.join(random.choice(characters) for _ in range(length))

            # Display generated password
            self.password_label.config(text=password)
        except ValueError as e:
            self.password_label.config(text="Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
