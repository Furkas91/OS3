import win32file, win32api
import os
import pywintypes
from win32con import *
from time import localtime

def attribute_encoder(attr):
    if (attr & FILE_ATTRIBUTE_ARCHIVE):
        print("Файл или каталог - архивные.")
    if (attr & FILE_ATTRIBUTE_COMPRESSED):
        print("Файл или каталог сжатые.")
    if (attr & FILE_ATTRIBUTE_DEVICE):
        print("Зарезервировано, не используется.")
    if (attr & FILE_ATTRIBUTE_DIRECTORY):
        print("Дескриптор идентифицирует каталог.")
    if (attr & FILE_ATTRIBUTE_ENCRYPTED):
        print("Файл или каталог - зашифрованные.")
    if (attr & FILE_ATTRIBUTE_HIDDEN):
        print("Файл или каталог скрытые.")
    if (attr & FILE_ATTRIBUTE_NORMAL):
        print("Файл или каталог не имеют других установленных атрибутов.")
    if (attr & FILE_ATTRIBUTE_NOT_CONTENT_INDEXED):
        print("Файл не будет индексирован содержащим индексы модулем обслуживания.")
    if (attr & FILE_ATTRIBUTE_OFFLINE):
        print("Данные файла доступны не сразу.")
    if (attr & FILE_ATTRIBUTE_READONLY):
        print("Файл или каталог только для чтения.")
    if (attr & FILE_ATTRIBUTE_REPARSE_POINT):
        print("Файл или каталог имеет связанную точку повторной обработки")
    if (attr & FILE_ATTRIBUTE_SPARSE_FILE):
        print("Файл - разреженный файл.")
    if (attr & FILE_ATTRIBUTE_SYSTEM):
        print("Файл или каталог - используются операционной системой.")
    if (attr & FILE_ATTRIBUTE_TEMPORARY):
        print("Файл используется для временного хранения.")

def time_encoder(time):
    print('Creation Time: ', time[0].__str__())
    print('Access Time: ', time[1].__str__())
    print('Write Time: ', time[2].__str__())

class Miracle:

    def __init__(self):
        pass

    def process1(self):
        drivebits = win32file.GetLogicalDrives()
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        print(drives)

    def process2(self):
        drivetype = {
            0: 'DRIVE_UNKNOWN',
            1: 'DRIVE_NO_ROOT_DIR',
            2: 'DRIVE_REMOVABLE',
            3: 'DRIVE_FIXED',
            4: 'DRIVE_REMOTE',
            5: 'DRIVE_CDROM',
            6: 'DRIVE_RAMDISK'
        }
        FILE_NAMED_STREAMS = 262144
        FILE_PERSISTENT_ACLS = 0x00000008
        FILE_READ_ONLY_VOLUME = 0x00080000
        FILE_SEQUENTIAL_WRITE_ONCE = 0x00100000
        FILE_SUPPORTS_ENCRYPTION = 0x00020000
        FILE_SUPPORTS_EXTENDED_ATTRIBUTES = 0x00800000
        FILE_SUPPORTS_HARD_LINKS = 0x00400000
        FILE_SUPPORTS_OBJECT_IDS = 0x00010000
        FILE_SUPPORTS_OPEN_BY_FILE_ID = 0x01000000
        FILE_SUPPORTS_REPARSE_POINTS = 0x00000080
        FILE_SUPPORTS_SPARSE_FILES = 0x00000040
        FILE_SUPPORTS_TRANSACTIONS = 0x00200000
        FILE_SUPPORTS_USN_JOURNAL = 0x02000000
        FILE_UNICODE_ON_DISK = 0x00000004
        FILE_VOLUME_IS_COMPRESSED = 0x00008000
        FILE_VOLUME_QUOTAS = 0x00000020
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        # 2print(drives[0])

        choose = input()
        for drive in drives:
            if choose in drive:
                choose = drive
        type = win32file.GetDriveType(choose)
        print(drivetype[type], "\n")
        volume = win32api.GetVolumeInformation(choose)
        print('serial number: ', volume[1])
        print('name of fail system: ', volume[4], '\n')
        if (volume[3] & FILE_CASE_PRESERVED_NAMES):
            print("The specified volume supports preserved case of file names when it places a name on disk.")
        if (volume[3] & FILE_CASE_SENSITIVE_SEARCH):
            print("The specified volume supports casesensitive file names.")
        if (volume[3] & FILE_FILE_COMPRESSION):
            print("The specified volume supports file-based compression.")
        if (volume[3] & FILE_NAMED_STREAMS):
            print("The specified volume supports named streams.")
        if (volume[3] & FILE_PERSISTENT_ACLS):
            print("The specified volume preserves and enforces access control lists (ACL).")
        if (volume[3] & FILE_READ_ONLY_VOLUME):
            print("The specified volume is read-only.")
        if (volume[3] & FILE_SEQUENTIAL_WRITE_ONCE):
            print("The specified volume supports a single sequential write.")
        if (volume[3] & FILE_SUPPORTS_ENCRYPTION):
            print("The specified volume supports the Encrypted File System (EFS).")
        if (volume[3] & FILE_SUPPORTS_EXTENDED_ATTRIBUTES):
            print("The specified volume supports extended attributes.")
        if (volume[3] & FILE_SUPPORTS_HARD_LINKS):
            print("The specified volume supports hard links")
        if (volume[3] & FILE_SUPPORTS_OBJECT_IDS):
            print("The specified volume supports object identifiers.")
        if (volume[3] & FILE_SUPPORTS_OPEN_BY_FILE_ID):
            print("The file system supports open by FileID.")
        if (volume[3] & FILE_SUPPORTS_REPARSE_POINTS):
            print("The specified volume supports reparse points.")
        if (volume[3] & FILE_SUPPORTS_SPARSE_FILES):
            print("The specified volume supports sparse files.")
        if (volume[3] & FILE_SUPPORTS_TRANSACTIONS):
            print("The specified volume supports transactions.")
        if (volume[3] & FILE_SUPPORTS_USN_JOURNAL):
            print("The specified volume supports update sequence number (USN) journals.")
        if (volume[3] & FILE_UNICODE_ON_DISK):
            print("The specified volume supports Unicode in file names as they appear on disk.")
        if (volume[3] & FILE_VOLUME_IS_COMPRESSED):
            print("The specified volume is a compressed volume, for example, a DoubleSpace volume.")
        if (volume[3] & FILE_VOLUME_QUOTAS):
            print("The specified volume supports disk quotas.")

        space = win32file.GetDiskFreeSpace(choose)
        free_space = space[0] * space[1] * space[2] #/ 1024 / 1024
        total_space = space[0] * space[1] * space[3] #/ 1024 / 1024
        print('free space:', free_space, '\n')
        print('total space:', total_space, '\n')

    def process3(self):

        answer3 = 5

        while answer3 != '10':
            print('1 - To create directory\n'
                  '2 - To remove directory\n'
                  '10 - To exit to menu')

            answer3 = input()

            if answer3 == '1':
                print("Enter the name of directory\n")
                directory = input()
                win32file.CreateDirectory(directory, None)

            elif answer3 == '2':
                print("Enter the name of directory to delete\n")
                directory = input()
                win32file.RemoveDirectory(directory, None)
        answer = 9

    def process4(self):
        print("Enter the name of file to create\n")
        handle = win32file.CreateFile(input(),
                                      win32file.GENERIC_WRITE,
                                      0,
                                      None,
                                      CREATE_ALWAYS,
                                      0,
                                      None)
        print(handle.__str__())

    def process5(self):
        answer5 = 5

        while answer5 != '10':
            print('1 - To copy file\n'
                  '2 - To move file\n'
                  '3 - To advanced move file\n'
                  '10 - To exit to menu')

            answer5 = input()

            if answer5 == '1':
                print("Enter the name of file to copy and the name of new file\n")
                win32api.CopyFile(input(), input(), 0)

            elif answer5 == '2':
                print("Enter the name of file and the directory to move\n")
                win32api.MoveFile(input(), input())
                # win32file.MoveFileWithProgress(input(), input())
            elif answer5 == '3':
                print("Enter the name of file and the directory to move\n")
                win32api.MoveFileEx(input(),
                                    input(),
                                    11)

    def process6(self):
        answer6 = 6

        while answer6 != '10':
            print('1 - To get file attributes\n'
                  '2 - To set file attributes\n'
                  '3 - To get file information by handle\n'
                  '4 - To get file time\n'
                  '5 - To set file time\n'
                  '10 - To exit to menu')

            answer6 = input()

            if answer6 == '1':
                # print(win32con.FILE_ATTRIBUTE_*)
                print("Enter the name of file to get file attributes\n")
                attr = win32api.GetFileAttributes(input())
                attribute_encoder(attr)

            elif answer6 == '2':
                #print("Enter the name of file\n")
                #path = ''
                attr = 0
                #ans = 0
                path = input("Enter the name of file\n")
                ans = input("Файл или каталог - архивные?Y-да, иначе-нет")

                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_ARCHIVE
                ans = input("Файл или каталог сжатые?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_COMPRESSED
                ans = input("Зарезервировано, не используется?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_DEVICE
                ans = input("Дескриптор идентифицирует каталог?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_DIRECTORY
                ans = input("Файл или каталог - зашифрованные?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_ENCRYPTED
                ans = input("Файл или каталог скрытые?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_HIDDEN
                ans = input("Файл или каталог не имеют других установленных атрибутов?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_NORMAL
                ans = input("Файл не будет индексирован содержащим индексы модулем обслуживания?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
                ans = input("Данные файла доступны не сразу?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_OFFLINE
                ans = input("Файл или каталог только для чтения?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_READONLY
                ans = input("Файл или каталог имеет связанную точку повторной обработки?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_REPARSE_POINT
                ans = input("Файл - разреженный файл?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_SPARSE_FILE
                ans = input("Файл или каталог - используются операционной системой?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_SYSTEM
                ans = input("Файл используется для временного хранения?Y-да, иначе-нет")
                if ans == 'Y' or ans == 'y':
                    attr += FILE_ATTRIBUTE_TEMPORARY
                win32api.SetFileAttributes(path, attr)

            elif answer6 == '3':
                print('Input path to file:')
                handle = win32file.CreateFile(input(),
                                              win32file.GENERIC_WRITE,
                                              0,
                                              None,
                                              OPEN_EXISTING,
                                              0,
                                              None)
                input()
                inf = win32file.GetFileInformationByHandle(handle)
                attribute_encoder(inf[0])
                time_encoder(inf[1:4])
                #print("Serial number: ", inf[4])
                win32api.CloseHandle(handle)

            elif answer6 == '4':
                print('Input path to file:')
                handle = win32file.CreateFile(input(),
                                              win32file.GENERIC_WRITE,
                                              0,
                                              None,
                                              OPEN_EXISTING,
                                              0,
                                              None)
                time = win32file.GetFileTime(handle)
                #strftime("%a, %d %b %Y %H:%M:%S +0000", time[0])
                time_encoder(time)
                win32api.CloseHandle(handle)

            elif answer6 == '5':
                print('Input path to file:')
                handle = win32file.CreateFile(input(),
                                              win32file.GENERIC_WRITE,
                                              0,
                                              None,
                                              OPEN_EXISTING,
                                              0,
                                              None)
                PyTIME = pywintypes.Time(localtime())
                win32file.SetFileTime(handle, PyTIME, PyTIME, PyTIME, False)
                win32api.CloseHandle(handle)

    def process0(self):
        pass

    def dispatch(self, value):
        method_name = 'process' + str(value)
        method = getattr(self, method_name)
        return method()

class myerr(BaseException):
    def __init__(self):
        pass


answer = 9

X = Miracle()
#print(FILE_ATTRIBUTE_READONLY)
while answer != '0':

    print("Choose option:\n"
          "1 - To see drives list\n"
          "2 - To see info about the drive\n"
          "3 - To create and delete directories\n"
          "4 - To create files\n"
          "5 - To copy and move files\n"
          "6 - To analyse changes in attributes\n"
          "0 - To exit\n")

    answer = input()

    try:
        X.dispatch(answer)
    except AttributeError as a:
        raise myerr()
    except ValueError as e:
        raise ValueError('Undefined unit: {}'.format(e.args[0]))
