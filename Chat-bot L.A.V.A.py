import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog, Menu, ttk
import pyperclip
import re
import io
import contextlib
import datetime
import atexit
import os

# -------------------------------
# Definicja komend
# -------------------------------
def cmd_hello():
    return "print('Hello, World!')"

def cmd_add():
    return (
        "def add(a, b):\n"
        "    return a + b\n\n"
        "# Przykład użycia:\nprint(add(5, 3))"
    )

def cmd_subtract():
    return (
        "def subtract(a, b):\n"
        "    return a - b\n\n"
        "# Przykład użycia:\nprint(subtract(5, 3))"
    )

def cmd_multiply():
    return (
        "def multiply(a, b):\n"
        "    return a * b\n\n"
        "# Przykład użycia:\nprint(multiply(5, 3))"
    )

def cmd_divide():
    return (
        "def divide(a, b):\n"
        "    if b == 0:\n"
        "        return 'Nie można dzielić przez zero!'\n"
        "    return a / b\n\n"
        "# Przykład użycia:\nprint(divide(5, 0))"
    )

def cmd_factorial():
    return (
        "import math\n\n"
        "# Przykład użycia:\nprint(math.factorial(5))"
    )

def cmd_loop():
    return (
        "for i in range(5):\n"
        "    print(i)\n\n"
        "# Przykład użycia:\n# Pętla wykonuje się 5 razy."
    )

def cmd_while():
    return (
        "i = 0\n"
        "while i < 5:\n"
        "    print(i)\n"
        "    i += 1\n\n"
        "# Przykład użycia:\n# Pętla while wykonuje się dopóki warunek jest prawdziwy."
    )

def cmd_if():
    return (
        "x = 10\n"
        "if x > 5:\n"
        "    print('x jest większe niż 5')\n"
        "else:\n"
        "    print('x jest mniejsze lub równe 5')"
    )

def cmd_list():
    return (
        "my_list = [1, 2, 3, 4, 5]\n"
        "for item in my_list:\n"
        "    print(item)\n\n"
        "# Przykład użycia:\n# Iteracja przez elementy listy."
    )

def cmd_fibonacci():
    return (
        "def fibonacci(n):\n"
        "    a, b = 0, 1\n"
        "    sequence = []\n"
        "    while len(sequence) < n:\n"
        "        sequence.append(a)\n"
        "        a, b = b, a + b\n"
        "    return sequence\n\n"
        "# Przykład użycia:\nprint(fibonacci(10))  # Pierwsze 10 elementów ciągu"
    )

def cmd_reverse():
    return (
        "def reverse_string(s):\n"
        "    return s[::-1]\n\n"
        "# Przykład użycia:\nprint(reverse_string('Hello'))  # Odwrócony ciąg znaków"
    )

def cmd_sort():
    return (
        "def sort_list(lst):\n"
        "    return sorted(lst)\n\n"
        "# Przykład użycia:\nprint(sort_list([3, 1, 4, 2]))  # Posortowana lista"
    )

def cmd_regex():
    return (
        "import re\n\n"
        "def find_emails(text):\n"
        "    pattern = r'[\\w\\.-]+@[\\w\\.-]+'\n"
        "    return re.findall(pattern, text)\n\n"
        "# Przykład użycia:\nsample_text = 'Kontakt: test@example.com, info@domain.org'\n"
        "print(find_emails(sample_text))"
    )

def cmd_class():
    return (
        "class Person:\n"
        "    def __init__(self, name, age):\n"
        "        self.name = name\n"
        "        self.age = age\n\n"
        "    def greet(self):\n"
        "        print(f'Hello, my name is {self.name} and I am {self.age} years old.')\n\n"
        "# Przykład użycia:\np = Person('Alice', 30)\np.greet()"
    )

def cmd_decorator():
    return (
        "def my_decorator(func):\n"
        "    def wrapper(*args, **kwargs):\n"
        "        print('Przed wykonaniem')\n"
        "        result = func(*args, **kwargs)\n"
        "        print('Po wykonaniu')\n"
        "        return result\n"
        "    return wrapper\n\n"
        "@my_decorator\n"
        "def say_hello(name):\n"
        "    print(f'Hello, {name}!')\n\n"
        "# Przykład użycia:\nsay_hello('Bob')"
    )

def cmd_generator():
    return (
        "def my_generator(n):\n"
        "    for i in range(n):\n"
        "        yield i * i\n\n"
        "# Przykład użycia:\nfor value in my_generator(5):\n"
        "    print(value)"
    )

def cmd_context_manager():
    return (
        "class MyContext:\n"
        "    def __enter__(self):\n"
        "        print('Wejście do kontekstu')\n"
        "        return self\n\n"
        "    def __exit__(self, exc_type, exc_val, exc_tb):\n"
        "        print('Wyjście z kontekstu')\n\n"
        "# Przykład użycia:\nwith MyContext() as mc:\n"
        "    print('Wewnątrz kontekstu')"
    )

def cmd_try_except():
    return (
        "try:\n"
        "    x = int(input('Podaj liczbę: '))\n"
        "    print('Liczba to:', x)\n"
        "except ValueError:\n"
        "    print('To nie jest prawidłowa liczba!')"
    )

def cmd_comment():
    return (
        "# To jest przykładowy komentarz\n"
        "# Poniżej przykładowa funkcja z komentarzem\n"
        "def greet(name):\n"
        "    # Funkcja wypisuje powitanie\n"
        "    print(f'Hello, {name}!')\n\n"
        "# Przykład użycia:\ngreet('World')"
    )

# Nowe komendy:
def cmd_dictionary():
    return (
        "person = {\n"
        "    'name': 'Alice',\n"
        "    'age': 30,\n"
        "    'city': 'Warsaw'\n"
        "}\n\n"
        "for key, value in person.items():\n"
        "    print(f'{key}: {value}')\n\n"
        "# Przykład użycia:\n# Słownik reprezentuje osobę."
    )

def cmd_list_comprehension():
    return (
        "numbers = [1, 2, 3, 4, 5]\n"
        "squared = [x*x for x in numbers]\n\n"
        "print('Lista kwadratów:', squared)\n\n"
        "# Przykład użycia:\n# List comprehension pozwala na zwięzłe generowanie list."
    )

# Słownik komend
COMMANDS = {
    'hello': cmd_hello,
    'add': cmd_add,
    'subtract': cmd_subtract,
    'multiply': cmd_multiply,
    'divide': cmd_divide,
    'factorial': cmd_factorial,
    'loop': cmd_loop,
    'while': cmd_while,
    'if': cmd_if,
    'list': cmd_list,
    'fibonacci': cmd_fibonacci,
    'reverse': cmd_reverse,
    'sort': cmd_sort,
    'regex': cmd_regex,
    'class': cmd_class,
    'decorator': cmd_decorator,
    'generator': cmd_generator,
    'context manager': cmd_context_manager,
    'try except': cmd_try_except,
    'comment': cmd_comment,
    'dictionary': cmd_dictionary,
    'list comprehension': cmd_list_comprehension
}


# -------------------------------
# Klasa ChatBot
# -------------------------------
class ChatBot:
    def __init__(self, master):
        self.master = master
        master.title("ChatBot - Python Script Generator")
        master.geometry("1100x800")
        master.minsize(800, 600)

        # Pasek menu
        self.menu = Menu(master)
        master.config(menu=self.menu)
        
        file_menu = Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Nowy", command=self.clear_all)
        file_menu.add_command(label="Eksportuj rozmowę (HTML)", command=self.export_history_as_html)
        file_menu.add_command(label="Eksportuj rozmowę (TXT)", command=self.export_history_as_txt)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjdź", command=self.exit_app)
        self.menu.add_cascade(label="Plik", menu=file_menu)

        help_menu = Menu(self.menu, tearoff=0)
        help_menu.add_command(label="Dostępne komendy", command=self.show_help)
        self.menu.add_cascade(label="Pomoc", menu=help_menu)
        
        history_menu = Menu(self.menu, tearoff=0)
        history_menu.add_command(label="Wyczyść historię", command=self.clear_history)
        self.menu.add_cascade(label="Historia", menu=history_menu)

        # Lista historii komunikatów
        self.history = []

        # Główne panele
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Pasek statusu
        self.status_var = tk.StringVar()
        self.status_var.set("Gotowy")
        self.status_bar = ttk.Label(master, textvariable=self.status_var, relief=tk.SUNKEN, anchor='w')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Obszar czatu
        self.chat_frame = tk.Frame(self.main_frame)
        self.chat_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.chat_area = scrolledtext.ScrolledText(self.chat_frame, state='disabled', width=100, height=15)
        self.chat_area.pack(fill=tk.BOTH, expand=True)

        # Panel wejścia
        self.input_frame = tk.Frame(self.main_frame)
        self.input_frame.pack(fill=tk.X, pady=5)
        self.user_input = tk.Entry(self.input_frame, width=80)
        self.user_input.pack(side=tk.LEFT, padx=(0,5), expand=True, fill=tk.X)
        self.send_button = tk.Button(self.input_frame, text="Wyślij", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        # Panel przycisków akcji
        self.action_frame = tk.Frame(self.main_frame)
        self.action_frame.pack(fill=tk.X, pady=5)
        self.copy_button = tk.Button(self.action_frame, text="Kopiuj skrypt", command=self.copy_script)
        self.copy_button.pack(side=tk.LEFT, padx=(0,5))
        self.save_button = tk.Button(self.action_frame, text="Zapisz skrypt", command=self.save_script)
        self.save_button.pack(side=tk.LEFT, padx=(0,5))
        self.run_button = tk.Button(self.action_frame, text="Uruchom skrypt", command=self.run_script)
        self.run_button.pack(side=tk.LEFT, padx=(0,5))
        self.clear_script_button = tk.Button(self.action_frame, text="Wyczyść panel skryptu", command=self.clear_script_area)
        self.clear_script_button.pack(side=tk.LEFT, padx=(0,5))
        self.history_button = tk.Button(self.action_frame, text="Pokaż historię", command=self.show_history)
        self.history_button.pack(side=tk.LEFT, padx=(0,5))

        # Panel wyświetlający wygenerowany skrypt
        self.script_frame = tk.LabelFrame(self.main_frame, text="Wygenerowany skrypt")
        self.script_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.script_area = scrolledtext.ScrolledText(self.script_frame, state='normal', width=100, height=15)
        self.script_area.pack(fill=tk.BOTH, expand=True)

        self.generated_script = ""

        # Rejestracja zapisu historii przy zamykaniu aplikacji
        atexit.register(self.save_history_to_file)

    def clear_all(self):
        """Czyści obszar chatu, panel skryptu oraz historię."""
        self.chat_area.config(state='normal')
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state='disabled')
        self.script_area.delete(1.0, tk.END)
        self.generated_script = ""
        self.history.clear()
        self.status_var.set("Wszystko wyczyszczone.")

    def clear_script_area(self):
        self.script_area.delete(1.0, tk.END)
        self.generated_script = ""
        self.status_var.set("Panel skryptu wyczyszczony.")

    def clear_history(self):
        self.history.clear()
        messagebox.showinfo("Informacja", "Historia została wyczyszczona.")
        self.status_var.set("Historia wyczyszczona.")

    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Historia komunikatów")
        history_area = scrolledtext.ScrolledText(history_window, state='normal', width=100, height=30)
        history_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        if not self.history:
            history_area.insert(tk.END, "Brak historii.\n")
        else:
            for entry in self.history:
                history_area.insert(tk.END, entry + "\n")
        history_area.config(state='disabled')
        self.status_var.set("Wyświetlono historię.")

    def export_history_as_html(self):
        if not self.history:
            messagebox.showwarning("Ostrzeżenie", "Brak historii do eksportu.")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML files", "*.html"), ("All Files", "*.*")],
            title="Zapisz historię rozmowy jako HTML"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("<html><head><meta charset='UTF-8'><title>Historia rozmowy</title></head><body>")
                    f.write("<h1>Historia rozmowy</h1><ul>")
                    for entry in self.history:
                        f.write(f"<li>{entry}</li>")
                    f.write("</ul></body></html>")
                messagebox.showinfo("Informacja", f"Historia rozmowy została zapisana w:\n{file_path}")
                self.status_var.set("Eksport HTML zakończony powodzeniem.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Wystąpił błąd podczas zapisywania historii:\n{e}")
                self.status_var.set("Błąd eksportu HTML.")

    def export_history_as_txt(self):
        if not self.history:
            messagebox.showwarning("Ostrzeżenie", "Brak historii do eksportu.")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All Files", "*.*")],
            title="Zapisz historię rozmowy jako TXT"
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    for entry in self.history:
                        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                        f.write(f"{timestamp} {entry}\n")
                messagebox.showinfo("Informacja", f"Historia rozmowy została zapisana w:\n{file_path}")
                self.status_var.set("Eksport TXT zakończony powodzeniem.")
            except Exception as e:
                messagebox.showerror("Błąd", f"Wystąpił błąd podczas zapisywania historii:\n{e}")
                self.status_var.set("Błąd eksportu TXT.")

    def show_help(self):
        help_text = (
            "Dostępne komendy do generowania skryptów:\n\n" +
            "\n".join([f"- {cmd}" for cmd in COMMANDS.keys()]) +
            "\n\nPrzykład: wpisz 'proszę dodać funkcję add' lub 'pokaż przykład pętli'"
        )
        messagebox.showinfo("Dostępne komendy", help_text)
        self.status_var.set("Wyświetlono pomoc.")

    def exit_app(self):
        self.save_history_to_file()
        self.master.quit()

    def save_history_to_file(self):
        if self.history:
            filename = f"chat_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    for line in self.history:
                        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                        f.write(f"{timestamp} {line}\n")
                print(f"Historia została zapisana do pliku: {filename}")
                self.status_var.set(f"Historia zapisana do pliku: {filename}")
            except Exception as e:
                print("Błąd podczas zapisywania historii:", e)
                self.status_var.set("Błąd zapisywania historii.")

    def send_message(self):
        user_text = self.user_input.get().strip()
        if user_text == "":
            messagebox.showwarning("Ostrzeżenie", "Proszę wpisać coś!")
            return

        self.display_message("Ty: " + user_text)
        self.history.append("Ty: " + user_text)
        self.user_input.delete(0, tk.END)

        response = self.generate_script(user_text)
        self.display_message("ChatBot: " + response)
        self.history.append("ChatBot: " + response)
        # Aktualizacja panelu wygenerowanego skryptu
        self.script_area.delete(1.0, tk.END)
        self.script_area.insert(tk.END, self.generated_script)
        self.status_var.set("Wygenerowano skrypt.")

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def generate_script(self, instruction):
        lower_instruction = instruction.lower()
        found = False
        for cmd in COMMANDS:
            if cmd in lower_instruction:
                self.generated_script = COMMANDS[cmd]()
                found = True
                break
        if not found:
            # Lista dostępnych poleceń
            available = "', '".join(COMMANDS.keys())
            self.generated_script = (
                "Przykro mi, nie rozumiem. Spróbuj użyć jednej z następujących komend:\n"
                f"'{available}'"
            )
        return self.generated_script

    def copy_script(self):
        if self.generated_script:
            pyperclip.copy(self.generated_script)
            messagebox.showinfo("Informacja", "Skrypt został skopiowany do schowka!")
            self.status_var.set("Skrypt skopiowany.")
        else:
            messagebox.showwarning("Ostrzeżenie", "Brak wygenerowanego skryptu do skopiowania.")
            self.status_var.set("Brak skryptu do kopiowania.")

    def save_script(self):
        if self.generated_script:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".py",
                filetypes=[("Python files", "*.py"), ("All Files", "*.*")],
                title="Zapisz skrypt"
            )
            if file_path:
                try:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(self.generated_script)
                    messagebox.showinfo("Informacja", f"Skrypt zapisany w:\n{file_path}")
                    self.status_var.set("Skrypt zapisany.")
                except Exception as e:
                    messagebox.showerror("Błąd", f"Wystąpił błąd podczas zapisywania pliku:\n{e}")
                    self.status_var.set("Błąd przy zapisie skryptu.")
        else:
            messagebox.showwarning("Ostrzeżenie", "Brak wygenerowanego skryptu do zapisania.")
            self.status_var.set("Brak skryptu do zapisu.")

    def run_script(self):
        if not self.generated_script:
            messagebox.showwarning("Ostrzeżenie", "Brak wygenerowanego skryptu do uruchomienia.")
            self.status_var.set("Brak skryptu do uruchomienia.")
            return

        output_window = tk.Toplevel(self.master)
        output_window.title("Wynik wykonania skryptu")
        output_text = scrolledtext.ScrolledText(output_window, state='normal', width=100, height=20)
        output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        stdout_capture = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout_capture):
                exec(self.generated_script, {})
        except Exception as e:
            error_message = f"Błąd podczas wykonywania skryptu:\n{e}\n"
            output_text.insert(tk.END, error_message)
            self.status_var.set("Błąd wykonania skryptu.")
        else:
            output_value = stdout_capture.getvalue()
            output_text.insert(tk.END, output_value)
            self.status_var.set("Skrypt wykonany poprawnie.")
        finally:
            stdout_capture.close()

# -------------------------------
# Główna pętla programu
# -------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    chat_bot = ChatBot(root)
    root.mainloop()
