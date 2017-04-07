var set_fire;
$(document).ready(function(e) {
    $(".toggle_uncheck").click(function() {
        $(this).toggleClass("toggle_check");
    });
    $('.header_panel .clickable').click();
    $(".monitor-button").click(function() {
        if ($(this).find(".glyphicon-stop").length > 0) {
            console.log("STOPPED");
            clearInterval(set_fire);
        }
        else {
            console.log("STARTED");
            set_fire = setInterval(atomic_step_poll,1000*4);
        }
        $(this).find(".glyphicon-play").toggleClass("glyphicon-stop");
        $(this).find(".glyphicon-play").parent().toggleClass("btn-danger");
    })
});

$(document).on('click', '#checkAll', function (e) {
    if(!$(this).attr('disabled')) {
        x = $('.child_panels').find('.atomic_checkbox')
        var start_roll = x[0].id*1
        var end_roll = x[x.length-1].id*1
        for(var i=start_roll; i <= end_roll; ++i) {
            elem = $(".child_panels #"+String(i)+".atomic_checkbox")
            if (!elem.is(':checked')) {
                elem.parent().find('.atomic_number').click();
            }
        }
    }
    $(this).attr('disabled', 'disabled');
});

$(document).on('click', '.header_panel .clickable', function (e) {
    var $this = $(this);
    if ($this.hasClass('panel-collapsed')) {
        $this.parents('.panel').find('.panel-body').slideDown();
        $this.removeClass('panel-collapsed');
        $this.find('span').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
    } else {
        $this.parents('.panel').find('.panel-body').slideUp();
        $this.addClass('panel-collapsed');
        $this.find('span').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
    }
});

var atomic_step_poll = function() {
    now = new Date().getTime()
    $.ajax({
        url: "/44eee68d93bd9ce7c9eca0047bbdb460/poll",
        cache: false,
        success: function(data, status, xhr) {
            data = $.parseJSON(data)
            if (data.status == 106) {
                update_sheet(data.data);
                update_server(data);
            }
            else { console.log(data.status); }
        },
        timeout: 600
    });
};


var update_sheet = function(data) {
    //console.log(data);
    for(var i=0; i<data.length; ++i) {
        if (!$(".child_panels #"+String(data[i])+".atomic_checkbox").is(':checked'))
            $(".child_panels #"+String(data[i])+".atomic_number").click()
    }
};

var update_server = function(data) {
    $.ajax({
        url: "/44eee68d93bd9ce7c9eca0047bbdb460/delete",
        type: "POST",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify(data),
        success: function(data, status, xhr) {
            data = $.parseJSON(data);
            console.log(data.status);
            console.log(data.data);
        },
        timeout: 1000*2
    });
};
