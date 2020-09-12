import os
import shutil
formats = {
	"音频":[".mp3",".wav"],
	"视频":[".mp4",".avi",".mov"],
	"图片":[".jpeg",".png",".jpg",".gif",".bmp",".psd"],
	"文档":[".txt",".pdf",".doc",".ppt",".xls",".csv",".xlsx",".docx",".pptx",".vsd",".chm",".xml"],
	"程序":[".exe",".msi"],
	"压缩":[".zip",".rar",".7z"],
	"镜像文件":[".iso"],
	"日志":[".log"],
	"图纸":[".dwg"],
	"快捷方式":["快捷方式"],
	"HTML文档":[".html"],
}
# os.chdir(r"Z:\192.168.17.251ziliao\文档")
for f in os.listdir():
	ext = os.path.splitext(f)[-1].lower()
	# print(ext)
	for d,exts in formats.items():
		if not os.path.isdir(d):
			os.mkdir(d)
		if ext in exts:
			shutil.move(f,"{0}/{1}".format(d,f))
print("整理完成")