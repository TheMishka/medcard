/*!
 * Modal for human documents
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
    $("#doc-modal").on('shown.bs.modal', function(){
        $(".modal-success").click(function(){
        var id = $(this).data('id');
        var doc_type = $('input[name=document_type]').val();
        var doc_number = $('input[name=document_number]').val();
        var doc_date = $('input[name=document_date]').val();
        var error = '';
        if ((doc_number == '') || (doc_type == '') || (doc_date == '')){
            error = 'Заполните все поля!';
            alert(error);
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
                    alert('Ошибка получения запроса');
                },
// При успехе выводим сообщение
                success: function(data) {
                    alert("Данные успешно изменены");
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
                            // Does this cookie string begin with the name we want?
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
        return false;

        })
    });
//    $("#doc-modal").modal('toggle');

})
