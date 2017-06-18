function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function comment(){
	var c = document.getElementById("comments").value;
	formData = new FormData();
	formData.append("comment",c);
	formData.append("hash", window.location)
	var csrftoken = getCookie('csrftoken');
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	$.ajax({
		url: "/comment",
		type: "POST",	
		data: formData,
		processData: false,
		contentType: false,
		success: function(data){
			console.log(data['url'])
			window.location = data['url'];				
		},
		error: function(xhr, status, error) {
			console.log("post error!!");
		}
	});	

}

function search(){
	var search = document.getElementById("search_bar").value;
	formData = new FormData();
	formData.append("keyword", search);
	var csrftoken = getCookie('csrftoken');
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	$.ajax({
		url: "/search",
		type: "POST",	
		data: formData,
		processData: false,
		contentType: false,
		success: function(data){
			console.log(data['url'])
			window.location = data['url'];				
		},
		error: function(xhr, status, error) {
			console.log("post error!!");
		}
	});	
}
function favor(id){
	var src = document.getElementById(id).src;
	var res = src.split("/");
	var image = res.pop();
	console.log(image);

	formData = new FormData();
	formData.append("image", image);
	var csrftoken = getCookie('csrftoken');
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	$.ajax({
		url: "/favor",
		type: "POST",
		data: formData,
		processData: false,
		contentType: false,
		success: function(data){
			console.log(data['url'])
			//window.location = data['url'];
		},
		error: function(xhr, status, error) {
			console.log("favor error!!");
		}
	});	
}
function upload(){
	var input = document.getElementById("my_file");
	var hash = document.getElementById("my_hash");
	file = input.files[0];
	formData= new FormData();
	formData.append("image", file);
	formData.append("hash",hash.value);
	var csrftoken = getCookie('csrftoken');
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
	$.ajax({ 
		url: "/upload",
		type: "POST",
		data: formData,
		processData: false,
		contentType: false,
		success: function(data) {
			console.log(data['url'])
			window.location = data['url'];			
		},                
		error: function(xhr, status, error) {
			console.log("post error!!");
		}
	});   
}
function openModal(){
	$('#preview').attr('src', "");
	document.getElementById('id01').style.display='block'
}
function closeModal(){
	document.getElementById('id01').style.display='none';
}
$("document").ready(function(){
    $("#my_file").change(function() {
		if (this.files && this.files[0]) {
			var reader = new FileReader();
			reader.onload = function (e) {
				$('#preview').attr('src', e.target.result);
			}
			reader.readAsDataURL(this.files[0]);
		}
		/*
        var input = document.getElementById("my_file");
        file = input.files[0];
        formData= new FormData();
        formData.append("image", file);
        var csrftoken = getCookie('csrftoken');
		$.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.ajax({ 
            url: "upload",
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                console.log(data);
            },                
            error: function(xhr, status, error) {
                console.log("post error!!");
            }
        });
		*/
    });
});
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
