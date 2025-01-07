class Journaled:

    journal = []

    def __init__(self):
        self.clear_journal()

    def append_to_journal(self, event):
        self.journal.append(event)

    def clear_journal(self):
        self.journal = []