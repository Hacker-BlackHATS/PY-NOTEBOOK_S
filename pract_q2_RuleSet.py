import numpy as np

def check_species(data_read):
    rule_1 = lambda sp: sp in ['versicolor', 'virginica', 'setosa']
    ans = data_read['Species'].apply(rule_1).rename('check_species')
    if np.any(False == ans):
        print('Violation : Species is not versicolor, virginica or setosa in some places')
        print(f'Violation : {ans.size - np.count_nonzero(ans)}')
    else:
        print('No Violation')
    return (ans)
def check_positive_numprop(data_read):
    # rule_2 = lambda npn: (npn[0] > 0) and (npn[1] > 0) and (npn[2] > 0) and (npn[3] > 0)
    rule_2 = lambda npn: npn > 0
    ans = data_read[['Sepal.Length','Sepal.Width', 'Petal.Length', 'Petal.Width']].apply(rule_2, axis=1).rename('check_positive_numprop')
    if np.any(False == ans):
        print('Violation : Measured numerical properties are not positive in some places')
        print(f'Violation : {ans.size - np.count_nonzero(ans)}')
    else:
        print('No Violation')
    return (ans)
def check_petalL(data_read):
    rule_3 = lambda pl: pl[0] >= 2*pl[1]
    ans = data_read[['Petal.Length', 'Petal.Width']].apply(rule_3).rename('check_petalL')
    if np.any(False == ans):
        print('Violation : Patel length is not at least 2 times its petal width in some places')
        print(f'Violation : {ans.size - np.count_nonzero(ans)}')
    else:
        print('No Violation')
    return (ans)
def check_sepalL(data_read):
    rule_4 = lambda sl: sl < 30
    ans = data_read['Sepal.Length'].apply(rule_4).rename('check_sepalL')
    if np.any(False == ans):
        print('Violation : Sepal length is exceding 30 in some places')
        print(f'Violation : {ans.size - np.count_nonzero(ans)}')
    else:
        print('No Violation')
    return (ans)
def check_sepal_p(data_read):
    rule_4 = lambda spl: spl[0] > spl[1]
    ans = data_read[['Sepal.Length', 'Petal.Length']].apply(rule_4).rename('check_sepal_p')
    if np.any(False == ans):
        print('Violation : Sepals are not longer than its petals in some places')
        print(f'Violation : {ans.size - np.count_nonzero(ans)}')
    else:
        print('No Violation')
    return (ans)

E = {'check_species':check_species, 'check_positive_numprop':check_positive_numprop, 'check_petalL':check_petalL, 'check_sepalL':check_sepalL, 'check_sepal_p':check_sepal_p}
