user_table = []
split_char = input()[-2]

input()

while True:
    user_line = input()

    if user_line == "":
        break
    else:
        user_table.append(user_line.split())

col, row = len(user_table[0]), len(user_table)
tab = " " * 2

print("<table>")

for r in range(row):
    print(tab + "<tr>", end="")

    for c in range(col):
        print(f'<td class="{user_table[r][c]}">', end="")

    print("</tr>")

print("</table>")
