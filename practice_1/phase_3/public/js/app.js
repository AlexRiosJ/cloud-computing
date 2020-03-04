$(document).ready(function () {
  $("#version").html("v0.14");

  $("#searchbutton").click(function (e) {
    displayModal();
  });

  $("#searchfield").keydown(function (e) {
    if (e.keyCode == 13) {
      displayModal();
    }
  });

  function displayModal() {
    $("#myModal").modal('show');

    $("#status").html("Searching...");
    $("#dialogtitle").html("Search for: " + $("#searchfield").val());
    $("#previous").hide();
    $("#next").hide();
    $.getJSON('/search/' + $("#searchfield").val(), function (data) {
      renderQueryResults(data);
    });
  }

  $("#next").click(function (e) {

  });

  $("#previous").click(function (e) {

  });


  function renderQueryResults(data) {
    images = [];
    if (data.error != undefined) {
      $("#status").html("Error: " + data.error);
    } else {
      currentIndex = 0;
      $("#status").html("" + data.num_results + " result(s)");
      console.log(data)
      let maxImagesToRender = (data.num_results >= 4) ? 4 : data.num_results;
      // for (i = 0; i < maxImagesToRender; i++) {
      //   images = data.results;
      //   $(`#img${i}`).attr("src", images[i]);
      // }

      for(let i in data.results) {
        $(`#url-${i}`).attr("src", data.results[i]);
      }

      // for (; i <= 3; i++) {
      //   $(`#img${i}`).hide();
      // }

      // if (data.num_results > 4) {
      //   $("#next").show();
      // }

    }
  }
});
