# coding: utf-8
# @FileName: :pythonic.py
# @Time: 2022/8/7 20:11
# @Author: QHB


"""
PEP8  python代码规范必读

1. 干净的python代码是很重要的
2. 编写更好的注释、文档字符串和注解
3. python中的命名和代码布局
4. python中的控制结构
5. 整洁的python代码模式
6. 代码质量执行工具

========================================
注释 -- 块注释, 内联注释

========================================
文档字符串 Docstring  描述代码的功能和用法

========================================
注解 annotations

========================================
布局  1.空行   2.每行最大的字符长度和字符数
3.

========================================
ctrl + alt + l ==> 代码自动格式化的快捷键

========================================
控制结构  顺序 选择 重复
1. 复杂的列表推导
2. lambda
3. 在循环中使用else
4. 生成器(需要执行的时候才会真正读取, 时间换空间, 不适合大量并发的场景)和列表推导(内存空间换时间)的选择  -- 根本区别在于如何使用内存
5. 使用增强的范围 range(40, 90)[3:]
=======================================
clean code patterns
1. 自由使用断言 assert()
2. 逗号
3. 上下文管理器的 "with" 语句
4. 魔术方法、下划线和其他功能
5. 格式化字符串

"""
from typing import List


def insert2(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    文档字符串区域, 描述函数/方法的功能和输入输出

    :param intervals: List[List[int]]
    :param new_interval:  List[int]
    :return: List[List[int]]
    """
    res = []
    if len(intervals) == 0:
        res.append(new_interval)  # 添加到res列表中  -- 内联注释
        # 尤其是linux生产环境下的代码注释, 都建议使用块注释, 不用内联注释
        return res
    elif len(new_interval) == 0:
        return intervals

    intervals.append(new_interval)
    # 先排序 -- 块注释
    intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        if len(res) == 0 or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(interval[1], res[-1][1])
    return res


print(insert2(intervals=[[1, 3], [6, 9]], new_interval=[2, 5]))
# 查看函数的注解
print(insert2.__annotations__)
