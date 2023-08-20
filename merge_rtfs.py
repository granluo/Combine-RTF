import glob, os

def readfile(filedir):
    os.chdir(filedir)
    return glob.glob("*.rtf")

def makedir(ndir):
  try:
    os.makedirs(ndir)
  except OSError:
    pass

def combinertf(filedir, filename,pagedelimit = True):

    """
    filedir: directory of the file containing all rtfs needed to be combined
    filename: the name of final combined rtf document.
    pagedelimit: determine if rtf would start in a new page or new line.
    """

    if '/' in filename:
        makedir('/'.join(filename.split('/')[:-1]))
    else:
        makedir('output')
        filename = 'output/' + filename

    filenames = readfile(filedir)
    test = filename
    try:
        filenames.remove(test)
    except ValueError:
        pass
    out_file = open(test, 'wb')
    out_file.write(b"{")

    for fname in filenames:

        if  test in fname:  continue
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

def main():
    combinertf('.','output.rtf',True)

if __name__ == '__main__':
    main()
