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
            $(data).insertAfter("#modal-content");
        })
//        $("#modal-content").load("docedit/", {doc_id:id, 'CSRFToken': getCSRFTokenValue()});
        $("#doc-modal").modal('show');
    });
})
