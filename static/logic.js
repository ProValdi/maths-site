
$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: data,
        dataType: "text",
        success: function (data) {
            let length = data.split(/\r\n|\n/).length - 1;
            (elem = []).length = length;
            elem.fill(0);

            for (let i = 1; i <= length; i++) {
                console.log("rect" + i)
                console.log(typeof ("rect" + i))
                console.log(document.getElementById("rect" + i))

                elem[i] = document.getElementById("rect" + i)

                document.getElementById("rect" + i).addEventListener('click', function (event) {
                    addLogicOfListener(i);
                }, false);
            }
        }
    });
});

function addLogicOfListener(index) {
    document.getElementById("txt" + index + "-1").style = "display:none; font-size: 2.1em; font-weight: normal;";
    document.getElementById("txt" + index + "-2").style = "font-size: 2.1em; font-weight: normal;";
    setTimeout(() => {
        document.getElementById("txt" + index + "-1").style = "font-size: 2.1em; font-weight: normal;";
        document.getElementById("txt" + index + "-2").style = "display:none; font-size: 2.1em; font-weight: normal;";
    }, 4000);
}

