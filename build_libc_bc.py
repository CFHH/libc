# coding=utf-8
import os

'''需要编译的文件
file(GLOB CRYPT_SOURCES  "upstream/src/crypt/*.c")
file(GLOB CTYPE_SOURCES  "upstream/src/ctype/*.c")
file(GLOB ENV_SOURCES  "upstream/src/env/*.c")
file(GLOB ERRNO_SOURCES  "upstream/src/errno/*.c")
file(GLOB EXIT_SOURCES  "upstream/src/exit/*.c")
file(GLOB LOCALE_SOURCES "upstream/src/locale/*.c")
file(GLOB MATH_SOURCES  "upstream/src/math/*.c")
file(GLOB MBYTE_SOURCES  "upstream/src/multibyte/*.c")
file(GLOB MISC_SOURCES "upstream/src/misc/*.c")
file(GLOB SEARCH_SOURCES "upstream/src/search/*.c")
file(GLOB STDIO_SOURCES "upstream/src/stdio/*.c")
file(GLOB STDLIB_SOURCES "upstream/src/stdlib/*.c")
file(GLOB STRING_SOURCES "upstream/src/string/*.c")
file(GLOB TIME_SOURCES "upstream/src/time/*.c")
file(GLOB THREAD_SOURCES "upstream/src/thread/*.c")
set(INTERNAL_SOURCES upstream/src/internal/floatscan.c upstream/src/internal/intscan.c upstream/src/internal/shgetc.c upstream/src/internal/libc.c)
'''
base_path = os.path.abspath(os.curdir)
#print(base_path)

folders = []
folders.append(os.path.join(base_path, r"src\crypt"))
folders.append(os.path.join(base_path, r"src\ctype"))
folders.append(os.path.join(base_path, r"src\env"))
folders.append(os.path.join(base_path, r"src\errno"))
folders.append(os.path.join(base_path, r"src\exit"))
folders.append(os.path.join(base_path, r"src\locale"))
folders.append(os.path.join(base_path, r"src\math"))
folders.append(os.path.join(base_path, r"src\multibyte"))
folders.append(os.path.join(base_path, r"src\misc"))
folders.append(os.path.join(base_path, r"src\search"))
folders.append(os.path.join(base_path, r"src\stdio"))
folders.append(os.path.join(base_path, r"src\stdlib"))
folders.append(os.path.join(base_path, r"src\string"))
folders.append(os.path.join(base_path, r"src\time"))
folders.append(os.path.join(base_path, r"src\thread"))

cfiles = []
'''不需要遍历子目录
for folder in folders:
    c = os.walk(folder)
    for root, dirs, files in c:
        for file_name in files:
            cfiles.append(os.path.join(root, file_name))
'''
for folder in folders:
    files = os.listdir(folder)
    for file in files:
        if os.path.splitext(file)[1] == '.c':
            cfiles.append(os.path.join(folder, file))
folder = os.path.join(base_path, r"src\internal")
cfiles.append(os.path.join(folder, 'floatscan.c'))
cfiles.append(os.path.join(folder, 'intscan.c'))
cfiles.append(os.path.join(folder, 'shgetc.c'))
cfiles.append(os.path.join(folder, 'libc.c'))
'''
for file in cfiles:
    print(file)
'''

'''头文件
INCLUDE_FOLDERS ${CMAKE_SOURCE_DIR}/contracts/musl/upstream/include
                  ${CMAKE_SOURCE_DIR}/contracts/musl/upstream/src/internal
                  ${CMAKE_SOURCE_DIR}/contracts/musl/upstream/arch/eos
                  ${CMAKE_SOURCE_DIR}/contracts/
'''
