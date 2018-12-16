import icu


def check(entry, line, line_number):
    column_count = 5
    if len(entry) != column_count:
        raise RuntimeError('Format error on line {}: "{}"'.format(
            line_number, line))
    if entry != list(map(str.strip, entry)):
        raise RuntimeError('Unnecessary whitespace characters on line {}:'
                           ' "{}"'.format(line_number, line))
    return entry


def read(file_obj, check_func=check):
    line_number = 0
    for line in file_obj:
        line_number += 1
        entry = line.rstrip('\n').split('\t')
        yield check_func(entry, line, line_number)


def write(entries, file_obj):
    for entry in entries:
        file_obj.write('\t'.join(entry))
        file_obj.write('\n')


def sort(entries):
    cs_sort_key = icu.Collator.createInstance(
        icu.Locale('cs_CZ.UTF-8')).getSortKey
    en_sort_key = icu.Collator.createInstance(
        icu.Locale('en_US.UTF-8')).getSortKey

    def sort_key(entry):
        return (
            en_sort_key(entry[0]),
            cs_sort_key(entry[1]),
            cs_sort_key(entry[2]),
            cs_sort_key(entry[3]),
            cs_sort_key(entry[4]))

    entries.sort(key=sort_key)
