import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkfont
from calculator import calculate_total, format_result


class PriceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор стоимости")
        self.root.geometry("420x480")
        self.root.resizable(False, False)

        # настройка шрифтов для элементов интерфейса
        self.font_title = tkfont.Font(family="Segoe UI", size=18, weight="bold")
        self.font_label = tkfont.Font(family="Segoe UI", size=12)
        self.font_entry = tkfont.Font(family="Consolas", size=13)
        self.font_result = tkfont.Font(family="Segoe UI", size=14, weight="bold")
        self.font_info = tkfont.Font(family="Segoe UI", size=11)
        self._setup_ui()

    def _setup_ui(self):
        # цветовая палитра интерфейса
        bg_main = "#F4F6F9"
        fg_text = "#2C3E50"
        bg_entry = "#ECF0F1"
        border_color = "#BDC3C7"
        btn_calc_bg = "#3498DB"
        btn_calc_hover = "#2980B9"
        btn_clear_bg = "#95A5A6"
        btn_clear_hover = "#7F8C8D"
        bg_result = "#E8F8F5"
        fg_result = "#16A085"

        # основной контейнер окна
        self.container = tk.Frame(self.root, padx=25, pady=25, bg=bg_main)
        self.container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(40, 20))

        # заголовок программы
        tk.Label(self.container, text=" Расчёт стоимости", font=self.font_title,
                 bg=bg_main, fg=fg_text).pack(pady=(0, 20))

        # поля ввода данных
        self._add_labeled_entry("Количество тетрадей:", bg_main, fg_text, bg_entry, border_color)
        self._add_labeled_entry("Цена одной тетради (₽):", bg_main, fg_text, bg_entry, border_color)
        self._add_labeled_entry("Цена одной обложки (₽):", bg_main, fg_text, bg_entry, border_color)

        # контейнер для кнопок управления
        btn_frame = tk.Frame(self.container, bg=bg_main)
        btn_frame.pack(fill=tk.X, pady=15)

        # кнопка расчёта
        self.btn_calc = tk.Button(btn_frame, text="Рассчитать", cursor="hand2",
                                  font=self.font_label, bg=btn_calc_bg, fg="white",
                                  relief=tk.FLAT, bd=0, pady=8, command=self.calculate_price)
        self.btn_calc.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 4))
        self.btn_calc.bind("<Enter>", lambda e: self.btn_calc.config(bg=btn_calc_hover))
        self.btn_calc.bind("<Leave>", lambda e: self.btn_calc.config(bg=btn_calc_bg))

        # кнопка очистки
        self.btn_clear = tk.Button(btn_frame, text="Очистить", cursor="hand2",
                                   font=self.font_label, bg=btn_clear_bg, fg="white",
                                   relief=tk.FLAT, bd=0, pady=8, command=self.clear_fields)
        self.btn_clear.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(4, 0))
        self.btn_clear.bind("<Enter>", lambda e: self.btn_clear.config(bg=btn_clear_hover))
        self.btn_clear.bind("<Leave>", lambda e: self.btn_clear.config(bg=btn_clear_bg))

        # блок вывода результата
        self.res_frame = tk.Frame(self.container, bd=1, relief=tk.SOLID, bg=bg_result,
                                  highlightbackground=bg_result)
        self.res_frame.pack(pady=10, fill=tk.X)
        self.lbl_total = tk.Label(self.res_frame, text="Итого: 0.00 ₽",
                                  font=self.font_result, bg=bg_result, fg=fg_result)
        self.lbl_total.pack(pady=8)
        self.lbl_info = tk.Label(self.res_frame, text="Введите данные для расчёта",
                                 font=self.font_info, bg=bg_result, fg=fg_text)
        self.lbl_info.pack(pady=(0, 8))

    def _add_labeled_entry(self, text, bg_main, fg_text, bg_entry, border_color):
        frame = tk.Frame(self.container, bg=bg_main)
        frame.pack(fill=tk.X, pady=6)
        tk.Label(frame, text=text, font=self.font_label, bg=bg_main, fg=fg_text,
                 anchor="w").pack(side=tk.LEFT, padx=(0, 12))
        entry = tk.Entry(frame, font=self.font_entry, justify="center", width=12,
                         bg=bg_entry, fg=fg_text, relief=tk.SOLID, bd=1,
                         highlightthickness=0, highlightbackground=border_color,
                         highlightcolor="#3498DB")
        entry.pack(side=tk.RIGHT)

        if "тетрадей" in text:
            self.entry_count = entry
        elif "тетради (₽)" in text:
            self.entry_price_tetr = entry
        else:
            self.entry_price_obloz = entry

    def clear_fields(self):
        self.entry_count.delete(0, tk.END)
        self.entry_price_tetr.delete(0, tk.END)
        self.entry_price_obloz.delete(0, tk.END)
        self.lbl_total.config(text="Итого: 0.00 ₽")
        self.lbl_info.config(text="Введите данные для расчёта")

    def calculate_price(self):
        try:
            count = int(self.entry_count.get())
            price_tetr = float(self.entry_price_tetr.get())
            price_obloz = float(self.entry_price_obloz.get())

            # Используем функцию из calculator.py
            total = calculate_total(count, price_tetr, price_obloz)

            self.lbl_total.config(text=f"Итого: {total:,.2f} ₽")
            self.lbl_info.config(text=f"Тетрадей: {count} | Обложек: {count}")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", f"Проверьте введённые данные.\n{e}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PriceCalculator(root)
    root.mainloop()