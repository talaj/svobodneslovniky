import icu

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


def write(entries, fileObj):
    for entry in entries:
        fileObj.write('\t'.join(entry))
        fileObj.write('\n')


def sort(entries):
    cs_sort_key = icu.Collator.createInstance(icu.Locale('cs_CZ.UTF-8')).getSortKey
    en_sort_key = icu.Collator.createInstance(icu.Locale('en_US.UTF-8')).getSortKey

    def sort_key(entry):
        return (
            en_sort_key(entry[0]),
            cs_sort_key(entry[1]),
            cs_sort_key(entry[2]),
            cs_sort_key(entry[3]),
            cs_sort_key(entry[4]))

    entries.sort(key=sort_key)
