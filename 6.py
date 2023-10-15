from collections import deque
import re


def check_html_str(html_str):
    stack = deque()

    for i in re.findall("[<]{1}[//a-zA-z0-9]*[>]{1}", html_str):
        if '/' in i:
            pop = stack.pop()
            if i.replace('/', '') == pop:
                continue
            else:
                print(pop, 'was not closed')
                return False
        else:
            stack.append(i)
    return True


html_str_right = \
    "<html> \
        <head> \
            <title>\
                 Example \
            </title> \
        </head>\
         <body>\
            <h1>Hello, world</h1>\
        </body>\
    </html>"

html_str_wrong = \
    "<html> \
        <head> \
            <title>\
                 Example \
        </head>\
         <body>\
            <h1>Hello, world</h1>\
        </body>\
    </html>"

print('right', check_html_str(html_str_right))
print('wrong', check_html_str(html_str_wrong))

