from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi  = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    mon = time.strftime('%m')
    year = time.strftime('%Y')
    day = time.strftime('%A')       # Full day name      # Change '%A' to '%a' for show short day name
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=mon)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(1000, date_time)  # Update every second


# Main window
clock = Tk()
clock.title("Digital Clock")
clock.geometry("1000x500") 
clock.config(bg="#1C1C1C")  

# Label Styles
label_style = {"font": ("Arial", 60, "bold"), "bg": "#1C1C1C", "fg": "#00FF00"}  # Green text
label_txt_style = {"font": ("Arial", 20, "bold"), "bg": "#1C1C1C", "fg": "#FFFFFF"}

# Time Section
lab_hr = Label(clock, text="00", **label_style)
lab_hr.place(x=70, y=50, height=110, width=100)

lab_hr_txt = Label(clock, text="HOUR", **label_txt_style)
lab_hr_txt.place(x=70, y=160, height=30, width=100)

lab_min = Label(clock, text="00", **label_style)
lab_min.place(x=270, y=50, height=110, width=100)

lab_min_txt = Label(clock, text="MIN", **label_txt_style)
lab_min_txt.place(x=270, y=160, height=30, width=100)

lab_sec = Label(clock, text="00", **label_style)
lab_sec.place(x=470, y=50, height=110, width=100)

lab_sec_txt = Label(clock, text="SEC", **label_txt_style)
lab_sec_txt.place(x=470, y=160, height=30, width=100)

lab_am = Label(clock, text="AM", **label_style)
lab_am.place(x=670, y=50, height=110, width=150)  

lab_am_txt = Label(clock, text="AM/PM", **label_txt_style)
lab_am_txt.place(x=670, y=160, height=30, width=150)

# Date Section
lab_date = Label(clock, text="00", **label_style)
lab_date.place(x=70, y=270, height=110, width=100)

lab_date_txt = Label(clock, text="DATE", **label_txt_style)
lab_date_txt.place(x=70, y=380, height=30, width=100)

lab_mo = Label(clock, text="00", **label_style)
lab_mo.place(x=270, y=270, height=110, width=100)

lab_mo_txt = Label(clock, text="MONTH", **label_txt_style)
lab_mo_txt.place(x=270, y=380, height=30, width=100)

lab_year = Label(clock, text="2024", **label_style)
lab_year.place(x=470, y=270, height=110, width=200)  

lab_year_txt = Label(clock, text="YEAR", **label_txt_style)
lab_year_txt.place(x=470, y=380, height=30, width=200)

lab_day = Label(clock, text="Wednesday", font=("Arial", 40, "bold"), bg="#1C1C1C", fg="#00FF00")
lab_day.place(x=700, y=270, height=110, width=300) 

lab_day_txt = Label(clock, text="DAY", **label_txt_style)
lab_day_txt.place(x=760, y=380, height=30, width=150)



date_time()
clock.mainloop()