
class Memento:
    """
    Memento class for saving the data
    """

    def __init__(self, file, content):
        """put all your file content here"""

        self.file = file
        self.content = content

class FileWriterUtility:
    """
    It's a file writing utility
    """

    def __init__(self, file):
        """
        store the input file data
        """
        self.file = file
        self.content = ""

    def write(self, string):
        """
        Write the data into the file
        """
        self.content += string

    def save(self):
        """
        save the data into the Memento
        """
        return Memento(self.file, self.content)

    def undo(self, memento):
        """UNDO feature provided"""
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    """CareTaker for FileWriter"""

    def save(self, writer):
        """saves the data"""
        self.obj = writer.save()

    def undo(self, writer):
        """undo the content"""
        writer.undo(self.obj)


if __name__ == '__main__':
    """create the caretaker object"""
    caretaker = FileWriterCaretaker()

    """create the writer object"""
    writer = FileWriterUtility("GFG.txt")

    """write data into file using writer object"""
    writer.write("First vision of GeeksforGeeks\n")
    print(writer.content + "\n\n")

    """save the file"""
    caretaker.save(writer)

    """again write using the writer """
    writer.write("Second vision of GeeksforGeeks\n")

    print(writer.content + "\n\n")

    """undo the file"""
    caretaker.undo(writer)

    print(writer.content + "\n\n")
