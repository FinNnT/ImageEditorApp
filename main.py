from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QRadioButton, QMessageBox, QTextEdit, QListWidget, QLineEdit, QInputDialog, QFileDialog
from PyQt5.QtGui import QFont, QPixmap
import os

from PIL import Image, ImageFilter, ImageEnhance

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.open()
    def open(self):
        self.img = Image.open(self.filename)
        self.showImageQLabel(self.filename)
    def showImageQLabel(self,filename):
        pixmap_image = QPixmap(filename)
        w = label_image.width()
        h = label_image.height()
        pixmap_image = pixmap_image.scaled(w,h, Qt.KeepAspectRatio)
        label_image.setPixmap(pixmap_image)
    def get_result_name(self,action):
        name = self.filename.split(".")[0]
        ext = self.filename.split(".")[1]
        result = name + "_" + action + "." + ext
        return result
    def do_gray(self):
        img_edit = self.img.convert("L")
        # img_edit.show()
        img_name = self.get_result_name("gray")
        img_edit.save(img_name)
        self.showImageQLabel(img_name)
    def do_blur(self):
        img_edit = self.img.filter(ImageFilter.BLUR)
        # img_edit.show()
        img_name = self.get_result_name("blur")
        img_edit.save(img_name)
        self.showImageQLabel(img_name)
    def do_left(self):
        img_edit = self.img.transpose(Image.ROTATE_90)
        # img_edit.show()
        img_name = self.get_result_name("left")
        img_edit.save(img_name)
        self.showImageQLabel(img_name)
    def do_right(self):
        img_edit = self.img.transpose(Image.ROTATE_270)
        # img_edit.show()
        img_name = self.get_result_name("right")
        img_edit.save(img_name)
        self.showImageQLabel(img_name)
    def do_mirror(self):
        img_edit = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        # img_edit.show()
        img_name = self.get_result_name("mirror")
        img_edit.save(img_name)
        self.showImageQLabel(img_name)
    def do_sharpness(self):
        enhance_obj = ImageEnhance.Contrast(self.img)
        img_edit = enhance_obj.enhance(1.5)
        # img_edit.show()
        img_name = self.get_result_name("sharpness")
        img_edit.save(img_name)
        self.showImageQLabel(img_name)

app = QApplication([])

main_win = QWidget()
main_win.show()
main_win.setWindowTitle("Winner ..")
main_win.resize(1500, 700)

layout_main = QHBoxLayout()
main_win.setLayout(layout_main)

# left
layout_left = QVBoxLayout()
layout_main.addLayout(layout_left, stretch= 2)

layout_top_left = QVBoxLayout()
layout_left.addLayout(layout_top_left)
button_folder = QPushButton("Folder")
layout_left.addWidget(button_folder)

list_note = QListWidget()
layout_left.addWidget(list_note)

# right
layout_right = QVBoxLayout()
layout_main.addLayout(layout_right, stretch= 1)

label_image = QLabel("image")
layout_right.addWidget(label_image)

buttons_right = QHBoxLayout()
layout_right.addLayout(buttons_right)

button_left = QPushButton("Left")
buttons_right.addWidget(button_left)

button_right = QPushButton("Right")
buttons_right.addWidget(button_right)

button_mirror = QPushButton("Mirror")
buttons_right.addWidget(button_mirror)

button_sharp = QPushButton("Sharpness")
buttons_right.addWidget(button_sharp)

button_gray = QPushButton("Gray")
buttons_right.addWidget(button_gray)

button_blur = QPushButton("Blur")
buttons_right.addWidget(button_blur)

def select_folder():
    dir = QFileDialog.getExistingDirectory()
    files = os.listdir(dir)
    img_files = []
    for f in files:
        if ".jpg" in f:
                img_files.append(f)
    list_note.clear()
    list_note.addItems(img_files)

button_folder.clicked.connect(select_folder)

def select_image():
    img_name = list_note.selectedItems()[0].text()
    global editor_obj
    editor_obj = ImageEditor(img_name) 
list_note.itemClicked.connect(select_image)

def right():
    global editor_obj
    editor_obj.do_right()
button_right.clicked.connect(right)   

def left():
    global editor_obj
    editor_obj.do_left()
button_left.clicked.connect(left)

def mirror():
    global editor_obj
    editor_obj.do_mirror()
button_mirror.clicked.connect(mirror)

def sharpness():
    global editor_obj
    editor_obj.do_sharpness()
button_sharp.clicked.connect(sharpness)

def gray():
    global editor_obj
    editor_obj.do_gray()
button_gray.clicked.connect(gray)

def blur():
    global editor_obj
    editor_obj.do_blur()
button_blur.clicked.connect(blur)

app.exec_()