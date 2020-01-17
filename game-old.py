# The ShisaNyama
# Demonstrate text entry and entry widgets,and the grid layout staff

from Tkinter import *

class Application(Frame):
    """ A GUI application with menu selection. """
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.FullChicken = 0.0
        self.BoerVoers = 0.0
        self.Steak = 0.0
        self.FullChicken_bttn_clicks = 0
        self.BoerVoers_bttn_clicks = 0
        self.Steak_bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets for menu selection. """
        # Prompt label
        self.inst_lbl = Label(self, text = "Enter your staff number please")
        self.inst_lbl.grid(row = 1, column = 0, sticky = W)
        self.staff_lbl = Label(self, text = "Staff number: ")
        self.staff_lbl.grid(row = 2, column = 0, sticky = W)
        
        # Text entry
        self.staff_ent = Entry(self)
        self.staff_ent.grid(row = 2, column = 1, sticky = W)

        # create enter button
        self.enter_bttn = Button(self, text = " Enter ", command = self.menu)
        self.enter_bttn.grid(row = 3, column = 1, sticky = W)

        # create clear button
        self.clear_bttn = Button(self, text = "Clear", command = self.clear)
        self.clear_bttn.grid(row = 3, column = 1, sticky = S)

        
        # create staff name label
        self.name_lbl = Label(self, text = "")
        
        # create first button
        self.FullChicken_bttn = Button(self)
        self.FullChicken_bttn["text"] = "FullChicken: 0"
        self.FullChicken_bttn["command"] = self.update_FullChicken
       
        

        # create second button
        self.BoerVoers_bttn = Button(self)
        self.BoerVoers_bttn["text"] = "BoerVoers: 0"
        self.BoerVoers_bttn["command"] = self.update_BoerVoers
        

        # create third button
        self.Steak_bttn = Button(self)
        self.Steak_bttn["text"] = "Steak: 0"
        self.Steak_bttn["command"] = self.update_Steak

        # create submit button
        self.submit_bttn = Button(self)
        self.submit_bttn["text"] = " Submit "
        self.submit_bttn["command"] = self.update_info

        # create logout button
        self.logout_bttn = Button(self)
        self.logout_bttn["text"] = "logout"
        self.logout_bttn["command"] = self.logout

        # create error label
        self.error_lbl = Label(self)
        self.error_lbl["text"] = ""
        

        # create label
        self.total_lbl = Label(self)
        self.total_lbl["text"] = "Total: R 0"
        

    def menu(self):
        """ Display menu. """
        staff = ["456", "457", "458"]
        staff_nr = self.staff_ent.get()
        if staff_nr == staff[0]:
            self.inst_lbl = Label(self, text = "")
            self.staff_lbl = Label(self, text = "")
            self.name_lbl = Label(self)
            self.name_lbl["text"] = "Thato"
            self.name_lbl.grid(row = 3, column = 0, sticky = W)
            self.FullChicken_bttn.grid(row = 5, column = 0, sticky = W)
            self.BoerVoers_bttn.grid(row = 6, column = 0, sticky = W)
            self.Steak_bttn.grid(row = 7, column = 0, sticky = W)
            self.total_lbl.grid(row = 8, column = 0, sticky = W)
            self.submit_bttn.grid(row = 10, column = 0, sticky = W)
            self.logout_bttn.grid(row = 3, column = 1, sticky = W)
            self.error_lbl["text"] = ""
            self.enter_bttn.destroy()
            
            
        elif staff_nr == staff[1]:
            self.inst_lbl = Label(self, text = "")
            self.staff_lbl = Label(self, text = "")
            self.name_lbl = Label(self)
            self.name_lbl["text"] = "Kenny"
            self.name_lbl.grid(row = 3, column = 0, sticky = W)
            self.FullChicken_bttn.grid(row = 5, column = 0, sticky = W)
            self.BoerVoers_bttn.grid(row = 6, column = 0, sticky = W)
            self.Steak_bttn.grid(row = 7, column = 0, sticky = W)
            self.total_lbl.grid(row = 8, column = 0, sticky = W)
            self.submit_bttn.grid(row = 10, column = 0, sticky = W)
            self.logout_bttn.grid(row = 3, column = 1, sticky = W)
            self.error_lbl["text"] = ""
            self.enter_bttn.destroy()
            
        elif staff_nr == staff[2]:
            self.inst_lbl = Label(self, text = "")
            self.staff_lbl = Label(self, text = "")
            self.name_lbl = Label(self)
            self.name_lbl["text"] = "Evans"
            self.name_lbl.grid(row = 3, column = 0, sticky = W)
            self.FullChicken_bttn.grid(row = 5, column = 0, sticky = W)
            self.BoerVoers_bttn.grid(row = 6, column = 0, sticky = W)
            self.Steak_bttn.grid(row = 7, column = 0, sticky = W)
            self.total_lbl.grid(row = 8, column = 0, sticky = W)
            self.submit_bttn.grid(row = 10, column = 0, sticky = W)
            self.logout_bttn.grid(row = 3, column = 1, sticky = W)
            self.error_lbl["text"] = ""
            self.enter_bttn.destroy()
            
        else:
            self.error_lbl["text"] = "Entry invalid!"
            self.error_lbl.grid(row = 9, column = 0, sticky = W)

    def clear(self):
        """ logging out. """
        self.FullChicken = 0.0
        self.BoerVoers = 0.0
        self.Steak = 0.0
        self.FullChicken_bttn_clicks = 0
        self.BoerVoers_bttn_clicks = 0
        self.Steak_bttn_clicks = 0
        self.FullChicken_bttn["text"] = "FullChicken: 0"
        self.BoerVoers_bttn["text"] = "BoerVoers: 0"
        self.Steak_bttn["text"] = "Steak: 0"
        self.total_lbl["text"] = "Total: R 0"
        self.error_lbl["text"] = ""
        

    def update_FullChicken(self):
        """ Update FullChicken. """
        self.FullChicken_bttn_clicks += 1
        self.FullChicken += 45
        self.FullChicken = self.FullChicken
        self.FullChicken_bttn["text"] = "FullChicken:  " + str(self.FullChicken_bttn_clicks)\
                             + "   =     R " + str(self.FullChicken)
        self.total_lbl["text"] = "Total: R "\
                            + str(self.FullChicken+self.BoerVoers+self.Steak)

    def update_BoerVoers(self):
        """ Update BoerVoers. """
        self.BoerVoers_bttn_clicks += 1
        self.BoerVoers += 40
        self.BoerVoers = self.BoerVoers
        self.BoerVoers_bttn["text"] = "BoerVoers:  " + str(self.BoerVoers_bttn_clicks)\
                             + "   =     R " + str(self.BoerVoers)
        self.total_lbl["text"] = "Total: R "\
                             + str(self.BoerVoers+self.Steak+self.FullChicken)

    def update_Steak(self):
        """ Update Steak. """
        self.Steak_bttn_clicks += 1
        self.Steak += 15
        self.Steak = self.Steak
        self.Steak_bttn["text"] = "Icecream:  " + str(self.Steak_bttn_clicks)\
                             + "   =     R " + str(self.Steak)
        self.total_lbl["text"] = "Total: R "\
                             + str(self.Steak+self.FullChicken+self.BoerVoers)

    def update_info(self):
        """ updating text info. """
        text_file = open("info.txt", "w")
        text_file.write(self.staff_ent.get())
        text_file.write("\n")
        text_file.write(str(self.Steak+self.FullChicken+self.BoerVoers))
        
    def logout(self):
        """ logging out. """
        self.FullChicken = 0.0
        self.BoerVoers = 0.0
        self.Steak = 0.0
        self.FullChicken_bttn_clicks = 0
        self.BoerVoers_bttn_clicks = 0
        self.Steak_bttn_clicks = 0
        self.FullChicken_bttn["text"] = "FullChicken: 0"
        self.BoerVoers_bttn["text"] = "BoerVoers: 0"
        self.Steak_bttn["text"] = "Steak: 0"
        self.total_lbl["text"] = "Total: R 0"
        self.error_lbl["text"] = ""
        self.name_lbl.grid_forget()
        self.FullChicken_bttn.grid_forget()
        self.BoerVoers_bttn.grid_forget()
        self.Steak_bttn.grid_forget()
        self.total_lbl.grid_forget()
        self.submit_bttn.grid_forget()
        self.logout_bttn.grid_forget()
        self.error_lbl.grid_forget()
        self.staff_ent.delete(0, END)
        self.enter_bttn = Button(self, text = " Enter ", command = self.menu)
        self.enter_bttn.grid(row = 3, column = 1, sticky = W)
        
   
# main
root = Tk()
root.title("Menu Selection")
root.geometry("380x400")
      
app = Application(root)
root.mainloop()


