from turtle import home


def add_time(timeNow, addTime, dayNow=None):
    time_lst = timeNow.split()
    hour_mini = converInteger(time_lst[0].split(":"))
    add_Time = converInteger(addTime.split(":"))
    hours_now = hour_mini[0]
    hours_add = add_Time[0]
    minitues_now = hour_mini[1]
    minitues_add = add_Time[1]
    if time_lst[1] == "AM":
        hours_later = hours_now + hours_add
    elif time_lst[1] == "PM":
        hours_later = hours_now + hours_add + 12
    if minitues_now + minitues_add >= 60:
        hours_later = hours_later + 1
        minitues_later = minitues_now + minitues_add - 60
    else:
        minitues_later = minitues_now + minitues_add
    num_day = hours_later // 24
    hours_later %= 24
    if hours_later < 12: time_lst[1] = "AM"
    else: time_lst[1] = "PM"
    hours_later %= 12
    if hours_later == 0: hours_later = 12
    result = f"{hours_later:02}:{minitues_later:02} {time_lst[1]}"
    if dayNow:
        day_week = ["monday","tuesday","wednesday","thursday",
                    "friday","saturday","sunday"]
        day_later_index = day_week.index(dayNow.lower())
        day_index = day_week[(day_later_index + num_day) % 7]
        result += f", {day_index.capitalize()}"
    if num_day == 1:
        result += " (next day)"
    elif num_day > 1:
        result += f" {num_day} day later"

    return result
def converInteger(arr):
    lstInt = []
    for i in arr:
        lstInt.append(int(i))
    return lstInt

if __name__=="__main__":
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))