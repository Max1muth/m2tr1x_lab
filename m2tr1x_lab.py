from random import randint


class M2tr1x:
    def __init__(self, n1, n2):  # n1 - number of line items; n2 - number of column items
        self.n1 = n1
        self.n2 = n2
        self.m2tr1x = list([randint(10, 100) for _ in range(n1)] for _ in range(n2))

    def show_matrix(self):
        return self.m2tr1x

    def change_lines(self, x1, x2):

        self.m2tr1x[x1], self.m2tr1x[x2] = self.m2tr1x[x2], self.m2tr1x[x1]

        return self.m2tr1x

    def change_columns(self, y1, y2):

        for i in range(self.n2):
            self.m2tr1x[i][y1], self.m2tr1x[i][y2] = self.m2tr1x[i][y2], self.m2tr1x[i][y1]

        return self.m2tr1x

    def operation(self, z1, z2, axis=0, operation="+", coefficient=1):

        if axis == 0:  # lines

            if operation == "+":
                for i in range(self.n1):
                    self.m2tr1x[z1][i] += coefficient * self.m2tr1x[z2][i]
                    self.m2tr1x[z1][i] = round(self.m2tr1x[z1][i], 2)

            if operation == "-":
                for i in range(self.n1):
                    self.m2tr1x[z1][i] -= coefficient * self.m2tr1x[z2][i]
                    self.m2tr1x[z1][i] = round(self.m2tr1x[z1][i], 2)

            if operation == "*" and coefficient == 1:
                for i in range(self.n1):
                    self.m2tr1x[z1][i] *= self.m2tr1x[z2][i]
                    self.m2tr1x[z1][i] = round(self.m2tr1x[z1][i], 2)

            if operation == "/" and coefficient == 1:
                for i in range(self.n1):
                    self.m2tr1x[z1][i] /= self.m2tr1x[z2][i]
                    self.m2tr1x[z1][i] = round(self.m2tr1x[z1][i], 2)

        if axis == 1:  # columns

            if operation == "+":
                for i in range(self.n2):
                    self.m2tr1x[i][z1] += coefficient * self.m2tr1x[i][z2]
                    self.m2tr1x[i][z1] = round(self.m2tr1x[i][z1], 2)

            if operation == "-":
                for i in range(self.n2):
                    self.m2tr1x[i][z1] -= coefficient * self.m2tr1x[i][z2]
                    self.m2tr1x[i][z1] = round(self.m2tr1x[i][z1], 2)

            if operation == "*" and coefficient == 1:
                for i in range(self.n2):
                    self.m2tr1x[i][z1] *= self.m2tr1x[i][z2]
                    self.m2tr1x[i][z1] = round(self.m2tr1x[i][z1], 2)

            if operation == "/" and coefficient == 1:
                for i in range(self.n2):
                    self.m2tr1x[i][z1] /= self.m2tr1x[i][z2]
                    self.m2tr1x[i][z1] = round(self.m2tr1x[i][z1], 2)

        return self.m2tr1x
