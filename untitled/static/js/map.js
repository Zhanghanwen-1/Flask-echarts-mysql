window.init = function(){
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