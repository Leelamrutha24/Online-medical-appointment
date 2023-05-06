import tkinter as tk
from tkinter import messagebox
import mysql.connector


class AppointmentSystem:
    def __init__(self, master):
        self.master = master
        #CREATING ONLINE MEDICAL APPOINTMENT WINDOW
        self.master.title("Online Medical Appointment")
        self.master.geometry("700x500")
        
        #CREATING THE TITLE BUTTON
        self.title_button = tk.Button(master, text=self.master.title(),width=22, height=3,font=("Arial", 16,"bold"), bg='lightgreen', fg='white')
        self.title_button.grid(row=0, column=0,columnspan=2, padx=10, pady=10)
        
        #CREATING THE PATIENT INFORMATION BUTTON
        self.patient_info_button = tk.Button(master, text="Patient Information",width=20, height=3,command=self.patient_info,font=("Arial", 16,"bold"), bg='lightblue', fg='white')
        self.patient_info_button.grid(row=1, column=0,padx=10, pady=10)

        #CREATING THE SPECIALITY SELECTION BUTTON
        self.speciality_button = tk.Button(master, text="Speciality Selection",width=20, height=3,command=self.speciality,font=("Arial", 16,"bold"), bg='lightblue', fg='white')
        self.speciality_button.grid(row=1, column=1, padx=10, pady=10)

        #CREATING THE DOCTOR SELECTION BUTTON
        self.doctor_button = tk.Button(master, text="Doctor Selection",width=20, height=3,command=self.doctor,font=("Arial", 16,"bold"), bg='lightblue', fg='white')
        self.doctor_button.grid(row=2, column=0, padx=10, pady=10)
        
        #CREATING THE APPOINTMENT INFORMATION BUTTON
        self.appointment_button = tk.Button(master, text="Appointment Information",width=20, height=3,command=self.appointment_info, font=("Arial", 16,"bold"),bg='lightblue', fg='white')
        self.appointment_button.grid(row=2, column=1, padx=10, pady=10)

        #CREATING THE SUBMIT BUTTON
        self.submit_button = tk.Button(master, text="Submit", width=10, height=2,command=self.submit)
        self.submit_button.grid(row=3, column=0, columnspan=2,padx=10, pady=10)
        
        #DECLARING PATIENT INFORMATION VALUES AS NONE
        self.patient_name = None
        self.patient_age = None
        self.patient_gender = None
        self.patient_email = None
        self.speciality_selection = None
        self.doctor_selection = None
        self.appointment_date = None
        self.appointment_details = None
        self.reason_for_admission = None
        self.name_entry=None
        
    def patient_info(self):
        self.patient_info_window = tk.Toplevel(self.master)
        self.patient_info_window.title("Patient Information")
        self.patient_info_window.geometry("500x500")

        self.name_label = tk.Label(self.patient_info_window, text="Name:",width=20, height=3,font=("Arial", 10,"bold"))
        self.name_label.pack()

        self.name_entry = tk.Entry(self.patient_info_window)
        self.name_entry.pack()

        self.age_label = tk.Label(self.patient_info_window, text="Age:",width=20, height=3,font=("Arial", 10,"bold"))
        self.age_label.pack()

        self.age_entry = tk.Entry(self.patient_info_window)
        self.age_entry.pack()

        self.gender_label = tk.Label(self.patient_info_window, text="Gender:",width=20, height=3,font=("Arial", 10,"bold"))
        self.gender_label.pack()

        self.gender_entry = tk.Entry(self.patient_info_window)
        self.gender_entry.pack()

        self.email_label = tk.Label(self.patient_info_window, text="Email:",width=20, height=3,font=("Arial", 10,"bold"))
        self.email_label.pack()

        self.email_entry = tk.Entry(self.patient_info_window)
        self.email_entry.pack()
        self.save1=tk.Button(self.patient_info_window,text="Save",command=self.get_patient_details)
        self.save1.pack()
        global patient_record
        patient_record= (self.name_entry, self.age_entry, self.gender_entry, self.email_entry)
    def get_patient_details(self):
        global details
        details=[patient_record[0].get(),patient_record[1].get(),patient_record[2].get(),patient_record[3].get()]
        print(details[0],details[1],details[2],details[3])
        self.patient_info_window.destroy()
        
    def get_speciality(self):
        details.append(speciality.get())
        print(details[4])
        self.speciality_window.destroy()
            
    def get_doctor(self):
        details.append(doctor.get())
        print(details[5])
        self.doctor_window.destroy()
        
    def get_appointment_info(self):
        details.append(appointment_info[0].get())
        details.append(appointment_info[1].get())
        details.append(appointment_info[2].get())
        print(details[6],details[7],details[8])
        self.appointment_window.destroy()
        
    def speciality(self):
        self.speciality_window = tk.Toplevel(self.master)
        self.speciality_window.title("Speciality Selection")
        self.speciality_window.geometry("500x200")

        self.speciality_label = tk.Label(self.speciality_window, text="Select a speciality:",width=20, height=3,font=("Arial", 10,"bold"))
        self.speciality_label.pack()

        self.speciality_options = ["Cardiology", "Dermatology", "Gastroenterology", "Neurology", "Oncology", "Pediatrics"]
        self.speciality_selection = tk.StringVar(self.speciality_window)
        self.speciality_selection.set("Speciality")

        self.speciality_menu = tk.OptionMenu(self.speciality_window,self.speciality_selection, *self.speciality_options)
        self.speciality_menu.pack()
        
        # Add a spacer label
        tk.Label(self.speciality_window, text="", height=1).pack()
    
        self.save2=tk.Button(self.speciality_window,text="Save",command=self.get_speciality)
        self.save2.pack()
        global speciality
        speciality=self.speciality_selection
        
    def doctor(self):
        if self.speciality_selection is None:
            tk.messagebox.showerror("Error", "Please select a speciality.")
            return

        self.doctor_window = tk.Toplevel(self.master)
        self.doctor_window.title("Doctor Selection")
        self.doctor_window.geometry("500x200")

        self.doctor_label = tk.Label(self.doctor_window, text="Select a doctor:",width=20, height=3,font=("Arial", 10,"bold"))
        self.doctor_label.pack()

        if self.speciality_selection.get() == "Cardiology":
            self.doctor_options = ["Dr. Smith", "Dr. Johnson", "Dr. Lee"]
        elif self.speciality_selection.get() == "Dermatology":
            self.doctor_options = ["Dr. Brown", "Dr. White", "Dr. Kim"]
        elif self.speciality_selection.get() == "Gastroenterology":
                        self.doctor_options = ["Dr. Patel", "Dr. Gupta", "Dr. Khan"]
        elif self.speciality_selection.get() == "Neurology":
            self.doctor_options = ["Dr. Anderson", "Dr. Wilson", "Dr. Clark"]
        elif self.speciality_selection.get() == "Oncology":
            self.doctor_options = ["Dr. Baker", "Dr. Turner", "Dr. Davis"]
        elif self.speciality_selection.get() == "Pediatrics":
            self.doctor_options = ["Dr. Adams", "Dr. Carter", "Dr. Evans"]
        else:
            self.doctor_options = []

        if not self.doctor_options:
            tk.messagebox.showerror("Error", "No doctors found for this speciality.")
            return

        self.doctor_selection = tk.StringVar(self.doctor_window)
        self.doctor_selection.set("Select Doctor")

        self.doctor_menu = tk.OptionMenu(self.doctor_window, self.doctor_selection, *self.doctor_options)
        self.doctor_menu.pack()

        # Add a spacer label
        tk.Label(self.doctor_window, text="", height=1).pack()
        
        self.save3=tk.Button(self.doctor_window,text="Save",command=self.get_doctor)
        self.save3.pack()
        global doctor
        doctor = self.doctor_selection
        
    def appointment_info(self):
        self.appointment_window = tk.Toplevel(self.master)
        self.appointment_window.title("Appointment Information")
        self.appointment_window.geometry("500x400")

        self.date_label = tk.Label(self.appointment_window, text="Appointment Date:",width=20, height=3,font=("Arial", 10,"bold"))
        self.date_label.pack()

        self.date_entry = tk.Entry(self.appointment_window)
        self.date_entry.pack()

        self.details_label = tk.Label(self.appointment_window, text="Appointment Details:",width=20, height=3,font=("Arial", 10,"bold"))
        self.details_label.pack()

        self.details_entry = tk.Entry(self.appointment_window)
        self.details_entry.pack()

        self.reason_label = tk.Label(self.appointment_window, text="Reason for Admission:",width=20, height=3,font=("Arial", 10,"bold"))
        self.reason_label.pack()

        self.reason_entry = tk.Entry(self.appointment_window)
        self.reason_entry.pack()
        
        # Add a spacer label
        tk.Label(self.appointment_window, text="", height=1).pack()
        
        self.save4=tk.Button(self.appointment_window,text="Save",command=self.get_appointment_info)
        self.save4.pack()
        global appointment_info
        appointment_info = (self.date_entry,self.details_entry ,self.reason_entry)
        
    def submit(self):
        query="INSERT INTO appointments VALUES"+str(tuple(details))
        # connect the db
        db_connection = mysql.connector.connect( 
        host= "localhost", 
        user= "root", 
        passwd= "Sharmila@9597") 
        db_cursor = db_connection.cursor()
        db_cursor.execute("USE appointment_details")
        db_cursor.execute(query)
        db_connection.commit() 
        print("Inserted to DB successfully!")
        root = tk.Tk()
        root.withdraw()  # Hide the root window

        # Show a message box
        messagebox.showinfo("Data saved successfully", "Appointment has been successfully done" + "\U0001F44D")
        
        #Start the tkinter event loop
        root.mainloop()
        
        
if __name__ == "__main__":
    root = tk.Tk()
    appointment_system = AppointmentSystem(root)
    root.mainloop()
    db_connection = mysql.connector.connect( 
        host= "localhost", 
        user= "root", 
        passwd= "Sharmila@9597")
    db_cursor = db_connection.cursor()
    db_cursor.execute("USE appointment_details")
    db_cursor.execute("SELECT * FROM appointments")
    myresult = db_cursor.fetchall()
    db_cursor.execute("USE appointment_details")
    db_cursor.execute("SELECT * FROM appointments")
    myresult = db_cursor.fetchall()
    for patient in myresult:
        print(patient)
