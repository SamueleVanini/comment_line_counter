from _is_comment import _is_comment

def main(file_input):
    comment_count = 0
    line_count = 0
    comment_block = False
    file_input = open(file_input, 'r')
    for line in file_input:
        line_count += 1
        line = line.replace('\n', '')
        try:
            if line.startswith("'''") and comment_block is False:
                if (_is_comment(line) < 3):
                    comment_count += 1
                    comment_block = True
            elif line[-1] is "'" and line[-2] is "'" and line[-3] is "'" and comment_block is True:
                comment_block = False
                comment_count += 1
            elif comment_block is True:
                comment_count += 1
            elif line.startswith('#'):
                comment_count += 1
        except:
            pass
    return (comment_count/line_count)*100

if __name__ == '__main__':
    main()