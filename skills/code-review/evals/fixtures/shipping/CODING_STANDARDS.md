# Coding standards

运费阈值与费率只在 shipping.py 定义和计算。报价等调用方通过 shipping_fee 取得运费，不自行复制运费分段规则。

规则计算保持纯函数。框架、网络与界面装配不进入运费计算模块。
