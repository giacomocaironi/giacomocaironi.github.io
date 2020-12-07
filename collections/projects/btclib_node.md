---
name: Btclib node
description: Bitcoin node written in python
category: crypto
date: 2020-12-07
---

To test the code I was writing in btclib I wrote some logic to connect to bitcoin nodes with python. After a while I though I could use this foundation to start writing a very simple bitcoin node in python. I found out that none had done it before so I though I would give it a try.

Btclib_node is now hosted on [github](https://github.com/btclib-org/btclib_node) withing the btclib organization

For now it has the following abilities:
- maintain a fully fledged connection with other bitcoin nodes
- relay transactions with a mempool
- sync headers
- download blocks
- very basic rpc api

However it still can't handle reorgs(ouch) and when it downloads blocks it doesn't perform any logic on it
