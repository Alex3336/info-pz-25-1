from _math_functions_check import (
    division_check,
    sqrt_check,
    power_check,
    tan_check,
)
from tkinter import *
from tkinter import messagebox
from math import *
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

window_width = 500
window_height = 430

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.title("Виконання розрахунків")
root.iconbitmap(default="img/logo.ico")
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

input_data = LabelFrame(
    root, text="Вхідні дані", bg=BG_COLOR, font=FONT_BOLD, fg=ACCENT_COLOR
)

label_1 = Label(
    input_data,
    text="g",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
label_2 = Label(
    input_data,
    text="h",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
label_3 = Label(
    input_data,
    text="u",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
label_4 = Label(
    input_data,
    text="v",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)

entry_1 = Entry(
    input_data,
    width=6,
    font=FONT_MAIN,
    relief=FLAT,
    highlightthickness=2,
    highlightbackground=ACCENT_COLOR,
    highlightcolor=ACCENT_COLOR,
    borderwidth=0,
    background=ACCENT_COLOR,
    fg=TEXT_COLOR,
)
entry_2 = Entry(
    input_data,
    width=6,
    font=FONT_MAIN,
    relief=FLAT,
    highlightthickness=2,
    highlightbackground=ACCENT_COLOR,
    highlightcolor=ACCENT_COLOR,
    borderwidth=0,
    background=ACCENT_COLOR,
    fg=TEXT_COLOR,
)
entry_3 = Entry(
    input_data,
    width=6,
    font=FONT_MAIN,
    relief=FLAT,
    highlightthickness=2,
    highlightbackground=ACCENT_COLOR,
    highlightcolor=ACCENT_COLOR,
    borderwidth=0,
    background=ACCENT_COLOR,
    fg=TEXT_COLOR,
)
entry_4 = Entry(
    input_data,
    width=6,
    font=FONT_MAIN,
    relief=FLAT,
    highlightthickness=2,
    highlightbackground=ACCENT_COLOR,
    highlightcolor=ACCENT_COLOR,
    borderwidth=0,
    background=ACCENT_COLOR,
    fg=TEXT_COLOR,
)

input_data.pack(padx=10, pady=20, fill=BOTH)

input_data.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

label_1.grid(row=0, column=0, pady=20, sticky=E)
entry_1.grid(row=0, column=1, pady=20, sticky=W, padx=(2, 10))
label_2.grid(row=0, column=2, pady=20, sticky=E)
entry_2.grid(row=0, column=3, pady=20, sticky=W, padx=(2, 10))
label_3.grid(row=0, column=4, pady=20, sticky=E)
entry_3.grid(row=0, column=5, pady=20, sticky=W, padx=(2, 10))
label_4.grid(row=0, column=6, pady=20, sticky=E)
entry_4.grid(row=0, column=7, pady=20, sticky=W, padx=(2, 10))

button_calculate = Button(
    root,
    text="Обчислити",
    width=20,
    bg=BTN_COLOR,
    fg="white",
    font=FONT_BOLD,
    cursor="hand2",
    relief=FLAT,
)

button_calculate.pack(pady=15)

output_data = LabelFrame(
    root, text="Вихідні дані", bg=BG_COLOR, font=FONT_BOLD, fg=ACCENT_COLOR
)

result_1 = Label(
    output_data,
    text="Result_1 = ",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
result_2 = Label(
    output_data,
    text="Result_2 = ",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
result_3 = Label(
    output_data,
    text="Result_3 = ",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
result_4 = Label(
    output_data,
    text="Result_4 = ",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
result_5 = Label(
    output_data,
    text="Result_5 = ",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
max_result = Label(
    output_data,
    text="Максимальне значення: Max = ",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)
min_result = Label(
    output_data,
    text="Мінімальне значення: Min = ",
    bg=BG_COLOR,
    font=FONT_MAIN,
    fg=TEXT_COLOR,
)

output_data.pack(padx=10, pady=15, fill=BOTH)

result_1.grid(row=0, column=0, sticky=W, padx=10)
result_2.grid(row=1, column=0, sticky=W, padx=10)
result_3.grid(row=2, column=0, sticky=W, padx=10)
result_4.grid(row=3, column=0, sticky=W, padx=10)
result_5.grid(row=4, column=0, sticky=W, padx=10)
max_result.grid(row=5, column=0, sticky=W, padx=10)
min_result.grid(row=6, column=0, sticky=W, padx=10)


def calculate_all(event=None):
    try:
        g = float(entry_1.get())
        h = float(entry_2.get())
        u = float(entry_3.get())
        v = float(entry_4.get())

        def calculate_result_1():
            minuend_first_frac = h / sqrt(7)
            minuend_second_frac = division_check(sqrt(5), g + h)
            minuend_exponent = (2 * g) / (3 * h + 5)
            minuend = power_check(
                minuend_first_frac + minuend_second_frac, minuend_exponent
            )

            substrahend_numerator = sqrt_check(sqrt(3) + abs(g + h) + g * h)
            substrahend_denominator = g**2 - 4 * h + (g - h) ** 2
            substrahend = division_check(substrahend_numerator, substrahend_denominator)

            return minuend - substrahend

        def calculate_result_2():
            numerator = sin(9 * pi + u) + tan_check(5 * pi + sqrt_check(v))
            radicand = abs(sin(7 * pi + v**2) + cos(3 * pi + u**2))
            denominator = sqrt_check(radicand)

            return division_check(numerator, denominator)

        def calculate_result_3():
            cos_minuend = division_check(pi, u**2)
            cos_substrahend = division_check(sqrt(3), 2 * v)
            minuend = cos(cos_minuend - cos_substrahend) ** 2

            substrahend_numerator = cos(sqrt(3) * pi - u**2 + v**2) ** 2
            substrahend_denominator = 2 * sqrt(3) - 3 * v
            substrahend = sqrt_check(
                division_check(substrahend_numerator, substrahend_denominator)
            )

            return minuend - substrahend

        def calculate_result_4():
            numerator = cos(sqrt(2) * pi - g) - power_check(g, h)
            denominator = sqrt_check(power_check(h, 2 * g) + 5 * g * h)
            minuend = division_check(numerator, denominator)

            substrahend = power_check(g, h) * tan_check(pi / sqrt(5) + g**2 * h**2) ** 2

            return minuend - substrahend

        def calculate_result_5():
            augend_numerator = (
                sin(3 * pi - sqrt_check(abs(division_check(g * u, 2 * v)))) ** 2
            )
            augend_denominator = cos(5**g - division_check(pi, 2 * u * v)) ** 3
            augend = division_check(augend_numerator, augend_denominator)

            addend_numerator = (
                cos(sqrt_check(division_check(g, h) - sqrt(5) * pi / 3)) ** 3
            )
            addend_denominator = (
                sin(3 * pi / sqrt(5) - sqrt_check(division_check(u, v))) ** 2
            )
            addend = division_check(addend_numerator, addend_denominator)

            return augend + addend

        numeric_results = []

        def safe_run(func, label, name):
            try:
                val = func()
                label.config(text=f"{name} = {val:.3f}", fg=TEXT_COLOR)
                numeric_results.append(val)
                return val
            except Exception as e:
                label.config(text=f"{name}: {e}", fg=ERROR_COLOR)
                return None

        for i in range(1, 6):
            func = locals()[f"calculate_result_{i}"]
            label = globals()[f"result_{i}"]
            safe_run(func, label, f"Result_{i}")

        if numeric_results:
            max_val = max(numeric_results)
            min_val = min(numeric_results)
            max_result.config(
                text=f"Максимальне значення: Max = {max_val:.3f}", fg=TEXT_COLOR
            )
            min_result.config(
                text=f"Мінімальне значення: Min = {min_val:.3f}", fg=TEXT_COLOR
            )
        else:
            max_result.config(text="Max = Неможливо обчислити", fg=ERROR_COLOR)
            min_result.config(text="Min = Неможливо обчислити", fg=ERROR_COLOR)

    except ValueError:
        messagebox.showerror(
            "Помилка вводу",
            "Будь ласка, введіть числові значення у всі поля (g, h, u, v).",
        )
    except ValueError as error:
        messagebox.showerror("Помилка значення", str(error))
    except OverflowError:
        messagebox.showerror("Помилка", "Помилка переповнення числа!")
    except Exception as error:
        messagebox.showerror("Помилка", f"Невідома помилка: {error}")


button_calculate.bind("<Button-1>", calculate_all)

author = Label(
    root,
    text="\u00a9 Шарандак О.В, ПЗ-25-1",
    bg=BG_COLOR,
    font=(font_family, 8, "italic"),
    fg="#888888",
)
author.pack(side=BOTTOM, padx=10, pady=10)

root.mainloop()
