import os


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


header = ''
day = ''
f = None
folder_name = str(raw_input('Please enter full file name: '))
pfolder_name = folder_name.split('.')[0]
create_folder(pfolder_name)
for line in open(folder_name):
    if header == '':
        header = line
        continue

    lday = line.split(',')[1][1:11]
    if day != lday:
        day = lday
        if f is not None:
            print('file finished for ' + day + ', closing file..')
            f.close()
        print('found day ' + day + ', creating file..')
        f = open(pfolder_name + '/' + day + '.csv', 'w+')
        f.write(header)

    f.write(line)

if f is not None:
    f.close()
