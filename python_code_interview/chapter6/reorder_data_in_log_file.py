logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]


def reorder_data(log: list[str]) -> list[str]:
    letter, digit = [], []
    
    for log_data in log:
        number_filter: bool = log_data.split(" ")[1].isdigit()
        if number_filter:
            digit.append(log_data)
        else:
            letter.append(log_data)

    letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letter + digit


 
print(reorder_data(logs))