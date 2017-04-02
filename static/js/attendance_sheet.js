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
    })
});

var fun = function(data) {
    for(var i=0; i<data.length; ++i)
        $(".child_panels #"+String(data[i])).click()
};

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
        url: "/poll",
        cache: false,
        success: function(data, status, xhr) {
            data = $.parseJSON(data)
            if (data.status == 106) {
                update_sheet(data.data);
                update_server(data);
            }
            else { console.log(data.status); }
        },
        timeout: 500
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
        url: "/delete",
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
