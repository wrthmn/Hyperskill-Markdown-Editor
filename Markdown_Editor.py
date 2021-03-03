result = []
help_message = """\nThis program helps user to format text using markdown language.

Supported formatters:

- plain
- bold
- italic
- link
- inline-code
- new-line
- header
- unordered-list
- ordered-list

Use command !done to finish formatting and save the result to a file output.md in the program directory.
Use command !help to print this message.\n"""


def get_text():

    return input("Text: ")


def plain():

    return get_text()


def bold():

    return f"**{get_text()}**"


def italic():

    return f"*{get_text()}*"


def link():

    label = input("Label: ")
    url = input("URL: ")

    return f"[{label}]({url})"


def inline_code():

    return f"`{get_text()}`"


def new_line():

    return "\n"


def header():

    lvl = 0
    text = ""

    while lvl < 1 or lvl > 6:

        lvl = int(input("Level: "))
        text = get_text()

    return f"{'#' * lvl} {text}\n"


def create_list(ordered=False):

    rows = 0
    text = []

    while rows < 1:

        rows = int(input("Number of rows: "))

        if rows < 1:

            print("The number of rows should be greater than zero")

    for i in range(1, rows + 1):

        row = input(f"Row #{i}: ")

        if ordered:

            text.append(f"{i}. {row}\n")

        else:

            text.append(f"* {row}\n")

    return "".join(text)


def ordered_list():

    return create_list(ordered=True)


formatters = {"plain": plain,
              "bold": bold,
              "italic": italic,
              "link": link,
              "inline-code": inline_code,
              "new-line": new_line,
              "header": header,
              "unordered-list": create_list,
              "ordered-list": ordered_list}


print(help_message)

while True:

    input_ = input("Choose a formatter: ")

    if input_ == "!done":

        try:

            file = open("output.md", "w")

            for item in result:

                file.write(item)

            file.close()

        except FileExistsError:

            print("Failed to save file.")

        break

    elif input_ == "!help":

        print(help_message)

    elif input_ not in formatters:

        print("Unknown formatter or command. Please try again.")

    else:

        result.append(formatters[input_]())

        print(*result, sep="")

