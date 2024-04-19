import functions as func
import PySimpleGUI as gui

button0 = gui.Button("0", font=16, button_color="Grey25", size=(2, 2), expand_x=True, expand_y=True)
button1 = gui.Button("1", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button2 = gui.Button("2", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button3 = gui.Button("3", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button4 = gui.Button("4", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button5 = gui.Button("5", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button6 = gui.Button("6", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button7 = gui.Button("7", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button8 = gui.Button("8", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
button9 = gui.Button("9", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)
decimal_button = gui.Button(".", font=16, button_color="Gray25", size=(2, 2), expand_x=True, expand_y=True)

clear_button = gui.Button("Clear", font=16, expand_x=True, expand_y=True)
add_button = gui.Button("+", font=16, expand_x=True, expand_y=True)
subtract_button = gui.Button("-", font=16, expand_x=True, expand_y=True)
divide_button = gui.Button("/", font=16, expand_x=True, expand_y=True)
multiply_button = gui.Button("*", font=16, expand_x=True, expand_y=True)
equals_button = gui.Button("=", font=16, expand_x=True, expand_y=True)

output_label = gui.Text(key="output", size=(20, 2), expand_x=True, expand_y=True)
exit_button = gui.Button("Exit", button_color="Red", size=(3, 1), expand_x=True, expand_y=True)

window = gui.Window("Calculator", layout=[[exit_button, clear_button, output_label],
                                          [button7, button8, button9, divide_button],
                                          [button4, button5, button6, multiply_button],
                                          [button1, button2, button3, subtract_button],
                                          [button0, decimal_button, equals_button, add_button]],
                    size=(450, 450), resizable=True)
num = []
final_nums = []
operator = ""
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

        case".":
            num.append(".")
            window["output"].update(value=func.create_num(num))

        case "+":
            operator = "+"
            if len(final_nums) > 0 and len(num) == 0:
                pass
            else:
                number = func.create_num(num)
                final_nums.append(number)
                num.clear()

        case "-":
            operator = "-"
            if len(final_nums) > 0 and len(num) == 0:
                pass
            else:
                number = func.create_num(num)
                final_nums.append(number)
                num.clear()

        case "*":
            operator = "*"
            if len(final_nums) > 0 and len(num) == 0:
                pass
            else:
                number = func.create_num(num)
                final_nums.append(number)
                num.clear()

        case "/":
            operator = "/"
            if len(final_nums) > 0 and len(num) == 0:
                pass
            else:
                number = func.create_num(num)
                final_nums.append(number)
                num.clear()

        case "=":
            number = func.create_num(num)
            final_nums.append(number)
            num.clear()
            match operator:
                case "+":
                    result = func.addition(final_nums)
                    window["output"].update(value=result)
                    final_nums.clear()
                    final_nums.append(result)

                case "-":
                    result = func.subtraction(final_nums)
                    window["output"].update(value=result)
                    final_nums.clear()
                    final_nums.append(result)

                case "*":
                    result = func.multiplication(final_nums)
                    window["output"].update(value=result)
                    final_nums.clear()
                    final_nums.append(result)

                case "/":
                    try:
                        result = func.division(final_nums)
                        window["output"].update(value=result)
                        final_nums.clear()
                        final_nums.append(result)

                    except ZeroDivisionError:
                        window["output"].update(value=func.get_zero_divide_message())
        case "Clear":
            num.clear()
            final_nums.clear()
            running_total = ""
            x = ""
            y = ""
            window["output"].update(value="")
        case "Exit":
            break

window.close()
