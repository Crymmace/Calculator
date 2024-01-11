import functions as func
import PySimpleGUI as gui

button0 = gui.Button("0", button_color="Grey25", size=(2, 2), expand_x=True, expand_y=True)
button1 = gui.Button("1", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button2 = gui.Button("2", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button3 = gui.Button("3", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button4 = gui.Button("4", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button5 = gui.Button("5", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button6 = gui.Button("6", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button7 = gui.Button("7", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button8 = gui.Button("8", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button9 = gui.Button("9", button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)

add_button = gui.Button("+", font=16, expand_x=True, expand_y=True)
subtract_button = gui.Button("-", font=16, expand_x=True, expand_y=True)
divide_button = gui.Button("/", font=16, expand_x=True, expand_y=True)
multiply_button = gui.Button("*", font=16, expand_x=True, expand_y=True)
equals_button = gui.Button("=", font=16, expand_x=True, expand_y=True)

output_label = gui.Text(key="output", size=(20, 2), expand_x=True, expand_y=True)
exit_button = gui.Button("Exit", button_color="Red", size=(3, 1), expand_x=True, expand_y=True)

window = gui.Window("Calculator", layout=[[exit_button, output_label],
                                          [button7, button8, button9, divide_button],
                                          [button4, button5, button6, multiply_button],
                                          [button1, button2, button3, subtract_button],
                                          [button0, equals_button, add_button]],
                    size=(450, 450), resizable=True)
num = []
operator = ""
running_total = ""
x = ""
y = ""
while True:
    event, values = window.read()

    match event:
        case "1":
            num.append("1")
            window["output"].update(value=func.create_num(num))

        case "2":
            num.append("2")
            window["output"].update(value=func.create_num(num))

        case "3":
            num.append("3")
            window["output"].update(value=func.create_num(num))

        case "4":
            num.append("4")
            window["output"].update(value=func.create_num(num))

        case "5":
            num.append("5")
            window["output"].update(value=func.create_num(num))

        case "6":
            num.append("6")
            window["output"].update(value=func.create_num(num))

        case "7":
            num.append("7")
            window["output"].update(value=func.create_num(num))

        case "8":
            num.append("8")
            window["output"].update(value=func.create_num(num))

        case "9":
            num.append("9")
            window["output"].update(value=func.create_num(num))

        case "0":
            num.append("0")
            window["output"].update(value=func.create_num(num))

        case "+":
            if running_total == "":
                x = func.create_num(num)
                num.clear()
            operator = "+"

        case "-":
            if running_total == "":
                x = func.create_num(num)
                num.clear()
            operator = "-"

        case "*":
            if running_total == "":
                x = func.create_num(num)
                num.clear()
            operator = "*"

        case "/":
            if running_total == "":
                x = func.create_num(num)
                num.clear()
            operator = "/"

        case "=":
            y = func.create_num(num)
            num.clear()
            match operator:
                case "+":
                    if running_total == "":
                        result = func.addition(x, y)
                        window["output"].update(value=result)
                        running_total = result
                    else:
                        result = func.addition(running_total, y)
                        window["output"].update(value=result)
                case "-":
                    if running_total == "":
                        result = func.subtraction(x, y)
                        window["output"].update(value=result)
                    else:
                        result = func.subtraction(running_total, y)
                        window["output"].update(value=result)
                case "*":
                    if running_total == "":
                        result = func.multiplication(x, y)
                        window["output"].update(value=result)
                    else:
                        result = func.multiplication(running_total, y)
                        window["output"].update(value=result)
                case "/":
                    try:
                        if running_total == "":
                            result = func.division(x, y)
                            window["output"].update(value=result)
                        else:
                            result = func.division(running_total, y)
                            window["output"].update(value=result)
                    except ZeroDivisionError:
                        window["output"].update(value=func.get_zero_divide_message())

        case "Exit":
            break

window.close()
