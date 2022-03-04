var tasks = []; // Пустой массив

// Добавление элемента в массив, плюс увеличение индекса
function add_el() {
	var task = document.getElementById("task").value;
	if(task == '')
		return false; // Выход, так как ничего не ввел пользователь
	
	tasks.push(task);
	document.getElementById("task").value = "";
	
	// Пишем что элемент добавлен
	document.getElementById("results").innerHTML = "Элемент был добавлен";
	document.getElementById("results").style.display = 'block';
	setTimeout(hideResults, 2000);
}

// Прячем блок с результатами
function hideResults() {
	document.getElementById("results").style.display = 'none';
}

// Отображение элементов в списке
function displayList() {
	var list = "";
	for (var i = 0; i < tasks.length; i++)
		list += "<li>Задание #" + (i + 1) + ": " + tasks[i] + "</li>";
	
	document.getElementById("list").innerHTML = list;
}