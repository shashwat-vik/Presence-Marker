$(document).on('change', 'select', function() {
    $('.updated_number').html($('.hund').val()*100 +$('.ten').val()*10 + $('.zero').val()*1);
});
