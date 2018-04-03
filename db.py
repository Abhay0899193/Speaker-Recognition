from tkinter import *
from PIL import Image, ImageTk

class speaker_recog:
       def __init__(self, name):
              root = Toplevel()
              root.title("Speaker Recognition(result)")
              width = root.winfo_screenwidth()
              height = root.winfo_screenheight()
              root.geometry("%dx%d" % (width, height))
              root.state('zoomed')
              

              ## Resizable Image

              image = Image.open('bggif/6.gif')
              global copy_of_image
              copy_of_image = image.copy()
              photo = ImageTk.PhotoImage(image)
              global label
              label = Label(root, image=photo)
              label.place(x=0, y=0, relwidth=1, relheight=1)
              label.bind('<Configure>', self.resize_image)

              user_name = Label(root, text=name,  font=("Helvetica",35,'bold italic'), bg='black', fg='white')
              user_name.place(relx=0.1, rely=0.2)
              
              photo = PhotoImage(file="docu/gify doc/"+str(name)+".gif")
              user_image = Label(root, image=photo, anchor='n')
              user_image.image = photo
              user_image.place(relx=0.7, rely=0.1, width=250,height=300)

              desc_path = "docu/"+str(name)+".txt"
              desc_file = open(desc_path,'r', encoding="utf-8")
              user_description = Label(root, text=desc_file.read(), wraplength= 1200, justify=LEFT, font=("Courier",18), bg='black', fg='white')
              user_description.place(relx=0.1, rely=0.75, anchor='w')
              root.mainloop()
       ## Function for resizing the Image

       def resize_image(self,event):
              new_width = event.width
              new_height = event.height
              global copy_of_image
              image = copy_of_image.resize((new_width, new_height))
              global photo
              photo = ImageTk.PhotoImage(image)
              global label
              label.config(image = photo)
              label.image = photo

def recog(name):
       b = speaker_recog(name)



#c = speaker_recog('rajat SHARMA')
#d = speaker_recog('pm narendra MODI')
#d = speaker_recog('pm narendra MODI')
#E = speaker_recog('Abhay Pratap Singh')


