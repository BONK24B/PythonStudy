from datetime import datetime as dt

def result_logger(data_a, data_b, data_c, data_d):
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f"{time};{data_a} {data_b} {data_c} = {data_d}")
        file.write("\n")

def error_log():
    time = dt.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write(f"{time};Error")