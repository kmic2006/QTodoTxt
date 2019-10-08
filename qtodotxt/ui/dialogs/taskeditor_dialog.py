import sys
from PySide import QtGui
from qtodotxt.ui.dialogs.taskeditor_lineedit import TaskEditorLineEdit
from datetime import date, timedelta
import collections


class TaskEditorDialog(QtGui.QDialog):
    autocomplete_pairs = collections.OrderedDict([
        ('due:today', ''),
        ('due:1day', ''),
        ('due:2days', ''),
        ('due:3days', ''),
        ('due:4days', ''),
        ('due:5days', ''),
        ('due:6days', ''),
        ('due:7days', ''),
        ('due:8days', ''),
        ('due:9days', ''),
        ('due:10days', ''),
        ('due:11days', ''),
        ('due:12days', ''),
        ('due:13days', ''),
        ('due:14days', ''),
        ('due:15days', ''),
        ('due:16days', ''),
        ('due:17days', ''),
        ('due:18days', ''),
        ('due:19days', ''),
        ('due:20days', ''),
        
        ('due:1week', ''),
        ('due:2weeks', ''),
        ('due:3weeks', ''),
        ('due:4weeks', ''),
        ('due:5weeks', ''),
        ('due:6weeks', ''),
        ('due:7weeks', ''),
        ('due:8weeks', ''),
        
        ('due:1month', ''),
        ('due:2months', ''),
        ('due:3months', ''),
        ('due:4months', ''),
        ('due:5months', ''),
        ('due:6months', ''),
        ('due:7months', ''),
        ('due:8months', ''),
        ('due:9months', ''),
        ('due:10months', ''),
        ('due:11months', ''),
        ('due:12months', ''),
        
        ('due:1year', ''),
        ('due:2years', ''),
        ('due:3years', ''),

        
        ('t:today', ''),
        ('t:1day', ''),
        ('t:2days', ''),
        ('t:3days', ''),
        ('t:4days', ''),
        ('t:5days', ''),
        ('t:6days', ''),
        ('t:7days', ''),
        ('t:8days', ''),
        ('t:9days', ''),
        ('t:10days', ''),
        ('t:11days', ''),
        ('t:12days', ''),
        ('t:13days', ''),
        ('t:14days', ''),
        ('t:15days', ''),
        ('t:16days', ''),
        ('t:17days', ''),
        ('t:18days', ''),
        ('t:19days', ''),
        ('t:20days', ''),
        
        ('t:1week', ''),
        ('t:2weeks', ''),
        ('t:3weeks', ''),
        ('t:4weeks', ''),
        ('t:5weeks', ''),
        ('t:6weeks', ''),
        ('t:7weeks', ''),
        ('t:8weeks', ''),
        
        ('t:1month', ''),
        ('t:2months', ''),
        ('t:3months', ''),
        ('t:4months', ''),
        ('t:5months', ''),
        ('t:6months', ''),
        ('t:7months', ''),
        ('t:8months', ''),
        ('t:9months', ''),
        ('t:10months', ''),
        ('t:11months', ''),
        ('t:12months', ''),
        
        ('t:1year', ''),
        ('t:2years', ''),
        ('t:3years', ''),

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

    #def _endOfMonth(self, month):
        #month %= 12

        #eom = date.today().replace(month=month + 1, day=1) - timedelta(days=1)
        #if eom < date.today():
            #eom = eom.replace(year=eom.year + 1)
        #return eom.strftime('%Y-%m-%d')

    def _populateKeys(self, keys):
        today = date.today().strftime('%Y-%m-%d')
        tomorrow = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
        #EOW = (date.today() + timedelta((6 - date.today().weekday()) % 7)).strftime('%Y-%m-%d')
        #EOM = ((date.today().replace(day=1) +
                        #timedelta(days=32)).replace(day=1) -
                        #timedelta(days=1)).strftime('%Y-%m-%d')
        #EOY = (date.today().replace(year=date.today().year + 1, month=1, day=1) -
                        #timedelta(days=1)).strftime('%Y-%m-%d')

        #keys['due:Today'] = 'due:' + today
        #keys['due:Tomorrow'] = 'due:' + tomorrow
        #keys['due:EndOfWeek'] = 'due:' + EOW
        #keys['due:EndOfMonth'] = 'due:' + EOM
        #keys['due:EndOfYear'] = 'due:' + EOY
        #keys['due:January'] = 'due:' + self._endOfMonth(1)
        #keys['due:February'] = 'due:' + self._endOfMonth(2)
        #keys['due:March'] = 'due:' + self._endOfMonth(3)
        #keys['due:April'] = 'due:' + self._endOfMonth(4)
        #keys['due:May'] = 'due:' + self._endOfMonth(5)
        #keys['due:June'] = 'due:' + self._endOfMonth(6)
        #keys['due:July'] = 'due:' + self._endOfMonth(7)
        #keys['due:August'] = 'due:' + self._endOfMonth(8)
        #keys['due:September'] = 'due:' + self._endOfMonth(9)
        #keys['due:October'] = 'due:' + self._endOfMonth(10)
        #keys['due:November'] = 'due:' + self._endOfMonth(11)
        #keys['due:December'] = 'due:' + self._endOfMonth(12)


        keys['due:today'] = 'due:' + today
        keys['due:1day'] = 'due:' + tomorrow
        keys['due:2days'] = 'due:' + (date.today() + timedelta(days=2)).strftime('%Y-%m-%d')
        keys['due:3days'] = 'due:' + (date.today() + timedelta(days=3)).strftime('%Y-%m-%d')
        keys['due:4days'] = 'due:' + (date.today() + timedelta(days=4)).strftime('%Y-%m-%d')
        keys['due:5days'] = 'due:' + (date.today() + timedelta(days=5)).strftime('%Y-%m-%d')
        keys['due:6days'] = 'due:' + (date.today() + timedelta(days=6)).strftime('%Y-%m-%d')
        keys['due:7days'] = 'due:' + (date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        keys['due:8days'] = 'due:' + (date.today() + timedelta(days=8)).strftime('%Y-%m-%d')
        keys['due:9days'] = 'due:' + (date.today() + timedelta(days=9)).strftime('%Y-%m-%d')
        keys['due:10days'] = 'due:' + (date.today() + timedelta(days=10)).strftime('%Y-%m-%d')
        keys['due:11days'] = 'due:' + (date.today() + timedelta(days=11)).strftime('%Y-%m-%d')
        keys['due:12days'] = 'due:' + (date.today() + timedelta(days=12)).strftime('%Y-%m-%d')
        keys['due:13days'] = 'due:' + (date.today() + timedelta(days=13)).strftime('%Y-%m-%d')
        keys['due:14days'] = 'due:' + (date.today() + timedelta(days=14)).strftime('%Y-%m-%d')
        keys['due:15days'] = 'due:' + (date.today() + timedelta(days=15)).strftime('%Y-%m-%d')
        keys['due:16days'] = 'due:' + (date.today() + timedelta(days=16)).strftime('%Y-%m-%d')
        keys['due:17days'] = 'due:' + (date.today() + timedelta(days=17)).strftime('%Y-%m-%d')
        keys['due:18days'] = 'due:' + (date.today() + timedelta(days=18)).strftime('%Y-%m-%d')
        keys['due:19days'] = 'due:' + (date.today() + timedelta(days=19)).strftime('%Y-%m-%d')
        keys['due:20days'] = 'due:' + (date.today() + timedelta(days=20)).strftime('%Y-%m-%d')

        keys['due:1week'] = 'due:' + (date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        keys['due:2weeks'] = 'due:' + (date.today() + timedelta(days=14)).strftime('%Y-%m-%d')
        keys['due:3weeks'] = 'due:' + (date.today() + timedelta(days=21)).strftime('%Y-%m-%d')
        keys['due:4weeks'] = 'due:' + (date.today() + timedelta(days=28)).strftime('%Y-%m-%d')
        keys['due:5weeks'] = 'due:' + (date.today() + timedelta(days=35)).strftime('%Y-%m-%d')
        keys['due:6weeks'] = 'due:' + (date.today() + timedelta(days=42)).strftime('%Y-%m-%d')
        keys['due:7weeks'] = 'due:' + (date.today() + timedelta(days=49)).strftime('%Y-%m-%d')
        keys['due:8weeks'] = 'due:' + (date.today() + timedelta(days=56)).strftime('%Y-%m-%d')

        keys['due:1month'] = 'due:' + (date.today() + timedelta(days=30)).strftime('%Y-%m-%d')
        keys['due:2months'] = 'due:' + (date.today() + timedelta(days=60)).strftime('%Y-%m-%d')
        keys['due:3months'] = 'due:' + (date.today() + timedelta(days=90)).strftime('%Y-%m-%d')
        keys['due:4months'] = 'due:' + (date.today() + timedelta(days=120)).strftime('%Y-%m-%d')
        keys['due:5months'] = 'due:' + (date.today() + timedelta(days=150)).strftime('%Y-%m-%d')
        keys['due:6months'] = 'due:' + (date.today() + timedelta(days=180)).strftime('%Y-%m-%d')
        keys['due:7months'] = 'due:' + (date.today() + timedelta(days=210)).strftime('%Y-%m-%d')
        keys['due:8months'] = 'due:' + (date.today() + timedelta(days=240)).strftime('%Y-%m-%d')
        keys['due:9months'] = 'due:' + (date.today() + timedelta(days=270)).strftime('%Y-%m-%d')
        keys['due:10months'] = 'due:' + (date.today() + timedelta(days=300)).strftime('%Y-%m-%d')
        keys['due:11months'] = 'due:' + (date.today() + timedelta(days=330)).strftime('%Y-%m-%d')
        keys['due:12months'] = 'due:' + (date.today() + timedelta(days=360)).strftime('%Y-%m-%d')

        keys['due:1year'] = 'due:' + (date.today() + timedelta(days=365)).strftime('%Y-%m-%d')
        keys['due:2years'] = 'due:' + (date.today() + timedelta(days=2*365)).strftime('%Y-%m-%d')
        keys['due:3years'] = 'due:' + (date.today() + timedelta(days=3*365)).strftime('%Y-%m-%d')


        keys['t:today'] = 't:' + today
        keys['t:1day'] = 't:' + tomorrow
        keys['t:2days'] = 't:' + (date.today() + timedelta(days=2)).strftime('%Y-%m-%d')
        keys['t:3days'] = 't:' + (date.today() + timedelta(days=3)).strftime('%Y-%m-%d')
        keys['t:4days'] = 't:' + (date.today() + timedelta(days=4)).strftime('%Y-%m-%d')
        keys['t:5days'] = 't:' + (date.today() + timedelta(days=5)).strftime('%Y-%m-%d')
        keys['t:6days'] = 't:' + (date.today() + timedelta(days=6)).strftime('%Y-%m-%d')
        keys['t:7days'] = 't:' + (date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        keys['t:8days'] = 't:' + (date.today() + timedelta(days=8)).strftime('%Y-%m-%d')
        keys['t:9days'] = 't:' + (date.today() + timedelta(days=9)).strftime('%Y-%m-%d')
        keys['t:10days'] = 't:' + (date.today() + timedelta(days=10)).strftime('%Y-%m-%d')
        keys['t:11days'] = 't:' + (date.today() + timedelta(days=11)).strftime('%Y-%m-%d')
        keys['t:12days'] = 't:' + (date.today() + timedelta(days=12)).strftime('%Y-%m-%d')
        keys['t:13days'] = 't:' + (date.today() + timedelta(days=13)).strftime('%Y-%m-%d')
        keys['t:14days'] = 't:' + (date.today() + timedelta(days=14)).strftime('%Y-%m-%d')
        keys['t:15days'] = 't:' + (date.today() + timedelta(days=15)).strftime('%Y-%m-%d')
        keys['t:16days'] = 't:' + (date.today() + timedelta(days=16)).strftime('%Y-%m-%d')
        keys['t:17days'] = 't:' + (date.today() + timedelta(days=17)).strftime('%Y-%m-%d')
        keys['t:18days'] = 't:' + (date.today() + timedelta(days=18)).strftime('%Y-%m-%d')
        keys['t:19days'] = 't:' + (date.today() + timedelta(days=19)).strftime('%Y-%m-%d')
        keys['t:20days'] = 't:' + (date.today() + timedelta(days=20)).strftime('%Y-%m-%d')

        keys['t:1week'] = 't:' + (date.today() + timedelta(days=7)).strftime('%Y-%m-%d')
        keys['t:2weeks'] = 't:' + (date.today() + timedelta(days=14)).strftime('%Y-%m-%d')
        keys['t:3weeks'] = 't:' + (date.today() + timedelta(days=21)).strftime('%Y-%m-%d')
        keys['t:4weeks'] = 't:' + (date.today() + timedelta(days=28)).strftime('%Y-%m-%d')
        keys['t:5weeks'] = 't:' + (date.today() + timedelta(days=35)).strftime('%Y-%m-%d')
        keys['t:6weeks'] = 't:' + (date.today() + timedelta(days=42)).strftime('%Y-%m-%d')
        keys['t:7weeks'] = 't:' + (date.today() + timedelta(days=49)).strftime('%Y-%m-%d')
        keys['t:8weeks'] = 't:' + (date.today() + timedelta(days=56)).strftime('%Y-%m-%d')

        keys['t:1month'] = 't:' + (date.today() + timedelta(days=30)).strftime('%Y-%m-%d')
        keys['t:2months'] = 't:' + (date.today() + timedelta(days=60)).strftime('%Y-%m-%d')
        keys['t:3months'] = 't:' + (date.today() + timedelta(days=90)).strftime('%Y-%m-%d')
        keys['t:4months'] = 't:' + (date.today() + timedelta(days=120)).strftime('%Y-%m-%d')
        keys['t:5months'] = 't:' + (date.today() + timedelta(days=150)).strftime('%Y-%m-%d')
        keys['t:6months'] = 't:' + (date.today() + timedelta(days=180)).strftime('%Y-%m-%d')
        keys['t:7months'] = 't:' + (date.today() + timedelta(days=210)).strftime('%Y-%m-%d')
        keys['t:8months'] = 't:' + (date.today() + timedelta(days=240)).strftime('%Y-%m-%d')
        keys['t:9months'] = 't:' + (date.today() + timedelta(days=270)).strftime('%Y-%m-%d')
        keys['t:10months'] = 't:' + (date.today() + timedelta(days=300)).strftime('%Y-%m-%d')
        keys['t:11months'] = 't:' + (date.today() + timedelta(days=330)).strftime('%Y-%m-%d')
        keys['t:12months'] = 't:' + (date.today() + timedelta(days=360)).strftime('%Y-%m-%d')

        keys['t:1year'] = 't:' + (date.today() + timedelta(days=365)).strftime('%Y-%m-%d')
        keys['t:2years'] = 't:' + (date.today() + timedelta(days=2*365)).strftime('%Y-%m-%d')
        keys['t:3years'] = 't:' + (date.today() + timedelta(days=3*365)).strftime('%Y-%m-%d')

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
