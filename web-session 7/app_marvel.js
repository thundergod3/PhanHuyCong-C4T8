//1. Prepare: URL, Private key, Public key, MarvelKey
var URL = 'https://gateway.marvel.com:443/v1/public/characters';
var publicKey = 'aad27be74f3539f6638d944ed13377e5';
var privateKey = 'f89a91c2115a12b99b272e0a5bcd9cbdab147daf';

function fetchCharacterById(id) {
    var key = marvelKey(privateKey, publicKey);
    var fullURL = `${URL}/${id}?${key}`
   
    //3 . Send request, handle response data
    sendGetRequest(fullURL, function (responseData) {
        var characters = responseData.data.results;
        var charactersAfterGet = characters[0];
        var DOMrightSide = document.getElementById('rightSide');
        console.log(charactersAfterGet);
        var newName = charactersAfterGet.name;
        
        var characterHTMLRight = `
            <div id='newName'>${newName}</div>
            
            
            <div id='description'>
                
            </div>
            <div id='comics'>Related comics</div>
            <div id='new_comics' class='new_comics'>

            </div>
            <div id='events'>Related events</div>
            <div id='new_event' class='new_comics'>
            
            </div>

            <div id='new_references'>References</div>
            <div id='references' class='new_comics'>

            </div>
        `;
        DOMrightSide.insertAdjacentHTML('afterbegin', characterHTMLRight);
       
        // DESCRIPTION

        var DOMdescription = document.getElementById('description');
        if ( charactersAfterGet.description == "") {
            DOMdescription.insertAdjacentHTML('afterbegin', '<h8>No description</h8>')
        }
        else {
            var description = charactersAfterGet.description;
            var HTMLdescription = `
                
                <div>${description}</div>
            `
            DOMdescription.insertAdjacentHTML('afterbegin', HTMLdescription)
        }
       
        // COMICS

        var DOMNewComics = document.getElementById('new_comics');
        for (var m = 0; m < charactersAfterGet.comics.items.length; m++) {
            var newComics = charactersAfterGet.comics.items[m].name;
            var HTMLnewComics = `
                <div class='items'> ${newComics} </div>
            `
            DOMNewComics.insertAdjacentHTML('afterbegin', HTMLnewComics)
        }

        // EVENT
        var DOMnewEvents = document.getElementById('new_event');
        if (charactersAfterGet.events.items.length <= 0 ) {
            DOMnewEvents.insertAdjacentHTML('afterbegin', '<p>No events</p>')
        }
        else {
            for (var n = 0; n < charactersAfterGet.events.items.length; n++) {
                var NewEvents = charactersAfterGet.events.items[n].name;

                var HTMLnewEvents = `
                    <div class='items'> ${NewEvents} </div>
                `
                DOMnewEvents.insertAdjacentHTML('afterbegin', HTMLnewEvents)
            }
        }

        // REFERENCES 
        var references = document.getElementById('references');

        // YOUTUBE
        var DOMytb = document.getElementById('references');
        var HTMLytb = `<i id="ytb" class="fab fa-youtube"></i>`;
        DOMytb.insertAdjacentHTML('afterbegin', HTMLytb);
        var ytb = document.getElementById('ytb');
        ytb.addEventListener('click', function(ytb) {
            let URLytb = `https://www.youtube.com/results?search_query=${charactersAfterGet.name}`;
            window.open(URLytb)
        })

        // WIKIPEDIA




        var DOMwiki = document.getElementById('references');
        var HTMLwiki = `<i id='wiki' class="fab fa-wikipedia-w"></i>`;
        DOMwiki.insertAdjacentHTML('afterbegin', HTMLwiki);
        var wiki = document.getElementById('wiki');
        wiki.addEventListener('click', function(wiki) {
            var newString = charactersAfterGet.name.replace(' ', '_');
            var URLwiki = `https://en.wikipedia.org/wiki/${newString}`;
            window.open(URLwiki);
        })

    }); 
}


function renderCharacter(characters) {
    var content = document.getElementById('content');
    content.textContent = '';
    for (var i = 0; i < characters.length; i++) {
        var character = characters[i];
        var imgSrc = character.thumbnail.path + '.' + character.thumbnail.extension;
        var name = character.name;
        var comicsAvailable = character.comics.available;
        

        // HTML, => content
        var characterHTMl = `
        <div >
            <img class = 'img' src='${imgSrc}' id=${character.id}>
            <h2 class='nameBorder'>${name} </h2>
            <h3>Comics: ${comicsAvailable}</h3>
            </img>    
        </div>
        `;

        content.insertAdjacentHTML('beforeend', characterHTMl);
    }
}

function run(characters){
    let moreIFM = document.getElementsByClassName('img');
    for (var j = 0; j < moreIFM.length; j++) {
        moreIFM[j].addEventListener('click', function(event) {
            var noneContainer = document.getElementById('content');
            noneContainer.style.display = 'none';

            var newIMG = event.target.currentSrc;
            var newID = event.target.id;
            fetchCharacterById(newID)
 
            var characterNewHTML = `
            <div id='new_root'>
                <div id='new_content' >
                    <img class ='new_img' src='${newIMG}'></img>
                </div>
                <div id="rightSide" class='new_imf'>
                    
                </div>
            </div>
            `;

            var search_container = document.getElementById('search_container');
            search_container.insertAdjacentHTML('afterend', characterNewHTML);
        })
    }
}


function fetchCharacter() {
    //2. Generate key, key + url => full url
    var key = marvelKey(privateKey, publicKey);
    var fullURL = `${URL}?${key}`
 
    //3 . Send request, handle response data
    sendGetRequest(fullURL, function (responseData) {
        var characters = responseData.data.results;
        renderCharacter(characters);
        run(characters)
    }); 
}

fetchCharacter();

function setupEvents() {
    var btnSearch = document.getElementById('btn_search');
    btnSearch.addEventListener('click', function (e) {
        var searchBar = document.getElementById('search_bar');
        var searchString = searchBar.value;
        var key = marvelKey(privateKey, publicKey);
        var fullURL = `${URL}?${key}`;
        if (searchString != '') {
            fullURL += `&nameStartsWith=${searchString}`;
        } 

        sendGetRequest(fullURL, function (responseData) {
            var characters = responseData.data.results;
            renderCharacter(characters)
            run(characters)
        })
    })
}

var DOMbackBTN = document.getElementById('btn-back');
DOMbackBTN.addEventListener('click', function() {
    console.log('asdasd');
    var newRoot = document.getElementById('new_root');
    var content = document.getElementById('content');
    newRoot.style.display = 'none';
    content.style.display = 'flex';
});

setupEvents();
