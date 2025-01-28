class Employee:
    def __init__(
            self,
            designation: str = 'Developer',
            frontend: bool = False,
            backend: bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__(self):
        return '{}'.format(self.designation)

    def verifier(self):
        if self.frontend and self.backend:
            return "Fullstack"
        elif self.frontend:
            return "Frontend"
        elif self.backend:
            return "Backend"
        else:
            return "Not a developer"

if __name__ == '__main__':
    firstEmployee = Employee()

    print(firstEmployee.verifier())