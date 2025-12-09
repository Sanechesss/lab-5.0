import re 
text = 'He jests at scars. That never felt a wound!   Hello, friend!   Are you OK?'
sen = re.split(r'(?<=[.?!]) +', text)

def stroki (items):
    for item in items:
        print(item)


stroki(sen)

print(f'Предложений в тексте: {len(sen)}')
