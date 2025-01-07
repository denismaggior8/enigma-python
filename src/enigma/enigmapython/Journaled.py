class Journaled:

    journal = None

    def __init__(self):
        self.journal = []

    def append_to_journal(self, event):
        self.journal.append(event)

    def clear_journal(self):
        self.journal.clear()