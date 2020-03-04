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

  async function displayModal() {
    $("#myModal").modal('show');

    $("#status").html("Searching...");
    $("#dialogtitle").html("Search for: " + $("#searchfield").val());
    $("#previous").hide();
    $("#next").hide();
    let urls = [];
    for (let word of $("#searchfield").val().split(' ')) {
      console.log(word)
      await $.getJSON('/search/' + word, function (data) {
        urls.push(data.results);
      });
    }
    urls = [...new Set(urls.flat())];
    let data = {};
    data.results = urls;
    data.num_results = urls.length;
    renderQueryResults(data);
  }

  let imagesUrls = [];
  let pageIndex = 0;

  $("#next").click(function (e) {
    pageIndex++;
    let toRender = imagesUrls.length - pageIndex * 4;

    $('#url-0').attr("src", '');
    $('#url-1').attr("src", '');
    $('#url-2').attr("src", '');
    $('#url-3').attr("src", '');

    for (let i = pageIndex * 4; i < imagesUrls.length; i++) {
      console.log(i, imagesUrls)
      $(`#url-${i - pageIndex * 4}`).attr("src", imagesUrls[i]);
    }

    $("#previous").show();
    if (toRender < 4) {
      $(this).hide();
    }

  });

  $("#previous").click(function (e) {
    pageIndex--;

    $('#url-0').attr("src", '');
    $('#url-1').attr("src", '');
    $('#url-2').attr("src", '');
    $('#url-3').attr("src", '');

    for (let i = pageIndex * 4; i < (pageIndex + 1) * 4; i++) {
      console.log(i, imagesUrls)
      $(`#url-${i - pageIndex * 4}`).attr("src", imagesUrls[i]);
    }

    if (imagesUrls.length > 4) {
      $("#next").show();
    }

    if (pageIndex == 0) {
      $(this).hide();
    }

  });

  function renderQueryResults(data) {
    imagesUrls = [];
    pageIndex = 0;
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
