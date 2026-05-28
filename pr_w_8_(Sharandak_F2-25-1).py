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

window_width = 560
window_height = 360

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
    root,
    text="Вхідні дані:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)

input_data.place(x=10, y=20, width=180, height=260)

labels = ["a", "b", "c", "d"]
entries = []

for i in range(4):

    label = Label(
        input_data,
        text=labels[i],
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

    label.grid(row=i, column=0, padx=(15, 5), pady=12, sticky=E)
    entry.grid(row=i, column=1, padx=5, pady=12)

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
    row=5,
    column=0,
    columnspan=2,
    pady=10,
    padx=10,
)


output_data = LabelFrame(
    root,
    text="Результати",
    bg=BG_COLOR,
    font=FONT_BOLD,
    fg=ACCENT_COLOR,
    relief=RIDGE,
)

output_data.place(x=200, y=20, width=350, height=320)
output_data.pack_propagate(False)

result_values = []

for i in range(10):
    result_label = Label(
        output_data,
        text=f"Result_{i + 1}:",
        bg=BG_COLOR,
        font=FONT_MAIN,
        fg=TEXT_COLOR,
        anchor="w",
    )

    result_value = Label(
        output_data,
        text="---",
        bg=BG_COLOR,
        font=FONT_MAIN,
        fg=ACCENT_COLOR,
        width=15,
        anchor="w",
    )

    result_label.grid(row=i, column=0, padx=10, pady=3, sticky=W)
    result_value.grid(row=i, column=1, pady=3, sticky=W)

    result_values.append(result_value)


def calculate_all(event=None):
    try:
        a = float(entries[0].get())
        b = float(entries[1].get())
        c = float(entries[2].get())
        d = float(entries[3].get())

        def result_1():
            return power_check(b - a * c, d)

        def result_2():
            return 2 * (b - a) - c / sin(pi / 2)

        def result_3():
            return a * pi + c * b - 2 * d

        def result_4():
            return (a + c) * (b - d)

        def result_5():
            return power_check(a + b, a - b)

        def result_6():
            return sqrt_check((a - b) ** 2 + (c * d) ** 2)

        def result_7():
            return 3 * sqrt_check((2 * a - 4 * b + c / 3 - d / 2) ** 2 - a * b * c / 4)

        def result_8():
            return (5 * a + 3 * b) / (2 * pi) - (a * c + b * d) / 3**c

        def result_9():
            return sqrt_check(7**a + 4**b + 3**c + 5**d)

        def result_10():
            return 3 * cos(pi) - 2 / pi + 2 * sin(pi / 2)

        numeric_results = []

        def safe_run(func, label):
            try:
                val = func()
                label.config(text=f"{val:.3f}".rstrip("0").rstrip("."), fg=TEXT_COLOR)
                numeric_results.append(val)
                return val
            except Exception as e:
                label.config(text=f"{e}", fg=ERROR_COLOR)
                return None

        for i in range(1, 11):
            func = locals()[f"result_{i}"]
            label = result_values[i - 1]
            safe_run(func, label)

    except ValueError:
        messagebox.showerror("Помилка вводу", "Будь ласка, введіть числові значення у всі поля (g, h, u, v).")
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

author.place(x=25, y=320)

root.mainloop()
