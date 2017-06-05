"""
keyword -> modulo per avere le parola chiave del python
"""
import keyword


def _is_comment(line):
    """
    Controlla se la riga è realmente commento
    :param line: linea da controllare
    :return True/False: indicazione se la riga è commento
    """
    code_counter = 0
    code_word = keyword.kwlist
    for word in line:
        if word == code_word:
            code_counter += 1
    return code_counter < 3


def _is_start_comment(line):
    """
    Controlla se la riga è l'inizio di un blocco multi commento
    :param line: riga su cui effettuare il controllo
    :return True/False: indicazione se la riga è l'inizio di un commento
    """
    line = line.strip(' \t\n\r')
    return bool(line.startswith("'''") or line.startswith('"""'))


def _is_end_comment(line):
    """
    Controlla se la riga è la fine di un blocco multi commento
    :param line: riga su cui effettuare il controllo
    :return True/False: indicazione se la riga è la fine di un commento
    """
    return bool((line.endswith("'''")or line.endswith('"""')))


def _is_canc_comment(line):
    comment_block = False
    for letter in line:
        if letter == '\'' or letter == '\"':
            comment_block != comment_block
        if letter == '#' and comment_block is False:
            return True
        if letter == '#' and comment_block is True:
            return False
