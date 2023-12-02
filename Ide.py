from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from pygments import highlight



compiler = Tk()
compiler.title('Free IDE')
file_path =''

def set_file_path(path):
    global file_path
    file_path = path

def set_file_path(path):
    global file_path
    file_path = path


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Pyhton Files', '*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)
        set_file_path(path)

def open_file():
    path = askopenfilename(filetypes=[('Pyhton Files', '*.py')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def highlight_code(event=None):
    content = editor.get("1.0", "end-1c")
    highlighted_content = highlight(content, PythonLexer(), TkFormatter())
    editor.delete("1.0", END)
    editor.insert("1.0", highlighted_content)
    editor.bind("<KeyRelease>", highlight_code)

menu_bar = Menu(compiler)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)



run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)
compiler.config(menu=menu_bar)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Pyhton Files', '*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)
        set_file_path(path)


def open_file():
    path = askopenfilename(filetypes=[('Pyhton Files', '*.py')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)



editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()  
