import View
import model
import logger

def button_click():
    result = 0

    value_a = View.get_value()
    value_b = View.get_operation()
    value_c = View.get_value()
    model.init(value_a, value_c)

    if value_b == "+":
        result = model.sum()
        View.print_data(result)
        logger.result_logger(value_a, value_b, value_c, result)
    elif value_b == "-":
        result = model.sub()
        View.print_data(result)
        logger.result_logger(value_a, value_b, value_c, result)
    elif value_b == "*":
        result = model.mult()
        View.print_data(result)
        logger.result_logger(value_a, value_b, value_c, result)
    elif value_b == "/":
        if value_c == 0:
            View.print_data("You can't divide by 0")
        else:
            result = model.div()
            View.print_data(result)
            logger.result_logger(value_a, value_b, value_c, result)
    else:
        View.print_data("Error")
        logger.error_log()

    