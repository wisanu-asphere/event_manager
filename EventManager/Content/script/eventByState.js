
    function getEventByState() {
        console.log('evnets by state jai');
        var labels = [], data = [];
        $.ajax({
            url: 'Home/get_eventsByState?_start=' + startDate.format('YYYY-MM-DD 00:00') + '&_end=' + endDate.format('YYYY-MM-DD 23:59'),
            contentType: 'application/html; charset=utf-8',
            type: 'GET',
            dataType: 'json'
        })
            .done(function (result) {
                //$('#search_result').empty();
                for (var i = 0; i <= (result.length - 1); i++) {

                    labels.push(result[i].DisplayGroup);
                    data.push(result[i].num);
                }
                _success(result)
                function _success(result) {
                    var jsonArray = JSON.parse(JSON.stringify(data));
                    //console.log(labels, jsonArray);

                    var pieChartCanvas = $('#pieChart').get(0).getContext('2d');
                    var pieData = {
                        labels: labels,
                        datasets: [
                            {
                                data: data,
                                backgroundColor: ['#f56954', '#00a65a', '#17a2b8', '#f39c12', '#6c757d']
                            }
                        ]
                    }
                    var pieOptions = {
                        legend: {
                            display: true
                        }
                    }
                    var pieChart = new Chart(pieChartCanvas, {
                        type: 'doughnut',
                        data: pieData,
                        options: pieOptions
                    })

                }
            })
            .fail(function (xhr, status) {
                console.log(status);

            });
    }
