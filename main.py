from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image, ImageGrab

# Create program window
window = Tk()
window.title('Watermark Program')
window.config(padx=40, pady=40)

canvas = Canvas(width=400, height=400)
can_text = canvas.create_text(220, 200, fill="black", font="Times 15 italic bold",
                       text="Upload an image to add this watermark: \n"
                            "                   Imbir's Photo")
canvas.grid(row= 0, column= 0, columnspan = 2)


# Upload an image with PIL and add watermark
def find_image():
    global image
    file_path = askopenfilename(title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
    im_size = Image.open(file_path).size
    while im_size[0] > 600 or im_size[1] > 600:
        im_size = (round(im_size[0]*0.9), round(im_size[1]*0.9))
    image = ImageTk.PhotoImage(Image.open(file_path).resize(im_size))
    canvas.config(width= im_size[0]+20, height= im_size[1]+20)
    canvas.create_image(im_size[0]/2, im_size[1]/2, image=image)
    canvas.create_text(90, im_size[1]-10, fill="blue", font="Times 20 italic bold",
                       text="Imbir's Photo")
    canvas.delete(can_text)

# Save image to chosen destination
def save_image():
    save = asksaveasfilename(defaultextension = '.jpg')
    box = (canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(),
           canvas.winfo_rooty() + canvas.winfo_height())
    grab = ImageGrab.grab(bbox=box)
    grab.save(save)

# Save and upload buttons
upload_button = Button(text="Upload Photo", command= find_image)
upload_button.grid(row=1, column=0)

save_button = Button(text="Save Photo", command = save_image)
save_button.grid(row=1, column=1)




window.mainloop()