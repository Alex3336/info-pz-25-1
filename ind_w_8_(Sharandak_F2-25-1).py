from _math_functions_check import (
    division_check,
    sqrt_check,
    log_check,
    cot_check,
)
from tkinter import *
from tkinter import messagebox
from math import e
import os
import urllib.request
import ctypes

font_url = "https://github.com/google/fonts/raw/main/ufl/ubuntu/Ubuntu-Regular.ttf"
font_filename = "Ubuntu-Regular.ttf"

root = Tk()
root.withdraw()

if not os.path.exists(font_filename):
    if messagebox.askyesno(
        "Завантаження шрифту",
        "Шрифт 'Ubuntu' не знайдено. Бажаєте завантажити його для кращого вигляду програми?",
    ):
        try:
            print("Завантаження шрифту Ubuntu...")
            urllib.request.urlretrieve(font_url, font_filename)
            print("Завантаження завершено.")
        except Exception as e:
            print(f"Помилка завантаження шрифту: {e}")
    else:
        print(
            "Користувач відмовився від завантаження. Використовується системний шрифт."
        )

if os.name == "nt" and os.path.exists(font_filename):
    ctypes.windll.gdi32.AddFontResourceExW(font_filename, 0x10, 0)
    myappid = "mycompany.myproduct.subproduct.version"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

root.deiconify()

font_family = "Ubuntu" if os.path.exists(font_filename) else "Arial"

BG_COLOR = "#1f262b"
ACCENT_COLOR = "#4a90e2"
BTN_COLOR = "#4C4281"
TEXT_COLOR = "#f4f4f4"
ERROR_COLOR = "#ff6b6b"
FONT_MAIN = (font_family, 10)
FONT_BOLD = (font_family, 10, "bold")

window_width = 510
window_height = 220

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.title("Виконання розрахунків")
root.iconbitmap(default="img/logo_2.ico")
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)
root.configure(bg=BG_COLOR)


input_data = LabelFrame(
    root,
    text="Вхідні дані:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)

input_data.place(x=10, y=15, width=240, height=165)

Labels = ["Укажіть варіант:", "Значення аргументу:"]
entries = []

for i in range(2):

    label = Label(
        input_data,
        text=Labels[i],
        bg=BG_COLOR,
        fg=TEXT_COLOR,
        font=FONT_MAIN,
    )

    entry = Entry(
        input_data,
        width=10,
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        relief=FLAT,
        font=FONT_MAIN,
        justify=CENTER,
    )

    label.grid(row=i, column=0, padx=(5, 3), pady=8, sticky=W)
    entry.grid(row=i, column=1, padx=3, pady=8)

    entries.append(entry)

calculate_button = Button(
    input_data,
    text="Обчислити",
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    font=FONT_BOLD,
    relief=FLAT,
    cursor="hand2",
    width=16,
)

calculate_button.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=8,
)


output_data = LabelFrame(
    root,
    text="Результати",
    bg=BG_COLOR,
    font=FONT_BOLD,
    fg=ACCENT_COLOR,
    relief=RIDGE,
)

output_data.place(x=260, y=15, width=240, height=165)
output_data.pack_propagate(False)

task_name = Label(
    output_data,
    text="Індивідуальне завдання №8",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
)

task_var = Label(
    output_data,
    text="Варіант ---",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
)

task_argument = Label(
    output_data,
    text="x = ---",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
)

task_condition = Label(
    output_data,
    text="Умова: ---",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
)

task_result = Label(
    output_data,
    text="f(x) = ---",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT_MAIN,
    anchor="w",
)

task_name.grid(row=0, column=0, padx=10, pady=(5, 0), sticky=W)
task_var.grid(row=1, column=0, padx=10, pady=2, sticky=W)
task_argument.grid(row=2, column=0, padx=10, pady=2, sticky=W)
task_condition.grid(row=3, column=0, padx=10, pady=2, sticky=W)
task_result.grid(row=4, column=0, padx=10, pady=2, sticky=W)


def calculate_all():
    try:
        x = float(entries[1].get())
        v = int(entries[0].get())

        def f():
            if x <= -3:
                condition = "x ≤ -3"
                denominator = sqrt_check(2 * v)
                numerator = log_check(10, v - x)
                return division_check(numerator, denominator), condition
            elif x > -3 and x < 0:
                condition = "-3 < x < 0"
                numerator = 5 * v
                denominator = (1 - x) ** 2
                return division_check(numerator, denominator), condition
            elif x >= 0 and x <= 3:
                condition = "0 ≤ x ≤ 3"
                return v * x**2 * cot_check(2 * x + v), condition
            elif x > 3:
                condition = "x > 3"
                return (x - v) * e ** -(division_check(v, x)), condition

        result, condition = f()

        task_var.config(text=f"Варіант №{v}")

        task_argument.config(
            text=f"x = {x:g}",
            fg=TEXT_COLOR,
        )

        task_condition.config(
            text=condition,
            fg=TEXT_COLOR,
        )

        task_result.config(
            text=f"f({x:g}) = {result:.3f}".rstrip("0").rstrip("."),
            fg=TEXT_COLOR,
        )

    except ValueError as error:
        messagebox.showerror(f"Помилка: {error}")
    except OverflowError:
        messagebox.showerror("Помилка", "Помилка переповнення числа!")
    except Exception as error:
        messagebox.showerror("Помилка", f"Невідома помилка: {error}")


calculate_button.config(command=calculate_all)

author = Label(
    root,
    text="\u00a9 Шарандак О.В, ПЗ-25-1",
    bg=BG_COLOR,
    font=(font_family, 8, "italic"),
    fg=ACCENT_COLOR,
)

author.place(x=10, y=190)

root.mainloop()
