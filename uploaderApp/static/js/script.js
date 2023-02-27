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
    $('#fileSize').html("File Size: " + size + " Bytes")
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

$(document).on("click", ".logout", function() {
    Swal.fire({
        title: 'Are you sure want to logout?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, logout'
    }).then((result) => {
        if (result.isConfirmed) {
            window.open("/accounts/logout/", "_self")
        }
    })
})


$(document).on(" click ", ".remove-file", function() {
    me = $(this);
    id = me.data("id");
    Swal.fire({
        title: 'Are you sure?',
        text: "You can recover you file from Trash!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                "url": "/remove-files/",
                "type": "POST",
                "data": {
                    "csrfmiddlewaretoken": csrfcookie(),
                    "id": id
                },
                success: function(response) {
                    Swal.fire(
                        'Deleted!',
                        'Your file has been deleted.',
                        'success'
                    )
                    me.parent().parent().parent().parent().remove();
                },
                error: function(error) {
                    console.log(error);
                },
            });
        }
    })
})
$(document).on("click", ".make-fav", function() {
    me = $(this);
    id = me.data("id");
    $.ajax({
        "url": "/make-fav/",
        "type": "POST",
        "data": {
            "csrfmiddlewaretoken": csrfcookie(),
            "id": id,
        },
        success: function(response) {
            if (response["data"]) {
                me.removeClass("fa-heart-o")
                me.addClass("fa-heart")
            } else {
                me.removeClass("fa-heart")
                me.addClass("fa-heart-o")
            }
        },
        error: function(error) {
            console.log(error);
        }
    })
})
$(document).on("click", ".open-file", function() {
    var url = $(this).data("url");
    window.open(`${url}`, '_blank');
})
$(document).on("click", ".share-file", function() {
    url = $(this).data("url");
    base_url = window.location.origin;
    Swal.fire({
        title: 'Shareable Link',
        text: `${base_url}/${url}`,
    })
})

$(document).on("click", ".make-favs", function() {
    me = $(this);
    id = me.data("id");
    $.ajax({
        "url": "/make-fav/",
        "type": "POST",
        "data": {
            "csrfmiddlewaretoken": csrfcookie(),
            "id": id,
        },
        success: function(response) {
            me.removeClass("fa-heart")
            me.addClass("fa-heart-o")
            me.parent().parent().remove();
        },
        error: function(error) {
            console.log(error);
        }
    })
})

$(document).on(" click ", ".delete-file", function() {
    me = $(this);
    id = me.data("id");
    Swal.fire({
        title: 'Are you sure?',
        text: "You won 't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                "url": "/del-files/",
                "type": "POST",
                "data": {
                    "csrfmiddlewaretoken": csrfcookie(),
                    "id": id
                },
                success: function(response) {
                    Swal.fire(
                        'Deleted!',
                        'Your file has been deleted.',
                        'success'
                    )
                    me.parent().parent().remove();
                },
                error: function(error) {
                    console.log(error);
                },
            });
        }
    })
})
$(document).on("click", ".restore-file", function() {
    me = $(this);
    id = me.data("id");
    $.ajax({
        "url": "/restore-file/",
        "type": "POST",
        "data": {
            "csrfmiddlewaretoken": csrfcookie(),
            "id": id,
        },
        success: function(response) {
            me.removeClass("fa-heart")
            me.addClass("fa-heart-o")
            me.parent().parent().remove();
        },
        error: function(error) {
            console.log(error);
        }
    })
})