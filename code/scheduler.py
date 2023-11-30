import random
import customtkinter
from tkinter import *
from tkinter import ttk

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

colors = ['#ffc09f', '#ffee93', '#fcf5c7', '#a0ced9', '#adf7b6',
          '#ff7477', '#e69597', '#ceb5b7', '#b5d6d6', '#9cf6f6']

task_title = str
description_text = str

root = customtkinter.CTk()
root.title('Scheduler')
root.geometry('900x650+50+0')
root.resizable(False, False)

app_frame = customtkinter.CTkFrame(master=root)
app_frame.pack_configure(fill='both', expand=True)
tasks_label = customtkinter.CTkLabel(master=app_frame, text='Tasks', font=('Sans-serif', 25, 'bold'))
tasks_label.place(x=195, y=25)

events_label = customtkinter.CTkLabel(master=app_frame, text='Events', font=('Sans-serif', 25, 'bold'))
events_label.place(x=623, y=25)

task_scrollable_frame = customtkinter.CTkScrollableFrame(master=app_frame, width=400, height=500)
task_scrollable_frame.place(x=20, y=70)

event_scrollable_frame = customtkinter.CTkScrollableFrame(master=app_frame, width=400, height=500)
event_scrollable_frame.place(x=460, y=70)


def add_task_main():
    dialog = customtkinter.CTk()
    dialog.title('New Task')
    dialog.geometry('400x450+420+160')
    dialog.resizable(False, False)
    title_entry = customtkinter.CTkEntry(master=dialog, placeholder_text='Enter Task Title...', width=250, height=50, font=('sans-serif', 20,'bold'))
    title_entry.pack_configure(padx=30, pady=10)
    description_box = customtkinter.CTkTextbox(master=dialog, height=100, width=250, font=('sans-serif', 15), state='disabled')
    # description_box.insert(0.0, 'Enter Description for task..', tags=None)
    description_box.pack_configure(pady=10)

    def toggle_textbox():
        if checkbox_var.get():
            description_box.configure(state=customtkinter.NORMAL)
        else:
            description_box.delete(1.0, customtkinter.END)
            description_box.configure(state=customtkinter.DISABLED)
    checkbox_var = customtkinter.BooleanVar()
    check_description = customtkinter.CTkCheckBox(master=dialog, text="Enter Description", variable=checkbox_var, command=toggle_textbox)
    check_description.place(x=80, y=200)

    priority_title = customtkinter.CTkLabel(master=dialog, text='Priority:', font=('sans-serif', 15, 'bold'))
    priority_title.place(x=80, y=240)
    priority = customtkinter.CTkSlider(master=dialog, width=250, number_of_steps=2)
    priority.pack_configure(padx=20, pady=(90, 50))
    label1 = customtkinter.CTkLabel(master=dialog, height=25, width=25, text='Low', fg_color='#66BB6A', corner_radius=100, text_color='black')
    label1.place(x=60, y=310)
    label2 = customtkinter.CTkLabel(master=dialog, height=25, width=25, text='Medium', fg_color='#FFD700', corner_radius=100, text_color='black')
    label2.place(x=168, y=310)

    label3 = customtkinter.CTkLabel(master=dialog, height=25, width=25, text='High', fg_color='#FF5733', corner_radius=100, text_color='black')
    label3.place(x=295, y=310)
    # It's Button is defined below this method

    def add_task_dialogue():
        task_title = (title_entry.get()).capitalize()
        description_text = description_box.get(index1='0.0', index2=END)
        if description_text.__contains__('Enter Description for task..'):
            description_text = 'No description'
        if task_title == '':
            task_title = 'No Title'
        new_task_title_label = customtkinter.CTkLabel(master=task_scrollable_frame, text=task_title, width=300, height=150, corner_radius=7, fg_color=colors[random.randint(0, 4)], font=('sans-serif', 30, 'bold'), text_color='black')
        new_task_title_label.pack_configure(padx=0, pady=10)

        def done_box():
            if done_var.get():
                new_task_title_label.destroy()

        done_var = customtkinter.BooleanVar()
        done_var.set(FALSE)
        done_checkbox = customtkinter.CTkCheckBox(master=new_task_title_label, text='Achieved!', text_color='black', variable=done_var, command=done_box)
        done_checkbox.place(x=10, y=10)
        fg_color = str
        text = str
        if priority.get() == 0.0:
            fg_color = '#66BB6A'
            text = 'Low'
        elif priority.get() == 0.5:
            fg_color = '#FFD700'
            text = 'Medium'
        else:
            fg_color = '#FF5733'
            text = 'High'

        priority_color = customtkinter.CTkLabel(master=new_task_title_label, fg_color=fg_color, corner_radius=100, height=25, width=25, text=text)
        priority_color.place(x=220, y=15)
        new_task_descriptio_label = customtkinter.CTkLabel(master=new_task_title_label, text='\n'+description_text, font=('sans-serif', 15), text_color='black')
        new_task_descriptio_label.place(x=20, y=105)
        # switch = customtkinter.CTkCheckBox(master=new_task_title_label)
        # switch.pack_configure(padx=20, pady=20)
        dialog.destroy()

    add_button = customtkinter.CTkButton(master=dialog, text='Add Task', command=add_task_dialogue)  # above function executes on as command
    add_button.pack_configure(pady=20)
    dialog.mainloop()


add_task_button_on_task_task_scrollable_frame = customtkinter.CTkButton(task_scrollable_frame, text="Add Task", command=add_task_main)
add_task_button_on_task_task_scrollable_frame.pack(padx=20, pady=20)


def add_event_main():
    dialog = customtkinter.CTk()
    dialog.title('New Event')
    dialog.geometry('400x450+420+160')
    dialog.resizable(False, False)
    title_entry = customtkinter.CTkEntry(master=dialog, placeholder_text='Enter Event Title...', width=250, height=50,font=('sans-serif', 20, 'bold'))
    title_entry.pack_configure(padx=30, pady=10)
    description_box = customtkinter.CTkTextbox(master=dialog, height=100, width=250, font=('sans-serif', 15), state='disabled')
    # description_box.insert(0.0, 'Enter Description for task..', tags=None)
    description_box.pack_configure(pady=10)

    def toggle_textbox():
        if checkbox_var.get():
            description_box.configure(state=customtkinter.NORMAL)
        else:
            description_box.delete(1.0, customtkinter.END)
            description_box.configure(state=customtkinter.DISABLED)

    checkbox_var = customtkinter.BooleanVar()
    checkbox_var.set(FALSE)

    check_description = customtkinter.CTkCheckBox(master=dialog, text="Enter Description", variable=checkbox_var, command=toggle_textbox)
    check_description.place(x=80, y=200)

    priority_title = customtkinter.CTkLabel(master=dialog, text='Priority:', font=('sans-serif', 15, 'bold'))
    priority_title.place(x=80, y=240)

    priority = customtkinter.CTkSlider(master=dialog, width=250, number_of_steps=2)
    priority.pack_configure(padx=20, pady=(90, 50))

    label1 = customtkinter.CTkLabel(master=dialog, height=25, width=25, text='Low', fg_color='#66BB6A', corner_radius=100, text_color='black')
    label1.place(x=60, y=310)
    label2 = customtkinter.CTkLabel(master=dialog, height=25, width=25, text='Medium', fg_color='#FFD700', corner_radius=100, text_color='black')
    label2.place(x=168, y=310)
    label3 = customtkinter.CTkLabel(master=dialog, height=25, width=25, text='High', fg_color='#FF5733', corner_radius=100, text_color='black')
    label3.place(x=295, y=310)

    # It's Button is defined below this method
    def add_event_dialogue():
        task_title = (title_entry.get()).capitalize()
        description_text = description_box.get(index1='0.0', index2=END)

        if description_text == '':
            description_text = 'No description'
        if task_title == '':
            task_title = 'No Title'

        new_task_title_label = customtkinter.CTkLabel(master=event_scrollable_frame, text=task_title, width=300, height=150, corner_radius=7, fg_color=colors[random.randint(0, 4)], font=('sans-serif', 30, 'bold'), text_color='black')
        new_task_title_label.pack_configure(padx=0, pady=10)

        def done_box():
            if done_var.get():
                new_task_title_label.destroy()

        done_var = customtkinter.BooleanVar()
        done_var.set(FALSE)
        done_checkbox = customtkinter.CTkCheckBox(master=new_task_title_label, text='Attended!', text_color='black', variable=done_var, command=done_box)
        done_checkbox.place(x=10, y=10)

        fg_color = str
        text = str
        if priority.get() == 0.0:
            fg_color = '#66BB6A'
            text = 'Low'
        elif priority.get() == 0.5:
            fg_color = '#FFD700'
            text = 'Medium'
        else:
            fg_color = '#FF5733'
            text = 'High'

        priority_color = customtkinter.CTkLabel(master=new_task_title_label, fg_color=fg_color, corner_radius=100, height=25, width=25, text=text)
        priority_color.place(x=220, y=15)

        new_task_descriptio_label = customtkinter.CTkLabel(master=new_task_title_label, text='\n'+description_text, font=('sans-serif', 15), text_color='black')
        new_task_descriptio_label.place(x=20, y=105)
        dialog.destroy()

    add_button = customtkinter.CTkButton(master=dialog, text='Add Event', command=add_event_dialogue)  # above function executes on as command
    add_button.pack_configure(pady=20)

    dialog.mainloop()

add_even_button_on_event_task_scrollable_frame = customtkinter.CTkButton(event_scrollable_frame, text="Add Event", command=add_event_main)
add_even_button_on_event_task_scrollable_frame.pack(padx=20, pady=20)

root.mainloop()