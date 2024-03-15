import customtkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename


def save_file():
    filepath = asksaveasfilename(filetypes=[('text file', '*.txt')])

    if not filepath:
        return

    with open(filepath, 'w', encoding='utf8') as f:
        content = text_field.get('1.0', 'end')
        f.write(content)
    root.title(f'Notepad Ultra Over 9000 | file: {filepath}')


def open_file():
    filepath = askopenfilename(filetypes=[('text file', '*.txt')])

    if not filepath:
        return

    text_field.delete('1.0', 'end')
    with open(filepath, 'r', encoding='utf8') as f:
        content = f.read()
        text_field.insert('end', content)
    root.title(f'Notepad Ultra Over 9000 | file: {filepath}')


def font_type(*args):
    type_font = font_combobox_var.get()
    size = font_size_combobox_var.get()
    size = int(size)
    text_field.configure(font=(type_font, size))


def wrap():
    wrap_var = wrap_word.get()
    if wrap_var == 0:
        text_field.configure(wrap='none')
    elif wrap_var == 1:
        text_field.configure(wrap='word')


def count_characters_func(event):
    count_char = len(text_field.get('1.0', 'end'))
    lines = text_field.get('1.0', 'end')
    lines = lines.count('\n')
    count_characters.configure(text=f'{count_char - 1} characters | {lines} lines')


root = customtkinter.CTk()
root.title(f'Notepad Ultra Over 9000 | file: text file.txt')
root.geometry('1300x750')
root.config(background='#ffffff')
root.minsize(600, 300)

option_bar = customtkinter.CTkFrame(root, height=50, corner_radius=0, fg_color='#66545e')
option_bar.pack(fill='both')

open_button = customtkinter.CTkButton(option_bar, width=50, text='Open', fg_color='#66545e', hover_color='#a39193',
                                      command=open_file)
open_button.pack(side='left', padx=(5, 0), pady=2, anchor='center')

save_button = customtkinter.CTkButton(option_bar, width=50, text='Save', fg_color='#66545e', hover_color='#a39193',
                                      command=save_file)
save_button.pack(side='left', padx=5, pady=2, anchor='center')

font_combobox_var = customtkinter.StringVar()
font_combobox = customtkinter.CTkComboBox(option_bar, width=180, fg_color='#66545e', button_color='#66545e',
                                          border_color='#66545e', dropdown_hover_color='#a39193',
                                          dropdown_fg_color='#66545e', state='readonly',
                                          values=['Arial', 'Times New Roman', 'Comic Sans MS', 'Courier New', 'Impact'],
                                          variable=font_combobox_var)

font_combobox.set('Arial')
font_combobox.pack(side='left', padx=5, pady=2, anchor='center')
font_combobox_var.trace('w', font_type)

font_size_combobox_var = customtkinter.StringVar()
font_size_combobox = customtkinter.CTkComboBox(option_bar, width=125, fg_color='#66545e', button_color='#66545e',
                                               border_color='#66545e', dropdown_hover_color='#a39193',
                                               dropdown_fg_color='#66545e', state='readonly',
                                               values=['8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28',
                                                       '36', '48', '56'], variable=font_size_combobox_var)
font_size_combobox.set('24')
font_size_combobox.pack(side='left', padx=5, pady=2, anchor='center')
font_size_combobox_var.trace('w', font_type)

wrap_word_var = customtkinter.IntVar(value=1)
wrap_word = customtkinter.CTkCheckBox(option_bar, text='Word wrapping', border_width=0, bg_color='#66545e',
                                      hover_color='#a39193', fg_color='#66545e',
                                      variable=wrap_word_var, command=wrap)
wrap_word.pack(side='left', padx=5, pady=2, anchor='center')

text_field = customtkinter.CTkTextbox(root, corner_radius=0, fg_color='#a39193', wrap='word', font=('Arial', 24),
                                      text_color='#ffffff')
text_field.pack(fill='both', expand=True)

text_field.bind('<KeyPress>', count_characters_func)
text_field.bind('<KeyRelease>', count_characters_func)

info_bar = customtkinter.CTkFrame(root, height=30, corner_radius=0, fg_color='#66545e')
info_bar.pack(fill='both')

count_characters = customtkinter.CTkLabel(info_bar, text='0 characters | 1 lines')
count_characters.pack(side='left', padx=10, anchor='center')

utf_label = customtkinter.CTkLabel(info_bar, text='UTF-8')
utf_label.pack(side='right', padx=10, anchor='center')

root.mainloop()
