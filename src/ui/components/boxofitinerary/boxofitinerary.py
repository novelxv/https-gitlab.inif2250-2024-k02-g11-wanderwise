from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class ClickableWidget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal(int)

    def __init__(self, index, parent=None):
        super().__init__(parent)
        self.index = index

    def mousePressEvent(self, event):
        self.clicked.emit(self.index)

class ScheduleWidget(QtWidgets.QWidget):
    def __init__(self, header, places, hours, itinerary_ids, parent=None):
        super().__init__(parent)
        self.itinerary_ids = itinerary_ids

        self.setFixedWidth(500)  # Change 300 to your desired width

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.setLayout(self.main_layout)

        # Header Tanggal
        self.header_label = QtWidgets.QLabel(header)
        self.header_label.setStyleSheet("""
            QLabel {
                background-color: #C36F0C;
                color: black;
                font-size: 35px;
                font-weight: bold;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
                border-top: 5px solid;
                border-left: 5px solid;
                border-right: 5px solid;
                padding-top: 10px;
                padding-left: 10px;
            }
        """)
        self.header_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.header_label.setFixedHeight(80)
        self.main_layout.addWidget(self.header_label)

        # Table widget
        self.table_widget = QtWidgets.QWidget()
        self.table_layout = QtWidgets.QVBoxLayout()
        self.table_layout.setContentsMargins(0, 0, 0, 0)
        self.table_layout.setSpacing(0)
        self.table_widget.setLayout(self.table_layout)
        self.table_widget.setStyleSheet("""
            QWidget {
                background-color: #FFF9ED;
                border-left: 5px solid;
                border-right: 5px solid;
            }
        """)
        self.main_layout.addWidget(self.table_widget)

        # Populate the table
        for i, (place, hour) in enumerate(zip(places, hours)):
            row_widget = ClickableWidget(i)
            row_layout = QtWidgets.QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            row_widget.setLayout(row_layout)

            place_label = QtWidgets.QLabel(place)
            hour_label = QtWidgets.QLabel(hour)
            place_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            hour_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            place_label.setWordWrap(True)
            hour_label.setWordWrap(True)
            place_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            hour_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

            if i % 2 == 0:
                row_widget.setStyleSheet("background-color: #FFE589; padding: 10px; margin: 0px; border-radius: 0px")
            else:
                row_widget.setStyleSheet("background-color: #FFC800; padding: 10px; margin: 0px; border-radius: 0px")
            row_layout.addWidget(place_label)
            row_layout.addWidget(hour_label)
            if i == len(places) - 1:
                row_widget.setStyleSheet(row_widget.styleSheet() + "; border-bottom: 5px solid; ")
            place_label.setStyleSheet("border-right: 0px solid; font: bold 25px;")
            hour_label.setStyleSheet("border-left: 0px solid; font: bold 25px;")
            self.table_layout.addWidget(row_widget)

            row_widget.clicked.connect(lambda index=i: self.handleRowClick(index))

    def handleRowClick(self, index):
        print("Clicked row:", index)
