/* global Chart:false */
var startDate = moment().subtract(7, 'days');
var endDate = moment();

$(function () {
    'use strict'
   
    console.log('layout reday 14:07');

    $('#reservation').daterangepicker({
        startDate: startDate,
        endDate: endDate,
        locale: {
            format: 'DD/MM/YYYY',
        }
    },
        function (start, end) {
            console.log("Callback has been called!");
            //$('#reportrange span').html(start.format('D MMMM YYYY') + ' - ' + end.format('D MMMM YYYY'));
            startDate = start;
            endDate = end;
            getTop5Event();
            getTagCount();
            getEventByState();
            getActive();
            getClose();
            getListTagEvent();
            getTagMember();
            getComplinceTotal();
            getComplinceByArea();
        })

    //summary tag
    getActive();
    getClose();
    getTagCount();
    getTagMember();
    getTop5Event();
    getEventByState();
   
    //getjQueryKnob();
    getComplinceTotal();
    getComplinceByArea();
    getListTagEvent();
    //setInterval(getTop5Event, 60000);
    //setInterval(getEventByState, 70000);
    //setInterval(getActive, 50000);
    //setInterval(getClose, 55000);
    //setInterval(getTagCount, 60000);
    //setInterval(getTagMember, 60000);
    //setInterval(getListTagEvent, 60000);

    var i = 0;
    var c = 28500;
    function getRndInteger(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }
    function getActive() {
        //console.log('getActive');
        var url = "/Home/getActive?_start=" + startDate.format('YYYY-MM-DD 00:00') + "&_end=" + endDate.format('YYYY-MM-DD 23:59');
        $.get(url, null, function (data) {
            $("#ShowAcive").text(data);
        });
    }
    function getClose() {
        //console.log('getClose');
        var url = '/Home/getClose?_start=' + startDate.format('YYYY-MM-DD 00:00') + '&_end=' + endDate.format('YYYY-MM-DD 23:59');
        $.get(url, null, function (data) {
            $("#ShowClosed").text(data);
            //console.log(getClose);
        });
    }
    function getTagCount() {
        console.log("getTagCount");
        var url = '/Home/getTagCount?_start=' + startDate.format('YYYY-MM-DD 00:00') + '  &_end=' + endDate.format('YYYY-MM-DD 23:59');
        $.get(url, null, function (data) {
            $("#TagCount").text(data);
            //console.log("getTagCount");
        });
    }
    function getTagMember() {
        //console.log("getTagMember");
        var url = "/Home/getTagMember?_start=" + startDate.format('YYYY-MM-DD 00:00') + "&_end=" + endDate.format('YYYY-MM-DD 23:59');
        $.get(url, null, function (data) {
            $("#TagMember").text(data);
            //console.log("getTagMember");
        });
    }

    function getComplinceTotal() {
        console.log("getComplinceTotal");
        var url = "/Home/get_ComplinceTotal?_start=" + startDate.format('YYYY-MM-DD 00:00') + "&_end=" + endDate.format('YYYY-MM-DD 23:59');
        $("#ComplianceTotal").val(0);
        $.get(url, null, function (data) {
            $("#ComplianceTotal").val(data);
            //$("#TagCount").text("COMPLIANCE " + data + " %");
            $('#ComplianceTotal').trigger('change');

            //$('#ComplianceTotal').bind('change', function () { alert('Click on igo ID'); });
        });
    }

    function getComplinceByArea() {
        console.log("get_ComplinceByArea");
        var url = "/Home/get_ComplinceByArea?_start=" + startDate.format('YYYY-MM-DD 00:00') + "&_end=" + endDate.format('YYYY-MM-DD 23:59');
        //var labels = [], data = [];
        var str="";
        $.get(url, null, function (data) {
           console.log(data);
            for (var i = 0; i <= (data.length - 1); i++) {

                //labels.push(data[i].area);
                //data.push(data[i].percentComplince);
                console.log(data[i].area);
                console.log(data[i].percentComplince);
                str += ' <div class="progress-group"> Area:' + data[i].area 
                    + '  <span class="float-right">'+ data[i].percentComplince+'%</span>'
                    +    '<div class="progress progress-sm">'
                    + '<div class="progress-bar bg-primary" style="width: ' + data[i].percentComplince+'%"></div>'
                    +    '</div>'
                    + '</div >';
            }

            $("#complianceByArea").html(str);
        });
    }

    function getListTagEvent() {
        var url = "/Home/get_eventsLog?_start=" + endDate.format('YYYY-MM-DD 00:00') + "&_end=" + endDate.format('YYYY-MM-DD 23:59') +"&limit=2000";
        console.log('list tag event');
        //var url = "Home/getTagMember?_start=" + startDate.format('YYYY-MM-DD 00:00') + "&_end=" + endDate.format('YYYY-MM-DD 23:59');
       //var $table = $('#table_ListTag').DataTable();
        //$.fn.dataTable.moment('DD-MMM-Y HH:mm:ss');
        $.ajax({
            url: url,
            contentType: 'application/html; charset=utf-8',
            type: 'GET',
            dataType: 'json'
        })
            .done(function (result) {
                //console.log(JSON.parse(JSON.stringify(result)));
                //tag_name state_start	event_start	state_end event_end	lastmodify last_value
                $('#table_ListTag').DataTable({
                    //"paging": true,
                    //"lengthChange": true,
                    //"searching": true,
                    //"ordering": true,
                    //"info": true,
                    //"autoWidth": true,
                    //"responsive": true,
                    "processing": true,
                    //"serverSide": true,
                    destroy: true,
                    data: JSON.parse(JSON.stringify(result)),
                    columns: [
                        { "data": "tag_name" },
                        { "data": "state_start" },
                        {
                            "data": "event_start",
                            render: function (d) {
                                return moment(d).format('DD-MM-YYYY hh:mm:ss');
                            } },
                        { "data": "state_end" },
                        {
                            "data": "event_end",
                            render: function (d) {
                                return moment(d).format('DD-MM-YYYY hh:mm:ss');
                            }},
                        {
                            "data": "lastmodify",
                            render: function (d) {
                                return moment(d).format('DD-MM-YYYY hh:mm:ss');
                            }
                        },
                        { "data": "last_value" }
                    ]
                });
            })
            .fail(function (xhr, status) {
                console.log(status, xhr);
            });
    }
})
