function find_message(){
	url = window.location.href;
	url = url.split('/');
	if(url[3] == 'messages'){
		document.getElementByClass('conv_bar')
	}else{
		console.log('other')
	}
}