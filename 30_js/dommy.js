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


itemList.addEventListener("mouseover", function(e){
    document.getElementById("h").innerHTML = e.target.innerHTML;
});
