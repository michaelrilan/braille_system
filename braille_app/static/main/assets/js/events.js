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



