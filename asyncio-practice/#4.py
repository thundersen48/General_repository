from time import sleep

def spider (site_name):
    for page in range(1,4):
        sleep(1)
        print(site_name, page)

spider('Blog')
spider('News')
spider('Forum')