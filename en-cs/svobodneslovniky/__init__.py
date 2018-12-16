def read(fileObj):
    column_count = 5
    line_number = 0
    for line in fileObj:
        line_number += 1
        entry = line.rstrip('\n').split('\t')
        if len(entry) != column_count:
            raise RuntimeError('Format error on line {}: "{}"'.format(
                line_number, line))
        if entry != list(map(str.strip, entry)):
            raise RuntimeError('Unnecessary whitespace characters on line {}:'
                ' "{}"'.format(line_number, line))
        yield entry

