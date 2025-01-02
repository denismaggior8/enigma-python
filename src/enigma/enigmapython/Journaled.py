class Journaled:

    journal = []

    def __init__(self):
        self.journal = []

    def append_to_journal(self, event):
        self.journal.append(event)