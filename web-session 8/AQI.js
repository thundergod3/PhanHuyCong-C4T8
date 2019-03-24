function run() {
        var SearchBar = document.getElementById('search_bar');
        var newCity = SearchBar.value;
        var url = `https://wind.waqi.info/nsearch/full/${newCity}?n=4`;
        var BodyTable = document.getElementById('bodyTable');
        BodyTable.innerHTML = `<div id='loading_img'><img src='loading.gif' ></img></div>`
        
        sendGetRequest(url, function(responseData) {
            BodyTable.innerHTML = ''
            for(var i = 0; i < responseData.results.length; i ++) {    
                var city = responseData.results[i].n;
                var aqi = responseData.results[i].s.a;
                var time = responseData.results[i].s.t;   
                var color;
                if (aqi == '-') {
                    color = 'color_aqi_no';
                }
                else if (aqi > 1 && aqi <= 50) {
                    color = 'color_aqi_good';
                }
                else if (aqi <= 100) {
                    color = 'color_aqi_normal'
                }
                else if (aqi <= 150) {
                    color = 'color_aqi_less_bad'
                }
                else if (aqi <= 200) {
                    color = 'color_aqi_bad'
                }
                else if (aqi <= 300) {
                    color = 'color_aqi_very_bad'
                }
                else if (aqi <= 500) {
                    color = 'color_aqi_supper_bad'
                }

                var HTMLifm = `
                    <tr id='table'>
                        <td class='mouseover'>${city}</td>
                        <td class='${color}'>${aqi}</td>
                        <td class='mouseover'>${time == null ? '' : time}</td>
                    </tr>
                `
                BodyTable.insertAdjacentHTML('afterbegin', HTMLifm)
            }
        })
}
function setupEvents() {
    var btnSearch = document.getElementById('btn_search');
    btnSearch.addEventListener('click', run)
}

setupEvents()

var searchButton = document.getElementById('search_bar');
searchButton.addEventListener('keyup', function(e) {
    if(e.keyCode == 13) {
        run()
    }
})