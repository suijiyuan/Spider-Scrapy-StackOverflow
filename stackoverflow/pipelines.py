import os


class StackOverflowPipeline(object):
    def __init__(self):
        base_dir = os.getcwd()
        url = base_dir + '/datasets'
        if not os.path.exists(url):
            os.mkdir(url)
        file_path = url + '/data'
        if os.path.exists(file_path):
            os.remove(file_path)

    def process_item(self, item, spider):
        file_path = os.getcwd() + '/datasets/data'
        with open(file_path, 'a') as file:
            file.write(str(item) + '\n')
        return item
