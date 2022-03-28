
    function getTop5Event() {
        //var endDate = $("#reservation").data('daterangepicker').endDate;
        //var startDate = $("#reservation").data('daterangepicker').startDate;
        console.log('get_top5Events:' + startDate.format('YYYY-MM-DD') + '&_end=' + endDate.format('YYYY-MM-DD'));
        var DisplayGroup = [], num = [], numOCG = [], tagName = [], numOW = [], numPSV = [];
        var nameOCG = [], nameOW = [], namePSV = [];
        var backgroundColor, borderColor;
        $.ajax({
            url: 'Home/get_top5Events?_start=' + startDate.format('YYYY-MM-DD 00:00') + '&_end=' + endDate.format('YYYY-MM-DD 23:59'),
            contentType: 'application/html; charset=utf-8',
            type: 'GET',
            dataType: 'json'
        })
            .done(function (result) {
                for (var i = 0; i <= (result.length - 1); i++) {
                    DisplayGroup.push(result[i].DisplayGroup);
                    tagName.push(result[i].tag_name);
                    num.push(result[i].numTag_name);
                    if (result[i].DisplayGroup == 'OCG') {
                        numOCG.push(result[i].numTag_name);
                        nameOCG.push(result[i].tag_name);
                    }

                    if (result[i].DisplayGroup == 'OW') {
                        nameOW.push(result[i].tag_name);
                        numOW.push(result[i].numTag_name);
                    }

                    if (result[i].DisplayGroup == 'PSV') {
                        numPSV.push(result[i].numTag_name);
                        namePSV.push(result[i].tag_name);
                    }

                    backgroundColor = '#007bff';
                    setChart($('#OCG-chart'), numOCG, nameOCG, '#17a2b8', backgroundColor, 'OCG');
                    setChart($('#OW-chart'), numOW, nameOW, '#343a40', backgroundColor, 'OW');
                    setChart($('#PSV-chart'), numPSV, namePSV, '#28a745', backgroundColor, 'PSV');
                }
                //console.log(num);
                ////////
                function onlyUnique(value, index, self) {
                    return self.indexOf(value) === index;
                }
                var uniqueDisplayGroup = DisplayGroup.filter(onlyUnique);

                function setChart(obj, data, label, backgroundColor, borderColor, labelSet) {
                    var ticksStyle = {
                        fontColor: '#495057',
                        fontStyle: 'bold'
                    }

                    var mode = 'index'
                    var intersect = true

                    var $salesChart = obj;
                    // eslint-disable-next-line no-unused-vars
                    var salesChart = new Chart($salesChart, {
                        type: 'bar',
                        data: {
                            labels: label,
                            datasets: [
                                {
                                    label: labelSet,
                                    backgroundColor: backgroundColor,
                                    borderColor: borderColor,
                                    data: data
                                }
                            ]
                        },
                        options: {
                            maintainAspectRatio: false,
                            tooltips: {
                                mode: mode,
                                intersect: intersect
                            },
                            hover: {
                                mode: mode,
                                intersect: intersect
                            },
                            legend: {
                                display: true
                            },
                            scales: {
                                yAxes: [{
                                    display: true,
                                    gridLines: {
                                        display: true,
                                        lineWidth: '4px',
                                        color: 'rgba(0, 0, 0, .2)',
                                        zeroLineColor: 'transparent'
                                    },

                                }],
                                xAxes: [{
                                    display: true,
                                    gridLines: {
                                        display: true
                                    },
                                    ticks: ticksStyle
                                }]
                            }
                        }
                    })
                }

                /////////
            })
            .fail(function (xhr, status) {
                console.log(status);

            })
    }
    //end top 5
