import os

import sys

content1 = '''
package com.unistrong.luowei.factorysuite

import com.unistrong.luowei.factorysuite.item.*

/**
 * Created by luowei on 2017/11/13.
 */
object ItemSet {

    val items = arrayOf(
'''
content2 = '''
    )
}
'''


def generate(item, gen):
    file = open(gen, 'w+')
    file.write(content1)

    listdir = os.listdir(item)
    for f in listdir:
        if f.find("Item") >= 0:
            file.write("%s::class.java,\n" % f[0:f.find(".")])
            print(f)
    # print(listdir)


    file.write(content2)
    file.close()


if __name__ == "__main__":
    generate()
