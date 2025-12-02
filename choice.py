from prompt_toolkit.shortcuts import choice
from prompt_toolkit import prompt

text = prompt("Give me some input: ")
print(f"You said: {text}")


result = choice(
    message="Please choose you club",
    options=["FC Barcelona", "Liverpool FC", "AC Milan"],
    default="FC Barcelona"
)

print(f"you have chosen: {result}")