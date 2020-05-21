class Department:

    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee():
    def __init__(self, code, name, salary):
        # impedindo de instanciar a calsse Employee diretamente.
        if type(self) == Employee:
            raise TypeError('Nao instancie essa classe diretamente. Tente outra.')
        # protegendo os parqmetros da classe.
        self.__code = code
        self.__name = name
        self.__salary = salary
        self.hours = 8
    def calc_bonus(self):
        pass

    def get_hours(self):
        # torando nas horas como 8, por padrao.
        return 8

class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.code = code
        self.name = name
        self.salary = salary
        
        # protegendo o parametro departament.
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    # tornando a unica forma de acessar o departamento por um metodo get.
    def get_departament(self):
        return self.__departament.name

    # criando um metodo para alterar o departamento que fora utilizado no inicio.
    def set_departament(self, departament):
        self.__departament.name = departament.name

class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        # protegendo o parametro sales.
        self.__sales = 0
    # criando um metodo para retornar o parametro sales
    def get_sales(self):
        return self.__sales
    # criando um metodo para atualizar os valores de sales do funcionario vendedor.
    def put_sales(self, new_sales):
        self.__sales += new_sales

    # criando um metodo para calcular o bonus recebido por funcionarios vendedores.
    def calc_bonus(self):
        return self.__sales * 0.15
    # tornando a unica forma de acessar o departamento por um metodo get. 
    def get_departament(self):
        return self.__departament.name
    # criando um metodo para alterar o departamento que fora utilizado no inicio.
    def set_departament(self, departament):
        self.__departament.name = departament
#
