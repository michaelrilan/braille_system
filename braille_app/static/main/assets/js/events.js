runSpeechRecog = () => {
    var txt_content = document.getElementById("content");
    txt_content.placeholder = "Loading text...";
    txt_content.readOnly = true;
    
    var output = document.getElementById('content');
    var action = document.getElementById('action');
    let recognization = new webkitSpeechRecognition();
    recognization.onstart = () => {
       action.placeholder = "Listening...";
    }
    recognization.onresult = (e) => {
       var transcript = e.results[0][0].transcript;
       output.innerHTML = transcript;
       output.classList.remove("hide")
       action.innerHTML = "";
       txt_content.readOnly = false;
       txt_content.placeholder = "Type Something...";

    }
    recognization.start();
 }

// GRAMMAR CHECKER REQUEST

 $(document).ready(function () {
    $("#grammar_btn").click(function () {
      var inputData = $("#content").val();
      $("body").addClass("loading"); // Show loader
        $.ajax({
          type: "POST",
          url: "/grammar_check/",
          data: {
            text: inputData,
            csrfmiddlewaretoken: '{{ csrf_token }}' // Include CSRF token
          },
          success: function (responseData) {
            $("#content").val("");
            console.log(responseData.corrected_text);
            $("#content").val(responseData.corrected_text); // Use .text() for longer text
          },
          error: function (xhr, status, error) {
            console.error("AJAX request failed:", status, error);
          },
          complete: function() {
            $("body").removeClass("loading"); // Hide loader
          }
        });
      
    });
  });