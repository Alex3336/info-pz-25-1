from tkinter import messagebox, ttk
from calendar import monthrange
from datetime import date
from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import openpyxl
from openpyxl.styles import Alignment
import ctypes
import os

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
FONT_SMALL = (font_family, 8)

MONTHS = [
    "січень",
    "лютий",
    "березень",
    "квітень",
    "травень",
    "червень",
    "липень",
    "серпень",
    "вересень",
    "жовтень",
    "листопад",
    "грудень",
]


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year

    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    return age


def get_birth_date():
    day = int(day_combo.get())
    month = get_selected_month()
    year = int(year_combo.get())
    return date(year, month, day)


def get_selected_month():
    return MONTHS.index(month_combo.get()) + 1


def update_day_combo(event=None):
    if not month_combo.get() or not year_combo.get():
        return

    selected_day = day_combo.get()
    year = int(year_combo.get())
    month = get_selected_month()
    days_count = monthrange(year, month)[1]
    day_values = [str(day) for day in range(1, days_count + 1)]

    day_combo.config(values=day_values)

    if selected_day and int(selected_day) <= days_count:
        day_combo.set(selected_day)
    else:
        day_combo.set(str(days_count))


def reset_date_combos():
    today = date.today()
    month_combo.current(today.month - 1)
    year_combo.set(str(today.year))
    update_day_combo()
    days_count = monthrange(int(year_combo.get()), get_selected_month())[1]
    day_combo.current(min(today.day, days_count) - 1)


def capitalize_entry(entry):
    value = entry.get().strip()

    if value:
        value = value[0].upper() + value[1:]
        entry.delete(0, END)
        entry.insert(0, value)

    return value


def focus_next_entry(current, next_widget, capitalize=False):
    if capitalize and isinstance(current, Entry):
        capitalize_entry(current)
    next_widget.focus_set()
    if hasattr(next_widget, "icursor"):
        next_widget.icursor(END)
    return "break"


def clear_form():
    surname_entry.delete(0, END)
    name_entry.delete(0, END)
    patronymic_entry.delete(0, END)
    reset_date_combos()
    speciality_combo.set("Оберіть...")
    admission_combo.set("Оберіть...")
    parallel_combo.set("Оберіть...")
    surname_entry.focus_set()


def process_data():
    surname = capitalize_entry(surname_entry)
    name = capitalize_entry(name_entry)
    patronymic = capitalize_entry(patronymic_entry)

    spec = speciality_combo.get()
    adm = admission_combo.get()
    group_num = parallel_combo.get()

    if any(v == "Оберіть..." for v in (spec, adm, group_num)) or not all(
        [surname, name, patronymic]
    ):
        messagebox.showwarning(
            "Увага", "Будь ласка, заповніть всі поля ПІБ та оберіть параметри групи!"
        )
        return

    try:
        birthday = get_birth_date()
        age = calculate_age(birthday)
    except ValueError:
        messagebox.showerror("Помилка", "Вибрана дата не є коректною!")
        return

    status = "Повнолітній" if age >= 18 else "Неповнолітній"

    record = {
        "Прізвище": surname,
        "Ім'я": name,
        "По батькові": patronymic,
        "Спеціальність": spec,
        "Рік вступу": adm,
        "Група": group_num,
        "Дата народження": birthday.strftime("%d.%m.%Y"),
        "Вік": age,
        "Статус": status,
        "Телефон": phone_entry.get().strip(),
        "Email": email_entry.get().strip(),
    }

    filename = "students_data.xlsx"

    try:
        if os.path.exists(filename):
            workbook = openpyxl.load_workbook(filename)
            students_sheet = workbook.active
        else:
            workbook = openpyxl.Workbook()
            students_sheet = workbook.active
            students_sheet.append(list(record.keys()))

        students_sheet.append(list(record.values()))

        for col in students_sheet.columns:
            max_length = 0
            column_letter = col[0].column_letter
            for cell in col:
                cell.alignment = Alignment(horizontal='left')
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            students_sheet.column_dimensions[column_letter].width = max_length + 2

        workbook.save(filename)

        messagebox.showinfo(
            "Успіх", f"Дані збережено до {filename}!\nСтатус: {status} ({age} р.)"
        )
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося зберегти файл: {e}")


def open_excel_file():
    filename = "students_data.xlsx"
    if os.path.exists(filename):
        try:
            os.startfile(filename)
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося відкрити файл: {e}")
    else:
        messagebox.showwarning("Увага", "Файл із даними ще не створено!")


root.title("Реєстратор студентів")
center_window(root, 990, 400)
root.resizable(False, False)
root.configure(bg=BG_COLOR)

icon_path = os.path.join("img", "logo_3.ico")
if os.path.exists(icon_path):
    root.iconbitmap(default=icon_path)

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TCombobox",
    fieldbackground=ACCENT_COLOR,
    background=ACCENT_COLOR,
    foreground=TEXT_COLOR,
    arrowcolor=TEXT_COLOR,
    bordercolor=ACCENT_COLOR,
    lightcolor=ACCENT_COLOR,
    darkcolor=ACCENT_COLOR,
    focuscolor=ACCENT_COLOR,
    borderwidth=0,
    relief=FLAT,
    padding=1,
)
style.map(
    "TCombobox",
    fieldbackground=[("readonly", ACCENT_COLOR)],
    bordercolor=[("focus", ACCENT_COLOR), ("readonly", ACCENT_COLOR)],
    lightcolor=[("focus", ACCENT_COLOR), ("readonly", ACCENT_COLOR)],
    darkcolor=[("focus", ACCENT_COLOR), ("readonly", ACCENT_COLOR)],
)

canvas_logo = Canvas(root, width=309, height=309, highlightthickness=0, bg=BG_COLOR)
canvas_logo.place(x=15, y=25)

emblem_path = "img/emblem.png"
if os.path.exists(emblem_path):
    emblem_image = Image.open(emblem_path)
    emblem_image = emblem_image.resize((309, 309), Image.Resampling.LANCZOS)
    emblem = ImageTk.PhotoImage(emblem_image)
    img_1 = canvas_logo.create_image(0, 0, anchor=NW, image=emblem)
else:
    canvas_logo.create_text(150, 150, text="Зображення\nне знайдено", fill=TEXT_COLOR)

person_frame = LabelFrame(
    root,
    text="Вкажіть прізвище ім'я по батькові:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
person_frame.place(x=340, y=16, width=310, height=150)
for i in range(3):
    person_frame.grid_rowconfigure(i, weight=1)

person_labels = ("прізвище", "ім'я", "по батькові")
person_entries = []

for row, text in enumerate(person_labels):
    label = Label(person_frame, text=text, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN)
    label.grid(row=row, column=0, padx=(16, 8), pady=8, sticky=W)

    entry = Entry(
        person_frame,
        width=20,
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief=FLAT,
        font=FONT_MAIN,
    )
    entry.grid(row=row, column=1, padx=8, pady=8, sticky=W)
    person_entries.append(entry)

surname_entry, name_entry, patronymic_entry = person_entries

group_frame = LabelFrame(
    root,
    text="Вкажіть номер групи:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
group_frame.place(x=665, y=16, width=310, height=150)
for i in range(3):
    group_frame.grid_rowconfigure(i, weight=1)


today = date.today()
days = [str(day) for day in range(1, 32)]
years = [str(year) for year in range(today.year, 1900, -1)]

admision_years = [str(year)[2:] for year in range(today.year, today.year - 5, -1)]
specialities = ["КМ/БО", "БП", "ПЗ", "КС", "ТВ", "ЕП"]

group_labels = ("спеціальність", "рік вступу", "номер групи")
for row, text in enumerate(group_labels):
    label = Label(group_frame, text=text, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN)
    label.grid(row=row, column=0, padx=(16, 8), pady=6, sticky=W)

speciality_combo = ttk.Combobox(
    group_frame, values=specialities, width=12, state="readonly", font=FONT_MAIN
)
admission_combo = ttk.Combobox(
    group_frame, values=admision_years, width=12, state="readonly", font=FONT_MAIN
)
parallel_combo = ttk.Combobox(
    group_frame, values=["1", "2"], width=12, state="readonly", font=FONT_MAIN
)
speciality_combo.grid(row=0, column=1, padx=8, pady=6, sticky=W)
admission_combo.grid(row=1, column=1, padx=8, pady=6, sticky=W)
parallel_combo.grid(row=2, column=1, padx=8, pady=6, sticky=W)

speciality_combo.set("Оберіть...")
admission_combo.set("Оберіть...")
parallel_combo.set("Оберіть...")

date_frame = LabelFrame(
    root,
    text="Вкажіть день, місяць, рік народження:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
date_frame.place(x=340, y=181, width=310, height=154)
for i in range(3):
    date_frame.grid_rowconfigure(i, weight=1)

date_labels = ("дата", "місяць", "рік")
for row, text in enumerate(date_labels):
    label = Label(date_frame, text=text, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN)
    label.grid(row=row, column=0, padx=(16, 8), pady=6, sticky=W)

day_combo = ttk.Combobox(
    date_frame, values=days, width=12, state="readonly", font=FONT_MAIN
)
month_combo = ttk.Combobox(
    date_frame, values=MONTHS, width=12, state="readonly", font=FONT_MAIN
)
year_combo = ttk.Combobox(
    date_frame, values=years, width=12, state="readonly", font=FONT_MAIN
)

day_combo.grid(row=0, column=1, padx=8, pady=6, sticky=W)
month_combo.grid(row=1, column=1, padx=8, pady=6, sticky=W)
year_combo.grid(row=2, column=1, padx=8, pady=6, sticky=W)

month_combo.bind("<<ComboboxSelected>>", update_day_combo)
year_combo.bind("<<ComboboxSelected>>", update_day_combo)

personal_contacts = LabelFrame(
    root,
    text="Вкажіть персональні контакти:",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=FONT_BOLD,
    relief=RIDGE,
    bd=2,
)
personal_contacts.place(x=665, y=181, width=310, height=105)
for i in range(2):
    personal_contacts.grid_rowconfigure(i, weight=1)

contacts_labels = ("Номер телефону", "Email")
contacts_entries = []

for row, text in enumerate(contacts_labels):
    label = Label(
        personal_contacts, text=text, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_MAIN
    )
    label.grid(row=row, column=0, padx=(16, 8), pady=8, sticky=W)

    entry = Entry(
        personal_contacts,
        width=20,
        bg=ACCENT_COLOR,
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        relief=FLAT,
        font=FONT_MAIN,
    )
    entry.grid(row=row, column=1, padx=8, pady=8, sticky=W)
    contacts_entries.append(entry)

phone_entry, email_entry = contacts_entries

reset_date_combos()

process_button = Button(
    root,
    text="Обробити дані",
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=TEXT_COLOR,
    font=FONT_BOLD,
    relief=FLAT,
    cursor="hand2",
    command=process_data,
)
process_button.place(x=665, y=300, height=35, width=145)

clear_button = Button(
    root,
    text="Очистити",
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=TEXT_COLOR,
    font=FONT_BOLD,
    relief=FLAT,
    cursor="hand2",
    command=clear_form,
)
clear_button.place(x=830, y=300, height=35, width=145)

open_file_button = Button(
    root,
    text="Відкрити файл з даними",
    bg=BTN_COLOR,
    fg=TEXT_COLOR,
    activebackground=ACCENT_COLOR,
    activeforeground=TEXT_COLOR,
    font=FONT_BOLD,
    relief=FLAT,
    cursor="hand2",
    command=open_excel_file,
)
open_file_button.place(x=557, y=350, height=35, width=200)

author = Label(
    root,
    text="\u00a9 Шарандак О.В., ПЗ-25-1",
    bg=BG_COLOR,
    fg=ACCENT_COLOR,
    font=(font_family, 8, "italic"),
)
author.place(x=20, y=360)

focus_order = [
    (surname_entry, name_entry, True),
    (name_entry, patronymic_entry, True),
    (patronymic_entry, speciality_combo, True),
    (speciality_combo, admission_combo, False),
    (admission_combo, parallel_combo, False),
    (parallel_combo, day_combo, False),
    (day_combo, month_combo, False),
    (month_combo, year_combo, False),
    (year_combo, phone_entry, False),
    (phone_entry, email_entry, False),
    (email_entry, process_button, False),
]


def setup_focus_chain(chain):
    for current, next_w, cap in chain:
        for key in ("<Return>", "<KP_Enter>", "<Tab>"):
            current.bind(
                key, lambda e, c=current, n=next_w, cp=cap: focus_next_entry(c, n, cp)
            )


setup_focus_chain(focus_order)

process_button.bind("<Return>", lambda e: process_button.invoke())
process_button.bind("<Tab>", lambda e: focus_next_entry(process_button, clear_button))

clear_button.bind("<Return>", lambda e: clear_button.invoke())
clear_button.bind("<Tab>", lambda e: focus_next_entry(clear_button, surname_entry))

surname_entry.focus_set()
root.mainloop()
