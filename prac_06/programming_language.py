# programming_language.py
class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance with name, typing, reflection, and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a formatted string representation of the ProgrammingLanguage."""
        return f"{self.name}, Dynamic Typing, Reflection={self.reflection}, First appeared in {self.year}"