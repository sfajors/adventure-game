# Import necessary libraries
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Adventure Game')
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')
        self.main_frame.configure(bg='#14193C')

        # Basic styling
        self.main_frame.configure(background='#14193C')
        self.font_style = ('Roboto', 15)
        
        self.intro_label = tk.Label(self.main_frame, text="", wraplength=500, font=self.font_style, bg='#14193C', fg='white', highlightthickness=0)
        self.intro_label.pack(pady=20)

        self.start_button = tk.Button(self.main_frame, text="Begin the Adventure", command=self.start_game, bg='white', fg='#3C3714', highlightbackground='#14193C', highlightthickness=10, font=self.font_style)
        self.start_button.pack(padx=0,pady=0, ipadx=10, ipady=10)

        # Load room images (You can replace these with your own images and paths)
        self.images = {
            "The Kitchen": ImageTk.PhotoImage(Image.open("images/kitchen.png")),
            "The Living Room": ImageTk.PhotoImage(Image.open("images/living-room.png")),
            "The Bedroom": ImageTk.PhotoImage(Image.open("images/bedroom.png")),
            "The Study": ImageTk.PhotoImage(Image.open("images/study.png")),
            "The Attic": ImageTk.PhotoImage(Image.open("images/attic.png")),
            "The Basement": ImageTk.PhotoImage(Image.open("images/basement.png")),
            "The Garage": ImageTk.PhotoImage(Image.open("images/garage.png")),
            "The Bathroom": ImageTk.PhotoImage(Image.open("images/bathroom.png"))
        }

        self.rooms = [
            "The Kitchen", "The Living Room", "The Bedroom",
            "The Study", "The Attic", "The Basement",
            "The Garage", "The Bathroom"
        ]
        self.treasure_room = random.choice(self.rooms)
        self.current_room = None


        self.room_image_label = tk.Label(self.main_frame, bg='#14193C')
        self.room_image_label.pack(pady=20)

        self.root.after(2000, self.display_intro)

    def display_intro(self):
        self.intro_label.config(text="You, and a group of friends, "
                                    "wait in line to enter a haunted house.\n"
                                    "Rumor has it, there is a hidden treasure "
                                    "in one of the rooms.\n"
                                    "You and your friends enter the haunted house, "
                                    "all starting in different rooms.")
        self.start_button.config(state="normal")

    def start_game(self):
        self.start_button.pack_forget()
        self.intro_label.config(text="Let's begin the game!")
        self.start_button.config(state="disabled")
        
        if self.current_room  == self.treasure_room:
            response = messagebox.askyesno("Hold on...", "You found the secret treasure... It's $7 billion, YOU\'RE RICH!\nDo you want to play again?")
            if response:
                self.reset_game()
                return
            else:
                self.root.destroy()
                return

        self.root.after(2000, self.display_room)

    def display_room(self):
        rooms = ['The Kitchen', 'The Living Room', 'The Bedroom', 'The Study', 'The Attic', 'The Basement', 'The Garage']
        self.current_room = random.choice(rooms)
        self.intro_label.config(text=f"You are in the {self.current_room}")

        # Update room image
        self.room_image_label.config(image=self.images.get(self.current_room))

        self.action_buttons()

    def action_buttons(self):
        self.interact_button = tk.Button(self.main_frame, text='Interact', command=self.interact, bg='white', fg='#3C3714', highlightbackground='#14193C', highlightthickness=10)
        self.interact_button.pack(padx=0,pady=0, ipadx=10, ipady=10)

        self.move_button = tk.Button(self.main_frame, text='Move', command=self.move, bg='white', fg='#3C3714', highlightbackground='#14193C', highlightthickness=10)
        self.move_button.pack(padx=0,pady=0, ipadx=10, ipady=10)

    def remove_action_buttons(self):
        self.interact_button.pack_forget()
        self.move_button.pack_forget()

    def interact(self):
        self.remove_action_buttons()
        if self.current_room  == "The Kitchen":
            self.intro_label.config(text="A sink full of greasy pots and pans glared at me accusingly. " 
                                    "\"Keep moving,\" they seemed to say. \"We're not going to wash " 
                                    "ourselves.\"")
        elif self.current_room  == "The Bedroom":
            self.intro_label.config(text="The bedroom was a sterile white cube, devoid of any personality. " 
                                    "The bed was a perfectly made rectangle, and the only decoration on the "
                                    "walls was a single framed photo of a faceless person. It was as if the "
                                    "room had been designed to be as uninteresting as possible.")
        elif self.current_room  == 'The Living Room':
            self.intro_label.config(text="The wind whistled through the cracks in the windows, sending a "
                                    "chill down my spine. It was as if the room was haunted by the ghosts "
                                    "of its past.")
        elif self.current_room  == "The Study":
            self.intro_label.config(text="The study was dimly lit by a single lamp, casting eerie shadows "
                                    "on the walls. The shelves were lined with old books, their leather "
                                    "bindings cracked and worn. The air was thick with the smell of dust and "
                                    "decay. It was as if the study was a portal to another time, a place where "
                                    "the secrets of the past were still waiting to be discovered.")
        elif self.current_room  == "The Attic":
            self.intro_label.config(text="The attic was a treasure trove of forgotten memories, filled with old "
                                    "furniture, clothes, and toys. The dust motes danced in the sunlight, as if "
                                    "they were trying to tell me a story. I wondered what secrets the old things held "
                                    "within them. Did they come to life when no one was around? Or was there something "
                                    "more sinister going on in the attic?")
        elif self.current_room  == "The Basement":
            self.intro_label.config(text="The basement was dark and creepy, with cobwebs hanging from the ceiling "
                                    "and creaking floorboards under my feet. The only sound was the dripping of water "
                                    "from a leaky pipe. I felt like I was being watched, but when I turned around, there "
                                    "was nothing but shadows.")
        elif self.current_room  == "The Garage":
            self.intro_label.config(text="In the corner of the garage sat a rusty old car, its once-sleek body now "
                                    "covered in cobwebs. Beside it was a workbench cluttered with tools, each one "
                                    "with its own story to tell. I wondered what treasures the garage had once held, "
                                    "and where they had gone.")
        else:
            self.current_room == "The Bathroom"
            self.intro_label.config(text="The bathroom reeked of stale urine and rotting flesh. The toilet bowl was "
                                    "a crusted-over cesspool, and the walls were covered in a thick layer of grime. "
                                    "I felt my stomach churn as I gagged at the stench.")
            return
        
        if self.current_room  == self.treasure_room:
            response = messagebox.askyesno("Hold on...", "You found the secret treasure... It's $7 billion, YOU\'RE RICH!\nDo you want to play again?")
            if response:
                self.reset_game()
                return
            else:
                self.root.destroy()
                return

        self.root.after(5000, self.display_room)

    
    def reset_game(self):
        # Randomize the treasure's location
        self.treasure_room = random.choice(self.rooms)
        
        # Reset current room
        self.current_room = None
        
        # Reset UI elements
        self.intro_label.config(text="You, and a group of friends, "
                                    "wait in line to enter a haunted house.\n"
                                    "Rumor has it, there is a hidden treasure "
                                    "in one of the rooms.\n"
                                    "You and your friends enter the haunted house, "
                                    "all starting in different rooms.")
        self.start_button.config(state="normal")
        self.start_button.pack(padx=0,pady=0, ipadx=10, ipady=10)
        self.room_image_label.config(image=None)

    def move(self):
        self.remove_action_buttons()
        self.display_room()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x500')
    game = AdventureGame(root)
    root.mainloop()