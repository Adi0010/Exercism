def convert(number):
    s=''
    fact = {'3':'Pling','5':'Plang','7':'Plong'}
    for value , sound in fact.items():
        if number % int(value) == 0:
            s+=sound
    if not s:
        s+=str(number)
    return s
