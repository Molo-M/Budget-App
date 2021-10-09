class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.balance = 0
        self.input = 0
        self.outgoing = 0

    def deposit(self, amount, description=''):
        depo_transit = dict()
        depo_transit['amount'] = amount
        depo_transit['description'] = description
        self.ledger.append(depo_transit)
        self.input += amount
        return 'Amount and Description have been deposited in Ledger.'

    def withdraw(self, amount, description=''):
        if amount < self.input:
            withdraw_transit = dict()
            withdraw_transit['amount'] = - + amount
            withdraw_transit['description'] = description
            self.ledger.append(withdraw_transit)
            self.outgoing += amount
            return True
        else:
            return False

    def get_balance(self):
        for a in self.ledger:
            self.balance += a['amount']
        return self.balance

    def transfer(self, amount, budget_category):
        if amount < self.input:
            self.withdraw(amount, f'Transfer to {budget_category.name}')
            budget_category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        self.get_balance()
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self):
        display = ''

        # Calculating length and title
        title = self.name
        length = (30 - len(title))/2
        length = str(length)
        l1 = length.split('.')
        if l1[1] == '5':
            length = float(length)
            l_length = int(length - 0.5)
            r_length = int(length + 0.5)
        else:
            length = float(length)
            l_length = int(length)
            r_length = int(length)
        left = '*' * l_length
        right = '*' * r_length
        title_line = left + title + right

        # Displaying Ledger
        ledge_line = ''
        for stuff in self.ledger:
            money = float(stuff['amount'])
            money = "{:.2f}".format(money)
            money = str(money)
            descr = stuff['description']
            space = (30 - len(money) - len(descr))
            limit = (29 - len(money))
            if len(descr) > limit:
                descr = descr[:limit] + ' '
            nw_line = descr + ' ' * space + money + '\n'
            ledge_line += nw_line

        # Displaying Total
        self.get_balance()
        total = self.balance
        total = "{:.2f}".format(total)
        total = str(total)
        total_line = 'Total:' + ' ' + total

        # Making final display
        display += title_line + '\n' + ledge_line + total_line
        return display


def create_spend_chart(categories):
    # Making Y-xis of chart
    fst, scnd, thrd, frth, ffth, sx, svn, eght, nne, tn = '100|', ' 90|', ' 80|', ' 70|', \
                                                          ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|'
    lines = [fst, scnd, thrd, frth, ffth, sx, svn, eght, nne, tn]
    lines.reverse()

    length = list()
    plot = list()
    withdraw = 0
    axis = 0
    pos = 0
    run = 0
    obj_val = list()
    label = list()

    chart = 'Percentage spent by category' + '\n'

    for cat in categories:
        withdraw += cat.outgoing
        length.append(len(cat.name))
        run += 1

    # Calculating percentage
    for cat in categories:
        if cat.input != 0:
            percentage = (cat.outgoing/withdraw) * 100
            r_percentage = str(round(percentage))
        else:
            percentage = 100
            r_percentage = str(round(percentage))

        # Rounding off percentage to nearest ten
        r_percentage = list(r_percentage)
        if len(r_percentage) == 2:
            p1 = int(r_percentage[0])
            p2 = int(r_percentage[1])
            if p2 > 4:
                p1 += 1
                p1 = str(p1)
                p2 = str(0)
            else:
                p1 = str(p1)
                p2 = str(0)
            r_percentage = p1 + p2
            obj_val.append(int(r_percentage))
        elif len(r_percentage) == 3:
            r_percentage = 100
            obj_val.append(int(r_percentage))
        else:
            p1 = int(r_percentage[0])
            obj_val.append(p1)

    # Making Chart
    while True:
        line = ''
        label_line = ''
        k = ''
        m = ''

        # Plotting on the chart
        for obj in obj_val:
            if obj != obj_val[0]:
                if obj >= axis:
                    k += 'o  '
                else:
                    k += '   '
            else:
                if obj >= axis:
                    k += ' o  '
                else:
                    k += '    '

        # Making the chart display
        if axis == 0:
            line += '  ' + (str(axis)) + '|' + k + '\n'
            line += '    ' + '-' * (3 * len(obj_val) + 1)
        elif axis == 100:
            line += (str(axis)) + '|' + k
        elif 0 < axis < 100:
            line += ' ' + (str(axis)) + '|' + k
        elif axis > 100:
            for cat in categories:
                if cat != categories[0]:
                    if pos < len(cat.name):
                        cat = list(cat.name)
                        m += cat[pos] + '  '
                    else:
                        m += '   '
                else:
                    if pos < len(cat.name):
                        cat = list(cat.name)
                        m += ' ' + cat[pos] + '  '
                    else:
                        m += '    '
            if pos == max(length):
                break
            pos += 1
            print(m)
            label_line += '    ' + m
        plot.append(line)
        label.append(label_line)
        axis += 10

    plot.reverse()
    for pl in plot:
        if pl == '':
            del pl
        else:
            chart += pl + '\n'

    for lb in label:
        if lb == '':
            del lb
        else:
            chart += lb + '\n'

    chart = chart.strip()
    chart += '  '
    return chart


food = Category("Food")
entertainment = Category('Entertainment')
business = Category('Business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))
