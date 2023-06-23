def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * 2 ** power
        power -= 1
    return decimal

def parse_function(func_str, variable_names):
    func_str = func_str.replace('!', 'not ')
    func_str = func_str.replace('*', ' and ')
    func_str = func_str.replace('+', ' or ')
    func_str = func_str.replace('(', '(')
    func_str = func_str.replace(')', ')')
    res = eval('lambda ' + ', '.join(variable_names) + ': ' + func_str)
    return res


def get_variable_names(func_str):
    variable_names = set()
    for char in func_str:
        if char.isalpha():
            variable_names.add(char)
    return sorted(variable_names)

def get_truth_table(func_str):
    variable_names = get_variable_names(func_str)
    table = []
    indexes = ""
    table.append(variable_names + [func_str])

    #print('| ' + ' | '.join(variable_names) + ' | ' + func_str + ' |')
    #print('|' + '-' * len(func_str) + '|' + '-' * (len(' | '.join(variable_names)) + 2) + '|')

    for var_values in [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]:
        var_values_dict = {name: bool(var_values[j]) for j, name in enumerate(variable_names)}
        result = parse_function(func_str, variable_names)(*var_values_dict.values())
        #print(result)
        printed_table = '| ' + ' | '.join(str(int(var_values_dict[name])) for name in variable_names) + ' | ' + str(int(result)) + ' |'
        row = [int(var_values_dict[name]) for name in variable_names] + [int(result)]
        table.append(row)
        indexes += str(int(result))
        #print(printed_table)
    #print(binary_to_decimal(indexes))
    return table


def get_sdnf(func_str):
    truth_table = get_truth_table(func_str)
    variable_names = truth_table[0][:-1]
    sdnf_terms = []

    for row in truth_table[1:]:
        if row[-1] == 1:
            sdnf_term = []
            for i, value in enumerate(row[:-1]):
                if value == 1:
                    sdnf_term.append(variable_names[i])
                else:
                    sdnf_term.append('~' + variable_names[i])
            sdnf_terms.append('(' + '&'.join(sdnf_term) + ')')

    sdnf = ' * '.join(sdnf_terms)
    return sdnf


def get_sknf(func_str):
    truth_table = get_truth_table(func_str)
    variable_names = truth_table[0][:-1]
    sknf_terms = []
    for row in truth_table[1:]:
        if row[-1] == 0:
            sknf_term = []
            for i, value in enumerate(row[:-1]):
                if value == 0:
                    sknf_term.append(variable_names[i])
                else:
                    sknf_term.append('~' + variable_names[i])
            sknf_terms.append('(' + '|'.join(sknf_term) + ')')

    sknf = ' & '.join(sknf_terms)
    return sknf


def get_decimal_sdnf(func_str):
    truth_table = get_truth_table(func_str)
    variable_names = truth_table[0][:-1]
    sdnf_terms = []

    for row in truth_table[1:]:
        if row[-1] == 1:
            sdnf_term = []
            for i, value in enumerate(row[:-1]):
                if value == 1:
                    sdnf_term.append(variable_names[i])
                else:
                    sdnf_term.append('~' + variable_names[i])
            sdnf_terms.append('(' + '&'.join(sdnf_term) + ')')

    decimal_sdnf = []
    for term in sdnf_terms:
        decimal_term = ''
        for i, name in enumerate(variable_names):
            if '~' + name in term:
                decimal_term += '0'
            else:
                decimal_term += '1'
        decimal_sdnf.append(int(decimal_term, 2))

    return decimal_sdnf


def get_decimal_sknf(func_str):
    truth_table = get_truth_table(func_str)
    variable_names = truth_table[0][:-1]
    sknf_terms = []

    for row in truth_table[1:]:
        if row[-1] == 0:
            sknf_term = []
            for i, value in enumerate(row[:-1]):
                if value == 0:
                    sknf_term.append(variable_names[i])
                else:
                    sknf_term.append('~' + variable_names[i])
            sknf_terms.append('(' + '|'.join(sknf_term) + ')')

    decimal_sknf = []
    for term in sknf_terms:
        decimal_term = ''
        for i, name in enumerate(variable_names):
            if '~' + name in term:
                decimal_term += '1'
            else:
                decimal_term += '0'
        decimal_sknf.append(int(decimal_term, 2))

    return decimal_sknf

def convert_scdnf(expr):
    return expr.replace(' * ', '+').replace('&', '∙').replace('~', '!').replace('|', '+').replace(' ', '')

#print(convert_scdnf(get_sknf("(a+b)*!c")))
#print(get_truth_table("(a+b)*(!a+c)"))
#print(get_sknf("(a+b)*(!a+c)"))
#print(get_sdnf("(a+b)*(!a+c)"))
#print(get_decimal_sdnf("(a+b)*(!a+c)"))
#print(get_decimal_sknf("(a+b)*(!a+c)"))
