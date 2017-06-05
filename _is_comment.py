#keyword -> modulo per avere le parola chiave del python
import keyword


def _is_comment(line):
    '''
    Controlla se la linea è realmente commento
    :param line: linea da controllare
    :return True/False: indicazione se la linea è commento
    '''
    code_counter = 0
    CODE_WORD = keyword.kwlist
    for word in line:
        if word is CODE_WORD:
            code_counter += 1
    return code_counter
