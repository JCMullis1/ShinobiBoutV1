const didYou = document.getElementById("didyou")
let gameOn = false

const game = {
    init: () => {
        let myMatrix = []
        for (i = 0; i < 100; i++) {
            myMatrix.push([])
            for (j = 0; j < 100; j++) {
                myMatrix[i].push(null)
            }
        }    
        // logic after matrix creation
        
    }
}

const app = {
    baseURL: 'http://127.0.0.1:5500/venvdir/index.html',
    init: () => {
        document.addEventListener('DOMContentLoaded', app.getData);
        console.log('HTML loaded')
    },
    getData: () => {
        //based on the current page ...
        let page = document.body.id;
        switch (page) {
            case 'home':
                document.getElementById("open-btn").addEventListener("click", function() {
                    if (gameOn === false) {
                        gameOn = true
                        window.open("bout.html")
                    } else {
                        didYou.innerText = "Game is in progress"
                        console.log('bool value "gameOn" is set to true')
                    }
                })
                break;
            case 'bout':
                console.log('youre in another page now')
                
        }
    },
}


 
// takes the opposing players as arguments 
function testFight(p1, p2) {
    
}

app.init()
  