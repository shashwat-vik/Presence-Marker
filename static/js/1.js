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
        error: function(xhr, status, error) {
            console.log("Error  :"+ error);
            console.log("Status :"+ status);
            console.log("XHR    :"+ xhr);
            console.log("I Know.")
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
        timeout: 1000*6
    });
};

var add = function(x) {
    $.ajax({
        url: "/add/"+String(x),
        type: "GET",
        success: function(data, status, xhr) {
            data = $.parseJSON(data);
            console.log(data.status);
            console.log(data.data);
        },
    });
};

var add_all = function() {
    for(var i=1; i<=14; ++i)
        add(i);
}
