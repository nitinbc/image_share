$(function(){

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
    };

  $("btn-like").click(function(){
  	if (liked) {
  		num = -1;
  	}
  	else{
  		num= 1;
  	}
  	var span = $(this);
  	var csrftoken = getCookie('csrftoken');
  	var pic_id = $(this).attr("pic-id");
  	// var flag=true;

  	$.ajax({
  		url:'',
  		data:{
  			"num": num,
  			"pic_id": pic_id,
  			'csrfmiddlewaretoken': csrftoken,
  		},
  		type:'post',
  		cache:'false',
  		success: function(data){
  			if (num == 1){
  				liked =true;
  				$(span).removeClass('btn-default')
  				.addClass('btn-primary')
  				if ($("btn-dislike").hasClass('btn-primary')){
  					$('btn-dislike').removeClass('btn-primary')
  					.addClass('btn-default');
  				}
  				else{return;}
  			}
  			else {
  				$(span).removeClass("btn-primary")
  				.addClass("btn-default")
  			}
  		}

  	});
  });

  $("btn-dislike").click(function(){

  	if (disliked) {
  		num = 1;
  	}
  	else{
  		num= -1;
  	}
  	var span = $(this);
  	var csrftoken = getCookie('csrftoken');
  	var pic_id = $(this).attr("pic-id");
  	// var flag=true;

  	$.ajax({
  		url:'',
  		data:{
  			"num": num,
  			"pic_id": pic_id,
  			'csrfmiddlewaretoken':csrftoken,
  		},
  		type:'post',
  		cache:'false',
  		success: function(data){
  			if(num == -1){
  				$(span).
  			}

  		}
  	});

  });


});