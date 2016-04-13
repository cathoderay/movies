$(document).ready(function() {
    var $divs = $("div.movie"); 

    fixRows = function(sortedDivs) {
        var html = "";
        for(i = 0; i < sortedDivs.length; i++) {
             if (i % 5 == 0) {
                html += "<div class='row'>";
                html += "<div class='col-xs-1'></div>";
            }

            html += sortedDivs[i].outerHTML;

            if ((i + 1) % 5 == 0) {
                html += "<div class='col-xs-1'></div>";
                html += "</div>"
            }
        };
        return html;
    }

    sortAlpha = function(type) {
        var sortedDivs = $divs.sort(function(a,b){
            var va = $(a).find("span").text().toLowerCase();
            var vb = $(b).find("span").text().toLowerCase();
            v = (va < vb) ? -1 : (va > vb) ? 1 : 0;
            return type == 'az' ? v : -v;
        });

        $("#sortable").html(fixRows(sortedDivs));
    }


    $('#alphaBnt').on('click', function(){sortAlpha('az')});
    $('#alphaBntReverse').on('click', function(){sortAlpha('za')});
});
