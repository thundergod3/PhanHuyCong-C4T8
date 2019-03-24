var url = 'http://jsonplaceholder.typicode.com/posts?fbclid=IwAR1305FM6dv8lWe_tbSe4Hbo1DKTw0flJ2jo3D6igp2Kggbeh4QgzVz88KE';
var bodyTable = document.getElementById('bodytable');
var searchBar = document.getElementById('search_bar');
var table = document.getElementById('table');
function clear() {
    bodyTable.innerHTML = ''
}
function run() {
    sendGetRequest(url, function (responseData) {
        var btn_search = document.getElementById('btn_search');

        function fetchData() {
            clear()
            console.log(bodyTable);

            var fakeData = responseData;
            var listAfterFilter = fakeData.filter(function (el) {
                return el.body.includes(searchBar.value) || el.id === parseInt(searchBar.value);
            })

            for (var i = 0; i < listAfterFilter.length; i++) {
                var id = listAfterFilter[i].id;
                var title = listAfterFilter[i].title;
                var body = listAfterFilter[i].body;
                var HTMLtable = `
                            <tr id='border_container'>
                                <td class = 'border'>${id}</td>
                                <td class = 'border'>${title}</td>
                                <td class = 'border'>${body}</td>
                            </tr>
                    `
                bodyTable.insertAdjacentHTML('beforeend', HTMLtable)
            }
        }
        searchBar.addEventListener('keyup', function (e) {
            if (e.keyCode == 13) {
                console.log('hi');
                fetchData()
            }
        })

        btn_search.addEventListener('click', fetchData)

        // table.innerHTML = '';

    })
}



run()