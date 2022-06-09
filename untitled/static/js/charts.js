var myChart1 = echarts.init(document.getElementById("chart1"));
var myChart2 = echarts.init(document.getElementById("chart2"));
var myChart3 = echarts.init(document.getElementById("chart3"));
var myChart4 = echarts.init(document.getElementById("chart4"));
var myChart5 = echarts.init(document.getElementById("chart5"));
var myChart6 = echarts.init(document.getElementById("chart6"));
function set_comp(echart,x1,y1,y2,y3,clazz) {
    var charts = {
    unit: '单位(**)',
    names: ['东极','桃花','嵊泗'],
    lineX: x1,
    value: [
        y1,
        y2,
        y3
    ]
}
    echart.setOption({
     title: {
        text: clazz,
        textStyle: {
            fontWeight: 'normal',
            fontSize: 20,
            color: '#F1F1F3'
        },
        left: '45%',
        bottom: '1%'
    },
    backgroundColor:'rgba(1, 22, 53, 1)',
    tooltip: {
        trigger: 'axis'
    },

    legend: {
           top: '4%',
        data: charts.names,
        textStyle: {
            fontSize: 14,
            color: '#FFFFFF'
        },
        right: '4%'
    },
    grid: {
        top: '10%',
        left: '4%',
        right: '4%',
        bottom: '10%',
        containLabel: true
    },
    xAxis: {
        show: true,
        type: 'category',
        boundaryGap: false,
        data: charts.lineX,
        axisLabel: {
            textStyle: {
                color: 'rgb(0,253,255,0.6)'
            },
            formatter: function(params) {
                return params.split(' ')[0] + '\n' + params.split(' ')[1]
            }
        }
    },
    yAxis: {
    show: true,
     splitArea: {
     show: true,
     areaStyle: {
        color:"rgba(1, 22, 53, 1)"
       }
     },
        name: charts.unit,
        type: 'value',
        axisLabel: {
            formatter: '{value}',
            textStyle: {
                color: 'rgb(0,253,255,0.6)'
            }
        },
        splitLine: {
            lineStyle: {
                color: 'rgb(23,255,243,0.3)'
            }
        },

        axisLine: {
            	show:true,
            lineStyle: {
                color: 'rgb(0,253,255,0.6)'
            }
        }
    },
    series: [{
        name: "东极",
        type: 'line',
        itemStyle : {
            normal : {
                color:'#f88307',
                lineStyle:{
                    color:'#f88307'
                }
            }
        },
        smooth: false,
        symbol: 'circle',
        symbolSize: 5,
        data: y1
    },
    {
        name: "桃花",
        type: 'line',
        itemStyle : {
            normal : {
                color:'#15cbf8',
                lineStyle:{
                    color:'#15cbf8'
                }
            }
        },
        smooth: false,
        symbol: 'circle',
        symbolSize: 5,
        data: y2
    },
    {
        name: "嵊泗",
        type: 'line',
        itemStyle : {
            normal : {
                color:'#00FF00',
                lineStyle:{
                    color:'#00FF00'
                }
            }
        },
        // axisLine: {
        //     lineStyle: {
        //         color: '#f007f8'
        //     }
        // },
        // nameTextStyle:{
        //   color:  "#f007f8",
        // },
        smooth: false,
        symbol: 'circle',
        symbolSize: 5,
        data: y3
    }]
});
}



function f1(echart) {
    echart.setOption({
        xAxis: {
            data: ['2017-10-24', '2017-10-25', '2017-10-26', '2017-10-27']
        },
        yAxis: {},
        series: [{
            color: "#31e9ef",
            type: 'k',
            data: [
                [20, 34, 10, 38],
                [40, 35, 30, 50],
                [31, 38, 33, 44],
                [38, 15, 5, 42]
            ]
        }]
    });
}




