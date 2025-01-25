import pandas as pd

comments = []
with open("user_comments.txt", "r", encoding="utf-8") as file:
    for line in file:
        comments.append(eval(line.strip()))


df = pd.DataFrame(comments)

df.to_excel("user_comments.xlsx", index=False)