from contants import RESULTS_TXT_LOCATION


def get_lowest_number_from_list(list):
    return min(list)


def get_higher_number_from_list(list):
    return max(list)


def convert_string_price_to_float(string):
    value_without_unit = string.replace('£', '')
    value_with_dot = value_without_unit.replace(',', '.')
    return float(value_with_dot)


def convert_float_to_string_price(float):
    value = '%.3f' % float  # Set value with 3 decimal values
    value_with_unit = '£'+str(value)
    return value_with_unit


def save_results_to_txt_file(list_floats):
    f = open(RESULTS_TXT_LOCATION, mode="w", encoding="utf-8")
    f.write(f'Highest result = {convert_float_to_string_price(get_higher_number_from_list(list_floats))}\n')
    f.write(f'Lowest result = {convert_float_to_string_price(get_lowest_number_from_list(list_floats))}\n')
    f.close()