from ctypes import *

from libarchive.library import libarchive
from libarchive.types.archive import *
from libarchive.constants.archive import *

def _check_zero_success(value):
    if value != ARCHIVE_OK:
        raise ValueError("Function returned failure: (%d)" % (value))
    
    return value

c_archive_read_new = libarchive.archive_read_new
c_archive_read_new.argtypes = []
c_archive_read_new.restype = c_void_p

c_archive_read_support_filter_all = libarchive.archive_read_support_filter_all
c_archive_read_support_filter_all.argtypes = [c_void_p]
c_archive_read_support_filter_all.restype = _check_zero_success

c_archive_read_support_format_all = libarchive.archive_read_support_format_all
c_archive_read_support_format_all.argtypes = [c_void_p]
c_archive_read_support_format_all.restype = _check_zero_success

c_archive_read_open_filename = libarchive.archive_read_open_filename
c_archive_read_open_filename.argtypes = [c_void_p, c_char_p, c_size_t]
c_archive_read_open_filename.restype = _check_zero_success

c_archive_read_next_header = libarchive.archive_read_next_header
c_archive_read_next_header.argtypes = [c_void_p, POINTER(c_void_p)]
c_archive_read_next_header.restype = c_int

c_archive_entry_pathname = libarchive.archive_entry_pathname
c_archive_entry_pathname.argtypes = [c_void_p]
c_archive_entry_pathname.restype = c_char_p

c_archive_read_data_skip = libarchive.archive_read_data_skip
c_archive_read_data_skip.argtypes = [c_void_p]
c_archive_read_data_skip.restype = _check_zero_success

c_archive_read_free = libarchive.archive_read_free
c_archive_read_free.argtypes = [c_void_p]
c_archive_read_free.restype = _check_zero_success

