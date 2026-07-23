"""
Multiple inheritance allows a class to inherit from more than one parent class.
Python uses multiple inheritance extensively through mixins — small
classes that provide a specific capability. Rather than building huge
inheritance hierarchies, Python code often combines multiple focused
behaviors into a single class.

Multiple inheritance becomes manageable because Python's MRO provides a
deterministic method lookup order. Inheritance allows a class to inherit from
more than one parent class.
"""


class SaveMixin:

    def save(self):
        print(f"Saving '{self.title}'")


class ExportMixin:

    def export_pdf(self):
        print(f"Exporting '{self.title}' to PDF")


class ModificationTrackingMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.modified = False

    def mark_modified(self):
        self.modified = True

    def show_status(self):
        print(f"Modified: {self.modified}")


class Document(SaveMixin, ExportMixin, ModificationTrackingMixin):
    def __init__(self, title):
        super().__init__()
        self.title = title


def main():
    print(Document.mro())
    doc = Document("Project Proposal")

    doc.show_status()

    doc.mark_modified()

    doc.show_status()

    doc.save()

    doc.export_pdf()


if __name__ == "__main__":
    main()
