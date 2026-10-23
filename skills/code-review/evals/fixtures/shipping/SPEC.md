# Shipping contract

shipping_fee 接收以整数分表示的非负商品小计，返回整数分运费。

- 小计达到 5000 分时免运费，包含刚好 5000 分。
- 小计低于 5000 分时运费为 500 分。
- 小计为负数时抛出 ValueError。
