import glob
import os


# Adapted from: https://github.com/granluo/Combine-RTF

def _read_file(filedir):
    os.chdir(filedir)
    return glob.glob("*.rtf")


def _make_dir(ndir):
    try:
        os.makedirs(ndir)
    except OSError:
        pass


def combine_rtf(filedir, filename, page_delimit=True):
    """
    filedir: directory of the file containing all rtfs needed to be combined
    filename: the name of final combined rtf document.
    page_delimit: determine if rtf would start in a new page or new line.
    """

    if '/' in filename:
        _make_dir('/'.join(filename.split('/')[:-1]))
    else:
        _make_dir('output')
        filename = 'output/' + filename

    filenames = _read_file(filedir)
    test = filename
    try:
        filenames.remove(test)
    except ValueError:
        pass
    out_file = open(test, 'wb')
    out_file.write(b"{")

    for fname in filenames:
        if test in fname:
            continue

        with open(fname, 'rb') as f1:
            mylist = list(l1 for l1 in f1)
            mylist[0] = mylist[0].strip()[1:]
            mylist[-1] = mylist[-1].strip()[:-1]
            for i in mylist:
                out_file.write(i)
            if page_delimit & (fname != filenames[-1]):
                out_file.write(b"\par \page")

    out_file.write(b"} ")
    out_file.close()


def __main():
    combine_rtf('.', 'output.rtf', True)


if __name__ == '__main__':
    __main()
