# baidu-url-submit-by-using-sitemap

## 它可以干嘛

提取 sitemap 中的链接，并**自动**利用百度 API 进行推送，提升网站收录速度。

## 它的由来

博客从 Hexo 换到 Gridsome，没有相应的插件可以生产链接并推送至百度，于是就自己利用 Python 和 GitHub Action 写了一个自动推送。任何博客框架都可以用，只需要配置好，就可以每天自动利用百度的 API 进行链接提交。

## 它要怎么用

先前往百度资源搜索平台获取 `token`，就是 API 提交中，接口调用地址 `http://data.zz.baidu.com/urls?site=xxx&token=xxx`，`token=` 之后的那一串。

`fork` 本仓库，`Settings > Secrets > new New secret`，`Name` 中填写 `BAIDUTOKEN`，`Value` 即刚刚获取的。（放入 Secrets 中能防止 token 泄露）。再新建一个 secret，`name` 为 `site`，`Value` 为你的博客地址，需要协议头，结尾不能有 `/`

将 `generate.py` 文件中 `sitemap` 变量的值修改为你的 sitemap.xml 地址，请确保你的 sitemap 为正常格式。

```py
sitemap = 'https://blog.jalenchuh.cn/sitemap.xml'
```

好了，大功告成，接下来每天北京时间 0 点左右，GitHub 便会自动帮你推送链接至百度。

如果你配置完成后迫不及待想要查看结果，可以试着给你的仓库点个🌟（当然也别忘了给本仓库也来个🌟），之后便可进入 GitHub Acion 中查看结果。

Enjoy it!

---

🚀 **`baidu-url-submit-by-using-sitemap`** ©Jalen Chuh. Released under the MIT License.

Authored and maintained by Jalen Chuh.

[@Portfolio](https://jalenchuh.cn) · [@Blog](https://blog.jalenchuh.cn) · [@GitHub](https://github.com/jalenchuh)
