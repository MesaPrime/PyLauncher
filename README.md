# PyLauncher
 ## 一.启动  
 ### 0.前置
>命令行启动需要安装PYQT5  
> `pip install -r requirements.txt`  
>将.ui文件放置于.py或.exe同目录下
 ### 1.脚本启动  
>python batProducer.py
### 2.bat启动  
>双击 batProducer.py  
### 3.exe启动  
>双击 ./dist/batProducer.exe
>下载 realease 中的batProducer.exe 双击启动

##二.使用
>将文件拖入文本编辑区域  
>可拖入多个  
> 暂时只支持.py文件
> 点击“生成”按钮在拖入文件的同目录生成.bat 和.vbe文件  
> .bat文件启动的py文件带有控制台  
> .vbe文件启动的py不带控制台