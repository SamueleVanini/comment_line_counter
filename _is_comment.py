#keyword -> modulo per avere le parola chiave del python
import keyword


def _is_comment(line):
    '''
    Controlla se la linea è realmente commento
    :param line: linea da controllare
    :return True/False: indicazione se la linea è commento
    '''
    CODE_WORD = keyword.kwlist
    if CODE_WORD in line:
