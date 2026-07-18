with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

with open('output.txt', 'w') as file:
    file.write("Hello World!\\n")