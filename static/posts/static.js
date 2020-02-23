window.onscroll = function() {glue()};


function glue() {
  var search_div = $("#search-id");
  var header = document.getElementById("search-id");
  var sticky = header.offsetTop;
  if (window.pageYOffset > sticky) {
        search_div.css("paddingTop", "50px");
        header.classList.add("sticky");
  } else {
        search_div.css("paddingTop", "0px");
        header.classList.remove("sticky");
  }
};


function send_text_content(){
    textbox = document.getElementById("txt").value;
    if(textbox.length > 2){
        $.ajax({
            type: "POST",
            data: {
                'text': textbox,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            url: '',
            success: function(response){
                window.location.href = "?page=1";
                console.log(response.status);
            },
            error: function (xhr, ajaxOptions, thrownError) {
                console.log("xhr.status: " + xhr.status);
                console.log("thrownError: " + thrownError);
            }
        });
    }
    else{
        document.getElementById("action-div").innerHTML = "<i>You must enter atleast 3 characters!</i>";
    }
}