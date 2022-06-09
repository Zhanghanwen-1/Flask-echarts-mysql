function h_b_f(id,display) {
    // 该函数为隐藏、显示和flex布局,参数均为字符串类型
    document.getElementById(id).style.display=display;
}
function DongJi() {
        document.getElementById("map1").style.display = "none";
        document.getElementById("comp").style.display = "none";
        document.getElementById("location1").style.display = "flex";
}
// 当鼠标点击总览时触发此事件
// 总览地图触发
// 点击对比，显示6个对比图
function total_comp() {
        //隐藏地图
        h_b_f("map1","none");
        // document.getElementById("location1").style.display = "none";
        //显示对比图
        h_b_f("comp","flex");
        // document.getElementById("comp").style.display = "flex";
    //获取全部数据
    $.ajax({
        url:'/comp',
        data:{},
        type:'POST',
        async:false,
        dataType:'json',
        success: function (data) {
            var xtime = [];
            var ytaochl = [];
            var ydongchl = [];
            var yshengchl = [];
            var ytaotd = [];
            var ydongtd = [];
            var yshengtd = [];
            var ytaoph = [];
            var ydongph = [];
            var yshengph = [];
            var ytaodo = [];
            var ydongdo = [];
            var yshengdo = [];
            var ytaowt = [];
            var ydongwt = [];
            var yshengwt = [];
            var ytaosal = [];
            var ydongsal = [];
            var yshengsal = [];
            // 取出数据库每条数据，开始判断我们所需要的数据
            for(var i = 0 ; i < data.ad.length; i++){
                if (data.ad[i] === "桃花"){
                    // xtaolt.add(data.lt);
                    console.log(i);
                    xtime.push(data.lt[i]);
                    ytaochl.push(data.chl[i]);   //桃花岛的chl数据
                    ytaotd.push(data.td[i]);//桃花岛的浊度数据
                    ytaoph.push(data.ph[i]);//桃花岛的ph数据
                    ytaodo.push(data.do[i]);//桃花岛的溶氧量数据
                    ytaowt.push(data.wt[i]);//桃花岛的水温数据
                    ytaosal.push(data.sal[i]);//桃花岛的盐度数据
                }
                if(data.ad[i] === "东极"){
                    console.log(i);
                    ydongchl.push(data.chl[i]);    //东极岛的chl数据
                    ydongtd.push(data.td[i]);//东极岛的浊度数据
                    ydongph.push(data.ph[i]);//东极岛的ph数据
                    ydongdo.push(data.do[i]);//东极岛的溶氧量数据
                    ydongwt.push(data.wt[i]);//东极岛的水温数据
                    ydongsal.push(data.sal[i]);//东极岛的盐度数据
                }
                if(data.ad[i] === "嵊泗"){
                    console.log(i);
                    yshengchl.push(data.chl[i]);
                    yshengtd.push(data.td[i]);
                    yshengph.push(data.ph[i]);
                    yshengdo.push(data.do[i]);
                    yshengwt.push(data.wt[i]);
                    yshengsal.push(data.sal[i]);
                }
            }
            console.log(xtime);
            console.log(ytaochl);
            console.log(ydongchl);
            console.log(yshengchl);
            set_comp(myChart1,xtime,ytaochl,ydongchl,yshengchl,"chl");
            set_comp(myChart2,xtime,ytaotd,ydongtd,yshengtd,"td");
            set_comp(myChart3,xtime,ytaoph,ydongph,yshengph,"ph");
            set_comp(myChart4,xtime,ytaodo,ydongdo,yshengdo,"do");
            set_comp(myChart5,xtime,ytaowt,ydongwt,yshengwt,"wt");
            set_comp(myChart6,xtime,ytaosal,ydongsal,yshengsal,"sal");
            window.onresize = function () {
                myChart1.resize();
                myChart2.resize();
                myChart3.resize();
                myChart4.resize();
                myChart5.resize();
                myChart6.resize();
            }
        }
    })
    }
    //总览全图
function total_map() {
    h_b_f("map1","block");
    h_b_f("comp","none");
    // document.getElementById("map1").style.display = "block";
    // document.getElementById("location1").style.display = "none";
    // var char = document.getElementsByClassName("comp_box"); 类需要用数组取出，较麻烦
    // if(char[0].style.display === ''){
    //     for(var i = 0;i<char.length;i++){
    //         char[i].style.display = "none";
    //     }
    // }
    // document.getElementById("comp").style.display = "none";
    var map = new AMap.Map('map1', {
        center: [122.4499, 30.1180],
        zoom: 9,
        mapStyle: 'amap://styles/9fc4ebbf0b3ffb15d66641c88391ea3c',
    });
    var marker1 = new AMap.Marker({
        position: new AMap.LngLat(122.3037, 29.7747),   // 经纬度对象，如 new AMap.LngLat(116.39, 39.9); 也可以是经纬度构成的一维数组[116.39, 39.9]
        icon: '../static/img/fish.ico',
        title: '桃花'
    });
    var marker2 = new AMap.Marker({
        position: new AMap.LngLat(122.6840, 30.1889),   // 经纬度对象，如 new AMap.LngLat(116.39, 39.9); 也可以是经纬度构成的一维数组[116.39, 39.9]
        icon: '../static/img/fish.ico',
        title: '东极'
    });
    var marker3 = new AMap.Marker({
        position: new AMap.LngLat(122.4684, 30.6955),   // 经纬度对象，如 new AMap.LngLat(116.39, 39.9); 也可以是经纬度构成的一维数组[116.39, 39.9]
        icon: '../static/img/fish.ico',
        title: '嵊泗'
    });
    map.add(marker1);
    map.add(marker2);
    map.add(marker3);
}
    // 总要求：点击东极、桃花、嵊泗默认播放视频，后面选项框的参数要和点击的地点相连接
    // 点击东极后东极高亮，系统连接东极，如果再点击后续选项框可跳转东极数据
    // 否则取消东极高亮
    //1.点击东极，将其他选择器屏蔽，只留下视频

// 如何实现实时显示的思路：也就是监听数据库，当数据库增删改数据之后，echarts能够通过ajax相应重新绘制图表！！！