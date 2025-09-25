letter = '''Dear <|Name|>,
You are Selected!
<|Date|>'''

print(letter.replace("<|Name|>","Ram").replace("<|Date|>", "15 january 2050"))
#output =
#Dear Ram,
#You are Selected!
#15 january 2050