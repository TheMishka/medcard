/*!
 * for human documents
 * 
 * Mikhail Zavyalov
 *
 * Date: 2016-09-05
 */


$(document).ready(function(){
    $(".open-modal").click(function() {
        var id = $(this).data('id');
        $.get("docedit/" + id)
        .done(function(data) {
        $('#modal-content').html(data)
        })
        $("#doc-modal").modal('show');
    });
    $(".doc-del").click(function() {
        var id = $(this).data('id');
        var _this = $(this).closest('tr');
        swal({
            title: "Вы уверены?",
            text: "Удаленный документ невозможно будет восстановить!",
            type: "warning",
            showCancelButton: true,
            confirmButtonClass: "btn-danger",
            confirmButtonText: "Да, удалить",
            cancelButtonText: "Отменить",
            closeOnConfirm: false
        },
        function(){
            $.ajax({
                url: "docdel/",
                type: 'POST',
                data: {
                    "doc_id": id,
                },
// Сообщение после удаления
                success: function() {
                    swal({
                        title: "",
                        text: "Документ удален",
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

    $("#doc-modal").on('shown.bs.modal', function(){

        var chooseDate = $('#id_document_date').datepicker({
		    format: 'dd.mm.yyyy'
	    }).on('changeDate', function(ev){  /* Hidden calendar */
	        chooseDate.hide();
	    }).data('datepicker');

        $(".modal-success").click(function(){
        var id = $(this).data('id');
        var doc_type = $('input[name=document_type]').val();
        var doc_number = $('input[name=document_number]').val();
        var tempDate = $('input[name=document_date]').val().split('.');
        var doc_date = tempDate[2]+'-'+tempDate[1]+'-'+tempDate[0];
        var error = '';
        if ((doc_number == '') || (doc_type == '') || (doc_date == '')){
            error = 'Заполните все поля!';
            swal("Предупреждение!", error, "warning");
        }
        if (!error) {
            $.ajax({
                url: "docedit/" + id,
                type: 'POST',
                data: {
                    "doc_id": id,
                    "doc_type": doc_type,
                    "doc_number": doc_number,
                    "doc_date": doc_date,
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
                    $("#doc-modal").modal('toggle');
//                    var this_li = $('ul.nav-tabs').find("li.active");

                    swal({
                        title: "",
                        text: "Данные успешно изменены",
                        type: "success",
                    },
                    function(){
                        location.reload(true);

 /*
                        this_li.css({'backgroundColor': 'red'});


                        $('.nav-tabs .active').removeClass('active');
                        alert('stop');
                        this_li.addClass('active');
                        $("#diags").toggleClass('tab-pane fade in active');
                        $("#docs").toggleClass('tab-pane fade in active'); */
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
