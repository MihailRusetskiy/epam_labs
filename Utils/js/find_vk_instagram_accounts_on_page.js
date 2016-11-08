/*
Возвращает коллекцию аккаунтов на странице
аргументы:
    table_id   id обрабатываемой талицы
*/
function find(table_id){ 
    
    var rows = $("#" + table_id).find("tbody").find("tr"); //получаем коллекцию tr таблицы 
    var account = "";      
    
    rows.each(function(){  //в цикле парсим строки таблицы и вытягиваем из них значеия
        account = $(this).find("td").eq(0).text(); 
    });  
           
    return account;
}