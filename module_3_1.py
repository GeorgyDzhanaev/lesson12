calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(strings):
    count_calls()
    length = len(strings)
    upper_case = strings.upper()
    lower_case = strings.lower()
    return (length,upper_case,lower_case)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)


