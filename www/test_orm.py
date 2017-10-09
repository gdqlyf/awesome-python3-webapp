#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-07 15:04:37
# @Author  : guodong (guodong1250421@gmail.com)
# @Link    : ${link}
# @Version : $Id$
"测试orm"

import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop = loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()