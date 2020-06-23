# Business struct


businesses = []


def business_generator(name, employees, balance, product, salary, work_description):
    name = Business(name, employees, balance, product, salary, work_description)
    businesses.append(name)
    return name


class Business:
    def __init__(self, name, employees, balance, product, salary, work_description):
        self.name = name
        self.employee = employees
        self.balance = balance
        self.product = product
        self.salary = salary
        self.work_description = work_description
        self.employee_list = []
        self.storage_raw = 0
        self.storage_ready = 0
        self.import_source = []

    def hire(self, amount, population):
        count = 0
        for i in range(len(population)):
            if population[i].job == "no job" and count < amount:
                population[i].job = self.work_description
                population[i].salary = self.salary
                self.employee_list.append(population[i])
                count = count + 1

    # make salary payment work
    def pay_worker(self):
        for i in range(len(self.employee_list)):
            self.employee_list[i].money = self.employee_list[i].money + self.salary

    def fire(self, person_id):
        for i in range(len(self.employee_list)):
            if self.employee_list[i-1].identity == person_id:
                del self.employee_list[i-1]

    def resource_source(self, source):
        if source == "grass" or source == "water" or \
            source == "rock" or source == "corn" or source == "wheat":
            import environment
            for i in range(len(environment.land)):
                if source == environment.land[i].ground_type:
                    self.import_source.append(environment.land[i])
        else:
            for i in range(len(businesses)):
                if source == businesses[i].name:
                    self.import_source.append(businesses[i])

    def import_all_goods(self):
        for i in range(len(self.import_source)):
            self.storage_raw = self.storage_raw + self.import_source[i].storage_ready
            self.import_source[i].storage_ready = 0

    def productivity(self):
        if self.storage_raw > 0:
            if len(self.employee_list) <= self.storage_raw:
                self.storage_raw = self.storage_raw - len(self.employee_list)
                self.storage_ready = self.storage_ready + len(self.employee_list)
            else:
                self.storage_ready = self.storage_ready + self.storage_raw
                self.storage_raw = self.storage_raw - self.storage_raw


