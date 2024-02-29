# challenge 1
def squared(x):
    """
    Returns x * x
    :param x: int.
    :return: int squared x.
    """
    return x * x
print(squared(5))

# challenge 2
def text_output(text: str):
    """
    Prints text
    :param text: str.
    :return: None.
    """
    print(text)
text_output("Hello world!")

# challenge 3
def paragraph(noun, verb, adj, name="John", age=18):
    """
    Prints a paragraph
    :param noun: str.
    :param verb: str.
    :param adj: str.
    :param name: str.
    :param age: int.
    :return: None.
    """
    print(f"This {noun} can {verb}. This {noun} is {adj}.\n My name is {name}, and i am {age} years old. This is my story")
paragraph("Ball", "bounce", "round", "Sander", 31)

# challenge 4
def divided_by_two(num):
    """
    Returns num / 2
    :param num: int.
    :return: num divided by two
    """
    return num / 2
def multiplied_by_four(num):
    """
    Returns num * 4
    :param num: int.
    :return: num times four.
    """
    return num * 4
my_num = divided_by_two(26)
print(multiplied_by_four(my_num))

# challenge 5
def to_float(string):
    """
    Tries to convert string to float.
    :param string: str.
    :return: float or None 
    """
    try:
        return float(string)
    except ValueError:
        print("This value cannot be converted to float")
print(to_float("43"))

# challenge 6
# add docstrings