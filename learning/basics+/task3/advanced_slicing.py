"""
Create function that will cut out all content in Parentheses from given text. Text can contain many Parentheses,
each should be cut out and put into a list. function should return a list with all Parentheses sentences (list should
contain only sentences, without "(" and ")" parentheses symbols).

Tips: read more about slicing and string methods: count, find.
"""
example_text = "Parentheses are most often used to identify material that acts as an aside (such as this brief " \
               "comment) or to add incidental information. If the parentheses appear in the midst of a sentence " \
               "(as in this example), then any necessary punctuation (such as the comma that appeared just a few " \
               "words ago) is delayed until the parentheses are closed."


def cut_brackets(text):
    list_of_sentences = []
    # Put your code here
    return list_of_sentences


# Below you can find a simple test (assertion), it checks if your function works properly by comparing expected results
# with list obtained from your function. When you run this script and function will not return correct list it will
# tell you how your list looks like and how expected one should look like, just look at error log
expected = ["such as this brief comment", "as in this example", "such as the comma that appeared just a few words ago"]
assert expected == cut_brackets(example_text), f"List with sentences from your function is not as expected!\n" \
                                               f"Expected list:{expected} \nYour list:{cut_brackets(example_text)}"
