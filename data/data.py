from __future__ import print_function, division

import hashlib
import os


d = {'ds113_sub012.tgz': 'da19b5ca0417888a27464e919a719fdc',
     'smoothed_data.npy': 'faeebb34757619574248e963a44b265d'}


def generate_file_md5(filename, blocksize=2**20):
    m = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def check_hashes(d):
    all_good = True
    for k, v in d.items():
        digest = generate_file_md5(k)
        if v == digest:
            print("The file {0} has the correct hash.".format(k))
        else:
            print("ERROR: The file {0} has the WRONG hash!".format(k))
            all_good = False
    return all_good


if __name__ == "__main__":
    check_hashes(d)
