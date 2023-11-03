from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from PySide6.QtGui import QPixmap
import os

images_array = []
count = 0

folder_dir = "C:/Users/aaron/gui_telescope_drone/gui-telescope-drone/images"  # Config to your path....
for images in os.listdir(folder_dir):  # Iterates through and finds all images
    if images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg"):
        images_array.append(images)  # Adds them to  a list

print(images_array)  # Debug


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random")

        self.images_label = QLabel()
        self.update_image_label()  # Initialize the label with the first image

        next_button = QPushButton("Next")
        prev_button = QPushButton("Previous")
        # Connections
        next_button.clicked.connect(self.next_button_clicked)  # Go to next image.
        prev_button.clicked.connect(self.prev_button_clicked)
        # Layout
        vlayout = QHBoxLayout()
        vlayout.addWidget(prev_button)
        vlayout.addWidget(next_button)
        # vlayout.addWidget(self.images_label)
        fin_layout = QVBoxLayout()
        fin_layout.addWidget(self.images_label)
        fin_layout.addLayout(vlayout)
        self.setLayout(fin_layout)

    # Connections
    def next_button_clicked(self):
        global count
        count = count + 1
        if count >= len(images_array):
            count = 0
        self.update_image_label()  # Update the image label

    def prev_button_clicked(self):
        global count
        count = count - 1
        if count <= 0:
            count = len(images_array) - 1
        self.update_image_label()

    # Other methods
    def update_image_label(self):
        if images_array:  # Make sure the array has conotents
            image_path = os.path.join(folder_dir, images_array[count])  # Update picture
            pixmap = QPixmap(image_path)  # Handling image swap
            self.images_label.setPixmap(pixmap)
            self.images_label.setScaledContents(
                True
            )  # Ensure the image scales properly


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
