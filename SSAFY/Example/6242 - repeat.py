list_blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB','AB', 'O']
dic_blood = dict()
list_A = 0
list_O = 0
list_B = 0
list_AB = 0

for i in range(len(list_blood)):
    if list_blood[i] == 'A':
        list_A += 1
    elif list_blood[i] == 'O':
        list_O += 1
    elif list_blood[i] == 'B':
        list_B += 1
    else : list_AB += 1

dic_blood['A'] = list_A
dic_blood['O'] = list_O
dic_blood['B'] = list_B
dic_blood['AB'] = list_AB

print(dic_blood)