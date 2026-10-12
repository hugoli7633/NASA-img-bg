# NASA-img-bg
Setup NASA picture as desktop background

每次开机自动下载 NASA 每日天文图片（APOD）的原图并设为 Windows 桌面背景。

> 原先使用的 `api.nasa.gov/planetary/apod` 接口现在返回的是 NASA 的 logo 而不是当天图片，所以脚本改为读取 NASA 官方的 APOD RSS（ https://science.nasa.gov/feed/apod-basic/ ），不再需要 API KEY。

1. 安装 Python，并安装依赖：`pip install requests`
2. 设置图片保存目录：打开脚本文件，修改 `save_dir`
   - 这个文件夹用来存放每天下载的 APOD 原图，桌面背景直接使用其中的图片，所以**设为壁纸后不要删除当天的图片**。旧图片会一直保留，可以当作图库，不需要时可以手动清理
   - 原图有时会有几十 MB，长期积累会占用不少空间，**建议设定到 C 盘以外的盘**，推荐 `save_dir = r'D:\NASA_APOD'`
   - 默认是 `C:\Users\YOUR_USER_NAME\Pictures\NASA_APOD`
   - 不要设为启动项文件夹，否则开机时会把里面的图片全部打开
3. 先手动运行一次 `python get_img.py`，确认壁纸能正常更换
4. 给脚本文件建立快捷方式，打开快捷方式属性，在<目标>一栏写入 "python.exe 的路径" "get_img.py 的路径"，例如 "C:\Users\YOUR_USER_NAME\AppData\Local\Microsoft\WindowsApps\python.exe" D:\vswp\NASA_bg\get_img.py
   - python.exe 的路径可以在命令行用 `where python` 查到
   - 如果不想开机时弹出命令行窗口，可以把 python.exe 换成同目录下的 pythonw.exe
5. 将快捷方式放入启动项文件夹（ Windows默认在C:\Users\YOUR_USER_NAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup ，也可以按 Win+R 输入 `shell:startup` 打开）
6. 每次启动/重启都会运行该脚本进行桌面背景更新
   - 开机时如果网络还没连上，脚本会每 10 秒重试一次，最多等待约 1.5 分钟
