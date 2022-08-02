from cgitb import text
import textwrap

def wrap(string, max_width):
    fill_str =textwrap.fill(string, max_width) #return new string.
    wrap_str = textwrap.wrap(string, max_width) #return a list of wrapped lines.
    return(fill_str)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)