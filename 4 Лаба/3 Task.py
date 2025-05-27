class EnumOperations():
    plus = "+"
    minus = "-"
    asterisk = "*"
    obelus = "/"

def calculation(first_number,second_number,operation):
    match operation:
        case EnumOperations.plus:
            result = first_number + second_number
        case EnumOperations.minus:
            result = first_number - second_number
        case EnumOperations.asterisk:
            result = first_number * second_number
        case EnumOperations.obelus:
            result = first_number / second_number
    return first_number,second_number,operation,result
        
print(calculation(2,2,"*"))