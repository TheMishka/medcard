/*!
 * DataPicker function
 *
 * Mikhail Zavyalov
 *
 * Date: 2016-09-05
 */
$(function() {
    var chooseDate = $('#id_birthday').datepicker({
		format: 'dd.mm.yyyy'
	}).on('changeDate', function(ev){  /* Hidden calendar */
	    chooseDate.hide();
	}).data('datepicker');

	$('#submit').click(function(){  /* Change data format */
	    var tempDate = $('input[id=id_birthday]').val();
	    if (tempDate != ''){
	        var arrDate = tempDate.split('.');
	        var newDate = arrDate[2]+'-'+arrDate[1]+'-'+arrDate[0];
	        $('#id_birthday').val(newDate);
	    }
	})

});