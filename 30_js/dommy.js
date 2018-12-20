let fib = (n) => {
    if(n < 3){
	return 1;
    }
    return fib(n - 2) + fib(n - 1);
}

itemList = document.getElementById("thelist");

document.getElementById("b").addEventListener("click", function(e){
    let new_li = document.createElement("li");
    new_li.innerHTML = "New list element";
    itemList.appendChild(new_li);
});

itemList.addEventListener("click", function(e){
    e.target.remove();
});


var lis = document.getElementsByTagName("li");
for(var i = 0; i < lis.length; i++){
    lis[i].addEventListener("mouseenter", function(e){
	document.getElementById("h").innerHTML = e.target.innerHTML;
    });
    lis[i].addEventListener("mouseout", function(e){
	document.getElementById("h").innerHTML = "Hello world";
    });
}
			  
var fib_num = 0;

document.getElementById("fb").addEventListener("click", function(e){
    let new_li = document.createElement("li");
    new_li.innerHTML = fib(++fib_num);
    document.getElementById("fiblist").appendChild(new_li);
})
