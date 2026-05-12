# 响应鼠标事件 - 点击画圆并打印坐标和RGB值
import numpy as np
import cv2
# 打开一张图片（请修改为你的图片路径）
img = cv2.imread('OIP-C.jfif')
# 创建图片副本用于显示（保留原图颜色值）
display_img = img.copy()
# 颜色列表
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 0, 255), (255, 255, 0)]
color_index = 0
current_color = colors[color_index]
drawing = False  # 标记是否正在拖动
last_x, last_y = -1, -1  # 记录上一个鼠标位置
def draw(event, x, y, flag, param):
    """定义鼠标回调函数"""
    global current_color, color_index, drawing, last_x, last_y
    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下（单击）
        drawing = True
        last_x, last_y = x, y
        # 1. 在鼠标位置画空心圆，半径3像素，当前颜色，线宽1
        cv2.circle(display_img, (x, y), 3, current_color, 1)

        # 2. 获取该位置的RGB值（OpenCV存储的是BGR格式）
        bgr_value = img[y, x]  # 从原图获取颜色值
        # 转换为RGB格式显示
        rgb_value = (bgr_value[2], bgr_value[1], bgr_value[0])
        # 控制台打印圆心坐标和RGB值
        print(f"圆心坐标: ({x}, {y})")
        print(f"RGB值: {rgb_value}")
        print("-" * 40)
    elif event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_LBUTTON:
        # 鼠标左键拖动时画线
        if drawing:
            cv2.line(display_img, (last_x, last_y), (x, y), current_color, 1)
            last_x, last_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:  # 鼠标左键释放
        drawing = False
    elif event == cv2.EVENT_RBUTTONDOWN:  # 鼠标右键按下时清空
        display_img[:] = img[:]  # 恢复原图
        print("已清空所有绘制内容")
# 命名图像窗口
cv2.namedWindow('drawing')
# 为窗口绑定回调函数
cv2.setMouseCallback('drawing', draw)
print("=" * 50)
print("程序说明：")
print("1. 鼠标左键单击图片任意位置")
print("2. 在该位置画空心圆（半径3像素）")
print("3. 控制台打印圆心坐标和RGB值")
print("4. 鼠标左键拖动可以连续画线")
print("5. 按【R】键更改颜色")
print("6. 按【ESC】键或关闭窗口退出")
print("=" * 50)
while True:
    cv2.imshow('drawing', display_img)  # 显示图像
    k = cv2.waitKey(1)
    if k == 27:  # 按【Esc】键时结束循环
        break
    elif k == ord('r') or k == ord('R'):  # 按【R】键更改颜色
        color_index = (color_index + 1) % len(colors)
        current_color = colors[color_index]
        print(f"当前颜色已更改为: {current_color}")

cv2.destroyAllWindows()