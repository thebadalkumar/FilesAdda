function getFileInfo() {
    var x = document.getElementById('id_file')
    fname = x.files[0].name;
    size = x.files[0].size;
    type = x.files[0].type;
    if (size > 1073741824) { // 1 GB limit
        Swal.fire(
            'Info!',
            `File ${fname} of type ${type} is too big`,
            'success'
        )
        document.getElementById('file-upload-frm').reset();
        return false;
    }
    $("#id_title").val(fname.split(".")[0]);
    $('#fileName').html("File Name: " + fname)
    $('#fileSize').html("File Size: " + size)
    $('#fileType').html("File Type: " + type)
    $("#fileName").removeClass('hide-me')
    $("#fileSize").removeClass('hide-me')
    $("#fileType").removeClass('hide-me')
}

$(document).on("change", "#id_file", function() {
    getFileInfo();
})

var csrfcookie = function() {
    var cookieValue = null,
        name = 'csrftoken';
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};