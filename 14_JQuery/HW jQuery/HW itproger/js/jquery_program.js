var tasks = []; // Пустой массив

// Добавление элемента в массив, плюс увеличение индекса
$("#add").on("click", function () {
	var task = $("#task").val();
	if(task == '')
		return false; // Выход, так как ничего не ввел пользователь
	
	tasks.push(task);
	$("#task").val("");
	
	// Пишем что элемент добавлен
	$("#results").text("Элемент был добавлен");
	$("#results").show();
	setTimeout(hideResults, 2000);
});

// Прячем блок с результатами
function hideResults() {
	$("#results").hide();
}

// Отображение элементов в списке
function displayList() {
	var list = "";
	for (var i = 0; i < tasks.length; i++)
		list += "<li>Задание #" + (i + 1) + ": " + tasks[i] + "</li>";
	
	$("#list").html(list);
}