# 粉色旋转玫瑰 · 祝福弹窗

- Canvas 粉色玫瑰持续旋转 + 爱心粒子 + 光环
- 先展示动画，随后依次弹出祝福（可编辑）
- Python 本地预览；可用 GitHub Pages 一键上线

## 本地运行
```
python rose/app.py
```
浏览器会自动打开，手机同局域网可访问终端提示地址。

## 修改祝福
编辑 `rose/public/index.html` 中：
```js
const wishes = [
  '田梦莹宝宝，送你一束粉色旋转玫瑰，愿你被温柔围绕 ✨',
  '好好吃饭，照顾好自己，能量满满！',
  '天天开心，所念皆如愿，所行皆坦途。',
  '天气冷了记得添衣服，别感冒啦～',
];
```

## GitHub Pages 部署
1. 在 GitHub 新建一个空仓库（Public）
2. 在 `rose/` 目录初始化并推送：
```
cd rose
git init
git add .
git commit -m "init: pink rose"
git branch -M main
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git push -u origin main
```
3. 仓库 Settings → Pages，Source 选择 “GitHub Actions”
4. Actions 里 “Deploy Rose to GitHub Pages” 变绿后，Pages 页面会显示可访问链接

> 提示：工作流已设置发布 `rose/public` 为站点根目录。
