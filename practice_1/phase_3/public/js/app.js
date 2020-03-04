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

  let imagesUrls = [];
  let pageIndex = 0;

  $("#next").click(function (e) {
    pageIndex ++;
    let toRender = imagesUrls.length - pageIndex * 4;

    
    
    $('#url-0').attr("src", '');
    $('#url-1').attr("src", '');
    $('#url-2').attr("src", '');
    $('#url-3').attr("src", '');

    for (let i = pageIndex * 4; i < imagesUrls.length; i++) {
      console.log(i, imagesUrls)
      $(`#url-${i - 4}`).attr("src", imagesUrls[i]);
    }

    $("#previous").show();
    if(toRender < 4) $(this).hide();

  });

  $("#previous").click(function (e) {

  });

  function renderQueryResults(data) {
    imagesUrls = [];
    if (data.error != undefined) {
      $("#status").html("Error: " + data.error);
    } else {
      $("#status").html("" + data.num_results + " result(s)");
      
      let toRender = data.num_results >= 4 ? 4 : data.num_results;
      imagesUrls = data.results;

      $('#url-0').attr("src", '');
      $('#url-1').attr("src", '');
      $('#url-2').attr("src", '');
      $('#url-3').attr("src", '');

      for (let i = 0; i < toRender; i++) {
        $(`#url-${i}`).attr("src", data.results[i]);
      }

      if (data.num_results > 4) {
        $("#next").show();
      }

    }
  }
});
