import os


class StackOverflowPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        url = base_dir + '/datasets'
        if not os.path.exists(url):
            os.mkdir(url)
        file_path = url + '/data'
        with open(file_path, 'a') as file:
            file.write(str(item) + '\n')
        return item
