# coding=utf-8
import os
import subprocess


def callcmd(args):
    # subprocess.call(args)
    p = subprocess.Popen(args)
    returncode = p.wait()
    if returncode != 0:
        print('ERROR: \"', args, '\" return ', returncode)
    return returncode


def compile_wast(source_files, include_foders, destination_foder, output_name, nowarnings=True):
    '''打印信息
    print('source_files:')
    for file in source_files:
        print('   ', file)
    print('include_foders:')
    for folder in include_foders:
        print('   ', folder)
    print('destination_foder:', destination_foder)
    print('output_name:', output_name)
    '''
    clang_cmd_common = 'clang -emit-llvm -O3 --target=wasm32 -ffreestanding -nostdlib -nostdlibinc -fno-threadsafe-statics -fno-rtti -fno-exceptions'
    if nowarnings:
        clang_cmd_common = clang_cmd_common + ' -Wno-everything'
    else:
        clang_cmd_common = clang_cmd_common + ' -Weverything -Wno-c++98-compat -Wno-old-style-cast -Wno-vla -Wno-vla-extension -Wno-c++98-compat-pedantic -Wno-missing-prototypes -Wno-missing-variable-declarations -Wno-packed -Wno-padded -Wno-c99-extensions -Wno-documentation-unknown-command'
    for folder in include_foders:
        clang_cmd_common = clang_cmd_common + " -I " + folder
        # SYSTEM_INCLUDE_FOLDERS/DEFAULT_SYSTEM_INCLUDE_FOLDERS
        # set(DEFAULT_SYSTEM_INCLUDE_FOLDERS ${CMAKE_SOURCE_DIR}/contracts/libc++/upstream/include ${CMAKE_SOURCE_DIR}/contracts/musl/upstream/include ${Boost_INCLUDE_DIR})
        # set(STANDARD_INCLUDE_FOLDERS ${CMAKE_SOURCE_DIR}/contracts ${CMAKE_SOURCE_DIR}/externals/magic_get/include)
    link_cmd = 'llvm-link -o ' + os.path.join(destination_foder, 'output_name')

    for file in source_files:
        clang_cmd = clang_cmd_common
        st = os.path.splitext(file)
        root = st[0]
        ext = st[1]
        bcfile = ' ' + root + '.bc'
        if ext == '.c':
            clang_cmd = clang_cmd + ' -D_XOPEN_SOURCE=700'
        else:
            clang_cmd = clang_cmd + ' --std=c++14'
        clang_cmd = clang_cmd + ' -c ' + file + ' -o' + bcfile
        returncode = callcmd(clang_cmd)
        if returncode != 0:
            return returncode
        link_cmd = link_cmd + bcfile
    returncode = callcmd(link_cmd)
    return returncode

