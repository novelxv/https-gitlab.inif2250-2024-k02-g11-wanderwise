from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QWidget, QScrollArea, QFrame
from src.ui.components.addbutton.addbutton import FloatingAddButton
from src.ui.components.ovalbutton.ovalbutton import OvalButtonIcon
from src.ui.components.destinationscard.destinationscard import *
from src.ui.pages.form_add_destination import FormAddDestination
from src.ui.components.backbutton.backbutton import BackButton
import sys
from PyQt5.QtCore import Qt

class ListOfDestinations(QWidget):
    def __init__(self, destinations, main_window=None):
        super().__init__(main_window)
        self.main_window = main_window
        self.destinations = destinations
        self.stacked_widget = main_window.stacked_widget

        # Main window size
        main_window_width = main_window.width()
        main_window_height = main_window.height()

        # Set the size of the widget
        self.setFixedWidth(main_window_width)
        self.setFixedHeight(main_window_height)

        # Create a main layout for the central widget
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 40, 80, 0)  # Adjust margins to create space on the sides

        # Header layout to hold back button and header labels
        self.header_layout = QHBoxLayout()
        self.main_layout.addLayout(self.header_layout)

        # BACK BUTTON
        self.back_button = BackButton()
        self.header_layout.addWidget(self.back_button, alignment=Qt.AlignRight)

        # Add header ITINERARY label
        self.header_itinerary_label = QLabel("ALL DESTINATIONS")
        self.header_itinerary_label.setStyleSheet("""
            QLabel {
                font: bold 35px;
                text-align: left;
                color: #000080;
                background: none;
            }
        """)
        self.header_layout.addWidget(self.header_itinerary_label)

        self.header_layout.addStretch()  # Add stretch to push the header label to the left

        # Create a layout for the buttons
        idea_button = OvalButtonIcon("Idea", None, "#C5E5C0", 40)
        plan_button = OvalButtonIcon("Plan", None, "#FFCF52", 40)
        booked_button = OvalButtonIcon("Booked", None, "#FF5D00", 40)
        done_button = OvalButtonIcon("Done", None, "#00A6FF", 40)

        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(15)  # Set spacing between buttons

        buttons_layout.addWidget(idea_button)
        buttons_layout.addWidget(plan_button)
        buttons_layout.addWidget(booked_button)
        buttons_layout.addWidget(done_button)

        # Create a container for the buttons
        buttons_container = QWidget()
        buttons_container.setLayout(buttons_layout)
        buttons_container.setContentsMargins(0, 0, 150, 0)  # Add right margin to prevent cutting off

        # Add the buttons container to the header layout
        self.header_layout.addWidget(buttons_container)

        # Add a blue line divider
        self.divider_line = QFrame()
        self.divider_line.setFrameShape(QFrame.HLine)
        self.divider_line.setFrameShadow(QFrame.Sunken)
        self.divider_line.setStyleSheet("color: #005A6D; background-color: #005A6D; height: 2px; border-radius: 5px;")
        self.main_layout.addWidget(self.divider_line)

        # Scroll area setup
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        # Scroll content layout
        self.grid_layout = QtWidgets.QGridLayout(scroll_content)
        self.grid_layout.setHorizontalSpacing(60)  # Set horizontal spacing between cards
        self.grid_layout.setVerticalSpacing(30)    # Set vertical spacing between cards
        self.grid_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Populate the grid layout with destination cards
        for index, destination in enumerate(self.destinations):
            icon_path = "img/icons/destination.jpg"
            text = destination  
            width = 400  # Set the width for each card
            card = CustomButton(icon_path, text, width)
            row = index // 3
            col = index % 3
            self.grid_layout.addWidget(card, row, col)
            card.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.main_layout.addWidget(scroll_area)

        # Create and add footer
        self.footer_label = QLabel("")
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setFixedHeight(125)  # Adjust the height of the footer as needed
        self.main_layout.addWidget(self.footer_label)

        # Add the floating add button
        self.add_button = FloatingAddButton(self, position=(157, 170))
        self.add_button.clicked.connect(self.show_add_destination_form)
        self.add_button.setFloatingPosition()  # Ensure it is positioned correctly
        self.setStyleSheet("background: transparent; border:none;")

    def show_add_destination_form(self):
        self.add_destination_form = FormAddDestination(self)
        self.add_destination_form.done_signal.connect(self.on_done_signal)
        self.add_destination_form.setWindowModality(Qt.ApplicationModal)
        self.add_destination_form.setGeometry(40, 80, 800, 600)  # Set fixed size and position
        self.add_destination_form.show()

    def on_done_signal(self):
        print("Done adding destination")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.setFixedSize(800, 600)  # Example size for the main window
    destinations = ["Bandung", "Semarang", "Makassar", "Jakarta", "Surabaya", "Blitar"]  # Example destinations list
    widget = ListOfDestinations(destinations, main_window)
    main_window.setCentralWidget(widget)
    main_window.show()
    sys.exit(app.exec_())
