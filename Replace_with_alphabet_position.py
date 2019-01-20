alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z"]
print(alphabet.index("a"))
def alphabet_position(text):
    #making sure it's all in lower case
    text = text.lower()
    numbers = []
    for char in text:
    #try and except block for unrecognized characters
      try:
        if char != " " or char != "'" or char != ".":
          num = alphabet.index(char)
          number = num + 1
          numbers.append(number)
      except ValueError:
        num = 0
    return " ".join([str(i) for i in numbers])
