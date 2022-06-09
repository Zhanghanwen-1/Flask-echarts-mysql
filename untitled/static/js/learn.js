// 已经定义了一个按钮，我们要求点击按钮弹出对话框
// 1.事件三部分：事件源 事件类型 事件处理程序
// (1) 事件源：事件被触发的对象 谁 按钮
var btn = document.getElementById("btn");
//（2）事件类型 如何触发 什么事件 鼠标点击(onlick)、经过(onmouseover)
//(3) 事件处理程序 通过一个函数赋值的方式完成
btn.onclick = function () {
    alert("成功");
    btn.innerHTML = "111";
    //innerText 和 innerHTML 的区别，一个不识别，一个识别html标签
    //去除空格换行  保留格式
}
// 执行事件步骤
// 点击div 控制台输出 我被选中了
// 1.获取事件源