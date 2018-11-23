var data1 = [0, 0.005, 0.01, 0.015, 0.02, 0.025];
var slider2 = d3.sliderHorizontal()
    .min(0)
    .max(10)
    .step(1)
    .width(300)
    .displayValue(false)
    .on('onchange', val => {
      d3.select("p#value2").text(val);
    });

  var group2 = d3.select("div#slider2").append("svg")
    .attr("width", 500)
    .attr("height", 100)
    .append("g")
    .attr("transform", "translate(30,30)");

  group2.call(slider2);

  d3.select("p#value2").text((slider2.value()));
  d3.select("a#setValue2").on("click", () => { slider2.value(5); d3.event.preventDefault(); });
        