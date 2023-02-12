


from lxml import etree

from ebooklib import epub


class Ebook(object):
    '''
    制作电子书
    '''
    def __init__(self, params, outdir="./", proxy=""):
        if not isinstance(params, dict):
            raise TypeError("params type error! not dict type.")

        self.img_path = params['img_path']
        self.book_name = params['book_name']
        self.author = params['author']
        self.lang = params.get('lang', 'zh')
        self.identifier = params.get('id', 'id0001')
        self.cover_img_path = params.get('cover_img_path')
        self.intro = params.get('intro')
        self.outdir = outdir
        self.proxy = proxy
        self.opts = {}
        self.plugin = None


    def set_cover(self, img_path):
        """设置封面"""

        self.cover_img_path = img_path

        return None

    def set_intro(self, content):
        """设置简介"""

        self.intro = content
        return None

    def set_proxy(self, proxy):
        """设置简介"""

        self.proxy = proxy

    def set_plugin(self, plugin):
        """设置插件"""

        self.plugin = plugin
        if self.opts.get('plugins') is None:
            self.opts['plugins'] = []
        self.opts['plugins'].append(plugin)

    def create_book(self):
        """创建ebook对象"""
        self.book = epub.EpubBook()
        self.book.set_title(self.book_name)
        self.book.add_author(self.author)
        self.book.set_language(self.lang)
        self.book.set_identifier(self.identifier)
        return self.book


    def fetch_book(self):
        '''
        制作电子书主流程

        1. 获取所有章链接
        2. 按章获取所有小节链接
        '''
        import os

        book = self.create_book()

        # add navigation files
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        # add css file
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css",
                                media_type="text/css", content=style)
        book.add_item(nav_css)

        self.img_idx = 0
        for img_fn in os.listdir(self.img_path):
            img_item = epub.EpubImage()

            file_name = '{:03d}_{}'.format(
                self.img_idx, img_img_path.rsplit('/', maxsplit=1)[1]
            )
            img_item.file_name = file_name
            self.img_idx += 1
            
            img_item.set_content(resp.content)
            
            book.add_item(img_item)

        book_path = f'{self.outdir}/《{self.book_name}》_{self.author}.epub'
        print(f'输出文件名: {book_path}')

        # opts = {'plugins': ImagePlugin(), }
        epub.write_epub(book_path, book, self.opts)


if __name__ == '__main__':
    start_img_path_dic_lst = [
        {
            'img_path': 'G:/ML&DL/深度之眼/NLP-baseline-word2vec/videoppt/video_img_PPT/NLP-baseline-word2vec2-4模型复杂度',
            'book_name': '初中词汇',
            'author': '[中]韩宇',
        },
    ]

    for params in start_img_path_dic_lst[:]:

        ebook = Ebook(params, outdir="F:/WorkSpace/电子书/auto_gen")
        ebook.fetch_book()

