var check_roll = function() {
    start_roll = $(".info2_body [name='start_roll']").val()*1;
    end_roll = $(".info2_body [name='end_roll']").val()*1;
    if ($.isNumeric(start_roll) && $.isNumeric(end_roll))
        if (start_roll < end_roll && start_roll > 0)
            return true;
    return false;
};

$(document).on('change', ".info2_body [name='start_roll']", function() {
    if (check_roll()) {
        if ($("button[value='submit']").attr('disabled')) {
            $("button[value='submit']").removeAttr('disabled');
        }
    }
    else {
        if (!($("button[value='submit']").attr('disabled'))) {
            $("button[value='submit']").attr('disabled', 'disabled');
        }
    }
});
$(document).on('change', ".info2_body [name='end_roll']", function() {
    if (check_roll()) {
        if ($("button[value='submit']").attr('disabled')) {
            $("button[value='submit']").removeAttr('disabled');
        }
    }
    else {
        if (!($("button[value='submit']").attr('disabled'))) {
            $("button[value='submit']").attr('disabled', 'disabled');
        }
    }
});
