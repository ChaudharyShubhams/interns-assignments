with open('files.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        expression = line.strip()
        temp=expression
        expression = expression.replace("=", '')
        expression = expression.replace("^", '')
        expression = expression.replace(") (", ') * (')

        result = eval(expression)
        output_file.write(f"{temp}= {result}\n")