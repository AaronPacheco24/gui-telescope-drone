from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QFileDialog,
)
from PySide6.QtGui import QPixmap
from PySide6.QtGui import Qt

import os

# globals
images_array = []
count = 0


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        # Create QLineEdit for directory path
        self.path_line_edit = QLineEdit()
        self.path_line_edit.setReadOnly(True)  # read-only

        # Button to open file dialog
        self.select_directory_label = QLabel("Select Directory:")
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.select_directory)

        self.setWindowTitle("Random")
        self.setFixedSize(800, 600)

        # Create a layout for path input
        path_layout = QHBoxLayout()
        path_layout.addWidget(self.select_directory_label)
        path_layout.addWidget(self.path_line_edit)
        path_layout.addWidget(self.browse_button)

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
        fin_layout.addLayout(path_layout)
        fin_layout.addWidget(self.images_label)
        fin_layout.addLayout(vlayout)
        self.setLayout(fin_layout)

    # Connections
    def next_button_clicked(self):
        global count, images_array
        count = count + 1
        if count >= len(images_array):
            count = 0
        self.update_image_label()  # Update the image label

    def prev_button_clicked(self):
        global count, images_array
        count = count - 1
        if count <= 0:
            count = len(images_array) - 1
        self.update_image_label()

    def select_directory(self):
        global images_array
        self.folder_dir = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.folder_dir:  # checks if a new directory was selected
            self.path_line_edit.setText(self.folder_dir)  # saves selected directory
            self.update_images_list()  # updates list with the new selected directory
            for images in os.listdir(
                self.path_line_edit.text()
            ):  # iterates through directory
                if (
                    images.endswith(".png")
                    or images.endswith(".jpg")
                    or images.endswith(".jpeg")
                ):
                    images_array.append(images)

            # print(self.images_array)  # Debug

    # Other methods
    def update_image_label(self):
        global images_array, count
        if images_array:  # Make sure the array has contents
            image_path = os.path.join(
                self.folder_dir, images_array[count]
            )  # Update picture
            pixmap = QPixmap(image_path)  # Handling image swap
            available_width = self.width()
            available_height = self.height()
            pixmap = pixmap.scaled(  # resize the image to fit in window
                available_width,
                available_height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.images_label.setPixmap(pixmap)
            self.images_label.setAlignment(Qt.AlignCenter)  # center the image

    def update_images_list(self):
        global images_array, count
        count = 0  # reset count so if new directory was selected it would display the first picture
        images_array = []  # reset images_array
        directory_path = self.path_line_edit.text()
        if directory_path:  # checks if directory was selected
            for images in os.listdir(directory_path):
                if (
                    images.endswith(".png")
                    or images.endswith(".jpg")
                    or images.endswith(".jpeg")
                ):
                    images_array.append(
                        images
                    )  # iterates through directory and adds images to images_array
            print(images_array)
            self.update_image_label()


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
