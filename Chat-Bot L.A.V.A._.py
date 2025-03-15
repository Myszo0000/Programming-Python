import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import pyperclip

class ChatBot:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot - Python Script Generator")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', width=80, height=20)
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.user_input = tk.Entry(master, width=70)
        self.user_input.grid(row=1, column=0, padx=5, pady=5)

        self.send_button = tk.Button(master, text="Wyślij", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=5, pady=5)

        self.copy_button = tk.Button(master, text="Kopiuj skrypt", command=self.copy_script)
        self.copy_button.grid(row=2, column=0, padx=5, pady=5)

        self.save_button = tk.Button(master, text="Zapisz skrypt", command=self.save_script)
        self.save_button.grid(row=2, column=1, padx=5, pady=5)

        self.generated_script = ""

    def send_message(self):
        user_text = self.user_input.get()
        if user_text.strip() == "":
            messagebox.showwarning("Ostrzeżenie", "Proszę wpisać coś!")
            return

        self.display_message("Ty: " + user_text)
        self.user_input.delete(0, tk.END)

        response = self.generate_script(user_text)
        self.display_message("ChatBot: " + response)

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def generate_script(self, instruction):
        instruction = instruction.lower()
        if "hello" in instruction:
            self.generated_script = "print('Hello, World!')"
        elif "add" in instruction:
            self.generated_script = (
                "def add(a, b):\n"
                "    return a + b\n\n"
                "# Przykład użycia:\nprint(add(5, 3))"
            )
        elif "subtract" in instruction:
            self.generated_script = (
                "def subtract(a, b):\n"
                "    return a - b\n\n"
                "# Przykład użycia:\nprint(subtract(5, 3))"
            )
        elif "multiply" in instruction:
            self.generated_script = (
                "def multiply(a, b):\n"
                "    return a * b\n\n"
                "# Przykład użycia:\nprint(multiply(5, 3))"
            )
        elif "divide" in instruction:
            self.generated_script = (
                "def divide(a, b):\n"
                "    if b == 0:\n"
                "        return 'Nie można dzielić przez zero!'\n"
                "    return a / b\n\n"
                "# Przykład użycia:\nprint(divide(5, 0))"
            )
        elif "factorial" in instruction:
            self.generated_script = (
                "import math\n\n"
                "# Przykład użycia:\nprint(math.factorial(5))"
            )
        elif "loop" in instruction:
            self.generated_script = (
                "for i in range(5):\n"
                "    print(i)\n\n"
                "# Przykład użycia:\n# Wykonuje pętlę 5 razy."
            )
        elif "if" in instruction:
            self.generated_script = (
                "x = 10\n"
                "if x > 5:\n"
                "    print('x jest większe niż 5')\n"
                "else:\n"
                "    print('x jest mniejsze lub równe 5')"
            )
        elif "list" in instruction:
            self.generated_script = (
                "my_list = [1, 2, 3, 4, 5]\n"
                "for item in my_list:\n"
                "    print(item)\n\n"
                "# Przykład użycia:\n"
                "# Iteruje przez listę i drukuje każdy element."
            )
        else:
            self.generated_script = (
                "Przykro mi, nie rozumiem. Spróbuj 'hello', 'add', 'subtract', 'multiply', 'divide', 'factorial', 'loop', 'if' lub 'list'."
            )

        return self.generated_script

    def copy_script(self):
        if self.generated_script:
            pyperclip.copy(self.generated_script)
            messagebox.showinfo("Informacja", "Skrypt został skopiowany do schowka!")
        else:
            messagebox.showwarning("Ostrzeżenie", "Brak wygenerowanego skryptu do skopiowania.")

    def save_script(self):
        if self.generated_script:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".py",
                filetypes=[("Python files", "*.py"), ("All Files", "*.*")],
                title="Zapisz skrypt"
            )
            if file_path:
                try:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(self.generated_script)
                    messagebox.showinfo("Informacja", f"Skrypt zapisany w:\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Błąd", f"Wystąpił błąd podczas zapisywania pliku:\n{e}")
        else:
            messagebox.showwarning("Ostrzeżenie", "Brak wygenerowanego skryptu do zapisania.")

if __name__ == "__main__":
    root = tk.Tk()
    chat_bot = ChatBot(root)
    root.mainloop()
      
