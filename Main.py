"""
Comment_Controll -> modulo per il controllo del commento in una determinata riga
"""
from Components import Comment_Controll


def main(file_input):
    """
    Main che gestisce il conteggio delle righe di commento in un sorgente
    :param file_input: file in cui contare le righe di commento
    :return: percentuale di commento contenente il file
    """
    comment_count = 0
    line_count = 0
    comment_block = False
    file = open(file_input, 'r')
    for line in file:
        line_count += 1
        line = line.replace('\n', '')
        try:
            if Comment_Controll._is_start_comment(line) and comment_block is False:
                if Comment_Controll._is_comment(line):
                    comment_count += 1
                    comment_block = True
            elif Comment_Controll._is_end_comment(line) and comment_block is True:
                comment_block = False
                if Comment_Controll._is_comment(line):
                    comment_count += 1
            elif comment_block is True:
                if Comment_Controll._is_comment(line):
                    comment_count += 1
            elif line.startswith('#'):
                if Comment_Controll._is_comment(line):
                    comment_count += 1
        except IndexError:
            pass
    file_input.close()
    return (comment_count/line_count)*100
