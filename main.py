#for saving data:
import pandas as pd

classified = pd.read_csv('Classified.csv').dropna(how='all')
expenses = pd.read_csv('Expenses.csv')

#for the loading screen:
from PIL import Image, ImageTk

#for viewing insights:
import webview
from jinja2 import FileSystemLoader, Environment
import matplotlib.pyplot as plt
import os

#for saving dates:
import datetime

#for encrypting passwords {I made this module :)}
import simple_encrypter

#for the user interface:
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Expense tracker')
root.iconbitmap('icon.ico')

def show_frame(frame):
    frame.tkraise()

frame0 = tk.Frame(root)
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

for frame in (frame0, frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

#frame0 (loading screen)
image = Image.open("logo.png")
image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize to fit window

bg_img = ImageTk.PhotoImage(image)

# Place the image as background
bg_label = tk.Label(frame0, image=bg_img)
bg_label.image = bg_img
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
copyright_label = tk.Label(frame0, text="© 2025 Kevin Ehab. All rights reserved.", font=("Arial", 10))
copyright_label.place(relx=0.5, rely=0.95, anchor='center')
show_frame(frame0)
root.after(5000, lambda: show_frame(frame1))

n = 0
def signup_login(type):
    global n, classified, account
    account = account_entry.get().strip().lower()
    entered_password = password_entry.get().strip()

    if not account or not entered_password:
        messagebox.showerror('Error', "All fields must have at least 1 charachter")
        return

    if type == 'sign up':
        if len(entered_password) < 8:
            messagebox.showerror('Error', 'Password must be at least 8 characters long')
            return
        if account in classified['account'].values:
            messagebox.showerror('Error', 'Account already exists.\nSign in.')
            return
        if n == 0:
            global budget_ent, saving_ent
            tk.Label(frame1, text= "enter monthly budget:").grid(row=3, column=0)
            budget_ent = tk.Entry(frame1, width=20)
            budget_ent.grid(row=3, column=1)

            tk.Label(frame1, text= "enter how much you \n want to save per month:").grid(row=4, column=0)
            saving_ent = tk.Entry(frame1, width=20)
            saving_ent.grid(row=4, column=1)
            n+=1
            return
        else:
            try:
                budget = int(budget_ent.get())
                saving = int(saving_ent.get())
                if saving >= budget:
                    messagebox.showerror('Error', 'Saving exceeds budget')
                    return
                if saving < 0 or budget < 0:
                    messagebox.showerror('Error', "negative numbers aren't allowed")
                    return
                budget = str(budget)
            except:
                messagebox.showerror('Error', 'Budget and saving must both be a number')
                return
            if not budget or not saving:
                messagebox.showerror('Error', 'Please Enter your monthly budget and saving')
                return
        encrypted_password = simple_encrypter.encrypt(entered_password)
        encrypted_budget = simple_encrypter.encrypt(budget)
        data = {
            "account": account,
            "password_code": encrypted_password['code'],
            "password_key": encrypted_password['key'],
            "budget_code": encrypted_budget['code'],
            "budget_key": encrypted_budget['key'],
            "saving": saving
        }
        classified = pd.concat([classified, pd.DataFrame([data])], ignore_index=True)
        classified.to_csv('Classified.csv', index=False)
        messagebox.showinfo('Success', 'Account created successfully')
        show_frame(frame3)

    elif type == 'login':
        if account in classified['account'].values:
            user_data = classified[classified['account'] == account].iloc[0]
            decrypted_password = simple_encrypter.decrypt({'code': user_data['password_code'],
                                                            'key': user_data['password_key']})
            if decrypted_password != entered_password:
                messagebox.showerror('Error', "Wrong password")
                return
            else:
                messagebox.showinfo('Success', 'Login successful')
                show_frame(frame2)
        else:
            messagebox.showerror('Error', "Account not found")
            return
    
#login or sign up screen(AKA. frame1)    
tk.Label(frame1, text="login or sign up:", font=('Aerial', 20)).grid(row=0, column=0)
tk.Label(frame1, text='enter your account address').grid(row=1, column=0)
account_entry = tk.Entry(frame1, width=20)
account_entry.grid(row=1, column=1)

tk.Label(frame1, text='enter your password').grid(row=2, column=0)
password_entry = tk.Entry(frame1, width=20, show='*')
password_entry.grid(row=2, column=1)

tk.Label(frame1).grid(row=5, column=0)
tk.Label(frame1).grid(row=6, column=0)

signup = tk.Button(frame1, text='sign up',command= lambda: signup_login('sign up'))
signup.grid(row=7, column=0)

login = tk.Button(frame1, text='login',command= lambda: signup_login('login') )
login.grid(row=7, column=1)

#options screen(AKA. frame2)
tk.Label(frame2, text="Options:", font=('Aerial', 20)).grid(row=0, column=1)
   
tk.Label(frame2).grid(row=1, column=0)
tk.Label(frame2).grid(row=2, column=0)

def add_data():
    show_frame(frame3)

add_data_btn = tk.Button(frame2, text='add new expenses', command=add_data)
add_data_btn.grid(row=3, column=0)

#added a counter to check if the budget is changed
c = 0
def edit_budget():
    global budget_ent, saving_ent , c, classified
    if c == 0:
        tk.Label(frame2, text='Budget:').grid(row=4, column=1)
        budget_ent = tk.Entry(frame2, width=18)
        budget_ent.grid(row=5, column=1)
        tk.Label(frame2, text='Saving:').grid(row=6, column=1)
        saving_ent = tk.Entry(frame2, width=18)
        saving_ent.grid(row=7, column=1)
        c += 1
    else:
        try:
            budget = int(budget_ent.get())
            saving = int(saving_ent.get())
            if saving >= budget:
                messagebox.showerror('Error', 'Saving exceeds budget')
                return
            if saving < 0 or budget < 0:
                messagebox.showerror('Error', "negative numbers aren't allowed")
                return
            budget = str(budget)
        except:
            messagebox.showerror('Error', 'budget and saving must be a number')
            return
        encrypted_budget = simple_encrypter.encrypt(budget)
        classified.loc[classified['account'] == account, 'budget_code'] = encrypted_budget['code']
        classified.loc[classified['account'] == account, 'budget_key'] = encrypted_budget['key']
        classified.loc[classified['account'] == account, 'saving'] = saving
        classified.to_csv('Classified.csv', index=False)
        messagebox.showinfo('Success!', 'budget and saving edited successfully')
        c=0

edit_budget_btn = tk.Button(frame2, text='edit budget\nand saving', command=edit_budget)
edit_budget_btn.grid(row=3, column=1)

def remove_dashboard():
    os.remove('dashboard.html')
    os.remove('trend.png')
    os.remove('pie.png')
    os.remove('plot.png')

def view_data():
    global expenses
    budget = int(simple_encrypter.decrypt({'code': classified[classified['account'] == account]['budget_code'].iloc[0],
                                           'key': classified[classified['account'] == account]['budget_key'].iloc[0]}))
    
    saving = classified.loc[classified['account'] == account, 'saving'].iloc[0]
    expenses = pd.read_csv('Expenses.csv')
    days = len(pd.unique(expenses['date']))
    if days > 30:
        days = 30
    extracted_df = expenses[expenses['account'] == account].tail(days)
    total_sum = sum(extracted_df['total'])

    food = sum(extracted_df['food'])
    transportation = sum(extracted_df['transportation'])
    shopping = sum(extracted_df['shopping'])
    bills = sum(extracted_df['bills'])
    entertainment = sum(extracted_df['entertainment'])
    healthcare= sum(extracted_df['healthcare'])

    sum_by_categories = {"food":food, 
                         "transportation":transportation,
                         "shopping": shopping,
                         "bills":bills,
                         "entertainment":entertainment,
                         "healthcare": healthcare}
    max_category = max(sum_by_categories, key=sum_by_categories.get)
    max_category = max_category.title()

    biggest_day = extracted_df[extracted_df['total'] == extracted_df['total'].max()]['date'].iloc[0]
    smallest_day = extracted_df[extracted_df['total'] == extracted_df['total'].min()]['date'].iloc[0]

    daily_spending = round(total_sum / days)

    if daily_spending > (budget - saving)/30:
        decrease = round(((daily_spending - (budget - saving)/30) / daily_spending) * 100)
        message = '⚠️ Be carful. You need to spend less to reach your saving goal, '
        message += f'which is <strong>{saving}</strong>. '
        message += f'So decrease your spending by {decrease}% !'
    else:
        message = '✅ You are on the right track to achieving your saving goal!'
    #pie chart:
    plt.figure(figsize=(6, 6))
    plt.pie(sum_by_categories.values(), labels=sum_by_categories.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.savefig('pie.png')
    plt.close()
    
    #trend chart:
    plt.figure(figsize=(8, 6))
    plt.plot(extracted_df['date'], extracted_df['total'])
    plt.axhline(daily_spending, color="#00039e", linestyle='--',
                 linewidth=2, label=f'Average spending: ({daily_spending})')
    plt.axhline(round(budget/30), color="#b30000", linestyle='--',
                linewidth=2, label=f'Suggested spending: ({round(budget/30)})')
    plt.xticks(rotation=90)
    plt.title('Expense Trend Over Time')
    plt.savefig('trend.png')
    plt.close()

    #plot chart (total / budget percentage per day)
    plt.figure(figsize=(8,6))
    percent = round(extracted_df['total'] / budget* 100) 
    plt.bar(extracted_df['date'], percent, color='#e67e22')
    plt.gca().set_yticklabels([f'{int(y)}%' for y in plt.gca().get_yticks()])
    plt.xticks(rotation=90)
    plt.title('Date VS Spending Percentage')
    plt.savefig('plot.png')
    plt.close()
    #table:
    html_table = extracted_df.to_html()
    #All the data:
    data = {
        'account': account,
        'biggest_day': biggest_day,
        'budget': budget,
        'saving': saving,
        'smallest_day': smallest_day,
        'total_sum': total_sum,
        'days': days,
        'food': food,
        'transportation': transportation,
        'shopping': shopping,
        'bills': bills,
        'entertainment': entertainment,
        'healthcare': healthcare,
        'max_category': max_category,
        'daily_spending': daily_spending,
        'html_table': html_table,
        'message': message
    }
    #rendering:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    html = template.render(data)

    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html)

    file_path = os.path.abspath('dashboard.html')
    window = webview.create_window('Expense Tracker', f'file://{file_path}')

    #remove the dasboard to hide the user's information
    window.events.closed +=  remove_dashboard
    webview.start()


view_data_btn = tk.Button(frame2, text='view current expenses', command=view_data)
view_data_btn.grid(row=3, column=2)

#adding expenses screen(AKA. frame3)
tk.Label(frame3, text= "Categories:", font=('Aerial', 20)).grid(row=0,column=0)

tk.Label(frame3, text= "food expenses:").grid(row=1, column=0)
food_ent = tk.Entry(frame3, width=20)
food_ent.grid(row=1, column=1)

tk.Label(frame3, text= "transportaition expenses:").grid(row=2, column=0)
transportation_ent = tk.Entry(frame3, width=20)
transportation_ent.grid(row=2, column=1)

tk.Label(frame3, text= "shopping expenses:").grid(row=3, column=0)
shopping_ent = tk.Entry(frame3, width=20)
shopping_ent.grid(row=3, column=1)

tk.Label(frame3, text= "bills expenses:").grid(row=4, column=0)
bills_ent = tk.Entry(frame3, width=20)
bills_ent.grid(row=4, column=1)

tk.Label(frame3, text= "entertainment expenses:").grid(row=5, column=0)
entertainment_ent = tk.Entry(frame3, width=20)
entertainment_ent.grid(row=5, column=1)

tk.Label(frame3, text= "healthcare expenses:").grid(row=6, column=0)
healthcare_ent = tk.Entry(frame3, width=20)
healthcare_ent.grid(row=6, column=1)

def submit_expenses():
    global expenses
    food = food_ent.get()
    transportation = transportation_ent.get()
    shopping = shopping_ent.get()
    bills = bills_ent.get()
    entertainment = entertainment_ent.get()
    healthcare = healthcare_ent.get()
    try:
        food = int(food) if food.strip() else 0
        transportation = int(transportation) if transportation.strip() else 0
        shopping = int(shopping) if shopping.strip() else 0
        bills = int(bills) if bills.strip() else 0
        entertainment = int(entertainment) if entertainment.strip() else 0
        healthcare = int(healthcare) if healthcare.strip() else 0
    except:
        messagebox.showerror('Error', "Invalid entry:\nonly integers allowed")
        return

    total = food + transportation + shopping + bills + entertainment + healthcare
    data = {
        'account': account,
        'date': datetime.date.today().strftime('%Y-%m-%d'),
        'food': food,
        'transportation': transportation,
        'shopping': shopping,
        'bills': bills,
        'entertainment': entertainment,
        'healthcare': healthcare,
        'total': total
    }
    
    expenses = pd.concat([expenses, pd.DataFrame([data])], ignore_index=True)
    expenses.to_csv('Expenses.csv', index=False)
    messagebox.showinfo('Success', 'info added successfully')
    show_frame(frame2)

tk.Button(frame3, text= "submit expenses", command=submit_expenses).grid(row=7, column=0)

root.mainloop()
