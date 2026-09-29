# Day 21

class Statistics:

    def __init__ (self, data = None):

        data = data if data is not None else []

        self.count = len(data)
        self.sum = sum(data)
        self.min = min(data)
        self.max = max(data)
        self.range = self.max - self.min
        self.mean = self.sum / self.count
        self.median = 0
        self.var = sum((x - self.mean) ** 2 for x in data) / self.count
        self.std = self.var ** 0.5

        sorted_data = sorted(data)

        if self.count % 2 == 0:
            self.median = (sorted_data[self.count // 2] + sorted_data[self.count // 2 - 1])/2
        else:
            self.median = sorted_data[self.count // 2]

        counts = {}

        for value in data:
            counts[value] = counts.get(value, 0) + 1

        percentages = [(count / self.count * 100, value) for value, count in counts.items()]

        self.freq_dist = sorted(percentages, key = lambda x: x[0], reverse = True)
        self.mode = sorted(counts.items(), key = lambda x: x[1], reverse = True)[:1]

    def describe (self):

        print(f"Count: {self.count}")
        print(f"Sum: {self.sum}")
        print(f"Min: {self.min}")
        print(f"Max: {self.max}")
        print(f"Range: {self.range}")
        print(f"Mean: {self.mean}")
        print(f"Median: {self.median}")
        print(f"Mode: {self.mode}")
        print(f"Variance: {self.var}")
        print(f"Standard Deviation: {self.std}")
        print(f"Frequency Distribution: {self.freq_dist}")

class PersonAccount:

    def __init__ (self, firstname = "", lastname = "", incomes = None, expenses = None):

        self.fn = firstname
        self.ln = lastname
        self.incomes = incomes if incomes is not None else {}
        self.expenses = expenses if expenses is not None else {}

    def total_income (self):

        total = 0

        for income in self.incomes.values():
            total += income

        return total

    def total_expense (self):

        total = 0

        for expense in self.expenses.values():
            total += expense

        return total

    def account_info (self):
        return f"First name: {self.fn} \n Last name: {self.ln} \n Incomes: {self.incomes} \n Expenses: {self.expenses}"

    def add_income (self, income, context):
        self.incomes[context] = income

    def add_expense (self, expense, context):
        self.expenses[context] = expense

    def account_balance (self):
        return self.total_income() - self.total_expense()


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
data.describe()