function getAll(callback){
    $.ajax({
        "url": "http://andrewbeatty1.pythonanywhere.com/books",
        "method": "GET", 
        "data":"",
        "dataType":"JSON",
        "success": function(result){
            //console.log(result);
            callback(result)
        },
        "error": function(xhr, status, error){
            console.log("error: "+status+" msg: "+error);
        }
    });
}

function createBook(book,callback){
        //console.log(JSON.stringify(book));
        $.ajax({
            "url": "http://andrewbeatty1.pythonanywhere.com/books",
            "method": "POST", 
            "data":JSON.stringify(book),
            "dataType":"JSON",
            contentType: "application/json; charset=utf-8",
            "success": function(result){
                //console.log(result);
                callback(result)
            },
            "error": function(xhr, status, error){
                console.log("error: "+status+" msg: "+error);
            }
        });
}

function UpdateBook(book, callback){
    //console.log(JSON.stringify(book))
    $.ajax({
        "url": "http://andrewbeatty1.pythonanywhere.com/books/" + encodeURI(book.id),
        "method": "PUT", 
        "data":JSON.stringify(book),
        "dataType":"JSON",
        contentType: "application/json; charset=utf-8",
        "success": function(result){
            //console.log(result);
            callback(result)
        },
        "error": function(xhr, status, error){
            console.log("error: "+status+" msg: "+error);
        }
    });
}

function deleteBook(id, callback){
    $.ajax({
        "url": "http://andrewbeatty1.pythonanywhere.com/books/" + id,
        "method": "DELETE", 
        "data":"",
        "dataType":"JSON",
        contentType: "application/json; charset=utf-8",
        "success": function(result){
            //console.log(result);
            callback(result)
        },
        "error": function(xhr, status, error){
            console.log("error: "+status+" msg: "+error);
        }
    });
}

// Testing code
function processGetAll(result){
    console.log("in process")
    //console.log(result)
    for(book of result){
        console.log(result)

        displayBook = {}
        displayBook.id = book.id
        displayBook.author = book.Author
        displayBook.title = book.Title
        displayBook.price = book.Price

        console.log(displayBook)

    }
}
getAll(processGetAll)

function processCreateResponse(result){
    console.log(result)
}
//var book = {"Title":"Hello World", "Author":"Clare", "Price":123}
//createBook(book, processCreateResponse)

function processUpdateResponse(result){
    console.log(result)
}
//var book = {id:385, "Price":999}
//UpdateBook(book, processUpdateResponse)

function processDeleteResponse(result){
    console.log("in process delete")
    console.log(result)
}
//deleteBook(385, processDeleteResponse)