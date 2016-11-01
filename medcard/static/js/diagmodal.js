/*!
 * for human diagnosis
 *
 * Mikhail Zavyalov
 *
 * Date: 2016-10-26
 */


$(document).ready(function(){
    $(".open-diagmodal").click(function() {
        var id = $(this).data('id');
        $.get("diagstree/" + id)
        .done(function(data) {
        $('#diagmodal-content').html(data)
        if (id != ''){
            var d_id = $('#id_diags').val();
            $('input[value=' +d_id+ ']').parents('a[data-toggle="collapse"]').removeClass('collapsed');
            $('input[value=' +d_id+ ']').parents('ul.collapse').toggleClass('collapse in');
            $('input[value=' +d_id+ ']').attr("checked", true);
        }
        })
        $("#diag-modal").modal('show');
    });
    $(".diag-del").click(function() {
        var id = $(this).data('id');
        var _this = $(this).closest('tr');
        swal({
            title: "Вы уверены?",
            text: "Удаленный диагноз невозможно будет восстановить!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Да, удалить",
            cancelButtonText: "Отменить",
            closeOnConfirm: false
        },
        function(){
            $.ajax({
                url: "diagdel/",
                type: 'POST',
                data: {
                    "diag_id": id,
                },
// Сообщение после удаления
                success: function() {
                    swal({
                        title: "",
                        text: "Диагноз удален",
                        type: "success",
                    },
                    function(){
                        _this.remove();
                    })
                },
// CSRF механизм защиты Django
                beforeSend: function(xhr, settings) {
                    console.log('-------------before send--');
                    function getCookie(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '') {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++) {
                                var cookie = jQuery.trim(cookies[i]);
                            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                    }
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                }
            });// ajax
        });
    });

    $("#diag-modal").on('shown.bs.modal', function(){

        var chooseDate = $('#d_date').datepicker({
		    format: 'dd.mm.yyyy'
	    }).on('changeDate', function(ev){  // Hidden calendar
	        chooseDate.hide();
	    }).data('datepicker');

        $(".diagmodal-success").click(function(){

        var id = $('#relation_id').val();
        var diags_id = $('input[name=radio]:checked').val();
        var tempDate = $('#d_date').val().split('.');
        var error = '';
        if ((tempDate == '')||(diags_id == '')){
            error = 'Укажите диагноз и дату постановки диагноза!';
            swal("Предупреждение!", error, "warning");
        }
        var diags_date = tempDate[2]+'-'+tempDate[1]+'-'+tempDate[0];
        if (!error) {
            $.ajax({
                url: "diagstree/" + id,
                type: 'POST',
                data: {
                    "diags_id": diags_id,
                    "diags_date": diags_date,
                },
                error: function() {
                    swal(
                    {
                        title: "",
                        text: "Ошибка получения запроса",
                        type: "warning",
                    });
                },
// При успехе выводим сообщение
                success: function() {
                    $("#diag-modal").modal('toggle');
                    swal({
                        title: "",
                        text: "Данные успешно изменены",
                        type: "success",
                    },
                    function(){
                        location.reload(true);
                    })
                },
// CSRF механизм защиты Django
                beforeSend: function(xhr, settings) {
                    console.log('-------------before send--');
                    function getCookie(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '') {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++) {
                                var cookie = jQuery.trim(cookies[i]);
                            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                    }
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                }
            });// ajax

        }


        })

    });

})
