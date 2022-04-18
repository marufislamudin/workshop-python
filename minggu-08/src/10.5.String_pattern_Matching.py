# modul re
# Untuk pencocokan dan manipulasi yang kompleks 
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# dengan perintah string sederhana
'tea for too'.replace('too', 'two')