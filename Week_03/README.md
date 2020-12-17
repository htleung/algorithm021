# 学习笔记
## 递归
* 递归实现
	* 递归终结条件，处理当前层逻辑，下探到下一层，清理当前层(回溯恢复，一些非局部变量)
* 思维要点
	* 抛弃人肉递归
	* 找最近重复子问题
## 分治
* 就是递归+分治，分解成子问题，本质就是找重复性，分解问题以及组合子问题的结果
## 回溯
* 有效结果：什么时候将当前结果加入到结果列表中
* 回溯范围
* 剪枝条件
```python
	result = []
	def backtrack(path, items):
		if satisfy_terminate_condition:
			result.add(path)
			return
		for item in items:
			add item to path
			backtrack(deepcopy(path), newitems)
			remove item
```