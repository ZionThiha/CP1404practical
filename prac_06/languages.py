class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == 'dynamic'

java = ProgrammingLanguage('Java', 'Static', 'Yes', 1995)
python = ProgrammingLanguage('Python', 'Dynamic', 'Yes', 1991)

print(java.is_dynamic())
print(python.is_dynamic())