function trimText(str ,wordCount){
    var strArray = str.split(' ');
    var subArray = strArray.slice(0, wordCount);
    var result = subArray.join(" ");
    return result + '...';
}

var str = $('div .summary').text();
var result = trimText(str, 10);
$('div .summary').text(result);