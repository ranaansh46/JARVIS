from rich import print
from rich.panel import Panel

print(Panel("Hello, [red]World!", title="Welcome", subtitle="Thank you"))

# # # print(Panel("Hello, [red]World!"))
# from rich.console import Console
# from rich.table import Table
# from rich import print
# from rich.layout import Layout

# layout = Layout()
# layout.split_column(
#     Layout(name="upper"),
#     Layout(name="lower")
# )
# print(layout)

# def conte():
#     table = Table(title="Basic commands for Jarvis module")

#     table.add_column("Command", justify="right", style="cyan", no_wrap=True)
#     table.add_column("Function", style="magenta")

#     table.add_row("help", "prints all the commands")
#     table.add_row("open", "to open any website")
#     table.add_row("exit", "exit command can be accessed using multiple keywords like bye,exit,terminate or quit")
#     table.add_row("wiki", "this will search the provided keyword and return a result summary from wikipedia")

#     console = Console()
#     console.print(table)

# def help():
#     Layout[upper].update(
#         conte()
#     )
#     print(layout)