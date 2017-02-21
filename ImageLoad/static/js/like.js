$(function(){

	$("btn-like").click(function(){
		$(this).toggleClass("liked");

		if ($("btn-dislike").hasAttribute("disliked")){
			$("btn-dislike").toggleClass("disliked");
		}
		else{}
		$.ajax({
			url: "",
			data:{
				"pic_id": pic_id,
  			"csrfmiddlewaretoken": csrftoken,
			}
			cache: false,
			type: 'post',
			success: function(data){
				
			}
		});
	});
});