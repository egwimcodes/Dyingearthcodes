$(function () {
	"use strict";

// chart 1
var options = {
    series: [{
        name: 'Sessions',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 257]
    }],
    chart: {
        type: 'area',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#8833ff',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#ffc107"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 2.5,
        curve: 'smooth'
    },
    colors: ["#ffc107"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart1"), options);
chart.render();



// chart 2
var options = {
    series: [{
        name: 'Total Users',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 257]
    }],
    chart: {
        type: 'bar',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#f41127',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#f41127"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '40%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 2.5,
        curve: 'smooth'
    },
    colors: ["#00ff00"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart2"), options);
chart.render();


// chart 3
var options = {
    series: [{
        name: 'Page Views',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 257]
    }],
    chart: {
        type: 'line',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#ffc107',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#ffc107"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 2.5,
        curve: 'smooth'
    },
    colors: ["#ffc107"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart3"), options);
chart.render();



// chart 4
var options = {
    series: [{
        name: 'Bounce Rate',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 257]
    }],
    chart: {
        type: 'line',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#0dcaf0',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#0dcaf0"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '40%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 2.4,
        curve: 'smooth'
    },
    colors: ["#ffffff"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart4"), options);
chart.render();




// chart 5
var options = {
    series: [{
        name: 'Avg. Session Duration',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 957]
    }],
    chart: {
        type: 'line',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#29cc39',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#29cc39"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 2.5,
        curve: 'smooth'
    },
    colors: ["#29cc39"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart5"), options);
chart.render();




// chart 6a
var options = {
    series: [{
        name: 'Sales',
        data: [4, 8, 6, 9, 6, 7, 4, 5, 2.5, 3]
    }],
    chart: {
        type: 'area',
        foreColor: '#9a9797',
        height: 250,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#8833ff',
        },
        sparkline: {
            enabled: false
        }
    },
    markers: {
        size: 0,
        colors: ["#8833ff"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shade: 'light',
            type: 'vertical',
            shadeIntensity: 0.5,
            gradientToColors: ['#fff'],
            inverseColors: false,
            opacityFrom: 0.8,
            opacityTo: 0.5,
            stops: [0, 100]
        }
    },
    colors: ["#8833ff"],
    grid: {
        show: true,
        borderColor: '#ededed',
        //strokeDashArray: 4,
    },
    yaxis: {
        labels: {
            formatter: function (value) {
                return value + "K";
            }
        },
    },
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    
    tooltip: {
        theme: 'dark',
        y: {
            formatter: function (val) {
                return "" + val + "K"
            }
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart6a"), options);
    chart.render();
    


// chart 6b
var options = {
    series: [{
        name: 'Sales',
        data: [4, 8, 6, 9, 6, 7, 4, 5, 2.5, 3]
    }],
    chart: {
        type: 'area',
        foreColor: '#9a9797',
        height: 250,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#8833ff',
        },
        sparkline: {
            enabled: false
        }
    },
    markers: {
        size: 0,
        colors: ["#8833ff"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shade: 'light',
            type: 'vertical',
            shadeIntensity: 0.5,
            gradientToColors: ['#fff'],
            inverseColors: false,
            opacityFrom: 0.8,
            opacityTo: 0.5,
            stops: [0, 100]
        }
    },
    colors: ["#8833ff"],
    grid: {
        show: true,
        borderColor: '#ededed',
        //strokeDashArray: 4,
    },
    yaxis: {
        labels: {
            formatter: function (value) {
                return value + "K";
            }
        },
    },
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    
    tooltip: {
        theme: 'dark',
        y: {
            formatter: function (val) {
                return "" + val + "K"
            }
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart6b"), options);
    chart.render();
    



    // chart 6c
var options = {
    series: [{
        name: 'Sales',
        data: [4, 8, 6, 9, 6, 7, 4, 5, 2.5, 3]
    }],
    chart: {
        type: 'area',
        foreColor: '#9a9797',
        height: 250,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#8833ff',
        },
        sparkline: {
            enabled: false
        }
    },
    markers: {
        size: 0,
        colors: ["#8833ff"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shade: 'light',
            type: 'vertical',
            shadeIntensity: 0.5,
            gradientToColors: ['#fff'],
            inverseColors: false,
            opacityFrom: 0.8,
            opacityTo: 0.5,
            stops: [0, 100]
        }
    },
    colors: ["#8833ff"],
    grid: {
        show: true,
        borderColor: '#ededed',
        //strokeDashArray: 4,
    },
    yaxis: {
        labels: {
            formatter: function (value) {
                return value + "K";
            }
        },
    },
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    
    tooltip: {
        theme: 'dark',
        y: {
            formatter: function (val) {
                return "" + val + "K"
            }
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart6c"), options);
    chart.render();
    


    // chart 6d
var options = {
    series: [{
        name: 'Sales',
        data: [4, 8, 6, 9, 6, 7, 4, 5, 2.5, 3]
    }],
    chart: {
        type: 'area',
        foreColor: '#9a9797',
        height: 250,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#8833ff',
        },
        sparkline: {
            enabled: false
        }
    },
    markers: {
        size: 0,
        colors: ["#8833ff"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
        curve: 'smooth'
    },
    fill: {
        type: 'gradient',
        gradient: {
            shade: 'light',
            type: 'vertical',
            shadeIntensity: 0.5,
            gradientToColors: ['#fff'],
            inverseColors: false,
            opacityFrom: 0.8,
            opacityTo: 0.5,
            stops: [0, 100]
        }
    },
    colors: ["#8833ff"],
    grid: {
        show: true,
        borderColor: '#ededed',
        //strokeDashArray: 4,
    },
    yaxis: {
        labels: {
            formatter: function (value) {
                return value + "K";
            }
        },
    },
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    },
    
    tooltip: {
        theme: 'dark',
        y: {
            formatter: function (val) {
                return "" + val + "K"
            }
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart6d"), options);
chart.render();

    


// chart 7
var options = {
    series: [{
        name: 'New Visitors',
        data: [66, 76, 85, 101, 65, 87, 105, 91, 86]

    }, {
        name: 'Old Visitors',
        data: [55, 44, 55, 57, 56, 61, 58, 63, 60]
    }],
    chart: {
        foreColor: '#9ba7b2',
        type: 'bar',
        height: 260,
        stacked: false,
        toolbar: {
            show: false
        },
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    legend: {
        show: false,
        position: 'top',
        horizontalAlign: 'left',
        offsetX: -20
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
        colors: ['transparent']
    },
    colors: [ "#8833ff", '#cba6ff'],
    yaxis: {
        labels: {
            formatter: function (value) {
                return value + "K";
            }
        },
    },
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
    },
    grid: {
        show: true,
        borderColor: '#ededed',
        //strokeDashArray: 4,
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        y: {
            formatter: function (val) {
                return "" + val + "K"
            }
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart7"), options);
chart.render();



// chart 8
var options = {
    series: [{
        name: 'Sessions',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 257]
    }],
    chart: {
        type: 'bar',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#8833ff',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#8833ff"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
       // curve: 'smooth'
    },
    colors: ["#8833ff"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart8"), options);
chart.render();



// chart 9
var options = {
    series: [{
        name: 'Sessions',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 257]
    }],
    chart: {
        type: 'area',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#f41127',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#f41127"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
       // curve: 'smooth'
    },
    colors: ["#f41127"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart9"), options);
chart.render();


// chart 10
var options = {
    series: [{
        name: 'Sessions',
        data: [414, 555, 257, 901, 613, 727, 414, 555, 257]
    }],
    chart: {
        type: 'area',
        height: 60,
        toolbar: {
            show: false
        },
        zoom: {
            enabled: false
        },
        dropShadow: {
            enabled: false,
            top: 3,
            left: 14,
            blur: 4,
            opacity: 0.12,
            color: '#17a00e',
        },
        sparkline: {
            enabled: true
        }
    },
    markers: {
        size: 0,
        colors: ["#17a00e"],
        strokeColors: "#fff",
        strokeWidth: 2,
        hover: {
            size: 7,
        }
    },
    plotOptions: {
        bar: {
            horizontal: false,
            columnWidth: '45%',
            endingShape: 'rounded'
        },
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        show: true,
        width: 3,
       // curve: 'smooth'
    },
    colors: ["#17a00e"],
    xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    },
    fill: {
        opacity: 1
    },
    tooltip: {
        theme: 'dark',
        fixed: {
            enabled: false
        },
        x: {
            show: false
        },
        y: {
            title: {
                formatter: function (seriesName) {
                    return ''
                }
            }
        },
        marker: {
            show: false
        }
    }
};
var chart = new ApexCharts(document.querySelector("#chart10"), options);
chart.render();



// chart 12
	Highcharts.chart('chart12', {
		chart: {
            width: '190',
            height: '190',
			plotBackgroundColor: null,
			plotBorderWidth: null,
			plotShadow: false,
			type: 'pie',
			styledMode: true
		},
		credits: {
			enabled: false
		},
        exporting: {
			buttons: {
				contextButton: {
					enabled: false,
				}
			}
		},
		title: {
			text: ''
		},
		tooltip: {
			pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
		},
		accessibility: {
			point: {
				valueSuffix: '%'
			}
		},
		plotOptions: {
			pie: {
				allowPointSelect: true,
				cursor: 'pointer',
				dataLabels: {
					enabled: false
				},
				showInLegend: false
			}
		},
		series: [{
			name: 'Users',
			colorByPoint: true,
			data: [{
				name: 'Male',
				y: 61.41,
				sliced: true,
				selected: true
			}, {
				name: 'Female',
				y: 11.84
			}]
		}]
	});




 // world map
	
 jQuery('#geographic-map').vectorMap({
    map: 'world_mill_en',
    backgroundColor: 'transparent',
    borderColor: '#818181',
    borderOpacity: 0.25,
    borderWidth: 1,
    zoomOnScroll: false,
    color: '#009efb',
    regionStyle: {
        initial: {
            fill: '#6c757d'
        }
    },
    markerStyle: {
        initial: {
            r: 9,
            'fill': '#fff',
            'fill-opacity': 1,
            'stroke': '#000',
            'stroke-width': 5,
            'stroke-opacity': 0.4
        },
    },
    enableZoom: true,
    hoverColor: '#009efb',
    markers: [{
        latLng: [21.00, 78.00],
        name: 'I Love My India'
    }],
    series: {
        regions: [{
            values: {
                IN: '#29cc39',
                US: '#8833ff',
                CN: '#f41127',
                CA: '#e91e63',
                AU: '#ffd200'
            }
        }]
    },
    hoverOpacity: null,
    normalizeFunction: 'linear',
    scaleColors: ['#b6d6ff', '#005ace'],
    selectedColor: '#c9dfaf',
    selectedRegions: [],
    showTooltip: true,
    onRegionClick: function (element, code, region) {
        var message = 'You clicked "' + region + '" which has the code: ' + code.toUpperCase();
        alert(message);
    }
});





});