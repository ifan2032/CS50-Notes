//Initialize new request
const request = new XMLHttpRequest();
const currency = document.querySelector('#currency').value;
request.open('POST', '/convert');

//callback function when request completes
request.onload = () => {
	//Extract JSON data from request
	const data = JSON.parse(request.responseText);

	//Update the result div (from html)
	if (data.success) {
		const contents = `1 USD is equal to ${data.rate} ${currency}.`
		document.querySelector('#result').innerHTML = contents;
	}
	else {
		document.querySelector('#result').innerHTML = "something went wrong. "
	}
}
//add data to send with request
const data = new FormData();
data.append('currency', currency);

//send reqeust
request.send(data);
return false;