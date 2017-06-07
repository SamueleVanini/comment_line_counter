"""
sys -> module for command line argument
Comment_Control -> module for the validation of a comment
Comments_Distribution -> module for the control of comment distribution into the code
"""
import sys
from Components import Comment_Control, Comments_Distribution


def main(file_input):
    """
    Main che gestisce il conteggio delle righe di commento in un sorgente
    :param file_input: file with the comments to count
    :return: comments percentage
    """
    file = open(file_input, 'r')
    result_list = file_reader(file)
    file.close()
    print(result_list[1]/result_list[0]*100)
    # return(result_list[1]/result_list[0]*100)


def file_reader(file):
    """
    Function for read the file and check for comment
    :param file: file to read
    :return result_result: list with line_count and comment_count
    """
    comment_count = 0
    line_count = 0
    comment_block = False
    function_start = False
    for line in file:
        line_count += 1
        line = line.replace('\n', '')
        try:
            if Comments_Distribution._function_comment(line):
                function_start = True
            elif Comment_Control._is_start_comment(line) and comment_block is False:
                if Comment_Control._is_comment(line):
                    comment_count += 1
                    comment_block = True
                    function_start = False
            elif Comment_Control._is_end_comment(line) and comment_block is True:
                comment_block = False
                if Comment_Control._is_comment(line):
                    comment_count += 1
            elif comment_block is True:
                if Comment_Control._is_comment(line):
                    comment_count += 1
            elif Comment_Control._is_canc_comment(line) and comment_block is False:
                if Comment_Control._is_comment(line):
                    comment_count += 1
                    function_start = False
            elif function_start:
                # print("Ti sei dimenticato di commentare una funzione/metodo!!")
                function_start = False
        except IndexError:
            pass

    result_list = [line_count, comment_count]
    return result_list

if __name__ == "__main__":
    main(sys.argv[1])
