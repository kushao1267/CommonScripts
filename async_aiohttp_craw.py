#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date : 2016-11-18 10:41:46
# @Author  : Liu Jian (461698053@qq.com)
# import json
import asyncio
from aiohttp import ClientSession

global URLS
URLS = ["http://www.baidu.com", "http://www.souhu.com", "http://www.sina.com"]


class FetchPage(object):
    '''
        aiohttp+async异步爬取
    '''

    def __init__(self):
        self = self

    async def fetch(self, url, method, data):
        async with ClientSession() as session:
            if method == 'get':
                async with session.get(url) as response:
                    return await response.read()
            elif method == 'post':
                async with session.post(url, data= data) as response:
                    return await response.read()

    async def run(self, loop, urls):
        tasks = []
        for each in urls:
            task = asyncio.ensure_future(self.fetch(each, 'get', None))
            tasks.append(task)
            responses = await asyncio.gather(*tasks)
            print(responses)

    def raw(self, URLS):
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.run(loop, URLS))
        loop.run_until_complete(future)


if __name__ == '__main__':
    f = FetchPage()
    f.raw(URLS)
