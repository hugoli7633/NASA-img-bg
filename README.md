# NASA-img-bg
Setup NASA picture as desktop background

1. 到NASA官网注册得到自己的API KEY（ https://api.nasa.gov/ ）
2. 在脚本文件中将API KEY改为自己的这个KEY
3. 给脚本文件建立快捷方式，打开快捷方式属性，在<目标>一栏写入 "C:\Users\YOUR_USER_NAME\AppData\Local\Microsoft\WindowsApps\python.exe" D:\vswp\NASA_bg\get_img.py 并在<起始位置>写入想要存储图片的路径，例如 D:\WP
4. 将快捷方式放入启动项文件夹（ Windows默认在C:\Users\YOUR_USER_NAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup ）
5. 每次启动/重启都会运行该脚本进行桌面背景更新5. The script runs for desktop background updates every time you start/restart
