import sys
from PySide import QtGui
from qtodotxt.ui.dialogs.taskeditor_lineedit import TaskEditorLineEdit
from datetime import date, timedelta
import collections


class TaskEditorDialog(QtGui.QDialog):
    autocomplete_pairs = collections.OrderedDict([
        ('due:Today', ''),
        ('due:Tomorrow', ''),
        ('due:EndOfWeek', ''),
        ('due:EndOfMonth', ''),
        ('due:EndOfYear', ''),
        ('due:January', ''),
        ('due:February', ''),
        ('due:March', ''),
        ('due:April', ''),
        ('due:May', ''),
        ('due:June', ''),
        ('due:July', ''),
        ('due:August', ''),
        ('due:September', ''),
        ('due:October', ''),
        ('due:November', ''),
        ('due:December', ''),

        ('<br/>', '<br/>'),
        ('<b>', '<b>'),
        ('</b>', '</b>'),
        ('<i>', '<i>'),
        ('</i>', '</i>'),
        ('<s>', '<s>'),
        ('</s>', '</s>')
    ])

    def __init__(self, values, parent=None):
        super(TaskEditorDialog, self).__init__(parent)
        self._initUI(values)
        self._populateKeys(self.autocomplete_pairs)

    def _endOfMonth(self, month):
        month %= 12

        eom = date.today().replace(month=month + 1, day=1) - timedelta(days=1)
        if eom < date.today():
            eom = eom.replace(year=eom.year + 1)
        return eom.strftime('%Y-%m-%d')

    def _populateKeys(self, keys):
        today = date.today().strftime('%Y-%m-%d')
        tomorrow = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        EOW = (date.today() + timedelta((6 - date.today().weekday()) % 7)).strftime('%Y-%m-%d')
        EOM = ((date.today().replace(day=1) +
                        timedelta(days=32)).replace(day=1) -
                        timedelta(days=1)).strftime('%Y-%m-%d')
        EOY = (date.today().replace(year=date.today().year + 1, month=1, day=1) -
                        timedelta(days=1)).strftime('%Y-%m-%d')

        keys['due:Today'] = 'due:' + today
        keys['due:Tomorrow'] = 'due:' + tomorrow
        keys['due:EndOfWeek'] = 'due:' + EOW
        keys['due:EndOfMonth'] = 'due:' + EOM
        keys['due:EndOfYear'] = 'due:' + EOY
        keys['due:January'] = 'due:' + self._endOfMonth(1)
        keys['due:February'] = 'due:' + self._endOfMonth(2)
        keys['due:March'] = 'due:' + self._endOfMonth(3)
        keys['due:April'] = 'due:' + self._endOfMonth(4)
        keys['due:May'] = 'due:' + self._endOfMonth(5)
        keys['due:June'] = 'due:' + self._endOfMonth(6)
        keys['due:July'] = 'due:' + self._endOfMonth(7)
        keys['due:August'] = 'due:' + self._endOfMonth(8)
        keys['due:September'] = 'due:' + self._endOfMonth(9)
        keys['due:October'] = 'due:' + self._endOfMonth(10)
        keys['due:November'] = 'due:' + self._endOfMonth(11)
        keys['due:December'] = 'due:' + self._endOfMonth(12)

        return keys

    def _initUI(self, values):
        self.setWindowTitle("Task Editor")
        vbox = QtGui.QVBoxLayout()

        self._label = QtGui.QLabel("Task:")
        vbox.addWidget(self._label)

        self._edit = TaskEditorLineEdit(values, self.autocomplete_pairs)
        vbox.addWidget(self._edit)

        hbox = QtGui.QHBoxLayout()
        okButton = QtGui.QPushButton("Ok")
        okButton.clicked.connect(self.accept)
        cancelButton = QtGui.QPushButton("Cancel")
        cancelButton.clicked.connect(self.reject)
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def textValue(self):
        return self._edit.toPlainText()

    def setTextValue(self, text):
        self._edit.setPlainText(text)

    def setLabelText(self, text):
        self._label.setText(text)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    values = ['(A)', '(B)', '(C)', '@home', '@call', '@work', '+qtodotxt', '+sqlvisualizer']
    view = TaskEditorDialog(values)
    view.show()
    sys.exit(app.exec_())
