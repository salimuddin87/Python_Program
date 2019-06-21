#!/usr/bin/python
import os
import subprocess
import pdb


def has_no_e_average():

    pdb.set_trace()
    withE = 0
    withoutE = 0
    with open('words.txt', 'r') as fin:
        for line in fin:
            status = has_no_e(line.rstrip())
            if status:
                withoutE += 1
            else:
                withE += 1
    """
    print noE_list
    cmd = "wc -l /home/salim/program_python/wordplay/words.txt"
    p = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    status = p.poll()
    TotalWords = out.split()
    print float(len(noE_list))
    print float(TotalWords[0])
    """
    average = 100 * withoutE/float(withE + withoutE)
    print "Percentage of no_e_words is : %0.2f" % average
    return


def has_no_e(word):

    for letter in word:
        if letter == 'e':
            return False
    return True


if __name__ == '__main__':
    has_no_e_average()
