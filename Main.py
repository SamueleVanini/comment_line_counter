
comment_count = 0
comment_block = False
file_input = open('code_main_test.py', 'r')
for line in file_input:
    line = line.replace('\n', '')
    if line.startswith("'''") and comment_block is False:
        if _is_comment(line):
            comment_count += 1
            comment_block = True
    elif line[-1] is "'" and line[-2] is "'" and line[-3] is "'" and comment_block is True:
        comment_block = False
        comment_count += 1
    elif comment_block is True:
        comment_count += 1
    elif line.startswith('#'):
        comment_count += 1
print(comment_count)