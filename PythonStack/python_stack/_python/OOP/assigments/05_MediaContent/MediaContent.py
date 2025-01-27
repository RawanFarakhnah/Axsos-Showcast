#Inheritance and Polymorphism
#PARENT (base) class
class MediaContent:
    def __init__(self, title, size, extention):
        self.title = title
        self.size = size
        self.extention = extention
    
    def display(self):
        print("Call PARENT display function!!")

#CHILD (driver) class
class Audio(MediaContent):
    def __init__(self, title, size, extention, duration):
        super().__init__(title, size, extention)
        self.duration = duration # Specific to Audio
    
    def display(self):
        print("Displaying audio!!")

#CHILD (driver) class
class Video(MediaContent):
    pass
 
    #This is the overridden display function in the child class.
    def display(self):
        print("Displaying video!!")

#CHILD (driver) class
class Image(MediaContent):
    def __init__(self, title, size, extention):
        super().__init__(title, size, extention)

    def display(self):
        print("Displaying image!")

#Creating Objects
video1 = Video("Any Video", 150, "mp4")
audio1 = Audio("Any Audio", 50, "png", "1 min")
image1 = Image("Any Image", 2, "png")

#Polymorphism
for obj in (video1, audio1, image1):
    obj.display()
